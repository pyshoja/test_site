# Generated by Django 3.2.3 on 2021-07-12 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0029_alter_support_title_suppurt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='title_suppurt',
            field=models.IntegerField(choices=[(1, 'مالی سایت'), (2, 'آموزش ها'), (3, 'روند ثبت نام و ورود'), (4, 'پیگیری ها'), (5, 'متفرقه')], null=True, verbose_name='موضوع پیگیری'),
        ),
    ]
