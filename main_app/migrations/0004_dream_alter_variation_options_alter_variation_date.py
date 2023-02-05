# Generated by Django 4.1.5 on 2023-02-02 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_variation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band', models.CharField(max_length=50)),
                ('stock', models.CharField(max_length=20)),
                ('tour', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='variation',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='variation',
            name='date',
            field=models.DateField(verbose_name='date printed'),
        ),
    ]