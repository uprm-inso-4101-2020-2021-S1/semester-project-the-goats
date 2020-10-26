from django.shortcuts import render
from calendar import HTMLCalendar
from datetime import datetime
from django.utils.safestring import mark_safe
from .models import Event
# Create your views here.



class EventCalendar(HTMLCalendar):
    def __init__(self, events=None):
        super(EventCalendar, self).__init__()
        self.events = events

    def formatday(self, day, weekday, events):

        day_events = events.filter(day__day=day)
        events_html = "<ul>"
        for event in day_events:
            events_html += event.get_absolute_url() + "<br>"
        events_html += "</ul>"
        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # day outside month
        else:
            return '<td class="%s">%d%s</td>' % (self.cssclasses[weekday], day, events_html)

    def formatweek(self, theweek, events):
        s = ''.join(self.formatday(d, wd, events) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s

    def formatmonth(self, theyear, themonth, withyear=True):
        events = Event.objects.filter(day__month=themonth)

        v = []
        a = v.append
        a('<table border="0" cellpadding="0" cellspacing="0" class="month">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week, events))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)







def CalendarView(request, pk, kpk):
    if pk == 0:
        month = datetime.date(datetime.now()).month
    else:
        month = pk
    if kpk == 0:
        year = datetime.date(datetime.now()).year
    else:
        year = kpk

    cal = EventCalendar().formatmonth(year, month, withyear=True).replace('<td ', '<td  width="150" height="150"')

    prev_month = month - 1
    prev_year = year
    next_month = month + 1
    next_year = year

    if prev_month == 0:
        prev_month = 12
        prev_year = year - 1

    if next_month ==13:
        next_month = 1
        next_year = year + 1

    return render(request, 'calendar.html', {'cal': mark_safe(cal), 'prev_month': prev_month, 'prev_year': prev_year,
                                             'next_month': next_month, 'next_year': next_year})