# Generated by Django 3.2.3 on 2021-07-09 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=2, max_length=254, unique=True, verbose_name='ایمیل'),
            preserve_default=False,
        ),
    ]
