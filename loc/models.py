from django.db import models


class Unit(models.Model):
    text = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.text[:50]

