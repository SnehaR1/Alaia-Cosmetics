# Generated by Django 4.2.6 on 2023-11-06 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0011_alter_product_brand_alter_product_category"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cartorder",
            old_name="product_status",
            new_name="order_status",
        ),
        migrations.RenameField(
            model_name="cartorderitems",
            old_name="item",
            new_name="product_title",
        ),
        migrations.RemoveField(
            model_name="cartorder",
            name="price",
        ),
        migrations.RemoveField(
            model_name="cartorderitems",
            name="product_status",
        ),
        migrations.AddField(
            model_name="cartorder",
            name="total_price",
            field=models.DecimalField(decimal_places=2, default=50.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="cartorderitems",
            name="price",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="adminapp.productvariant",
            ),
        ),
        migrations.AlterField(
            model_name="cartorderitems",
            name="total",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
