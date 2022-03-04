from django.forms import ModelForm
from .models import JobModel
class JobForm(ModelForm):
    class Meta:
        model = JobModel
        fields = '__all__'