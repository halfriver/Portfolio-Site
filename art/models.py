from django.db import models


class ArtTag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class ArtPiece(models.Model):
    name = models.CharField(max_length=30, unique=True)
    image = models.ImageField(null=True)
    description = models.TextField(null=True)
    date = models.DateField(null=True)
    tags = models.ManyToManyField(ArtTag)

    def __str__(self):
        return self.name
