from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Event)
def create_slots(sender, instance, created, **kwargs):
    if created and instance.ensemble:
        # Create slots based on ensemble type
        for i in range(1, instance.ensemble.slots + 1):
            Slot.objects.create(
                event=instance, 
                name=f"Musician {i}"  # Default names, customizable later
            )
