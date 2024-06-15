# Generated by Django 4.2 on 2024-06-13 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("leftkomendacje", "0002_bookmark_is_archived_bookmark_is_duplicate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="parent_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="leftkomendacje.comment",
            ),
        ),
    ]
