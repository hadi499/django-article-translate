from django.db import models
from ckeditor.fields import RichTextField

class Book(models.Model):
  title = models.CharField(max_length=255) 

  def __str__(self):
    return self.title
  

class Page(models.Model):
  title= models.ForeignKey(Book, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='images/', null=True, blank=True)
  english = RichTextField(blank=True, null=True)
  indonesian = RichTextField(blank=True, null=True)

  def __str__(self):
    return self.english
