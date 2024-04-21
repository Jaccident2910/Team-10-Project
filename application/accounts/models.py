from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    puzzle_reached = models.IntegerField()

    def __str__(self):
        return self.user.username




'''
puzzleGroups = []

for i in range(0,15):
    newGroup = Group("Puzzle " + i, [])
    for j in range(0,i):
        newPermission = Permission()
        newGroup.permissions.add()
    puzzleGroups.insert(i, )
'''