from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genres(models.Model):
    genre=models.CharField(max_length=120,unique=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.genre
    
class Movies(models.Model):
    name=models.CharField(max_length=250,unique=True)
    genre=models.ManyToManyField(Genres,null=True)
    year=models.CharField(max_length=200)
    options={
        ('malayalm','malayalm'),
        ('telungu','telungu'),
        ('tamil','tamil'),
        ('english','english')
    }
    language=models.CharField(max_length=200,choices=options,default='malayalm')
    runtime=models.FloatField()
    poster_image=models.ImageField(upload_to="images",null=True,blank=True)
    description=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
    
class Reviews(models.Model):
    movie=models.ForeignKey(Movies,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    rating=models.PositiveBigIntegerField()