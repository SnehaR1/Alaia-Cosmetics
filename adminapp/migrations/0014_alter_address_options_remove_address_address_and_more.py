# Generated by Django 4.2.6 on 2023-11-08 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0013_alter_cartorderitems_unique_together"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="address",
            options={"ordering": ["-is_default"], "verbose_name_plural": "Addresses"},
        ),
        migrations.RemoveField(
            model_name="address",
            name="address",
        ),
        migrations.RemoveField(
            model_name="address",
            name="product",
        ),
        migrations.RemoveField(
            model_name="address",
            name="status",
        ),
        migrations.AddField(
            model_name="address",
            name="address_line1",
            field=models.CharField(
                default="", max_length=100, verbose_name="Address Line 1"
            ),
        ),
        migrations.AddField(
            model_name="address",
            name="address_line2",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Address Line 2"
            ),
        ),
        migrations.AddField(
            model_name="address",
            name="city",
            field=models.CharField(default="", max_length=50, verbose_name="City"),
        ),
        migrations.AddField(
            model_name="address",
            name="is_default",
            field=models.BooleanField(default=False, verbose_name="Default Address"),
        ),
        migrations.AddField(
            model_name="address",
            name="state",
            field=models.CharField(default="", max_length=50, verbose_name="State"),
        ),
        migrations.AddField(
            model_name="address",
            name="zip_code",
            field=models.CharField(default="", max_length=10, verbose_name="ZIP Code"),
        ),
    ]
