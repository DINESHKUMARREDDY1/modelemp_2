from django.db import models

# Create your models here.
class dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=50)
    location=models.CharField(max_length=50)

    def __str__(self):
        return self.dname

class employee(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=50)
    job=models.CharField(max_length=50)
    sal=models.IntegerField()
    hiredate=models.DateField()
    comm=models.IntegerField(null=True,blank=True)
    deptno=models.ForeignKey(dept,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.ename