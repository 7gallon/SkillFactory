from django.contrib import admin
from django import forms
from .models import Post, Author, Category, PostCategory
# from ckeditor_uploader.fields import RichTextFormField


# class PostAdminForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['text']
#         widgets = {
#             'content': RichTextFormField(),
#         }


class PostAdmin(admin.ModelAdmin):
    # model = PostAdminForm
    model = Post


class AuthorAdmin(admin.ModelAdmin):
    model = Author


class CategoryAdmin(admin.ModelAdmin):
    model = Category


class PostCategoryAdmin(admin.ModelAdmin):
    model = PostCategory


admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(PostCategory)
