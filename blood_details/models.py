from django.db import models


class DonorDetails(models.Model):
    name = models.CharField(max_length=264)
    blood_group = models.CharField(max_length=4)
    contact_no = models.CharField(max_length=10)
    email = models.EmailField()
