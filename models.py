from django.db import models

# Create your models here.

class Post(models.Model):
    post_name = models.CharField(max_length=50)
    post_location = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    post_date=models.DateField()
    image=models.ImageField(upload_to="tieup/images", default="")

    def __str__(self):
        return self.post_name






