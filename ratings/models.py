# ratings/models.py
from django.db import models

#class User(models.Model):
#    name = models.CharField(max_length=100)
#
#class Movie(models.Model):
#    title = models.CharField(max_length=100)
#
#class Rating(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#    rating = models.DecimalField(max_digits=3, decimal_places=1)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_age = models.IntegerField()
    user_name = models.CharField(max_length=50)
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=50)
class Rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
