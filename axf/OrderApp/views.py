from alipay import AliPay
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from AXF.settings import PRIVATE_KEY, PUBLIC_KEY
from CartApp.models import AxfCart
from CartApp.views import getTotalPrice
from OrderApp.models import Order, OrderGoods


def makeOrder(request):

    user_id = request.session.get('user_id')

    # 创建一个订单
    order = Order()
    order.user_id = user_id
    order.o_total_price = getTotalPrice(user_id)
    order.save()


    # goods  订单的商品 都应该有哪些？ 数据是哪来的？  应该是购物车中 被选中的数据

    # 当前帐号中被选中的数据
    cart_list = AxfCart.objects.filter(user_id=user_id).filter(c_is_select=True)

    for cart in cart_list:
        # 订单商品
        ordergoods = OrderGoods()
        ordergoods.order = order
    #     通过购物车能不能找到对应的商品
        goods = cart.goods
        ordergoods.goods = goods

        ordergoods.c_goods_num = cart.c_goods_num

        ordergoods.save()

        cart.delete()

    data = {
        'msg':'ok',
        'status':200,
        'order_id':order.id
    }

    return JsonResponse(data=data)


def orderDetail(request):

    order_id = request.GET.get('order_id')


    order = Order.objects.get(pk=order_id)


    context = {
        'order':order
    }

    # order_detail.html 渲染的数据是  总价  order  编号  order  图片名字和价格 ordergoods
    return render(request,'axf/order/orderDetail.html',context=context)


def testpay(request):

    alipay = AliPay(
        appid="2016101800719334",
        app_notify_url=None,  # 默认回调url
        app_private_key_string=PRIVATE_KEY,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=PUBLIC_KEY,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug = False  # 默认False
    )

    # 如果你是Python 2用户（考虑考虑升级到Python 3吧），请确保非ascii的字符串为utf8编码：
    # subject = u"测试订单".encode("utf8")
    # 如果你是 Python 3的用户，使用默认的字符串即可
    subject = "iphone11 pro max"

    # 电脑网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no="20161112",
        total_amount=200,
        subject=subject,
        return_url="https://example.com",
        notify_url="https://example.com/notify"  # 可选, 不填则使用默认notify url
    )

    return redirect('https://openapi.alipaydev.com/gateway.do?'+order_string)