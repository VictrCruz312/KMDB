from rest_framework import serializers

from movies.models import Movie
from genres.models import Genre
from genres.serializers import GenreSerializer
import ipdb


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "duration", "premiere", "budget", "overview", "genres"]

    def create(self, validated_data):
        validated_genres = validated_data.pop("genres")

        instance_movie = Movie.objects.create(**validated_data)

        for genre in validated_genres:
            instance_movie.genres.add(Genre.objects.create(**genre))

        return instance_movie
