from django.conf.urls import url

from CartApp import views

urlpatterns = [
    #构建购物车页面
    url(r'^cart', views.cart, name='cart'),
    #将商品添加到购物车
    url(r'^addToCart', views.addToCart, name='addToCart'),
    #减少购物车中的商品数量
    url(r'^subCart/', views.subCart, name='subCart'),
    #修改购物车选中状态
    url(r'^changeStatus/',views.changeStatus),
    #全选
    url(r'^allSelect/',views.allSelect),
]
