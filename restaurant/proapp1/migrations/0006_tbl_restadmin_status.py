# Generated by Django 4.2 on 2023-05-11 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("proapp1", "0005_tbl_restaurant_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="tbl_restadmin",
            name="status",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
