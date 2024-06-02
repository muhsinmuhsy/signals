from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Define the signal handler function
@receiver(post_save, sender=MyModel)
def handle_new_mymodel_instance(sender, instance, created, **kwargs):
    if created:
        print("A new instance of MyModel was created with name:", instance.name)



class SourceModel(models.Model):
    value_to_copy = models.CharField(max_length=100)

class DestinationModel(models.Model):
    copied_value = models.CharField(max_length=100)

# Define the signal handler function
@receiver(post_save, sender=SourceModel)
def copy_value_to_destination_model(sender, instance, created, **kwargs):
    if created:
        # Create an instance of DestinationModel and copy the value
        DestinationModel.objects.create(copied_value=instance.value_to_copy)