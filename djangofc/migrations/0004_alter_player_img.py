# Generated by Django 4.2.6 on 2023-10-20 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangofc', '0003_alter_player_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
