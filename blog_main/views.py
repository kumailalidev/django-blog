from django.shortcuts import render

from blogs.models import Category


def home(request):
    categories = Category.objects.all()
    print(categories)
    context = {
        "categories": categories,
    }

    return render(request, "home.html", context)
