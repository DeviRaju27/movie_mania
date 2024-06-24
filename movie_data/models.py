from django.db import models

class MovieData(models.Model):
    name = models.CharField(max_length= 150)
    duration = models.FloatField()
    rating = models.FloatField()
    category = models.CharField(max_length=100, default= 'drama')
    image = models.ImageField(upload_to='images', default='images/default.png')

    def __str__(self):
        return f'{self.name}'