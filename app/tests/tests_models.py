"""This module test the models of app/models.py"""

from django.test import TestCase
from django.contrib.auth.models import User
from app.models import Product, Category, Rating


class Modelstests(TestCase):
    """
    This class will mock a fake product, fake user, fake rating
    and fake category and will tests if
    all the atributes from the fake database are matching.
    """

    def setUp(self):
        """Setup the four mocks"""

        self.mock_user = User.objects.create(
            id='1',
            username='Hello_test',
            email='hello.test@hellotest.com',
            password='Coverate8462'
        )

        self.mock_product = Product.objects.create(
            id='1',
            product_name_fr='testname',
            brands='testbrand',
            nutriscore_grade="e",
            stores='teststore',
            url='test/url.com',
            image='testimage'
        )

        self.mock_category = Category.objects.create(
            id='1',
            name='testcategory'
        )

        self.mock_rate1 = Rating.objects.create(
            id='1',
            date='2022-01-25 20:00:04',
            text='A test comment',
            rate='3',
            product_id='1',
            user_id='1'
        )

    def test_id_product(self):
        """Test the id value of the product"""

        result = self.mock_product.id
        self.assertEqual(result, 1)

    def test_name_product(self):
        """Test the name 'product_name_fr' value of the product"""

        result = self.mock_product.product_name_fr
        self.assertEqual(result, 'testname')

    def test_brands_product(self):
        """Test the brands value of the product"""

        result = self.mock_product.brands
        self.assertEqual(result, 'testbrand')

    def test_nutriscore_grade_product(self):
        """Test the nutriscore_grade value of the product"""

        result = self.mock_product.nutriscore_grade
        self.assertEqual(result, 'e')

    def test_stores_product(self):
        """Test the stores value of the product"""

        result = self.mock_product.stores
        self.assertEqual(result, 'teststore')

    def test_url_product(self):
        """Test the url value of the product"""

        result = self.mock_product.url
        self.assertEqual(result, 'test/url.com')

    def test_image_product(self):
        """Test the image value of the product"""

        result = self.mock_product.image
        self.assertEqual(result, 'testimage')

    def test_str_product(self):
        """Test the return of the name value of the product"""

        result = self.mock_product.__str__()
        self.assertEqual(result, 'testname')

    def test_str_category(self):
        """Test the return of the name value of the category"""

        result = self.mock_category.__str__()
        self.assertEqual(result, 'testcategory')

    def test_id_rating(self):
        """Test the id value of a rating"""

        result = self.mock_rate1.id
        self.assertEqual(result, 1)

    def test_text_rating(self):
        """Test the text value of a rating"""

        result = self.mock_rate1.text
        self.assertEqual(result, 'A test comment')

    def test_text_rating(self):
        """Test the rate value of a rating"""

        result = self.mock_rate1.rate
        self.assertEqual(result, '3')

    def test_product_id_rating(self):
        """Test the product_id value of a rating"""

        result = self.mock_rate1.product_id
        self.assertEqual(result, '1')

    def test_user_id_rating(self):
        """Test the user_id value of a rating"""

        result = self.mock_rate1.user_id
        self.assertEqual(result, '1')
