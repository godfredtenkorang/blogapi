from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='img')
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})
    
    def get_image(self):
        if self.image:
            return 'https://godey-api.xyz/' + self.image.url
        return ''
