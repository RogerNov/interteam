# Generated by Django 2.0.5 on 2018-06-04 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrapartes', '0002_auto_20180521_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='contraparte',
            name='slug',
            field=models.SlugField(default=1, editable=False, max_length=200),
            preserve_default=False,
        ),
    ]