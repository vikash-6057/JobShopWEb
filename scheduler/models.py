from django.db import models

class JobModel(models.Model):
    job = models.FileField( upload_to='jobs', max_length=100)