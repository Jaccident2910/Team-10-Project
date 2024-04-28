from django.urls import path

from . import views


app_name = "puzzles"
urlpatterns = [
    path("<int:puzzle_id>/", views.viewpuzzle, name="viewpuzzle"),
    path("<int:puzzle_id>/answer/", views.answer, name="answer"),
    path("<int:puzzle_id>/correct/", views.correct, name="correct"),
    path("<int:puzzle_id>/incorrect/", views.incorrect, name="incorrect"),
    path("<int:puzzle_id>/error/", views.error, name="error"),
]