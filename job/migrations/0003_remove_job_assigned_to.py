# Generated by Django 4.0.2 on 2022-04-26 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0002_job_assigned_to"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="job",
            name="assigned_to",
        ),
    ]
