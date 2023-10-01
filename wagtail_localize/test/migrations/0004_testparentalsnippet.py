# Generated by Django 3.2.5 on 2022-05-06 18:53

import uuid

import django.db.models.deletion
import modelcluster.fields

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wagtail_localize_test", "0003_wagtail_3_use_json_field"),
    ]

    operations = [
        migrations.CreateModel(
            name="TestParentalSnippet",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "translation_key",
                    models.UUIDField(default=uuid.uuid4, editable=False),
                ),
                (
                    "field",
                    modelcluster.fields.ParentalManyToManyField(
                        blank=True, to="wagtail_localize_test.TestUUIDModel"
                    ),
                ),
                (
                    "locale",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="wagtailcore.locale",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "unique_together": {("translation_key", "locale")},
            },
        ),
    ]