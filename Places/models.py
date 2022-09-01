from django.db import models

# Create your models here.
class Description(models.Model):
    name = models.CharField(max_length=100)
    descrip = models.CharField(max_length=2000)
    img = models.CharField(max_length=720)
    img1 = models.CharField(max_length=2080)
    img2 = models.CharField(max_length=2080)
    img3 = models.CharField(max_length=2080)
    link = models.CharField(max_length=2080)

class Contact(models.Model):
    fname=models.CharField(max_length=122)
    lname=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.email