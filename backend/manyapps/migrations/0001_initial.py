# Generated by Django 5.0.4 on 2024-05-10 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StagingTable",
            fields=[
                (
                    "sales_order",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("engineer", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "staging_status",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("date_drawn", models.DateTimeField(blank=True, null=True)),
                ("no_carton", models.IntegerField(blank=True, null=True)),
                ("last_status_update", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "staging_table",
                "managed": True,
            },
        ),
    ]
