from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    price_per_night = models.FloatField()
    currency = models.CharField(max_length=10)
    total_price = models.FloatField(blank=True, null=True)
    image_urls = models.JSONField(default=list)
    ratings = models.FloatField()
    description = models.TextField(blank=True, null=True)
    num_reviews = models.IntegerField()
    amenities = models.JSONField(default=list)
    host = models.JSONField()
    property_type = models.CharField(max_length=100)
