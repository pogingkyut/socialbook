# Generated by Django 4.1.4 on 2023-01-27 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_post_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user_id',
            field=models.IntegerField(blank=True),
        ),
    ]