# Generated by Django 4.2.7 on 2023-12-04 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0067_alter_productreview_product_variant"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productreview",
            name="product_variant",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="reviews",
                to="adminapp.productvariant",
            ),
        ),
    ]
