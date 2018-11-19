"""Users Models"""

#Django
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    """
    Profile Model

    Proxy model that extends the base data with other information
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField()
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username