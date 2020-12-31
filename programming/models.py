from django.db import models


class Program(models.Model):
    name = models.CharField(max_length=30, unique=True)
    html = models.CharField(max_length=30, null=True, blank=True)
    code = models.FileField(null=True, upload_to="code")
    demo = models.BooleanField(null=True, default=False)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name
