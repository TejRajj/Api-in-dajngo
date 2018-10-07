from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    title = models.TextField(null=False, blank=False)
    status = models.CharField(default=True, max_length=50)
    create_by = models.ForeignKey(User, null=True, blank = True, on_delete=models.CASCADE)

    start_date= models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title