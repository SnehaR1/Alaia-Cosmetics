# Generated by Django 4.2.6 on 2023-12-02 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userauth", "0005_alter_customuser_username"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactUs",
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
                ("mail", models.EmailField(max_length=254)),
                ("subject", models.TextField()),
                ("message", models.TextField()),
            ],
        ),
    ]
