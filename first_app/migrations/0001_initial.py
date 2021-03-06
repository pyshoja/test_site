# Generated by Django 3.2.3 on 2021-05-30 15:40

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='My',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_site', models.CharField(max_length=100, null=True, verbose_name='نام سایت')),
                ('name_admin', models.CharField(max_length=100, null=True, verbose_name='نام ادمین')),
                ('time_start', models.DateTimeField(null=True, verbose_name='سال افتتاح سایت')),
                ('title', models.CharField(max_length=200, null=True, verbose_name='عنوان کسب و کار')),
                ('copy_site', models.CharField(max_length=200, null=True, verbose_name='جواز کپی')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='توضیحات سایت')),
                ('logo', models.ImageField(upload_to='media/my_images', verbose_name='لوگوی من')),
            ],
            options={
                'verbose_name': '* ادمین سایت *',
                'verbose_name_plural': '* ادمین سایت *',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان اسلایدر')),
                ('image', models.ImageField(upload_to='media/slid_images')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدر',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='عنوان')),
                ('slug', models.SlugField(max_length=100, null=True, unique=True, verbose_name='آدرس')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='توضیحات')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/post_images', verbose_name='عکس')),
                ('status', models.BooleanField(null=True, verbose_name='نمایش برای کاربران عمومی')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='first_app.category', verbose_name='زیر دسته')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
    ]
