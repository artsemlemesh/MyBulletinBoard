# Generated by Django 5.0 on 2023-12-26 01:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("board", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="text",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
