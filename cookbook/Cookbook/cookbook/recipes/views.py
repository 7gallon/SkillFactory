from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Recipe
from .serializaers import RecipeSerializer


class RecipeView(viewsets.ViewSet):
    def list(self, request):
        queryset = Recipe.objects.all()
        serializer = RecipeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Recipe.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = RecipeSerializer(user)
        return Response(serializer.data)



