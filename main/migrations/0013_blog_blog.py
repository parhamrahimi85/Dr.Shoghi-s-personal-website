# Generated by Django 4.2.15 on 2024-08-09 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_blog_blog_title_en_blog_blog_title_fa_blog_des_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Blog',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='main.vars'),
            preserve_default=False,
        ),
    ]
