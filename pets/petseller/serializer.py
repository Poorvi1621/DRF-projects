from rest_framework import serializers
from .models import *


class Breedserializer(serializers.Modelserializer):
        
      class Meta:
        model = Breed
        fields='__all__'

class Colorserializer(serializers.Modelserializer):
      
    class Meta:
        model = Color
        fields='__all__'

class Animalsserializer(serializers.Modelserializer):
    
    class Meta:
        model = Animals
        fields='__all__'
    
class Animallocationserializer(serializers.Modelserializer):
    
    class Meta:
        model = Animallocation
        fields='__all__'

class AnimalImagesserializer(serializers.Modelserializer):
   
    class Meta:
        model = AnimalImages
        fields='__all__'

class Categoryserializer(serializers.Modelserializer):
     
     class Meta:
        model = Category
        fields='__all__'
