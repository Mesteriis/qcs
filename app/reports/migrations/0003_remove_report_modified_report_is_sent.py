# Generated by Django 4.1.7 on 2023-02-26 18:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reports", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="report",
            name="modified",
        ),
        migrations.AddField(
            model_name="report",
            name="is_sent",
            field=models.BooleanField(default=False),
        ),
    ]
