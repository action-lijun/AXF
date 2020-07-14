from django.db import models

# Create your models here.
from MarketApp.models import AxfGoods
from UserApp.models import AxfUser


class Order(models.Model):
    user = models.ForeignKey(AxfUser)
    o_time = models.DateTimeField(auto_now_add=True)
    o_total_price = models.FloatField()

    class Meta:
        db_table = 'axf_order'


class OrderGoods(models.Model):
    order = models.ForeignKey(Order)
    goods = models.ForeignKey(AxfGoods)

    c_goods_num = models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_orderGoods'