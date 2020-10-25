from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, Http404
import datetime
from .forms import *
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            user.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def friendlist(request):
    user = request.user
    followers = user.followers.all()
    return render(request, 'friend_list.html', {'followers':followers})


@login_required
def addfriend(request):
    if request.method == 'POST':
        form = FriendForm(request.POST)
        user = request.user
        if form.is_valid():
            connection = form.save()
            connection.created = datetime.datetime.now()
            connection.creator = user
            connection.accepted = False
            if connection.following == user:
                connection.delete
            else:
                connection.save()
                return redirect('home')
    form = FriendForm()
    return render(request, 'add_friend.html', {'form': form})


@login_required
def pendingrequests(request):
    user = request.user
    following = user.following.filter(accepted=False)
    return render(request, 'requests.html', {'following': following})


def requestaccept(request, pk):
    connection = Connection.objects.get(pk=pk)
    connection.accepted = True
    connection.save()
    connection2 = Connection(creator=request.user, following=connection.creator, rank=connection.rank, accepted=True)
    connection2.save()
    return redirect('friendlist')


def requestdecline(request, pk):
    connection = Connection.objects.get(pk=pk)
    connection.delete()

    return redirect('friendlist')