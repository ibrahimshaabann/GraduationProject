from django.db import models
from django.contrib.auth.models import AbstractUser
from app.manager import UserManager
from PIL import Image
import dhash
class User(AbstractUser):
    def upload_to(instance, filename):
     return 'images/{filename}'.format(filename=filename)

    username = None
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=16)
    bio = models.CharField(max_length=164, null=True)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    # image_hash = models.CharField(max_length=255, blank=True, null=True)


    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()
   

class Post(models.Model):
    def upload_to(instance, filename):
       return 'images/{filename}'.format(filename=filename)

    title = models.CharField(max_length=32)
    description = models.CharField(max_length=164)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image_hash = models.CharField(max_length=255, blank=True, null=True)
   
    def save(self, *args, **kwargs):
        if self.image_url and not self.image_hash:
            # Open the uploaded image
            img = Image.open(self.image_url)
            
            # Calculate the dhash
            row, col = dhash.dhash_row_col(img)
            self.image_hash = dhash.format_hex(row, col)

        super(Post, self).save(*args, **kwargs)

# app/models.py

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    action_taken = models.CharField(max_length=10, null=True, blank=True)  

    def __str__(self):
        return f"{self.user.username} - {self.post}"
    

class PostLike(models.Model):
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("post", "user"), )

class PostComment(models.Model):
    comment_text = models.CharField(max_length=264)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)

class UserFollow(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name="src_follow")
    follows = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name="dest_follow")