from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)

    readonly_fields = (
        'order_number', 'date',
        'delivery_total', 'bag_total',
        'grand_total', 'original_bag',
        'stripe_pid',
    )

    fields = (
        'order_number', 'user_profile', 'first_name', 'last_name',
        'email_address', 'phone_number', 'address1',
        'address2', 'town_or_city', 'county', 'postcode',
        'country', 'date', 'delivery_total', 'bag_total',
        'grand_total', 'original_bag', 'stripe_pid',
    )

    list_display = (
        'order_number', 'date',
        'first_name', 'last_name',
        'bag_total', 'delivery_total',
        'grand_total',
    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
