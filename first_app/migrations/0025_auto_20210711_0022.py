# Generated by Django 3.2.3 on 2021-07-10 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0024_alter_post_preview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apiadress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_adress', models.GenericIPAddressField(verbose_name='آدرس آی پی')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', to='first_app.Apiadress', verbose_name='بازدیدها'),
        ),
    ]
