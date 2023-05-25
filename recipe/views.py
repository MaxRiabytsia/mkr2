from .models import Recipe, Category
from django.shortcuts import render


def main(request):
    context = {
        'recipes': Recipe.objects.all().order_by('-created_at')[:5],
        'title': 'Main'
    }
    return render(request, 'main.html', context)


def category_list(request):
    categories = Category.objects.all().order_by('name')

    context = {
        'categories_and_number_of_recipes': [(category, Recipe.objects.filter(category=category).count())
                                             for category in categories],
        'title': 'Categories'
    }
    return render(request, 'category_list.html', context)
