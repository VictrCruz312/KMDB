from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from reviews.models import Review
from reviews.models import Review
import ipdb


class ReviewSerializer(serializers.ModelSerializer):
    critic = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ["id", "stars", "review", "spoilers", "movie_id", "critic"]
        read_only_fields = ["movie_id", "critic"]

    def get_critic(self, obj):
        return {
            "id": obj.critic.id,
            "first_name": obj.critic.first_name,
            "last_name": obj.critic.last_name,
        }

    def create(self, validated_data):
        self.raise_errors_on_nested_writes = True
        if validated_data["stars"] > 5:
            raise ValidationError(
                {"stars": ["Ensure this value is less than or equal to 5."]}
            )
        if validated_data["stars"] < 1:
            raise ValidationError(
                {"stars": ["Ensure this value is greater than or equal to 1."]}
            )

        return Review.objects.create(**validated_data)
