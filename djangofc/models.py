from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    nickname = models.CharField(max_length=100)
    twitter = models.CharField(max_length=50)
    previous_club = models.CharField(max_length=100)
    joined = models.PositiveIntegerField()
    fav_player = models.CharField(max_length=100)
    fav_club = models.CharField(max_length=100)
    img = models.ImageField()


    def __str__(self):
        return self.name
    
