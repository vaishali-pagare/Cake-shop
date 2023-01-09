from django.contrib import admin
from .models import Category,Product,Payment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","category_name")

class ProductAdmin(admin.ModelAdmin):
    list_display = ("id","pname","price","description","size" ,"quantity","cat")

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("cardno","cvv","expiry","balance")


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Payment,PaymentAdmin)
