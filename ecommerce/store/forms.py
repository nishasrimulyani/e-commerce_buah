from django import forms

from django import forms
from .models import tambahProduk
 
 
# creating a form
class tambahForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = tambahProduk
 
        # specify fields to be used
        fields = [
            "nama_produk",
            "harga",
            "deskripsi",
            "gambar",
            "slug",
        ]