# Generated by Django 4.0.6 on 2022-08-30 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddDealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, verbose_name='Username')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('password', models.CharField(max_length=20, verbose_name='Password')),
                ('panNumber', models.CharField(max_length=30, verbose_name='Pan Number')),
                ('panPhoto', models.ImageField(upload_to='PanCard/Dealer/', verbose_name='Pan Photo')),
                ('totalPoint', models.IntegerField(default=0, verbose_name='Total Point')),
                ('createdOn', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('updatedOn', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('dealerName', models.CharField(max_length=255, verbose_name='Dealer Name')),
                ('referrelCode', models.CharField(max_length=20, unique=True, verbose_name='Referrel Code')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DealerInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=255, verbose_name='Product Name')),
                ('productCategory', models.CharField(max_length=255, verbose_name='Product Category')),
                ('productQuantity', models.CharField(max_length=255, verbose_name='Product Quantity')),
                ('dealer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Dealer.adddealer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
