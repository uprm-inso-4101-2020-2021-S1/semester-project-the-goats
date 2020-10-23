from django.shortcuts import render
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe
# Create your views here.


def CalendarView(request):

    cal = HTMLCalendar().formatmonth(2020,10,withyear=True).replace('<td ', '<td  width="150" height="150"')

    return render(request, 'calendar.html', {'cal': cal})