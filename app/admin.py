from django.contrib import admin

from app.models import *


class cart_inline(admin.TabularInline):
    model = CartItem
    extra = 1


class cartAdmin(admin.ModelAdmin):
    inlines = (cart_inline,)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number','date','status')
    list_filter = ('status',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Order,OrderAdmin)
admin.site.register(Cart, cartAdmin)
