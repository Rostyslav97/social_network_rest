# Generated by Django 4.0.1 on 2022-02-17 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('counter', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
