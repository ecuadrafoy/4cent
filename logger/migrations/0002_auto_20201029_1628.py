# Generated by Django 3.1.1 on 2020-10-29 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traffic',
            name='PIR',
        ),
        migrations.AddField(
            model_name='traffic',
            name='PIR',
            field=models.ManyToManyField(to='logger.PIR'),
        ),
    ]
