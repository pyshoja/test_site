# Generated by Django 3.2.3 on 2021-07-18 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_post_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='لینک یوتیوب یا آپارات'),
        ),
    ]
