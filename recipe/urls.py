from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='recipe-main'),
    path('categories', views.category_list, name='recipe-categories')
]
