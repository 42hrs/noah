# Generated by Django 2.1.1 on 2018-09-20 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noah_core', '0007_auto_20180919_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='hubmodel',
            name='map_url',
            field=models.TextField(null=True),
        ),
    ]