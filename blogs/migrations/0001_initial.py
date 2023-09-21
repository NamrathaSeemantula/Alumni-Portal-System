# Generated by Django 4.1.2 on 2022-10-24 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogtopic', models.CharField(max_length=200, unique=True)),
                ('blogcontent', models.CharField(max_length=1000, unique=True)),
            ],
        ),
    ]