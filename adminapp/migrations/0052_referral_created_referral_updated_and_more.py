# Generated by Django 4.2.6 on 2023-11-30 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("adminapp", "0051_alter_order_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="referral",
            name="created",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="referral",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="referral",
            name="referral_code",
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name="referral",
            name="referred_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="referred_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="referral",
            name="referrer",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="referrals",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
