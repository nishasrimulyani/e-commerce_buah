# Generated by Django 5.0.4 on 2024-05-01 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_tambahproduk_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tambahproduk',
            name='title',
        ),
    ]
