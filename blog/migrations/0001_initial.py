# Generated by Django 4.2.4 on 2023-09-19 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_post', models.CharField(max_length=50, verbose_name='Заголовок статьи')),
                ('content_post', models.CharField(max_length=3500, verbose_name='Содержание статьи')),
                ('image_post', models.ImageField(blank=True, null=True, upload_to='preview', verbose_name='Изображение')),
                ('data_post', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('publ_on_off', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('views_count', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('slug', models.CharField(blank=True, max_length=50, null=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
