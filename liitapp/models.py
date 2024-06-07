from django.db import models

# Create your models here.
class Register(models.Model):
    leaderName = models.CharField(max_length=100)
    member1 = models.CharField(max_length=100)
    member2 = models.CharField(max_length=100)
    member3 = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    mobileNumber = models.CharField(max_length=10)
    domain = models.CharField(max_length=100)
    designation1 = models.CharField(max_length=100, default='')
    designation2 = models.CharField(max_length=100, default='')
    designation3 = models.CharField(max_length=100, default='')
    designation4 = models.CharField(max_length=100, default='')
    college = models.CharField(max_length=100, default='')
    unique_id = models.CharField(max_length=50, unique=True)
    uploaded_file = models.FileField(upload_to='media/uploaded_files', default='')