from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=25)
    city_image = models.ImageField(upload_to='media', default=None)
    # we will see how this works 

    def __str__(self):
        return self.name 
        
    class Meta:
        unique_together = ['name']
        verbose_name_plural = 'cities'

    
