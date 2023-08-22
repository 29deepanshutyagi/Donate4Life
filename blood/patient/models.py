from django.db import models

# Create your models here.
class Patient(models.Model):
    name=models.CharField( max_length=122)
    birthofdate=models.DateField()
    email=models.CharField(max_length=122)
    mobilenumber=models.CharField(max_length=12)
    gender = models.CharField(
        max_length=1,
        choices=(('M', 'Male'), ('F', 'Female'),('O','Others')),
        default='M',
    )
    occupation=models.TextField()
    IDtype=models.CharField(max_length=122)
    IDnumber=models.CharField(max_length=122)
    expirydate=models.DateField()
    PermanentorTemporary=models.TextField()
    state=models.CharField(max_length=122)
    district=models.CharField(max_length=122)
    father=models.CharField(max_length=122)
    mother=models.CharField()
    grandfather=models.CharField(max_length=122)
    bloodgroup=models.CharField(max_length=122)
   
    def __str__(self):
        return self.name