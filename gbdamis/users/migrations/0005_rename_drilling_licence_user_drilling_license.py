# Generated by Django 4.1.9 on 2023-06-12 01:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_remove_user_profile_complete"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="drilling_licence",
            new_name="drilling_license",
        ),
    ]
