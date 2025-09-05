from django.db import models

class Mail(models.Model):
    mail=models.EmailField()  #mailname
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=12)
    place=models.CharField(max_length=100)
    #models la modify pannaum


