# Generated by Django 3.1.3 on 2021-02-06 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_comment_emotion'),
    ]

    operations = [
        migrations.AddField(
            model_name='recomment',
            name='emotion',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]