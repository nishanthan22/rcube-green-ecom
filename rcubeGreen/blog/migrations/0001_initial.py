

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="VisitCounter",
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
                ("count", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="EcoProducts",
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
                ("title", models.CharField(max_length=200, unique=True)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("content", models.TextField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Draft"), (1, "Publish")], default=0
                    ),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="eco_products_posts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_on"],
            },
        ),
        migrations.CreateModel(
            name="GreenInnovation",
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
                ("title", models.CharField(max_length=200, unique=True)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("content", models.TextField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Draft"), (1, "Publish")], default=0
                    ),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="green_innovation_posts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_on"],
            },
        ),
        migrations.CreateModel(
            name="SustainableLiving",
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
                ("title", models.CharField(max_length=200, unique=True)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("content", models.TextField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Draft"), (1, "Publish")], default=0
                    ),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sustainable_living_posts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_on"],
            },
        ),
    ]
