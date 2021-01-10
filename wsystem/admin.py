from django.contrib import admin

# Register your models here.
from wsystem.models import *



class PurchaseTableAdmin(admin.ModelAdmin):

    list_display = ['id',  'wmodels', 'nums', 'time']
    search_fields = ( 'wmodels', 'nums', 'time')

class CustomerTableAdmin(admin.ModelAdmin):
    list_display = ['id',  'username', 'password', 'name', 'address', 'phone']
    search_fields = ( 'username', 'password', 'name', 'address', 'phone')

class OrdersTableAdmin(admin.ModelAdmin):
    list_display = ['id','time','username','dis_address','wmodels', 'nums', 'money','paymodels']
    fieldsets = [
            ('订单信息', {'fields': ['time','wmodels','nums','money','paymodels']}),
            ('用户信息', {'fields': ['username']}),
        ]
    search_fields = ('time','wmodels', 'nums', 'username__address','money','paymodels')


class UserInformationTableAdmin(admin.ModelAdmin):
    list_display = ['id','username', 'wmodels', 'nums', 'state', 'money']
    search_fields = ( 'wmodels', 'nums', 'state', 'money')

class InventoryTableAdmin(admin.ModelAdmin):
    list_display = ['id', 'wmodels', 'nums']
    search_fields = ('wmodels', 'nums')


admin.site.register(UserInformationTable,UserInformationTableAdmin)
admin.site.register(OrdersTable,OrdersTableAdmin)
admin.site.register(CustomerTable,CustomerTableAdmin)
admin.site.register(PurchaseTable,PurchaseTableAdmin)
admin.site.register(InventoryTable,InventoryTableAdmin)




