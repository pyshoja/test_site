# Generated by Django 3.2.3 on 2021-07-01 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210629_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images', verbose_name='عکس پرسنلی'),
        ),
    ]
