# Generated by Django 2.1 on 2019-11-11 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
