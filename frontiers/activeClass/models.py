from django.db import models

# Create your models here.
class ect_project_repository(models.Model):
    matric_no=models.CharField(max_length=6)
    first_name= models.CharField(max_length=30)
    surname= models.CharField(max_length=15)
    othername= models.CharField(max_length=30)
    gender= models.CharField(max_length=1)
    phone_number= models.CharField( max_length=11)
    project_topic=models.CharField(max_length=70)
    department=models.CharField(max_length=3)
    supervisor=models.CharField(max_length=30)
    year_of_sub=models.CharField(max_length=4)
    accession_no=models.CharField(max_length=6)
    shell_no=models.IntegerField()
    row_no=models.IntegerField()
    copies=models.IntegerField()
    date_created= models.DateTimeField(auto_now_add=True)
    date_updated= models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{surname} {first}".format(surname=self.first_name, first=self.last_name)
        # return self.last_name + " " + self.first_name
    