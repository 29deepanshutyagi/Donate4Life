# Generated by Django 4.2.2 on 2023-07-18 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_remove_patient_requirements_alter_patient_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='birthdate',
            new_name='birthofdate',
        ),
    ]