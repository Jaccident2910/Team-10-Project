from django.urls import path

from . import views


app_name = "puzzles"
urlpatterns = [
    path("<int:puzzle_id>/", views.viewpuzzle, name="viewpuzzle"),
    path("<int:puzzle_id>/answer/", views.answer, name="answer"),
    path("<int:puzzle_id>/correct/", views.correct, name="correct"),
    path("<int:puzzle_id>/incorrect/", views.incorrect, name="incorrect"),
    path("<int:puzzle_id>/error/", views.error, name="error"),
    path('download/7_input', views.download_7_input, name='download_7_input'),
    path('download/9_input', views.download_9_input, name='download_9_input'),
    path('download/5_input', views.download_5_input, name='download_5_input'),
    path('download/6_input', views.download_6_input, name='download_6_input')
]