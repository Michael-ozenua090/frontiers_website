from django.forms import ModelForm
from .models import ect_project_repository

class ect_project_repositoryForm(ModelForm):
    class Meta:
        model= ect_project_repository
        # fields= ['last_name','']
        exclude =['date_created', 'date_updated']