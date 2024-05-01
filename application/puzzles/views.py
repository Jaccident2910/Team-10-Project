from os import path
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from .checker import checkAnswer
from accounts.models import Account
from django.contrib.auth.models import User
from accounts.apps import puzzlePerms
import pickle

def viewpuzzle(request, puzzle_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("accounts:signup"))
    if request.user.account.solved_puzzles:
        solved_puzzles = pickle.loads(request.user.account.solved_puzzles)
        if puzzle_id in solved_puzzles:
            return HttpResponseRedirect(reverse("puzzles:error", args=(puzzle_id,)))
    puzzle_path = path.join(path.dirname(__file__), f"templates/puzzleContent/{puzzle_id}.html")
    with open(puzzle_path, "r") as puzzle_file:
        puzzle_content = puzzle_file.read()
    context = {"puzzle_content": puzzle_content, "puzzle_id": puzzle_id, "puzzle_path": puzzle_path}
    return render(request, "puzzles/viewpuzzle.html", context)
# Create your views here.

def download_7_input(request):
    # fill these variables with real values
    fl_path = path.join(path.dirname(__file__), f"static/puzzleData/7_input.txt")
    filename = "Puzzle 7 Input"

    fl = open(fl_path, "r")
    #mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def download_9_input(request):
    # fill these variables with real values
    fl_path = path.join(path.dirname(__file__), f"static/puzzleData/9_input.txt")
    filename = "Puzzle 9 Input"

    fl = open(fl_path, "r")
    #mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def download_5_input(request):
    # fill these variables with real values
    fl_path = path.join(path.dirname(__file__), f"static/puzzleData/5_input.txt")
    filename = "Puzzle 5 Input"

    fl = open(fl_path, "r")
    #mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def download_6_input(request):
    # fill these variables with real values
    fl_path = path.join(path.dirname(__file__), f"static/puzzleData/6_input.txt")
    filename = "Puzzle 6 Input"

    fl = open(fl_path, "r")
    #mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def answer(request, puzzle_id):
    if request.user.account.solved_puzzles:
        solved_puzzles = pickle.loads(request.user.account.solved_puzzles)
    else:
        solved_puzzles = set()
    if puzzle_id in solved_puzzles:
        return HttpResponseRedirect(reverse("puzzles:error", args=(puzzle_id,)))
    try:
        correct = checkAnswer(puzzle_id, request.POST["answer"])
    except KeyError:
        return HttpResponseNotFound
    if correct:
        user = request.user
        account = Account.objects.get(user=user)
        account.puzzles_finished = account.puzzles_finished + 1
        solved_puzzles.add(puzzle_id)
        account.solved_puzzles = pickle.dumps(solved_puzzles)
        account.save()
        return HttpResponseRedirect(reverse("puzzles:correct", args=(puzzle_id,)))
    else:
        return HttpResponseRedirect(reverse("puzzles:incorrect", args=(puzzle_id,)))

def correct(request, puzzle_id):
    context = {"puzzle_id": puzzle_id}
    return render(request, "puzzles/correct.html/", context)

def incorrect(request, puzzle_id):
    context = {"puzzle_id": puzzle_id}
    return render(request, "puzzles/incorrect.html/", context)

def error(request, puzzle_id):
    context = {"puzzle_id": puzzle_id}
    return render(request, "puzzles/error.html/", context)