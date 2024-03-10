# Generated by Django 4.1.13 on 2024-03-09 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('Comments', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Feedback',
            },
        ),
    ]
