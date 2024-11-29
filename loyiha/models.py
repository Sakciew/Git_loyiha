from django.db import models
from django.urls import reverse
from django.conf import settings

class Category(models.Model):
    objects = None
    name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts/', null=True)

    def __str__(self):
        return self.name

class Region(models.Model):
    objects = None
    name=models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class New(models.Model):
    objects = None
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=300)
    text = models.TextField()
    image = models.ImageField(upload_to='posts/')
    date = models.DateField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.pk)])


    
    