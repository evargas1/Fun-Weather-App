from django.db import models
STATIC_URL = '/static/'
STATIC_ROOT = '/tutorial/site/public/static'

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=25, unique=True)
    city_image = models.ImageField(upload_to='./media/', blank=True, null=True)
    # we will see how this works 

    def __str__(self):
        return self.name 
        
    class Meta:
        unique_together = ['name']
        verbose_name_plural = 'cities'

    
