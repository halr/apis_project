from django.db import models
from django.utils import timezone

# Create your models here.
class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"


class Thing(models.Model):
    name = models.CharField(max_length=255, null=False)
    location = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} at {}".format(self.name, self.location)