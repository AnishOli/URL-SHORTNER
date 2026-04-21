from django.db import models

# Create your models here.
class UrlData(models.Model):
    url= models.URLField(max_length=200)
    slug= models.CharField(max_length=10,unique=True,db_index=True)
    clicks = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"Short url for :{self.url} is {self.slug}"
    
    