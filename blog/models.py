from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    img = models.ImageField(upload_to='blog/static/images/', blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=50)
    text = models.TextField()
    created = models.DateField(auto_now_add=True)
    # so the comments get deleted when the post does
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}, \"{self.post}\""

