from django.db import models

# Create your models here.

class DaiLi(models.Model):
    country = models.CharField(max_length=50)
    ipaddress = models.CharField(max_length=50)
    port = models.IntegerField()
    serveraddr = models.CharField(max_length=20)
    isanonymous = models.CharField(max_length=10)
    type = models.CharField(max_length=20)
    alivetime = models.CharField(max_length=20)
    verifictiontime = models.CharField(max_length=20)

    def __str__(self):
        return self.ipaddress
