# Generated by Django 3.2.3 on 2021-07-19 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id'], 'verbose_name': 'پست', 'verbose_name_plural': 'پست ها'},
        ),
    ]