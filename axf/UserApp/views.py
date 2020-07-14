import uuid
from io import BytesIO

from PIL import Image
from PIL.ImageDraw import ImageDraw
from PIL import ImageFont

from django.core.cache import cache
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from AXF import settings
from UserApp.models import AxfUser
from UserApp.views_constaint import send_email


def register(request):
    if request.method == 'GET':
        return render(request, 'axf/user/register/register.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        icon = request.FILES.get('icon')
        token = uuid.uuid4()

        user = AxfUser()

        user.name = name
        user.password = password
        user.email = email
        user.icon = icon
        user.u_token = token

        user.save()

        cache.set(token, user.id, timeout=30)

        send_email(email, name, token)
    return redirect(reverse('axfuser:login'))


def login(request):
    if request.method == 'GET':
        return render(request, 'axf/user/login/login.html')

    elif request.method == 'POST':
        # 从页面的文本框中获取的验证码
        imagecode = request.POST.get('icode')

        # 图片中的验证码
        verify_code = request.session.get('verify_code')

        if imagecode.lower() == verify_code.lower():
            # 如果姓名是唯一的  那么我们会单独的查询name
            name = request.POST.get('name')

            users = AxfUser.objects.filter(name=name)

            if users.count() > 0:
                user = users.first()
                password = request.POST.get('password')
                if user.password == password:
                    if user.active:
                        # session不能不能绑定对象 只能绑定属性
                        request.session['user_id'] = user.id

                        return redirect(reverse('axfmine:mine'))

                    else:
                        context = {
                            'msg': '帐号未激活'
                        }
                        return render(request, 'axf/user/login/login.html', context=context)

                else:
                    context = {
                        'msg': '密码错误'
                    }
                    return render(request, 'axf/user/login/login.html', context=context)


            else:
                context = {
                    'msg': '用户不存在'
                }
                return render(request, 'axf/user/login/login.html', context=context)


        else:
            context = {
                'msg': '验证码错误'
            }
            return render(request, 'axf/user/login/login.html', context=context)


# ajax都是返回的是json数据
def checkName(request):
    data = {
        'status': 200,
    }
    name = request.GET.get('name')

    users = AxfUser.objects.filter(name=name)

    if users.count() > 0:
        data['status'] = 201
        data['msg'] = '用户名字已注册！'
    else:
        data['msg'] = '用户名字可以注册'

    return JsonResponse(data=data)


def testEmail(request):
    subject = '啊哈'
    message = '白茶清欢无别事'
    from_email = 'li_jun_aha@163.com'
    recipient_list = ['li_jun_aha@163.com']

    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)
    return HttpResponse('邮件发送成功')


def account(request):
    # 怎么在account中修改的是当前注册的那个用户
    # token的值和cache绑定的值都是一致
    token = request.GET.get('token')

    # user_id = cache.get(token)

    # if user_id:
    #     user = AxfUser.objects.get(pk=user_id)
    #     user.active = True
    #     user.save()
    #
    #     cache.delete(token)
    #
    #     return HttpResponse('激活成功')
    #
    # else:
    #     return HttpResponse('邮件已过期或者邮件已经激活了')

    users = AxfUser.objects.filter(u_token=token)
    if users.exists():
        user = users.first()
        user.active = True
        user.save()
        return HttpResponse('激活成功')
    else:
        return HttpResponse('激活失败')


# 验证码
def get_code(request):
    # 初始化画布，初始化画笔

    mode = "RGB"

    size = (200, 100)

    red = get_color()

    green = get_color()

    blue = get_color()

    color_bg = (red, green, blue)

    image = Image.new(mode=mode, size=size, color=color_bg)

    imagedraw = ImageDraw(image, mode=mode)

    imagefont = ImageFont.truetype(settings.FONT_PATH, 100)

    # 获取了自动生成的4个验证码
    verify_code = generate_code()

    request.session['verify_code'] = verify_code

    for i in range(4):
        fill = (get_color(), get_color(), get_color())
        imagedraw.text(xy=(50 * i, 0), text=verify_code[i], font=imagefont, fill=fill)

    for i in range(100):
        fill = (get_color(), get_color(), get_color())
        xy = (random.randrange(201), random.randrange(100))
        imagedraw.point(xy=xy, fill=fill)

    fp = BytesIO()

    image.save(fp, "png")

    return HttpResponse(fp.getvalue(), content_type="image/png")


import random


def get_color():
    return random.randrange(256)


def generate_code():
    source = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

    code = ""

    for i in range(4):
        code += random.choice(source)

    return code


def logout(request):
    request.session.flush()

    return redirect(reverse('axfmine:mine'))
