# ratings/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Movie, Rating
from .forms import RatingForm
from .forms import UserForm, MovieForm


def rating_list(request):
    ratings = Rating.objects.all().select_related('user_id', 'movie_id')
    print(ratings)
    return render(request, 'ratings/rating_list.html', {'ratings': ratings})

def create_rating(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rating_list')
    else:
        form = RatingForm()
        
    # Query User and Movie names
    users = User.objects.all()
    movies = Movie.objects.all()
    
    # Get user and movie choices as tuples (id, name)
    user_choices = [(user.id, user.user_name) for user in users]
    movie_choices = [(movie.id, movie.movie_name) for movie in movies]
    
    # Update choices in the form's fields
    form.fields['user_id'].choices = user_choices
    form.fields['movie_id'].choices = movie_choices

    return render(request, 'ratings/rating_form.html', {'form': form})

def update_rating(request, pk):
    rating = get_object_or_404(Rating, pk=pk)
    
    if request.method == 'POST':
        form = RatingForm(request.POST, instance=rating)
        if form.is_valid():
            form.save()
            return redirect('rating_list')
    else:
        form = RatingForm(instance=rating)
    
    # Query User and Movie names
    users = User.objects.all()
    movies = Movie.objects.all()
    
    # Get user and movie choices as tuples (id, name)
    user_choices = [(user.id, user.user_name) for user in users]
    movie_choices = [(movie.id, movie.movie_name) for movie in movies]
    
    # Update choices in the form's fields
    form.fields['user_id'].choices = user_choices
    form.fields['movie_id'].choices = movie_choices

    return render(request, 'ratings/rating_form.html', {'form': form})

def delete_rating(request, pk):
    rating = get_object_or_404(Rating, pk=pk)
    if request.method == 'POST':
        rating.delete()
        return redirect('rating_list')
    print(rating)
    return render(request, 'ratings/rating_confirm_delete.html', {'rating': rating})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rating_list')  # Redirect to the ratings list or another appropriate page
    else:
        form = UserForm()
    print(form)
    return render(request, 'ratings/user_form.html', {'form': form})

def create_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rating_list')  # Redirect to the ratings list or another appropriate page
    else:
        form = MovieForm() 
    print
    return render(request, 'ratings/movie_form.html', {'form': form})
