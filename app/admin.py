from django.contrib import admin
from .models import Book

# Register your models here.

# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id","title","info","cover","book_pdf","datetime")


