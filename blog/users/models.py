from django.db import models
from django.contrib.auth.models import User
from PIL  import Image
from project.models import Post, Business
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return " %s Profile" % self.user
    

    def save(self):
        super().save()  #save method of the parent class

        img = Image.open(self.image.path) 

        if img.height > 300 or img.width > 300:
            output_size = (300,300) #maximum picture size
            img.thumbnail(output_size) #resizing our image
            img.save(self.image.path)


