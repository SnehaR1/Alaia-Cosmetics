# Generated by Django 4.2.6 on 2023-11-14 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0025_remove_cartorderitems_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderitem",
            name="price",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="adminapp.productvariant",
            ),
        ),
    ]
