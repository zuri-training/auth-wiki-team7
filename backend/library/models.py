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
    likes = models.ManyToManyField(User, related_name='likes', blank=True, default=0)
    unlikes = models.ManyToManyField(User, related_name='unlikes', blank=True, default=0)
    
    
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_added']


    def total_likes(self):
        return self.likes.count()

    def total_unlikes(self):
        return self.unlikes.count()      

    def get_absolute_url(self):
        return reverse('library_detail', args=[self.slug])




#     @property
#     def num_likes(self):
#         return self.liked.all.count()

# LIKE_CHOICES =(
#     ('Like', 'Like'),
#     ('Unlike', 'Unlike')
# )            

# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete = models.CASCADE)
#     library = models.ForeignKey(Post, on_delete = models.CASCADE, related_name ='like')
#     value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)


#     def __str__(self):
#         return str(self.library)







class Comment(models.Model): 
    library = models.ForeignKey(Post, on_delete = models.CASCADE, related_name ='comments')
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField() 
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added'] 
        

   