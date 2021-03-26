from  django.urls import path,include
from . import views
app_name = 'store'
urlpatterns = [
    path('',views.home,name='home'),
    path('store/',views.store,name='store'),
    path('category_items/<int:category_id>/',views.category_items,name='category_items'),
    path('start_order/',views.startOrder,name='start_order'),
    path('item_order/<int:order_id>/',views.item_order,name='item_order'),
    path('increase_quantity/<int:id>/',views.increase_quantity,name='increase_quantity'),
    path('decrease_quantity/<int:id>/',views.decrease_quantity,name='decrease_quantity'),
    path('comfirm_payment/<int:order_id>/<str:pay_price>/',views.comfirm_payment,name='comfirm_payment'),
]
