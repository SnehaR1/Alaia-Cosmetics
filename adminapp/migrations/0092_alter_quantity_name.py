# Generated by Django 4.2.7 on 2023-12-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0091_quantity_unit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quantity",
            name="name",
            field=models.DecimalField(decimal_places=2, default=1.5, max_digits=10),
        ),
    ]
