from django.contrib import admin

from .models import tambahProduk, Order

class ProdukItemAdmin(admin.ModelAdmin):
    list_display = ['nama_produk','harga', 'deskripsi', 'gambar', 'slug', 'tanggal_ditambahkan']


admin.site.register(tambahProduk, ProdukItemAdmin)
# Register your models here.

new_order = Order(
    gambar="path/to/image.jpg",
    nama="Product Name",
    harga=100.00,
    quantity=2,
)

new_order.save()
admin.site.register(Order)
