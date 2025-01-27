from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.location}"

class Role(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Employee(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    salary = models.IntegerField()
    bonus = models.IntegerField()
    phonenum = models.IntegerField()
    hiredate = models.DateField(null=True,blank=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.salary} {self.bonus} {self.phonenum} {self.hiredate} {self.dept} {self.role}"
