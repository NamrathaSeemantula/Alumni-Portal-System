# Generated by Django 4.1.2 on 2022-11-29 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventTopic', models.CharField(max_length=300)),
                ('eventDesc', models.CharField(max_length=3000)),
                ('eventImg', models.ImageField(blank=True, upload_to='event_pics')),
            ],
        ),
    ]
