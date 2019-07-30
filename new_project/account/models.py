<<<<<<< HEAD
from django.db import models

class Account(models.Model):
    userID = models.CharField(max_length=15, unique=True, primary_key=True)
    password = models.CharField(max_length=15)
    nick = models.CharField(max_length=10)


# Create your models here.
=======
from django.db import models

class Account(models.Model):
    userID = models.CharField(max_length=15, unique=True, primary_key=True)
    password = models.CharField(max_length=15)
    nick = models.CharField(max_length=10)


# Create your models here.
>>>>>>> 2480c54b8f7df51e28a370924a66f630a3ddc302
