# Generated by Django 3.2.8 on 2021-11-15 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-from_date', '-to_date'], 'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AlterField(
            model_name='event',
            name='comment',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Comment'),
        ),
    ]
