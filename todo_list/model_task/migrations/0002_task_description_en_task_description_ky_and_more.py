# Generated by Django 5.1.3 on 2024-11-28 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='title_ky',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
