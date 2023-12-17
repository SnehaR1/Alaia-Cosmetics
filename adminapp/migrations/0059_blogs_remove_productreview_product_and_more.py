# Generated by Django 4.2.6 on 2023-12-01 17:22

import adminapp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0058_alter_productreview_rating"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blogs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, unique=True)),
                ("content", models.TextField(blank=True, null=True)),
                ("author", models.CharField(max_length=100)),
                (
                    "image",
                    models.ImageField(
                        default="images\x08ackgrounds\\Face.jpeg",
                        upload_to=adminapp.models.user_directory_path,
                    ),
                ),
                ("date", models.DateField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="productreview",
            name="product",
        ),
        migrations.AddField(
            model_name="productreview",
            name="product_variant",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="adminapp.productvariant",
            ),
        ),
    ]
