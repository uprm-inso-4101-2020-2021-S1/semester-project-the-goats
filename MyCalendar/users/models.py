from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Connection(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    creator = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE, null=True)
    following = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE, null=True)
    accepted = models.BooleanField(null=True)
    rank = models.CharField(max_length=100, null=True)


