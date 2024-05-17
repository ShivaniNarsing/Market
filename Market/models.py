from django.db import models

class Fruit(models.Model):
    name=models.CharField(max_length=100)
    scientific_name=models.CharField(max_length=100)
    medical_use=models.CharField(max_length=200)
    season=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='images')
    cost=models.CharField(max_length=10,blank=True)