from django.db import models

class ArtPiece(models.Model):
    name = models.CharField(max_length=30, unique=True)
    image = models.ImageField(null=True)
    description = models.TextField(null=True)
    date = models.DateField(null=True)
    tags = models.TextField(null=True)

    def tag_set(self):
        return self.tags.split(",")

    def __str__(self):
        return self.name
