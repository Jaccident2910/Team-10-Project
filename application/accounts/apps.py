from django.apps import AppConfig

puzzlePerms = []
employerGroup = None
class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    
    def ready(self):
    
    # This sets up the array of permissions that let users access certain puzzles.
        
        from django.contrib.auth.models import User, Group, Permission 
        from django.contrib.contenttypes.models import ContentType

        

        content_type = ContentType.objects.get_for_model(User) 
        # this will almost certainly cause problems later!!
        # I assume this is probably supposed to be our model for a puzzle or something???

        for i in range(0,15):
            newPerm = Permission.objects.get_or_create(
                codename = "puzzle_" + str(i),
                name = "Puzzle " + str(i),
                content_type = content_type,
            )[0]
            puzzlePerms.append(newPerm)





