from django.contrib import admin
from .models import Account, Transaction, Category


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'currency', 'balance', 'created_at']
    list_filter = ['currency', 'created_at']
    search_fields = ['user__username', 'name']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'transaction_type', 'amount', 'currency', 'category', 'date']
    list_filter = ['transaction_type', 'currency', 'date']
    search_fields = ['user__username', 'category', 'description']
    date_hierarchy = 'date'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'transaction_type', 'user', 'icon']
    list_filter = ['transaction_type']
    search_fields = ['name', 'user__username']
