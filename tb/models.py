from django.db import models
from django.utils import timezone
# Create your models here.


class User(models.Model):
    name = models.CharField('用户名',max_length=128,unique=True)
    password = models.CharField('密码',max_length=256)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name




#业务员管理表
class salesman(models.Model):

    name = models.CharField('业务员',max_length=100)
    mobile_phone=models.CharField('手机号',max_length=12,null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '业务员'
        verbose_name_plural = verbose_name

#现存客户表
class usertable(models.Model):

    add_date = models.DateTimeField('日期', default=timezone.now)
    name = models.CharField('名称',max_length=120)
    eventDetail = models.CharField('摘要',max_length=120,null=True,blank=True)
    money = models.CharField('金额',max_length=12)
    rate = models.CharField('利率',max_length=12)

    interest = models.CharField('每期利息',max_length=12)

    salesman = models.ForeignKey('salesman',verbose_name='业务员',on_delete=models.CASCADE)
    note = models.TextField('备注',blank=True, null=True)
    daoxiri = models.DateTimeField('到息日',default=timezone.now)
    phone = models.CharField('联系方式',max_length=12,null=True,blank=True)
    addres = models.CharField('住址',max_length=200,null=True,blank=True)
    mortgage = models.CharField('抵押物',max_length=200,null=True,blank=True)
    type = models.CharField('类型',max_length=100,null=True,blank=True)
    addresMortgage =models.CharField('抵押物位置',max_length=200,null=True,blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '现存客户'
        verbose_name_plural = verbose_name


#收入类型
class incomeType(models.Model):
        income_type = models.CharField('收入类型', max_length=100)

        def __str__(self):
            return self.income_type

        class Meta:
            verbose_name = '收入类型'
            verbose_name_plural = verbose_name
# 支出类型
class incomeUntype(models.Model):
    income_untype = models.CharField('支出类型', max_length=100)

    def __str__(self):
        return self.income_untype

    class Meta:
        verbose_name = '支出类型'
        verbose_name_plural = verbose_name
#收入明细表
class IncomeSpending(models.Model):
    incomeDate = models.DateField('日期',auto_now=True)
    incomeName = models.CharField('名称',max_length=120)
    income_event_detail = models.CharField('摘要',max_length=120,null=True)
    incomeFor = models.ForeignKey('incomeType',on_delete=models.CASCADE)
    incomeamount = models.CharField('金额',max_length=13)

    def __str__(self):
        return self.incomeName

    class Meta:
        verbose_name = '收入明细表'
        verbose_name_plural = verbose_name
#支出明细表
class IncomeupSpending(models.Model):
    incomeupDate = models.DateField('日期',auto_now=True)
    incomeupName = models.CharField('名称',max_length=120)
    income_upevent_detail = models.CharField('摘要',max_length=120,null=True)
    incomeupFor = models.ForeignKey('incomeUntype',on_delete=models.CASCADE)
    incomeupamount = models.CharField('金额',max_length=13)

    def __str__(self):
        return self.incomeupName

    class Meta:
        verbose_name = '支出明细表'
        verbose_name_plural = verbose_name


