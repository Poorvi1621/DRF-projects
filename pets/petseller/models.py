from django.db import models
from django.contrib.auth.models import User
from .choices import GENDER_CHOICES
import uuid

class BaseModel(models.Model):
    uuid=models.UUIDField(default=uuid.uuid4,primary_key=True)
    created_at= models.DateField(auto_now_add=True)
    updated_at= models.DateField(auto_now_add=True)

    class meta:
        abstract =True

class Category(BaseModel):
    animal_category=models.CharField(max_length=100)

class Breed(BaseModel):
    animal_breed=models.CharField(max_length=100)    

class Color(BaseModel):
    animal_color=models.CharField(max_length=100)        

class Animals(BaseModel):
    
    animal_owner=models.ForeignKey(User, related_name='animals', on_delete=models.CASCADE)
    animal_category=models.ForeignKey(Category,related_name='cat',on_delete=models.CASCADE)
    animal_views=models.IntegerField(default=0)
    animal_likes=models.IntegerField(default=1)
    animal_name=models.CharField(max_length=100)
    animal_desc=models.TextField(default='None')
    animal_breed=models.ManyToManyField(Breed)
    animal_color=models.ManyToManyField(Color)
    animal_slug=models.SlugField(max_length=100,unique=True)
    animal_gender=models.CharField(max_length=100 , choices= GENDER_CHOICES)

    class meta:
        ordering = 'animal_name'
    
class Animallocation(BaseModel):
    animal=models.ForeignKey(Animals, related_name='animal_location', on_delete=models.CASCADE)

class AnimalImages(BaseModel):
    animal=models.ForeignKey(Animals, related_name='animal_img', on_delete=models.CASCADE)
    animal_images=models.ImageField(upload_to='Images')
 