from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=25)
    city_image = models.ImageField(upload_to=STATIC_ROOT, blank=True, null=True)
    # we will see how this works 

    def __str__(self):
        return self.name 
        
    class Meta:
        verbose_name_plural = 'cities'
    
