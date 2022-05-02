from operator import mod
from django.db import models
import os
from django.conf import settings

class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(default="")
    email = models.EmailField(default="")
    man = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = "blog/", blank="True", null="True")  
    
    def __str__(self):
        return self.title  
    
    def summary(self):
        return self.content[:100]

    def delete(self, *args, **kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        super(Blog, self).delete(*args, **kargs)