# Generated by Django 3.1.3 on 2021-02-07 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_merge_20210207_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='introduce_text',
            field=models.TextField(blank=True),
        ),
    ]
