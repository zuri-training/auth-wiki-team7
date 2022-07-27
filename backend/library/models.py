from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    libary_intro = models.TextField(default='Library Introduction')
    library_content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    adminupload = models.FileField(upload_to='media', default='DEFAULT VALUE')
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_added']


class Comment(models.Model): 
    library = models.ForeignKey(Post, on_delete = models.CASCADE, related_name ='comments')
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField() 
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added'] 
        

   