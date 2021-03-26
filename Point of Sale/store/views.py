from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ProductForm,OrderItemForm
from .utils import *



@login_required(login_url='accounts:login')
def home(request):

    is_order_complete = True
    pay_price =0
    context ={
        'is_order_complete':is_order_complete,
        'pay_price':pay_price,
    }
    return render(request,'store/index.html', context)
    
@login_required(login_url='accounts:login')
def store(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    product_form = handle_form(request)
    context = {
        'categories':categories,
        'products':products,
        'product_form':product_form
    }
    return render(request,'store/store.html',context)
def category_items(request,category_id):
    categories = Category.objects.all()
    category = Category.objects.get(id = category_id)
    products = category.product_set.all()
    product_form = handle_form(request)
    context = {
        'categories':categories,
        'products':products,
        'product_form':product_form
    }
    return render(request,'store/store.html',context)


@login_required(login_url='accounts:login')
def startOrder(request):
    order = Order.objects.create(created_to = request.user)
    order.save()
    return redirect(reverse('store:item_order', args=(order.id,)))

def item_order(request,order_id):
    change = 0.00
    order = Order.objects.get(id = order_id)
    cart_items = OrderItem.objects.filter(order = order)
    pay_price = 0

    for item in cart_items:
        pay_price += item.product.price * item.quantity 
    item_form = OrderItemForm()
    if request.method == 'POST':
        item_form = OrderItemForm(request.POST)

        if item_form.is_valid():
            item = item_form.save(commit = False)
            item.order = order
            item.save()
            return redirect(reverse('store:item_order', args=(order.id,)))

    context ={
        'item_form':item_form,
        'is_order_complete': order.complete,
        'cart_items':cart_items,
        'pay_price':pay_price,
        'change':change,
        'order':order
    }
    return render(request,'store/index.html',context)

def increase_quantity(request,id):
    item = OrderItem.objects.get(id = id)
    item.quantity += 1
    item.save()
    return redirect(reverse('store:item_order', args=(item.order.id,)))

def decrease_quantity(request,id):
    item = OrderItem.objects.get(id = id)
    order = Order.objects.get(id = item.order.id)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect(reverse('store:item_order', args=(order.id,)))

def comfirm_payment(request,order_id,pay_price):
    order = Order.objects.get(id = order_id)
    change = 0.00
    customer_amount = 0.00
    if request.method == 'POST':
        customer_amount = float(request.POST.get('customer_amount'))
        change = customer_amount - float(pay_price)
        order.complete = True
        order.save()
    context ={
        'is_order_complete':order.complete,
        'pay_price':pay_price,
        'change':change
    }
    return render(request,'store/index.html', context)