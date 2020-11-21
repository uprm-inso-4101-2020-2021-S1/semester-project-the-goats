from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.urls import reverse
# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=50)
    day = models.DateField(editable=True, null=True)
    start = models.TimeField(editable=True, null=True)
    end = models.TimeField(editable=True, null=True)
    description = models.TextField()
    creator = models.ForeignKey(User, related_name="events", on_delete=models.CASCADE, null=True)
    rank = models.CharField(max_length=100)

    def check_overlap(self, existing_start, existing_end, new_start, new_end):
        overlap = False
        if existing_start == new_end or existing_end == new_start:
            overlap = False
        elif (existing_start <= new_start <= existing_end) or (existing_start <= new_end <= existing_end):
            overlap = True
        elif new_start <= existing_start and new_end >= existing_end:
            overlap = True

        return overlap
    def clean(self):
        if self.end <= self.start:
            raise ValidationError('Ending time must be after start time')

        events = Event.objects.filter(day=self.day, creator=self.creator)

        for event in events:
            if self.check_overlap(event.start, event.end, self.start, self.end):
                raise ValidationError('There is time overlap with another event.')

    def get_absolute_url(self):
        # url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        url = reverse('eventview', args=[self.pk])
        return u'<a href="%s">%s</a>' % (url, str(self.start))
