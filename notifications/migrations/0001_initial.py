# Generated by Django 3.1.4 on 2020-12-14 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('name_receiver', models.CharField(max_length=150)),
                ('receiver', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('send_data', models.DateTimeField()),
                ('notification_type', models.CharField(max_length=50)),
                ('send_status', models.BooleanField(default=False)),
                ('id_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notifications.messages')),
            ],
            options={
                'verbose_name_plural': 'Notifications',
            },
        ),
    ]