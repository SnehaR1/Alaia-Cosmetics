# Generated by Django 4.2.6 on 2023-11-29 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0050_alter_order_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
