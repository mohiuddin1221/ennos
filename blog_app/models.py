from django.db import models
from django.utils.text import slugify

# Create your models here.
class services(models.Model):
    icon = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    Description = models.TextField()
    
    class Meta:
        db_table  = "Services Area" 
    
    def __str__(self) :
        return self.title
    
class Team(models.Model):
    title = models.CharField(max_length=30)
    designation = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='static/assets/img/team_images/')
    
    def __str__(self) :
        return self.title
     
     
class Testimonials(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    designation = models.TextField()
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    title = models.CharField(max_length =30)
    def __str__(self):
        return self.title
    
    
class protfolio(models.Model):
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length =20)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='static/assets/img/team_images/')
    def __str__(self):
        return self.title
    
    
class contact(models.Model):
    name = models.CharField(max_length= 50)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    
    def __str__(self) :
        return self.subject
    
    

    
    
    
