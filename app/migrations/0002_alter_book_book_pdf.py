# Generated by Django 3.2.7 on 2021-09-29 16:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_pdf',
            field=models.FileField(upload_to='book_pdf', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='Book_PDF'),
        ),
    ]
