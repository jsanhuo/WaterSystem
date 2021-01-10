from django.db import models

# Create your models here.

from django.utils import timezone


class PurchaseTable(models.Model):
    wmodels = models.CharField('规格',max_length=20)
    nums = models.PositiveIntegerField('进货数量')
    time = models.DateTimeField('进货时间',default = timezone.now)

    def __str__(self):
        return self.wmodels
    class Meta:
        verbose_name_plural = '进货信息表'

class CustomerTable(models.Model):
    username = models.CharField('用户名',max_length=20)
    password = models.CharField('密码',max_length=20)
    name = models.CharField('昵称',max_length=10)
    address = models.CharField('地址',max_length=50)
    phone = models.CharField('电话',max_length=15)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = '用户信息表'

class OrdersTable(models.Model):
    time = models.DateTimeField('订单时间',default = timezone.now)
    username = models.ForeignKey(CustomerTable,on_delete=models.CASCADE)
    wmodels = models.CharField('规格',max_length=20)
    nums = models.PositiveIntegerField('数量')
    money = models.DecimalField('金额', max_digits=1000, decimal_places=2)
    paymodels = models.CharField('支付方式', max_length=10,choices=(('pay', u'支付宝'), ('wechat', u'微信'), ('now', u'货到付款')), default='now')
    def dis_name(self):
        return self.username.name
    def dis_address(self):
        return self.username.address
    dis_name.short_description = '用户名'
    dis_address.short_description='地址'
    class Meta:
        verbose_name_plural = '订单信息表'


class UserInformationTable(models.Model):
    username = models.ForeignKey(CustomerTable,on_delete=models.CASCADE)
    wmodels = models.CharField('规格',max_length=15)
    nums = models.PositiveIntegerField('数量')
    state = models.CharField('状态', max_length=10,choices=(('state_1', u'欠桶'), ('state_2', u'压桶'), ('state_3', u'还桶')), default='state_1')
    money = models.DecimalField('押金', max_digits=1000, decimal_places=2)
    class Meta:
        verbose_name_plural = '抵押信息表'


class InventoryTable(models.Model):
    wmodels = models.CharField('规格',max_length=20)
    nums = models.PositiveIntegerField('数量')
    class Meta:
        verbose_name_plural = '库存信息表'
