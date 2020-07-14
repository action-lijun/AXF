from django.db import models


# Create your models here.
class AxfUser(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=64)
    icon = models.ImageField(upload_to='icons')

    # 注册之后 默认情况下应该是未激活状态  在激活之后才会修改为激活 允许登录
    active = models.BooleanField(default=False)

    # 用来表示记录/对象的唯一性的一个字段
    u_token = models.CharField(max_length=256)


    class Meta:
        db_table = 'axf_user'
