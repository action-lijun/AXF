from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from CartApp.models import AxfCart


def cart(request):
    user_id = request.session.get('user_id')

    carts = AxfCart.objects.filter(user_id=user_id)

    if user_id:

        is_all_select = not AxfCart.objects.filter(user_id=user_id).filter(c_is_select=False).exists()

        carts = AxfCart.objects.filter(user_id=user_id)

        # for c in carts:
        #     print(c.c_is_select, c.user_id)

        context = {
            'carts': carts,
            'is_all_select': is_all_select,
            'totalprice': getTotalPrice(user_id)
        }

        return render(request, 'axf/main/cart/cart.html', context=context)
    else:
        return redirect(reverse('axfuser:login'))


def addToCart(request):
    user_id = request.session.get('user_id')

    data = {}

    if user_id:
        goodsid = request.GET.get('goodsid')
        carts = AxfCart.objects.filter(user_id=user_id).filter(goods_id=goodsid)

        if carts.exists():
            cart = carts.first()
            cart.c_goods_num = cart.c_goods_num + 1
        else:
            cart = AxfCart()
            cart.user_id = user_id
            cart.goods_id = goodsid

        cart.save()

        data['status'] = 200
        data['msg'] = 'success'
        data['c_goods_num'] = cart.c_goods_num

        return JsonResponse(data=data)
    else:
        data['status'] = 201
        data['msg'] = 'error'
        return JsonResponse(data=data)


@csrf_exempt
def subCart(request):
    cartid = request.POST.get('cartid')

    cart = AxfCart.objects.get(pk=cartid)

    data = {
        # 'status': 200,
        'msg': 'ok',
        # 'c_goods_num': cart.c_goods_num,

    }

    if cart.c_goods_num > 1:

        cart.c_goods_num = cart.c_goods_num - 1

        cart.save()
        data['status'] = 200
        data['c_goods_num'] = cart.c_goods_num

        user_id = request.session.get('user_id')

        data['totalprice'] = getTotalPrice(user_id)

    else:
        data['status'] = 204
        cart.delete()

    return JsonResponse(data=data)


def changeStatus(request):  #单选
    # 如果当前用户数据库中的购物车是全选的  那么就全选变成黄色 如果数据库中的数据有未选中的 那么就变成白色

    user_id = request.session.get('user_id')
    data = {}

    if user_id:
        cartid = request.GET.get('cartid')

        cart = AxfCart.objects.get(pk=cartid)

        cart.c_is_select = not cart.c_is_select

        cart.save()
        # 判断当前用户的购物车中的数据是否全部被选中？
        is_all_select = not AxfCart.objects.filter(user_id=user_id).filter(c_is_select=False).exists()

        data['status'] = 200
        data['msg'] = 'ok'
        data['c_is_select'] = cart.c_is_select
        data['is_all_select'] = is_all_select
        data['totalprice'] = getTotalPrice(user_id)


    else:
        data['status'] = 201
        data['msg'] = 'error'

    return JsonResponse(data=data)


def allSelect(request):
    # ajax发送的请求的时候 是不允许传递列表的
    # 解决方法：将列表变成字符串
    cartlist = request.GET.get('cartlist')

    cartid_list = cartlist.split('#')

    cart_list = AxfCart.objects.filter(id__in=cartid_list)

    for cart in cart_list:
        cart.c_is_select = not cart.c_is_select
        cart.save()

    user_id = request.session.get('user_id')

    is_all_select = not AxfCart.objects.filter(user_id=user_id).filter(c_is_select=False).exists()

    data = {
        'status': 200,
        'msg': 'ok',
        'cartlist': cartlist,
        'is_all_select': is_all_select,
        'totalprice': getTotalPrice(user_id)
    }

    return JsonResponse(data=data)


def getTotalPrice(user_id):
#     当前帐号    选中的数据   数量   单价
    cart_list = AxfCart.objects.filter(user_id=user_id).filter(c_is_select=True)

    total_price = 0

    for cart in cart_list:

        total_price = total_price + cart.c_goods_num * cart.goods.price

    return '%.2f' % total_price