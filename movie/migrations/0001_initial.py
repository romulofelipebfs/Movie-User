# Generated by Django 5.0.7 on 2024-09-03 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Filme",
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
                ("titulo", models.CharField(max_length=100)),
                ("ano", models.IntegerField(null=True)),
                ("genero", models.CharField(max_length=20)),
                ("diretor", models.CharField(max_length=50)),
                ("slug", models.SlugField(unique=True)),
            ],
        ),
    ]
