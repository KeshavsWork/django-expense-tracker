from django.contrib import admin
from .models import Category, Expense


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("title", "amount", "category", "payment_method", "date", "user")
    list_filter = ("category", "payment_method", "date")
    search_fields = ("title", "notes")
