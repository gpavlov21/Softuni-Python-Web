# Generated by Django 3.1.5 on 2021-01-16 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django102', '0004_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='game2',
            name='players',
            field=models.ManyToManyField(to='django102.Player'),
        ),
    ]
