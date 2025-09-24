from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
# Model untuk menyimpan data produk di database The Corners
class Product(models.Model):
    # List kategori produk yang tersedia
    CATEGORY_CHOICES = [
        ('bola', 'Bola'),
        ('sepatu', 'Sepatu'),
        ('jersey', 'Jersey'),
        ('aksesoris', 'Aksesoris'),
        ('bundle', 'Bundle')     
    ]

    # Primary key untuk masing-mnasing produk
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Atribut-atribut produk
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=False, null=False)
    is_featured = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # Atribut tambahan produk yang bersifat opsional
    stock = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0.0)
    brand = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)

    # Data waktu dibuat & terakhir diupdate
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        # Menampilkan nama, kategori, dan harga produk
        return f"{self.name} - {self.category} - ${self.price}"

    @property 
    # Mengecek ketersediaan produk berdasarkan stok
    def is_available(self):
        return self.stock > 0

    @property 
    # Mengecek apakah produk direkomendasikan berdasarkan rating
    def is_recommended(self):
        return self.rating >= 4.5