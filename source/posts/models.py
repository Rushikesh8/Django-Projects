from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce.models import HTMLField

User = get_user_model()

class PostView(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey('Post',on_delete=models.CASCADE)


    def __str__(self):
        return self.user.Username 


class Author(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    profile_picture = models.ImageField()
    bio = models.CharField(max_length = 300, blank = True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length = 100)
    description = HTMLField()
    timestamp = models.DateTimeField(auto_now_add = True)
    thumbnail = models.ImageField()
    author = models.ForeignKey(Author,on_delete= models.CASCADE)
    categories = models.ForeignKey(Category,on_delete = models.CASCADE)
    previous_post = models.ForeignKey('self', related_name='previous',on_delete= models.SET_NULL, blank= True, null= True)
    next_post = models.ForeignKey('self', related_name='next',on_delete= models.SET_NULL, blank= True, null= True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs = {'id': self.id }) 

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()    



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp =  models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
                  