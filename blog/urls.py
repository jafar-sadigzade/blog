from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name=""),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("blog", views.blog, name="blog"),
    path("blog-details/<int:id>", views.blog_details, name="blog-details"),
]
