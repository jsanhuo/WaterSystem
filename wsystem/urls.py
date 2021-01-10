from django.urls import path

from . import views
app_name = 'wsystem'
urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('orderlist/', views.orderList, name='orderlist'),
    path('addorder/', views.addOrder, name='addorder'),
    path('addorderlist/', views.addOrderList, name='addorderlist'),
    # path('customerList/', views.orderList, name='customerList'),
    # path('purchaseList/', views.orderList, name='purchaseList'),
    # path('hypothecateList/', views.orderList, name='hypothecateList'),
    # path('inventoryList/', views.orderList, name='inventoryList'),
]