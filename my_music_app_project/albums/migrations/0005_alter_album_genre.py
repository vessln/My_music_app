# Generated by Django 5.0.2 on 2024-02-22 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0004_alter_album_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(choices=[('Pop Music', 'Pop Music'), ('Jazz Music', 'Jazz Music'), ('R&B Music', 'R&B Music'), ('Rock Music', 'Rock Music'), ('Country Music', 'Country Music'), ('Dance Music', 'Dance Music'), ('Hip Hop Music', 'Hip Hop Music'), ('Other', 'Other')], max_length=30),
        ),
    ]
