# Generated by Django 4.2 on 2023-05-10 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("proapp1", "0003_rename_username_tbl_user_username"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tbl_user",
            old_name="firstName",
            new_name="firstname",
        ),
        migrations.RenameField(
            model_name="tbl_user",
            old_name="lastName",
            new_name="lastname",
        ),
    ]