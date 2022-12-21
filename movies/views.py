from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.permissions import IsAdmOrReadOnly
from movies.serializers import MovieSerializer
from movies.models import Movie


class MovieView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmOrReadOnly]

    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
