from django.contrib import admin

from .models import Pizza, Size


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('topping1', 'topping2', 'size',)


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Size)
