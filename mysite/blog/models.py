from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings


# class Voetbalspelers(models.Model):
#     naam = models.CharField(max_length=100)
#     actuele_club = models.CharField(max_length=100)
#     auteur = models.ForeignKey(User, on_delete=models.CASCADE)
#     datum_invoer = models.DateTimeField(default=timezone.now)
#     datum_laatste_aanpassing = models.DateTimeField(auto_now=True)
#     leeftijd = models.IntegerField()
#     positie = models.CharField(max_length=50)

#     def save(self, *args, **kwargs):
#         # Hier kun je extra acties uitvoeren vóór het opslaan
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.naam

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save

    def __str__(self):
        return self.title
