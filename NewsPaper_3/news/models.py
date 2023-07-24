# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.title

    def get_short_text(self):
        return " ".join(self.text.split()[:20]) + "..."

    def get_formatted_date(self):
        return self.pub_date.strftime("%d.%m.%Y")

    def get_absolute_url(self):
        return reverse('news:news_detail', args=[str(self.id)])

