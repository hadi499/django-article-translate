# Generated by Django 4.2.16 on 2024-09-23 22:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_page_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='english',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='indonesian',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
