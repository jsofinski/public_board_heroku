# Generated by Django 3.2.9 on 2021-11-26 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_messages', '0003_auto_20211126_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_text',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='message',
            name='pub_date',
            field=models.DateField(),
        ),
    ]
