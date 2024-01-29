from django.contrib import admin
from .models import Blog, About, Contact, ContactUs, BlogComment


# Register your models here.
class AdminBlog(admin.ModelAdmin):
    list_display = ("title", "date", "first", "is_comment")
    list_editable = ("first", "is_comment")


class AdminAbout(admin.ModelAdmin):
    list_display = ("title", "is_active")
    list_editable = ("is_active",)


class AdminContact(admin.ModelAdmin):
    list_display = ("address", "email")


class AdminContactUs(admin.ModelAdmin):
    list_display = ("name", "email", "date")


class AdminBlogComment(admin.ModelAdmin):
    list_display = ("name", "date")


admin.site.register(Blog, AdminBlog)
admin.site.register(About, AdminAbout)
admin.site.register(Contact, AdminContact)
admin.site.register(ContactUs, AdminContactUs)
admin.site.register(BlogComment, AdminBlogComment)