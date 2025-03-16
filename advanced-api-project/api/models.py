from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
        
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)  
    page_count = models.IntegerField(null=True, blank=True)  
    cover_image = models.URLField(null=True, blank=True) 
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title