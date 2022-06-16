from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import uuid

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 200)
    thumbnail = models.ImageField(null = True)
    body = RichTextUploadingField()
    slug = models.SlugField(null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = True)


    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = True)


    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    subject = models.CharField(max_length = 200)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = True)

    def __str__(self):
        return self.name