from django.db import models
from ckeditor.fields import RichTextField


LANGUAGE_CHOICES = (
    ('pt','PT'),
    ('en', 'EN'),
    ('es','ES'),
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField()
    created_on = models.DateTimeField()
    header_image = models.ImageField(upload_to="images/")
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='pt')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
