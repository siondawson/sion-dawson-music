from django.contrib.auth.models import User 
from django.db import models

class Ensemble(models.Model):
    name = models.CharField(max_length=50)
    num_slots = models.PositiveIntegerField(default=0)  

    def __str__(self):
        return self.name

class BandName(models.Model):
    name = models.CharField(max_length=255, unique=True)  # The brand name of the band

    def __str__(self):
        return self.name
    

class Event(models.Model):
    date = models.DateField()  # Required
    venue_name = models.CharField(max_length=255)  # Required
    postcode = models.CharField(max_length=20, blank=True, null=True)  # Optional
    arrival_time = models.TimeField(blank=True, null=True)  # Optional
    start_time = models.TimeField(blank=True, null=True)  # Optional
    finish_time = models.TimeField(blank=True, null=True)  # Optional
    ensemble = models.ForeignKey(Ensemble, on_delete=models.SET_NULL, null=True, blank=True)  # Optional
    band_name = models.ForeignKey('BandName', on_delete=models.SET_NULL, null=True, blank=True)  # Optional
    requests = models.TextField(blank=True, null=True)  # Optional


    def __str__(self):
        return f"{self.ensemble.name} Event on {self.date}"

    def create_slots(self):
        """Automatically create slots based on ensemble type"""
        num_slots = self.ensemble.num_slots
        for i in range(1, num_slots + 1):
            Slot.objects.create(event=self, slot_number=i)

class Slot(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='slots')  # Use 'slots' as the reverse name
    slot_number = models.IntegerField()
    musician = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Link to the user (musician)

    def __str__(self):
        return f"Slot {self.slot_number} for {self.event.venue_name}"

    def assign_musician(self, user):
        self.musician = user
        self.save()



