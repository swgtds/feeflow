# Generated by Django 5.0.2 on 2024-02-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0008_delete_addstudentdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeesTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n', models.CharField(max_length=100)),
                ('stdr', models.PositiveSmallIntegerField()),
                ('stId', models.CharField(max_length=100)),
                ('jan', models.BooleanField()),
                ('feb', models.BooleanField()),
                ('mar', models.BooleanField()),
                ('april', models.BooleanField()),
                ('may', models.BooleanField()),
                ('june', models.BooleanField()),
                ('july', models.BooleanField()),
                ('aug', models.BooleanField()),
                ('sept', models.BooleanField()),
                ('oct', models.BooleanField()),
                ('nov', models.BooleanField()),
                ('dec', models.BooleanField()),
            ],
            options={
                'db_table': 'FeesTracker',
            },
        ),
    ]