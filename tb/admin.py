from django.contrib import admin
from  . models import *
# Register your models here.
admin.site.site_title = '小贷管理办法'
admin.site.site_header = '财务软件'


#客户明细
class usertableAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('add_date',
              'name',
              'eventDetail',
              'money',
              'rate',
              'salesman',
              'note',
              'daoxiri',
              'phone',
              'addres',
              'mortgage',
              'type',
              'addresMortgage',
                )
    #置每页显示多少条记录，默认是100条
    list_per_page = 15


#业务员
class salesmanAdmin(admin.ModelAdmin):
    list_display = ('name','mobile_phone')
    search_fields = ('name',)
    list_per_page = 15

#支出
class incomeUntypeAdmin(admin.ModelAdmin):
    list_display = ('income_untype',)
#收入
class incomeTypeAdmin(admin.ModelAdmin):
    list_display = ('income_type',)

admin.site.register(incomeType,incomeTypeAdmin)
admin.site.register(incomeUntype,incomeUntypeAdmin)
admin.site.register(usertable,usertableAdmin)
admin.site.register(salesman,salesmanAdmin)
admin.site.register(User)