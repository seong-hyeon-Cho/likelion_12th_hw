from django.db import models

# Create your models here.

class Post(models.Model):
    title= models.CharField(max_length=50)
    stitle= models.CharField(max_length=10)
    writer= models.CharField(max_length=30)
    body= models.TextField()
    pub_date= models.DateTimeField()
    image= models.ImageField(upload_to="blog/", blank=True, null=True)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20] 
