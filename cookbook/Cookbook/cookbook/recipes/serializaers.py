from rest_framework import serializers


class RecipeSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    ingredients = serializers.CharField()
    description = serializers.CharField()
