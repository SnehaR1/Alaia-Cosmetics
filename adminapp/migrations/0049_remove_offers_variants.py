# Generated by Django 4.2.6 on 2023-11-29 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0048_offers_active_offers_valid_from_offers_valid_to"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="offers",
            name="variants",
        ),
    ]
