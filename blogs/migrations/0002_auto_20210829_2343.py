# Generated by Django 3.2.5 on 2021-08-29 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storyandblog',
            name='text_bg_blogs',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='storyandblog',
            name='text_bg_stories',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
    ]
