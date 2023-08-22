# Generated by Django 4.2.2 on 2023-07-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_rename_birthdate_patient_birthofdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mother',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='occupation',
            field=models.TextField(),
        ),
    ]
