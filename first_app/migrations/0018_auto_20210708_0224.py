# Generated by Django 3.2.3 on 2021-07-07 21:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0017_alter_my_phone_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my',
            name='adress_admin',
            field=models.CharField(max_length=1000, null=True, verbose_name='آدرس و موقعیت '),
        ),
        migrations.AlterField(
            model_name='my',
            name='copy_site',
            field=models.CharField(max_length=200, null=True, verbose_name='توضیح در مورد جواز کپی از سایت'),
        ),
        migrations.AlterField(
            model_name='my',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='توضیحات درباره من'),
        ),
        migrations.AlterField(
            model_name='my',
            name='email_admin',
            field=models.EmailField(max_length=100, null=True, verbose_name='ایمیل ادمین '),
        ),
        migrations.AlterField(
            model_name='my',
            name='logo',
            field=models.ImageField(upload_to='my_images', verbose_name='لوگوی سایت'),
        ),
        migrations.AlterField(
            model_name='my',
            name='name_admin',
            field=models.CharField(max_length=100, null=True, verbose_name='نام و نام خانوادگی ادمین'),
        ),
        migrations.AlterField(
            model_name='my',
            name='phone_admin',
            field=models.CharField(max_length=11, null=True, verbose_name='شماره تماس ادمین '),
        ),
        migrations.AlterField(
            model_name='my',
            name='title',
            field=models.CharField(max_length=200, null=True, verbose_name='مشهوریت سایت با نام'),
        ),
    ]
