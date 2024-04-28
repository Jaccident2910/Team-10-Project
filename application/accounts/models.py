from django.db import models
from django.contrib.auth.models import User


'''
class Account(User):
    puzzles_finished = models.IntegerField
'''


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    puzzles_finished = models.IntegerField()
    account_random = models.IntegerField(default="0")
    '''completedPuzzles = []
    for i in range(0,15):account = Account.objects.get(user=user)
    completedPuzzles.append(models.BooleanField(default=False))'''

    '''puzzle0_complete = models.BooleanField(default=False)
    puzzle1_complete = models.BooleanField(default=False)
    puzzle2_complete = models.BooleanField(default=False)
    puzzle3_complete = models.BooleanField(default=False)
    puzzle4_complete = models.BooleanField(default=False)
    puzzle5_complete = models.BooleanField(default=False)
    puzzle6_complete = models.BooleanField(default=False)
    puzzle7_complete = models.BooleanField(default=False)
    puzzle8_complete = models.BooleanField(default=False)
    puzzle9_complete = models.BooleanField(default=False)
    puzzle10_complete = models.BooleanField(default=False)
    puzzle11_complete = models.BooleanField(default=False)
    puzzle12_complete = models.BooleanField(default=False)
    puzzle13_complete = models.BooleanField(default=False)
    puzzle14_complete = models.BooleanField(default=False)'''
    

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