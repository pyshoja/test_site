# Generated by Django 3.2.3 on 2021-05-31 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0008_post_introduction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='media/slid_images', verbose_name='عکس'),
        ),
    ]
