# Generated by Django 3.2.3 on 2021-07-17 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_post_title_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='post_video', verbose_name='فایل ویدئو'),
        ),
        migrations.AlterField(
            model_name='post',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='post_audio', verbose_name='فایل صوتی'),
        ),
    ]
