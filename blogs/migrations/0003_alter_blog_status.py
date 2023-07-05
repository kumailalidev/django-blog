# Generated by Django 4.2.2 on 2023-07-03 15:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogs", "0002_alter_category_options_blog"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="status",
            field=models.CharField(
                choices=[("Draft", "Draft"), ("Published", "Published")],
                default="Draft",
                max_length=20,
            ),
        ),
    ]