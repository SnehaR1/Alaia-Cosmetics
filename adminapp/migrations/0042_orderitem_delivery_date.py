# Generated by Django 4.2.6 on 2023-11-23 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0041_remove_order_payment_done"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="delivery_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
