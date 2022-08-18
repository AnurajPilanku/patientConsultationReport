# Generated by Django 4.1 on 2022-08-18 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='pdf_form',
            field=models.FileField(default=datetime.datetime(2022, 8, 18, 10, 36, 11, 700020, tzinfo=datetime.timezone.utc), upload_to='generated_pdfs'),
            preserve_default=False,
        ),
    ]
