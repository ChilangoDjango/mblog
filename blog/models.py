from django.db import models


# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.modified)

