# Generated by Django 3.2.3 on 2021-05-31 11:14

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_alter_category_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان پست')),
                ('slug', models.SlugField(unique=True, verbose_name='آدرس')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='زمان پست')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='توضیحات')),
                ('image', models.ImageField(upload_to='media/post_images', verbose_name='عکس')),
                ('status', models.BooleanField(verbose_name='نمایش برای کاربران عمومی')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.category', verbose_name='زیر دسته')),
            ],
            options={
                'verbose_name': 'پست',
                'verbose_name_plural': 'پست ها',
            },
        ),
    ]
