from rest_framework import generics, response, status
from rest_framework.permissions import SAFE_METHODS
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404

generics.RetrieveAPIView
from movies.models import Movie
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from users.permissions import IsAdmOrCritic
import ipdb


class ReviewView(generics.ListCreateAPIView, generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmOrCritic]

    serializer_class = ReviewSerializer
    lookup_url_kwarg = "movie_id"

    def get_queryset(self):
        return Review.objects.filter(movie_id=self.kwargs[self.lookup_url_kwarg])

    def perform_create(self, serializer):
        movie = get_object_or_404(Movie, pk=self.kwargs[self.lookup_url_kwarg])
        return serializer.save(critic=self.request.user, movie=movie)
