from django.db import models
from django.contrib.auth.models import User


'''
class Account(User):
    puzzles_finished = models.IntegerField
'''


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    puzzles_finished = models.IntegerField()
    

    def __str__(self):
        return self.user.username
    
    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in Account._meta.fields]




'''
puzzleGroups = []

for i in range(0,15):
    newGroup = Group("Puzzle " + i, [])
    for j in range(0,i):
        newPermission = Permission()
        newGroup.permissions.add()
    puzzleGroups.insert(i, )
'''