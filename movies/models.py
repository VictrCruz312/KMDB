from django.db import models
import uuid
from genres.models import Genre
from users.models import User


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=127)
    duration = models.DurationField()
    premiere = models.DateField()
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    overview = models.TextField(null=True)

    genres = models.ManyToManyField("genres.Genre", related_name="movies")

    user = models.ForeignKey(
        User,
        related_name="movies",
        on_delete=models.CASCADE,
    )
