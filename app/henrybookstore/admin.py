from django.contrib import admin

# Register your models here.
from .models import Book, Branch, Inventory

class InventoryInline(admin.TabularInline):
    model = Inventory
    extra = 1

class BookAdmin(admin.ModelAdmin):
    inlines = [InventoryInline]

class BranchAdmin(admin.ModelAdmin):
    inlines = [InventoryInline]

admin.site.register(Book, BookAdmin)

admin.site.register(Branch, BranchAdmin)