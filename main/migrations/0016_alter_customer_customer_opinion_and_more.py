# Generated by Django 4.2.15 on 2024-08-10 19:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_customer_customer_opinion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Customer_opinion',
            field=ckeditor.fields.RichTextField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Customer_opinion_en',
            field=ckeditor.fields.RichTextField(max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Customer_opinion_fa',
            field=ckeditor.fields.RichTextField(max_length=3000, null=True),
        ),
    ]