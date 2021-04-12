# from django.db import models
from django.db import models
class Article(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True  )
    def __str__(self):   #self b class Article eshare darad
        return self.title
    def snippetttt(self):
        return self.body[:49]+'...'


# Create your models here.
