# Generated by Django 4.1.2 on 2022-10-29 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_blogs_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='author',
            field=models.CharField(default='', max_length=100),
        ),
    ]
