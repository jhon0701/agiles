from django.db import models


class Complaint(models.Model):

    complainant_name = models.CharField(max_length=60)
    place_event = models.CharField(max_length=120)
    complaint_date = models.DateField(auto_now_add=True)
    event_date = models.DateField()
    event_time = models.TimeField()
    description = models.TextField(blank=True, null=True)
    evidence = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return (
            str(self.id)
            + " - " + self.complainant_name
            + " - " + self.place_event
        )
