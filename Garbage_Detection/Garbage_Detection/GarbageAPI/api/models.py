from django.db import models

# Create your models here.

class SImg(models.Model):
    img = models.FileField(upload_to="img/")

class DImg(models.Model):
    # img = models.OneToOneField(SImg,on_delete=models.CASCADE)
    detect = models.CharField(max_length=1000,null=True)
