from django.db import models
from users.models import User

class Post(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    url = models.URLField(blank=True, null=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.ManyToManyField(User, blank=True, related_name="vote")

    def __str__(self):
        return self.title[:30]