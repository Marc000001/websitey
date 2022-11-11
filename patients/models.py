from django.db import models


# Create your models here.


class Personal(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    number = models.DecimalField(decimal_places=0, max_digits=999, default=1)
    level = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name