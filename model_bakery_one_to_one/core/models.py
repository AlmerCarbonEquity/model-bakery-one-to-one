from django.db import models

class Person(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, related_name="person", blank=True, null=True)
    
class Profile(models.Model):
    persons = models.ManyToManyField(Person, related_name="profiles")