from os import path
from django.shortcuts import render
from django.http import HttpResponseRedirect

def viewpuzzle(request, puzzle_id):
    puzzle_path = path.join(path.dirname(__file__), f"puzzleContent/{puzzle_id}.html")
    with open(puzzle_path, "r") as puzzle_file:
        puzzle_content = puzzle_file.read()
    context = {"puzzle_content": puzzle_content, "puzzle_id": puzzle_id}
    return render(request, "puzzles/viewpuzzle.html", context)
# Create your views here.

def answer(request, puzzle_id):
    return HttpResponseRedirect("puzzles:viewpuzzle", args=(puzzle_id))