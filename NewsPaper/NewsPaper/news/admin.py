from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ['time_emerged', 'name', 'author']
    list_filter = ['author']
    search_fields = ['category']


admin.site.register(Post, PostAdmin)
