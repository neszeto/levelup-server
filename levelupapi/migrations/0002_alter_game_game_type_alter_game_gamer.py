# Generated by Django 4.1.2 on 2022-11-03 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_by_type', to='levelupapi.gametype'),
        ),
        migrations.AlterField(
            model_name='game',
            name='gamer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_games', to='levelupapi.gamer'),
        ),
    ]
