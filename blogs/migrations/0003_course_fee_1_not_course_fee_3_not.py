# Generated by Django 4.0.6 on 2022-09-23 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_course_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='fee_1_not',
            field=models.CharField(default='14999/-', max_length=10),
        ),
        migrations.AddField(
            model_name='course',
            name='fee_3_not',
            field=models.CharField(default='24999/-', max_length=10),
        ),
    ]
