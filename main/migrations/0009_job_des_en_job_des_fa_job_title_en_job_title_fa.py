# Generated by Django 4.2.15 on 2024-08-09 15:14

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_vars_img1_remove_vars_img2_remove_vars_img3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='des_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='des_fa',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='title_en',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='title_fa',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
