# Generated by Django 4.2.11 on 2024-03-27 15:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("request", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="reference",
            field=models.CharField(max_length=17),
        ),
    ]
