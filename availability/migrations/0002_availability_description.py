# Generated by Django 5.2 on 2025-04-25 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('availability', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
