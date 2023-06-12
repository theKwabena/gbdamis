# Generated by Django 4.1.9 on 2023-06-07 15:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("forum", "0002_alter_post_tag"),
    ]

    operations = [
        migrations.CreateModel(
            name="UploadedFile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("uploaded_file", models.FileField(upload_to="storage/")),
                ("uploaded_at", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="featured_image",
            field=models.ImageField(blank=True, default="", upload_to="images"),
        ),
    ]