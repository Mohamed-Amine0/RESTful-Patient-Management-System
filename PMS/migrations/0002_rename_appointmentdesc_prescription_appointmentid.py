# Generated by Django 4.2.7 on 2023-11-26 12:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("PMS", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="prescription",
            old_name="appointmentDesc",
            new_name="appointmentId",
        ),
    ]
