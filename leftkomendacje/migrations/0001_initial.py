# Generated by Django 4.2 on 2024-06-28 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import leftkomendacje.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Bookmark",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_modified_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=200)),
                ("url", models.URLField()),
                ("rating", models.PositiveIntegerField(default=0)),
                ("is_duplicate", models.BooleanField(default=False)),
                ("is_archived", models.BooleanField(default=False)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=models.SET(leftkomendacje.models.get_sentinel_user),
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=200)),
                ("description", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_modified_at", models.DateTimeField(auto_now=True)),
                ("content", models.CharField(max_length=200)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=models.SET(leftkomendacje.models.get_sentinel_user),
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "parent_bookmark",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="leftkomendacje.bookmark",
                    ),
                ),
                (
                    "parent_comment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="leftkomendacje.comment",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="bookmark",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="leftkomendacje.category",
            ),
        ),
    ]
