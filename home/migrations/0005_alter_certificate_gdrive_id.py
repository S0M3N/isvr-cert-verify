# Generated by Django 4.0.6 on 2022-09-14 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_certificate_gdrive_id_alter_certificate_cert_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='gdrive_id',
            field=models.CharField(blank=True, default='1O0EVKgJOKO_Y4MYlz_eKuufdbcSKFsO7', max_length=50, null=True),
        ),
    ]
