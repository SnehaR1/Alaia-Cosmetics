# Generated by Django 4.2.6 on 2023-12-01 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0054_alter_referral_referrer"),
    ]

    operations = [
        migrations.RenameField(
            model_name="referral",
            old_name="discount_percentage",
            new_name="discount_amount",
        ),
    ]
