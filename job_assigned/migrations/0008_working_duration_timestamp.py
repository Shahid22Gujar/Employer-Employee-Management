# Generated by Django 4.0.2 on 2022-04-28 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job_assigned", "0007_alter_working_duration_duration"),
    ]

    operations = [
        migrations.AddField(
            model_name="working_duration",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
