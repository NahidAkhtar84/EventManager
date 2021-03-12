import os
import random

from ckeditor.fields import RichTextField
from django.db import models
from PIL import Image


# Create your models here.

def image_path(instance, filename):
    base_name, f_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    random_str = ''.join((random.choice(chars)) for _ in range(20))
    return 'blog/blog_img_{randomstring}{ext}'.format(basename=base_name, randomstring=random_str, ext=f_extension)


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    details = RichTextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    images = models.ImageField(blank=True, null=True, upload_to=image_path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.images.path)
        img.save(self.images.path, quality=20, optimize=True)

    def __str__(self):
        return f'{self.title}'

# https://www.youtube.com/watch?v=-yNJk2_mI9o&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=15
# https://www.youtube.com/watch?v=mF5jzSXb1dc&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=22
# https://www.youtube.com/watch?v=ygzGr51dbsY
