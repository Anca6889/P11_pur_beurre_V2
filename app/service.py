"""
    This module contains all the basic methods of app/views.py
    This way alow a optimise refactoring and make it easier to unittest.
"""

from app.models import Product, Category, Rating
from django.db.models import Count
from django.db.models import Q


class Service:
    """Contain all the methods of the app/views.py."""

    def manage_get_product(self, product_id):
        """Get a simple product with his id"""

        return Product.objects.get(pk=product_id)

    def manage_get_product_categories(self, product):
        """Get the all categories from a product in the table category"""

        return Category.objects.filter(
            product__id=product.id)

    def manage_get_potentials_substitutes(self, product, category):
        """
        Find out potentials substitutes with similar products what are
        sharing 4 similar categories and sort them out by nutriscore grade
        """

        return (
            Product.objects.filter(categories__in=category)
            .filter(nutriscore_grade__lt=product.nutriscore_grade)
            .annotate(nb_cat=Count("categories"))
            .filter(nb_cat__gte=4)
            .filter(nutriscore_grade__lt=product.nutriscore_grade)
            .order_by("nutriscore_grade")[:24]
        )

    def manage_sort_out_user_favorite_products(self, products, user):
        """
        check if a product in list of products is already
        in user's favorites list
        """

        for product in products:
            if product.favorites.filter(id=user.id).exists():
                product.is_fav = True
            else:
                product.is_fav = False
        return products

    def manage_sort_out_if_product_is_favorite(self, product, user):
        """check if a single product is already in user's favorites list"""

        if product.favorites.filter(id=user.id).exists():
            product.is_fav = True
        else:
            product.is_fav = False
        return product

    def manage_setup_get_substitutes_context(self, pr_to_repl, substitutes):
        """Setup the context of the view get_substitutes in views.py"""

        context = {
            "product": pr_to_repl,
            "substitutes": substitutes
        }
        return context

    def manage_setup_get_product_details_context(self, product):
        """Setup the context of the view get_product_details in views.py"""

        context = {"product": product}
        return context

    def manage_setup_favorites_list_context(self, favorites):
        """Setup the context of the view favorites_list in views.py"""

        context = {"favorites": favorites}
        return context

    def manage_add_or_remove_favorite(self, product, user):
        """Add or remove a product in favorites list by clicking on heart"""

        if product.favorites.filter(id=user.id).exists():
            product.favorites.remove(user.id)
        else:
            product.favorites.add(user.id)

    def search_results_with_name(self, query):
        """get results with research in search bar"""

        return (
            Product.objects.filter(
                Q(product_name_fr__icontains=query)
            )
        )

    def calculate_medium_rate_for_product_list(self, products):
        """ Calculate the medium rate of all users """

        for product in products:
            if Rating.objects.filter(product_id=product.id):
                rates = Rating.objects.filter(
                    product_id=product.id).values_list('rate', flat=True)
                sum_of_rates = sum(rates)
                number_of_rates = len(rates)
                medium_rate = sum_of_rates/number_of_rates
                product.medium_rate = round(medium_rate,1)
                product.number_of_voters = number_of_rates
        return products

    def calculate_medium_rate_of_one_product(self, product):
        """ Calculate the medium rate of all users """

        if Rating.objects.filter(product_id=product.id):
            rates = Rating.objects.filter(
                product_id=product.id).values_list('rate', flat=True)
            sum_of_rates = sum(rates)
            number_of_rates = len(rates)
            medium_rate = sum_of_rates/number_of_rates
            product.medium_rate = round(medium_rate, 1)
            product.number_of_voters = number_of_rates
        return product
