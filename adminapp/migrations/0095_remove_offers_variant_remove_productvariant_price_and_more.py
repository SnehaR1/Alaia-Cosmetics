# Generated by Django 4.2.7 on 2023-12-23 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0094_offers_variant"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="offers",
            name="variant",
        ),
        migrations.RemoveField(
            model_name="productvariant",
            name="price",
        ),
        migrations.AddField(
            model_name="productvariant",
            name="offer_price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
