from django.shortcuts import render
from .models import UserProfile, Rating, Movie, Comment
from django.contrib.auth.models import User

# Create your views here.
def Index(request):
    movie = Movie.objects.all()
    rating = Rating.objects.all()
    comment = Comment.objects.all()
    userprofile = UserProfile.objects.all()

    return render(request, 'user/index.html', {'movie': movie, 'rating': rating, 'comment': Comment, 'userprofile': UserProfile})
