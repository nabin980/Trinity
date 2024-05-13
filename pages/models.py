from django.db import models
from django.utils import timezone

from users.models import Profile

# Create your models here.

class QuotationRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    quotation_request = models.TextField()
    is_mailed = models.BooleanField(default = False)
    created_at = models.DateTimeField(default = timezone.now)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.name + ' - ' + self.email

class UserExperience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=300, blank=True)
    rating = models.IntegerField(default=0)
    comment = models.TextField()
    picture = models.ImageField(upload_to='user_experience_pics/', blank=True, null=True)
    created_at = models.DateTimeField(default = timezone.now)
    is_published = models.BooleanField(default = False)

    def __str__(self):
        return self.fullname
