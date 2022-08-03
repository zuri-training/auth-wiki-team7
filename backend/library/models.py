from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.




class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    libary_intro = models.TextField(default='Library Introduction')
    library_content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    adminupload = models.FileField(upload_to='media', default='DEFAULT VALUE')
    likes = models.ManyToManyField(User, related_name='likes', blank=True, default=[0])
    unlikes = models.ManyToManyField(User, related_name='unlikes', blank=True, default=[0])
    
    
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_added']


    def total_likes(self):
        return self.likes.count()

    def total_unlikes(self):
        return self.unlikes.count()      





class Comment(models.Model): 
    library = models.ForeignKey(Post, on_delete = models.CASCADE, related_name ='comments')
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField() 
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added'] 

    def __str__(self):
        return self.content 

   
        

   