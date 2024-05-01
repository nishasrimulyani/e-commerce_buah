# views.py

from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .models import tambahProduk
from .forms import tambahForm
class IndexView(TemplateView):
    template_name = 'index.html'
class AboutView(TemplateView):
    template_name = 'about.html'

class ShopView(TemplateView):
    template_name = 'shop.html'

class CartView(TemplateView):
    template_name = 'cart.html'

def create_view(request):
    if request.method == 'POST':
        form = tambahForm(request.POST, request.FILES)  # Jika menggunakan ModelForm dengan gambar
        if form.is_valid():
            form.save()
            return redirect('store:shop')  # Redirect ke halaman toko setelah data disimpan
    else:
        form = tambahForm()
    return render(request, 'create_view.html', {'form': form})



def shop(request):
    products = tambahProduk.objects.all()  # Fetch all products

    context = {'products': products}  # Create context dictionary

    return render(request, 'shop.html', context)
