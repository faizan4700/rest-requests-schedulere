# Generated by Django 3.1.7 on 2021-03-25 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_celery_beat', '0015_edit_solarschedule_events_choices'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIScheduler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_url', models.CharField(max_length=100)),
                ('request_type', models.CharField(choices=[('get', 'GET'), ('post', 'POST'), ('delete', 'DELETE'), ('put', 'PUT')], default='get', max_length=6)),
                ('request_headers', models.JSONField(blank=True, default=dict, null=True)),
                ('request_body', models.JSONField(blank=True, default=dict, null=True)),
                ('executable_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('done', 'Done'), ('failed', 'Failed')], default='pending', max_length=7)),
                ('task', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_celery_beat.periodictask')),
            ],
        ),
    ]
