# Generated by Django 4.1.3 on 2022-12-08 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hello', '0002_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField(max_length=1000)),
            ],
        ),
    ]