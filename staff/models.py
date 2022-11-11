from django.db import models


# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    symptoms = models.CharField(max_length=300, null=True, blank=True)
    ward = models.CharField(max_length=30, null=True, blank=True)
    time = models.TimeField(max_length=30, null=True, blank=True)
    number = models.DecimalField(decimal_places=0, max_digits=999, default=1)
    level = models.CharField(max_length=30, null=True, blank=True)
    Admitted = models.BooleanField(default=False)
    None_Admitted = models.BooleanField(default=False)

    @property
    def is_Admitted(self):
        return self.Admitted

    @property
    def is_None_Admitted(self):
        return self.None_Admitted

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Note(models.Model):
    patient = models.ForeignKey(Patient, related_name="notes", on_delete=models.CASCADE)
    created_by = models.CharField(max_length=200)
    note = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.patient.name, self.created_by)
