# Generated by Django 4.2 on 2023-05-16 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("proapp1", "0007_remove_tbl_offer_tbl_offer_tbl_offer_offer_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="tbl_restaurant",
            name="password",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="tbl_restaurant",
            name="username",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
