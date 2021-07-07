# Generated by Django 3.2.5 on 2021-07-05 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=80, unique=True)),
                ('slug', models.CharField(max_length=120, unique=True)),
                ('Description', models.TextField(blank=True)),
                ('category_iamge', models.ImageField(upload_to='images/photos/')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
    ]