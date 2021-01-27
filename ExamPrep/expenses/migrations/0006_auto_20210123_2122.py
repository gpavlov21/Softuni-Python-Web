# Generated by Django 3.1.5 on 2021-01-23 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0005_expenses_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='expenses.profile'),
            preserve_default=False,
        ),
    ]
