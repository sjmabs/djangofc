# Generated by Django 4.2.6 on 2023-10-20 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=100)),
                ('twitter', models.CharField(max_length=50)),
                ('previous_club', models.CharField(max_length=100)),
                ('joined', models.PositiveIntegerField()),
                ('fav_player', models.CharField(max_length=100)),
                ('fav_club', models.CharField(max_length=100)),
            ],
        ),
    ]