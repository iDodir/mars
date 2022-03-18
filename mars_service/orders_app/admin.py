from django.contrib import admin

from .models import Order, Device, Customer, DeviceInField


# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    # todo dodir на случай работы с запчастями можно добавить и поиск по id
    # search_fields = ('manufacturer', 'model')
    list_display = ('id', 'manufacturer', 'model')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'device', 'order_description', 'created_dt', 'last_updated_dt', 'order_status')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'customer_address', 'customer_city')


class DeviceInFieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'serial_number', 'customer', 'analyzer', 'owner_status')


admin.site.register(Order, OrderAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(DeviceInField, DeviceInFieldAdmin)
