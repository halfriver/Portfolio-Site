from django.db import models


class Program(models.Model):
    name = models.CharField(max_length=30, unique=True)
    html = models.CharField(max_length=30, null=True)
    code = models.CharField(max_length=30, null=True)
    demo = models.BooleanField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name
