import os

from django.db import models
from ckeditor.fields import RichTextField
import random
from  django.conf import settings
from font_icons.models import IconForeignKeyField

# Create your models here.

def image_path(instance, filename):
    base_name, f_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    random_str = ''.join((random.choice(chars)) for _ in range(20))
    return 'aboutus/about_img_{randomstring}{ext}'.format(basename=base_name, randomstring=random_str, ext=f_extension)


class about_us(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=image_path, null=True, blank=True)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_image_url(self):
        return "%s/%s" % (settings.MEDIA_URL, self.image)

class sociallinks(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=600)
    icon = IconForeignKeyField(on_delete=True, null=True, blank=True)

    def __str__(self):
        return self.name


class company_address(models.Model):
    title = models.CharField(max_length=100)
    title_desc = models.CharField(max_length=255)
    address_title = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=400)

    def __str__(self):
        return self.title


class copyright(models.Model):
    copyright = models.CharField(max_length=255)

    def __str__(self):
        return self.copyright


