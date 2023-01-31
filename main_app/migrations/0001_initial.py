# Generated by Django 4.1.5 on 2023-01-31 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('stock', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('printed', models.IntegerField()),
            ],
        ),
    ]
