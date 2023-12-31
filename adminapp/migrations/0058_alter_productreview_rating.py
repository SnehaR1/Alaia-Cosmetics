# Generated by Django 4.2.6 on 2023-12-01 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0057_alter_referral_referrer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productreview",
            name="rating",
            field=models.IntegerField(
                choices=[
                    (0, "☆☆☆☆☆"),
                    (1, "★☆☆☆☆"),
                    (2, "★★☆☆☆"),
                    (3, "★★★☆☆"),
                    (4, "★★★★☆"),
                    (5, "★★★★★"),
                ],
                default=None,
            ),
        ),
    ]
