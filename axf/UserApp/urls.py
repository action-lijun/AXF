from django.conf.urls import url

from UserApp import views

urlpatterns = [
    #注册
    url(r'^register/',views.register,name='register'),
    #登录
    url(r'^login/',views.login,name='login'),
    #用户名字后台验证
    url(r'^checkName/',views.checkName),
    #测试邮件的发送
    url(r'^testEmail/',views.testEmail),
    #激活
    url(r'^account/',views.account),
    #验证码
    url(r'^get_code/',views.get_code),
    # 退出
    url(r'^logout/', views.logout, name='logout'),
]