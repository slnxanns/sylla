from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Define roles for users
    AUTHOR = 'Author'
    COLLABORATOR = 'Collaborator'

    ROLE_CHOICES = (
        (AUTHOR, 'Author'),
        (COLLABORATOR, 'Collaborator'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=AUTHOR)

    def __str__(self):
        return self.username



class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    content = models.TextField()

    def __str__(self):
        return self.title


