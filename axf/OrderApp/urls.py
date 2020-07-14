from django.conf.urls import url

from OrderApp import views

urlpatterns = [
    url(r'^makeOrder/',views.makeOrder,name='makeOrder'),

    url(r'^orderDetail/', views.orderDetail, name='orderDetail'),
    # 支付
    url(r'^testpay/', views.testpay, name='testpay'),

]