# Generated by Django 4.2 on 2023-09-21 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_server', '0005_trackandtrace'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trackandtrace',
            name='track_and_trace_id',
        ),
        migrations.AlterField(
            model_name='trackandtrace',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]