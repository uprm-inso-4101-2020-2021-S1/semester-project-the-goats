"""MyCalendar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from manager import views as managerViews
from users import views as userViews
from Events import views as eventViews
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', managerViews.home, name='home'),
    path('signup', userViews.signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('friends/add', userViews.addfriend, name='addfriend'),
    path('friends/list', userViews.friendlist,name='friendlist'),
    path('friends/pending', userViews.pendingrequests, name='pendingfriends'),
    path('friends/pending/accept/<int:pk>', userViews.requestaccept, name='acceptfirend'),
    path('friends/pending/decline/<int:pk>', userViews.requestdecline, name='declinefriend'),
    path('calendar', eventViews.CalendarView, name='calendarview')
]
