from django.db import models

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class tambahProduk(models.Model):
    title = models.CharField(max_length=100)
    nama_produk = models.CharField(max_length=100)
    harga = models.FloatField()
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='product')
    slug = models.SlugField(unique=True)
    tanggal_ditambahkan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Order(models.Model):
    gambar = models.ImageField(upload_to='order_images')
    nama = models.CharField(max_length=255)
    harga = models.FloatField()
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.nama
    
    def save(self, *args, **kwargs):
        self.subtotal = self.harga * self.quantity
        super().save(*args, **kwargs)
