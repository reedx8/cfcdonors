from django.db import models


class Donor_List(models.Model):
    text = models.CharField(max_length=200)
    fileobj = models.FileField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
