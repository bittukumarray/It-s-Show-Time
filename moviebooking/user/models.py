from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator



class Movie(models.Model):
    name = models.CharField(max_length = 200)
    genre = models.CharField(max_length = 100)

    def __str__(self):
        return self.name



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10,blank=True,
                             validators=[
                                 RegexValidator(
                                     regex='^[1-9]{1}[0-9]{9}$',
                                     message='Enter a valid phone no',
                                     code='invalid_cell'
                                 ),
                             ]

                             )
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null = True, blank=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username


class Rating(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.movie.name

class Comment(models.Model):
    comment = models.CharField(max_length = 1000)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.movie.name
