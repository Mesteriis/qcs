# Generated by Django 4.1.7 on 2023-02-26 14:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("files", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Report",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "modified",
                    models.DateTimeField(blank=True, db_index=True, null=True),
                ),
                (
                    "file",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="files.codefile",
                    ),
                ),
                ("result", models.JSONField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("s", "Success"), ("f", "Fail")],
                        default="s",
                        max_length=1,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
