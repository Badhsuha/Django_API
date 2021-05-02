from django.db import models

class Advisor(models.Model):
    name = models.CharField(max_length=120)
    photo_url = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=125, unique=True)
    password = models.CharField(max_length=225)

    def __str__(self):
        return self.name
class Booking(models.Model):
    dateTime = models.CharField(max_length=120)
    adv_id = models.ForeignKey(Advisor, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.dateTime
