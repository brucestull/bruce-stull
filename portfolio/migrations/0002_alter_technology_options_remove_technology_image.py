# Generated by Django 4.1.9 on 2023-05-28 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='technology',
            options={'verbose_name_plural': 'technologies'},
        ),
        migrations.RemoveField(
            model_name='technology',
            name='image',
        ),
    ]