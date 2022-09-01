from django.urls import path

from .views import RecipeView


app_name = "recipes"

urlpatterns = [
    path('recipes/', RecipeView.as_view({'get': 'list'})),
    path('recipes/<int:pk>', RecipeView.as_view({'get': 'retrieve'})),

]
