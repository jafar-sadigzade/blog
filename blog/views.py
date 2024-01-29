from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Blog, About, Contact, ContactUs, BlogComment


# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    return render(request, "index.html", {"blogs": blogs})


def about(request):
    abouts = About.objects.filter(is_active=True)
    return render(request, "about.html", {"abouts": abouts})


def contact(request):
    contacts = Contact.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        new_contact_us = ContactUs(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        new_contact_us.save()

        return render(request, "contact.html", {"contacts": contacts, "success": "Mesajınız uğurla qeydə alındı!"})

    return render(request, "contact.html", {"contacts": contacts})


def blog(request):
    blogs = Blog.objects.all()
    blogpaginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    try:
        blogs = blogpaginator.page(page)
    except PageNotAnInteger:
        blogs = blogpaginator.page(1)
    except EmptyPage:
        blogs = blogpaginator.page(blogpaginator.num_pages)
    return render(request, "blog.html", {"blogs": blogs})


def blog_details(request, id):
    blog = Blog.objects.get(id=id)
    comments = BlogComment.objects.filter(choosen_blog=blog)
    num = comments.count()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        choosen_blog = blog

        new_comments = BlogComment(
            name=name,
            email=email,
            message=message,
        )
        new_comments.save()
        new_comments.choosen_blog.add(blog)
        new_comments.save()
        messages.success(request, 'Rəyiniz qeyd olundu!')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    return render(request, "single.html", {"blog": blog, "comments": comments, "num": num})
