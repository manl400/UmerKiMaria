from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    ImageURL = models.CharField(max_length=255, default='https://i.imgur.com/CcY947L.jpg')
    timeline = models.TextField()
    dressCode = models.TextField()
    duration = models.DurationField()
    date = models.DateTimeField()
    
    def __str__(self):
        return self.title
