from django.db import models

# Create your models here.
class Mysql_model(models.Model):
    name=models.CharField(max_length=30)
    student_id= models.IntegerField(primary_key= True)
    subject=models.CharField(max_length=30)
    marks=models.IntegerField()
    def __str__(self):
        return self.name 

    class Meta:
        managed = False
        db_table = 'student'
