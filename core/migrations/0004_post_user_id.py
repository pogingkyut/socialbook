# Generated by Django 4.1.5 on 2023-01-27 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_post_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]
