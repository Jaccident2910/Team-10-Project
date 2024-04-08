from django.urls import path

from . import views

app_name = "puzzles"
urlpatterns = [
    path("<int:puzzle_id>/", views.viewpuzzle, name="viewpuzzle"),
    path("<int:puzzle_id>/answer/", views.answer, name="answer"),
]