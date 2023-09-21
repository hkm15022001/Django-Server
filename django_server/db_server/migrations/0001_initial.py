# Generated by Django 4.2 on 2023-09-21 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1)),
                ('email', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('user_role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='registername',
            fields=[
                ('token', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_server.user')),
            ],
        ),
        migrations.CreateModel(
            name='device_model',
            fields=[
                ('device_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('device_name', models.CharField(max_length=255)),
                ('plate_no', models.CharField(max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_server.user')),
            ],
        ),
    ]
