# Generated by Django 4.2.15 on 2024-08-08 22:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images',
            new_name='ComImages',
        ),
        migrations.AddField(
            model_name='customer',
            name='Customer_opinion_en',
            field=models.TextField(max_length=350, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='Customer_opinion_fa',
            field=models.TextField(max_length=350, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='des_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='des_fa',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='name_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='name_fa',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='skills',
            name='Skill_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='skills',
            name='Skill_fa',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='aboutme_des_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='aboutme_des_fa',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='aboutme_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='aboutme_fa',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='aboutme_title_en',
            field=models.CharField(max_length=355, null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='aboutme_title_fa',
            field=models.CharField(max_length=355, null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='address_en',
            field=models.CharField(max_length=555, null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='address_fa',
            field=models.CharField(max_length=555, null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='blog_title1_en',
            field=models.CharField(max_length=455, null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='blog_title1_fa',
            field=models.CharField(max_length=455, null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='blog_title2_en',
            field=models.CharField(max_length=455, null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='blog_title2_fa',
            field=models.CharField(max_length=455, null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='blog_title3_en',
            field=models.CharField(max_length=455, null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='blog_title3_fa',
            field=models.CharField(max_length=455, null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='des_title1_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='des_title1_fa',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='des_title2_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='des_title2_fa',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='des_title3_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='des_title3_fa',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='name1_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='name1_fa',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='name2_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='name2_fa',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='name3_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='name3_fa',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='wcid_des1_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='wcid_des1_fa',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='wcid_des2_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='wcid_des2_fa',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='wcid_des3_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='wcid_des3_fa',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='what_can_i_do_title1_en',
            field=models.CharField(max_length=355, null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='what_can_i_do_title1_fa',
            field=models.CharField(max_length=355, null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='what_can_i_do_title2_en',
            field=models.CharField(max_length=355, null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='what_can_i_do_title2_fa',
            field=models.CharField(max_length=355, null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='what_can_i_do_title3_en',
            field=models.CharField(max_length=355, null=True),
        ),
        migrations.AddField(
            model_name='vars',
            name='what_can_i_do_title3_fa',
            field=models.CharField(max_length=355, null=True),
        ),
    ]
