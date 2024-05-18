from django.contrib import admin

from app.models import *

class cart_inline(admin.TabularInline):
    model = CartItem
    extra = 1
class cartAdmin(admin.ModelAdmin):
    inlines = (cart_inline,)
# Register your models here.
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Cart,cartAdmin)
admin.site.register(Service)
admin.site.register(UserProfile)