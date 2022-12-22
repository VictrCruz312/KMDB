from django.db import models
import uuid

from movies.models import Movie
from users.models import User


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(null=True, default=False)

    movie = models.ForeignKey(Movie, related_name="reviews", on_delete=models.CASCADE)

    critic = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
