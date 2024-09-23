from django.db import models

class Book(models.Model):
  title = models.CharField(max_length=255) 

  def __str__(self):
    return self.title
  

class Page(models.Model):
  title= models.ForeignKey(Book, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='images/', null=True, blank=True)
  english = models.TextField()
  indonesian = models.TextField()

  def __str__(self):
    return self.english
