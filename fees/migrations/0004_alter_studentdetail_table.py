# Generated by Django 5.0.2 on 2024-02-12 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0003_rename_admissiondate_studentdetail_admissiondate_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='studentdetail',
            table='StudentDetail',
        ),
    ]