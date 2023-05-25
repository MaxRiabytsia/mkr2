from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category


class ResponseTests(TestCase):

    def test_no_recipes(self):
        response = self.client.get(reverse('recipe-main'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['recipes'], [])

    def test_save_recipe(self):
        test_category = Category(name='Test Category')
        test_category.save()
        test_recipe = Recipe(title='Test Recipe',
                             description='Test Recipe content',
                             instructions='Test Recipe instructions',
                             ingredients='Test Recipe ingredients',
                             category=test_category)
        test_recipe.save()
        response = self.client.get(reverse('recipe-main'))
        self.assertQuerysetEqual(
            response.context['recipes'],
            [test_recipe]
        )

    def test_delete_recipe(self):
        test_category = Category(name='Test Category')
        test_category.save()
        test_recipe = Recipe(title='Test Recipe',
                             description='Test Recipe content',
                             instructions='Test Recipe instructions',
                             ingredients='Test Recipe ingredients',
                             category=test_category)
        test_recipe.save()
        response = self.client.get(reverse('recipe-main'))
        self.assertQuerysetEqual(
            response.context['recipes'],
            [test_recipe]
        )

        test_category.delete()
        test_recipe.delete()

        response = self.client.get(reverse('recipe-main'))
        self.assertQuerysetEqual(
            response.context['recipes'],
            []
        )

    def test_save_category(self):
        test_category = Category(name='Test Category')
        test_category.save()
        response = self.client.get(reverse('recipe-categories'))
        self.assertQuerysetEqual(
            response.context['categories_and_number_of_recipes'],
            [(test_category, 0)]
        )

    def test_delete_category(self):
        test_category = Category(name='Test Category')
        test_category.save()

        response = self.client.get(reverse('recipe-categories'))
        self.assertQuerysetEqual(
            response.context['categories_and_number_of_recipes'],
            [(test_category, 0)]
        )

        test_category.delete()

        response = self.client.get(reverse('recipe-categories'))
        self.assertQuerysetEqual(
            response.context['categories_and_number_of_recipes'],
            []
        )
