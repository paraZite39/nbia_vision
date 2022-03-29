from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=120)
    thumbnail = models.ImageField(upload_to='images/')
    collections = models.ManyToManyField('Collection')
    
    def __str__(self):
        return self.name

class Collection(models.Model):
    name = models.CharField(max_length=120)
    thumbnail = models.ImageField(upload_to='images/')
    date = models.DateTimeField()

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    collection = models.ManyToManyField('Collection')

    def __str__(self):
        return self.title
