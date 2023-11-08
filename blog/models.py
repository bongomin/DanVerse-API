from django.db import models
from userAuth.models import CustomUser as User

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    video = models.FileField(upload_to='post_videos/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    loves = models.ManyToManyField(User, related_name='loved_posts', blank=True)
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True)

    def total_likes(self):
        return self.likes.count()

    def total_loves(self):
        return self.loves.count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=400)
    created_at = models.DateField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
