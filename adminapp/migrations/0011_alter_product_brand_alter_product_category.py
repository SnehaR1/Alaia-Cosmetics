# Generated by Django 4.2.6 on 2023-11-06 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0010_alter_productvariant_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="brand",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="product_set",
                to="adminapp.brand",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="product_set",
                to="adminapp.category",
            ),
        ),
    ]
