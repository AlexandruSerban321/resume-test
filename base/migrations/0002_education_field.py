# Generated by Django 4.0.6 on 2022-07-17 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='field',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
