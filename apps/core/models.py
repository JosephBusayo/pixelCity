from django.db import models

class wallpaper(models.Model):
    img = models.ImageField(upload_to='')
    description = models.CharField(max_length=150)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
