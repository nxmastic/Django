from django.db import models

class Account(models.Model):
    userID = models.CharField(max_length=15, unique=True, primary_key=True)
    password = models.CharField(max_length=15)
    nick = models.CharField(max_length=10)
