# Generated by Django 4.1 on 2022-08-18 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic_name', models.CharField(blank=True, max_length=50, null=True)),
                ('physician_name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
