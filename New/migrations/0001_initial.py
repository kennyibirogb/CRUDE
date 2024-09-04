# Generated by Django 5.0.6 on 2024-08-21 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField(max_length=255)),
                ('phone', models.IntegerField(blank=True, verbose_name='phone number')),
                ('age', models.IntegerField(blank=True, verbose_name='age')),
            ],
        ),
    ]