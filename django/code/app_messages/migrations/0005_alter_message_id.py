# Generated by Django 3.2.9 on 2021-11-26 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_messages', '0004_auto_20211126_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
