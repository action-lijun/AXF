from django.shortcuts import render

# Create your views here.
from MarketApp.models import AxfFoodType, AxfGoods


def market(request):
    foodtype_list = AxfFoodType.objects.all()

    typeid = request.GET.get('typeid', '104749')

    goods_list = AxfGoods.objects.filter(categoryid=typeid)

    childtypenames = AxfFoodType.objects.filter(typeid=typeid)[0].childtypenames

    childtype_list = childtypenames.split('#')

    child_type_list = []

    for childtype in childtype_list:
        child_type = childtype.split(':')
        child_type_list.append(child_type)

    childcid = request.GET.get('childcid', '0')

    if childcid == '0':
        pass
    else:
        goods_list = goods_list.filter(childcid=childcid)

    sort_rule_list = [
        ['综合排序', '0'],
        ['价格升序', '1'],
        ['价格降序', '2'],
        ['销量升序', '3'],
        ['销量降序', '4'],
    ]

    sort_rule_id = request.GET.get('sort_rule_id', '0')

    if sort_rule_id == '0':
        pass
    elif sort_rule_id == '1':
        goods_list = goods_list.order_by('price')
    elif sort_rule_id == '2':
        goods_list = goods_list.order_by('-price')
    elif sort_rule_id == '3':
        goods_list = goods_list.order_by('productnum')
    elif sort_rule_id == '4':
        goods_list = goods_list.order_by('-productnum')

    context = {
        'foodtype_list': foodtype_list,
        'goods_list': goods_list,
        'typeid': typeid,
        'child_type_list': child_type_list,
        'childcid': childcid,
        'sort_rule_list': sort_rule_list,
        'sort_rule_id': sort_rule_id

    }

    return render(request, 'axf/main/market/market.html', context=context)
