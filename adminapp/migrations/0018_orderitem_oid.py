# Generated by Django 4.2.6 on 2023-11-10 11:54

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0017_alter_cartorderitems_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="oid",
            field=shortuuid.django_fields.ShortUUIDField(
                alphabet="abcdefgh12345",
                length=10,
                max_length=20,
                prefix="or",
                unique=True,
            ),
        ),
    ]
