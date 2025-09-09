from django.test import TestCase, Client
from .models import Product

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/nonexistent-page/')
        self.assertEqual(response.status_code, 404)

    def test_product_creation(self):
        product = Product.objects.create(
            name = "Baju Jersey Timnas Indonesia",
            price = 500000,
            description = "Jersey replika Timnas Indonesia",
            category = "jersey",
            is_featured = True,
            stock = 10,
            rating = 4.7,
            size = "L",
            color = "Merah Putih"
        )
        self.assertEqual(product.name, "Baju Jersey Timnas Indonesia") 
        self.assertEqual(product.price, 500000)       
        self.assertTrue(product.is_available)
        self.assertTrue(product.is_recommended)
        self.assertTrue(product.is_featured)
        
    def test_product_default_values(self):
        product = Product.objects.create(
          name = "Baju Jersey Timnas Indonesia",
            price = 500000,
            description = "Jersey replika Timnas Indonesia",
            category = "jersey",
        )
        self.assertFalse(product.is_featured)
        self.assertEqual(product.stock, 0)
        self.assertEqual(product.rating, 0.0)
        self.assertEqual(product.brand, None)
        self.assertEqual(product.size, None)
        self.assertEqual(product.color, None)