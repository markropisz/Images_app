from django.db import models

class TreePicture(models.Model):
    title   = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='uploads/')

    def get_absolute_url(self):
        return reverse("pictures:detail", kwargs={"id": self.id})


# Create your models here.
