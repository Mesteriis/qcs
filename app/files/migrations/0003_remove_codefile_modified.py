# Generated by Django 4.1.7 on 2023-02-26 18:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("files", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="codefile",
            name="modified",
        ),
    ]
