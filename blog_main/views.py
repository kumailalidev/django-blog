from django.shortcuts import render

from blogs.models import Blog, Category

from .forms import RegistrationForm


def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status="Published").order_by(
        "-updated_at"
    )
    posts = Blog.objects.filter(is_featured=False, status="Published")
    print(posts)

    context = {
        "featured_posts": featured_posts,
        "posts": posts,
    }

    return render(request, "home.html", context)


def register(request):
    form = RegistrationForm()
    context = {
        "form": form,
    }

    return render(request, "register.html", context)
