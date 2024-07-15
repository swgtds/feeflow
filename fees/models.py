from django.db import models

# Create your models here.
    
class StudentDetail(models.Model):
    name= models.CharField(max_length=100,null=True)
    guardianName= models.CharField(max_length=100,null=True)
    studentId= models.CharField(max_length=100,null=True)
    std= models.PositiveSmallIntegerField(null=True)
    amount= models.BigIntegerField(null=True)
    admissionDate= models.DateField(auto_now_add=True,null=True)
    jan= models.CharField(max_length=100,null=True)
    feb= models.CharField(max_length=100,null=True)
    mar= models.CharField(max_length=100,null=True)
    april= models.CharField(max_length=100,null=True)
    may= models.CharField(max_length=100,null=True)
    june= models.CharField(max_length=100,null=True)
    july= models.CharField(max_length=100,null=True)
    aug= models.CharField(max_length=100,null=True)
    sept= models.CharField(max_length=100,null=True)
    oct= models.CharField(max_length=100,null=True)
    nov= models.CharField(max_length=100,null=True)
    dec= models.CharField(max_length=100,null=True)
    class Meta:
        db_table="StudentDetail"
