from os import path
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from .checker import checkAnswer

def viewpuzzle(request, puzzle_id):
    puzzle_path = path.join(path.dirname(__file__), f"puzzleContent/{puzzle_id}.html")
    with open(puzzle_path, "r") as puzzle_file:
        puzzle_content = puzzle_file.read()
    context = {"puzzle_content": puzzle_content, "puzzle_id": puzzle_id}
    return render(request, "puzzles/viewpuzzle.html", context)
# Create your views here.

def answer(request, puzzle_id):
    try:
        correct = checkAnswer(puzzle_id, request.POST["answer"])
    except KeyError:
        return HttpResponseNotFound
    if correct:
        return HttpResponseRedirect(reverse("puzzles:correct", args=(puzzle_id,)))
    else:
        return HttpResponseRedirect(reverse("puzzles:incorrect", args=(puzzle_id,)))

def correct(request, puzzle_id):
    return HttpResponse("Correct")

def incorrect(request, puzzle_id):
    return HttpResponse("Incorrect")