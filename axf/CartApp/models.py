from django.db import models

# Create your models here.
from MarketApp.models import AxfGoods
from UserApp.models import AxfUser


class AxfCart(models.Model):
    user = models.ForeignKey(AxfUser)
    goods = models.ForeignKey(AxfGoods)

    c_is_select = models.BooleanField(default=True)
    c_goods_num = models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_cart'