# Generated by Django 3.1.3 on 2021-02-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alarm'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarm',
            name='object_id',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
