# Generated by Django 4.2.7 on 2023-12-04 04:47

import adminapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0072_alter_blogadditionalimage_add_images_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogadditionalimage",
            name="add_images",
            field=models.ImageField(
                blank=True, null=True, upload_to=adminapp.models.user_directory_path
            ),
        ),
        migrations.AlterField(
            model_name="blogs",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to=adminapp.models.user_directory_path
            ),
        ),
    ]
