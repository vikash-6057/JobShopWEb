from django.db import models

class JobModel(models.Model):
    job = models.FileField( upload_to='jobs', max_length=100)
    number_of_machine = models.IntegerField()
    job_created = models.DateTimeField(auto_now_add=True)