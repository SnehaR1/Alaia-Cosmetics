# Generated by Django 4.2.6 on 2023-11-15 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0033_brand_is_listed_category_is_listed_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="phone_number",
            field=models.CharField(default="6238648528", max_length=15),
        ),
    ]
