from django.db import models

# Create your models here.
class Event(models.Model):
    # Meta Data of APIs
    external_id = models.CharField(max_length=255,db_index=True,help_text='Unique External ID from APIs',verbose_name="External ID")
    source_api = models.CharField(max_length=50,db_index=True,help_text='APIs source name',verbose_name="Source API")

    # Main Event Details 
    
    name = models.CharField(
        max_length=500,
        help_text="Title of Event",
        verbose_name="Event Name"    
    )

    description = models.TextField(
        blank=True,
        null=True,
        default="TDB",
        help_text="Full description of the event",
        verbose_name="Description"
    )

    start_datetime = models.DateTimeField(help_text="Event date and time")

    end_datetime = models.DateTimeField(blank=True,help_text="End Date and Time of Event")

    timezone = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="IANA timezone string for the event",
        verbose_name="Timezone"
    )

    event_url = models.URLField(max_length=1000,blank=True,null=True,help_text="External URL for Event",verbose_name="Event URL")

    genre = models.CharField(max_length=100,blank=True,help_text="Type of Event")
    
    image_url = models.URLField(max_length=1000,blank=True,null=True,help_text="IMage URL for Event",verbose_name="Event Image URL")

    # Venue - Separate Model to be created
    venue_name = models.CharField(max_length=100,help_text="Place of Event taking place")
    
    raw_api_data = models.JSONField(blank=True,null=True,help_text="Full Event Api Response")

    def __str__(self):
        return self.name  + self.venue_name


# Venue Model 
class Venue(models.Model):
    venue_id = models.CharField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    country = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name} - {self.city}'