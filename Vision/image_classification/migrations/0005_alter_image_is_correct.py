# Generated by Django 5.0.2 on 2024-02-12 10:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "image_classification",
            "0004_rename_feedback_created_at_image_created_at_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="is_correct",
            field=models.BooleanField(null=True),
        ),
    ]
