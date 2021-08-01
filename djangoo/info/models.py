from django.db import models

# Create your models here.
class infoclass(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phonenumber = models.IntegerField()
    image = models.ImageField(default='defualt.jpg',blank=True)
    
    
    
def __str__(self):
    return self.firstname    
   

 
 
    