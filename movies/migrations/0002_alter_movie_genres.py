# Generated by Django 4.1 on 2022-12-21 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("genres", "0001_initial"),
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="genres",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="movies", to="genres.genre"
            ),
        ),
    ]
