# Generated by Django 4.1.2 on 2022-11-03 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postimage', models.ImageField(blank=True, upload_to='posts_pics')),
                ('caption', models.CharField(default='', max_length=1000)),
                ('author', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
