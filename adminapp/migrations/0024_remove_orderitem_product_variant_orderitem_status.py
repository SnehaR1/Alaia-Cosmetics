# Generated by Django 4.2.6 on 2023-11-11 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0023_alter_orderitem_product_variant"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orderitem",
            name="product_variant",
        ),
        migrations.AddField(
            model_name="orderitem",
            name="status",
            field=models.CharField(default="Pending", max_length=50),
        ),
    ]
