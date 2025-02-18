# Generated by Django 5.0.6 on 2024-05-16 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="JournalModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description_uz", models.TextField()),
                ("description_ru", models.TextField()),
                ("logo", models.ImageField(upload_to="images/")),
                ("document_uz", models.FileField(upload_to="docs/")),
                ("document_ru", models.FileField(upload_to="docs/")),
            ],
            options={
                "verbose_name": "Journal",
                "verbose_name_plural": "Journals",
                "db_table": "journal",
            },
        ),
    ]
