# Generated by Django 4.2.7 on 2023-12-15 13:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("adminapp", "0087_alter_productvariant_color_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="coupon",
            name="users",
            field=models.ManyToManyField(
                related_name="coupons", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
