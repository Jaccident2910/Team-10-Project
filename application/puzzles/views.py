from os import path
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from .checker import checkAnswer
from accounts.models import Account
from django.contrib.auth.models import User
from accounts.apps import puzzlePerms

def viewpuzzle(request, puzzle_id):
    puzzle_path = path.join(path.dirname(__file__), f"templates/puzzleContent/{puzzle_id}.html")
    with open(puzzle_path, "r") as puzzle_file:
        puzzle_content = puzzle_file.read()
    context = {"puzzle_content": puzzle_content, "puzzle_id": puzzle_id, "puzzle_path": puzzle_path}
    return render(request, "puzzles/viewpuzzle.html", context)
# Create your views here.

def download_file_1(request):
    # fill these variables with real values
    fl_path = 'static/puzzleData.1_data'
    filename = "1_data"

    fl = open(fl_path, "r")
    #mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


def answer(request, puzzle_id):
    try:
        correct = checkAnswer(puzzle_id, request.POST["answer"])
    except KeyError:
        return HttpResponseNotFound
    if correct:
        user = request.user
        account = Account.objects.get(user=user)
        if(account.completedPuzzles[puzzle_id]):
            return HttpResponseRedirect(reverse("puzzles:error", args=(puzzle_id,)))
        else:
            account.puzzles_finished = account.puzzles_finished + 1
            account.completedPuzzles[puzzle_id] = True
            account.save()
            #user.user_permissions.add(puzzlePerms[puzzle_id])
            return HttpResponseRedirect(reverse("puzzles:correct", args=(puzzle_id,)))
    else:
        return HttpResponseRedirect(reverse("puzzles:incorrect", args=(puzzle_id,)))

def correct(request, puzzle_id):
    return HttpResponse("Correct")

def incorrect(request, puzzle_id):
    return HttpResponse("Incorrect")

def error(request, puzzle_id):
    return HttpResponse("already completed puzzle " + str(puzzle_id))
