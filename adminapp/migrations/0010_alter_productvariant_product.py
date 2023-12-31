# Generated by Django 4.2.6 on 2023-11-04 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0009_remove_productimages_productvariants_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productvariant",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_variants",
                to="adminapp.product",
            ),
        ),
    ]
