from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Category', related_name='posts')
