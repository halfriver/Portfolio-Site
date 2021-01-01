from django.db import models


class ContactDisplay(models.Model):

    def __str__(self):
        return self.name
