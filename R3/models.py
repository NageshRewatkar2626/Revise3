from django.db import models


class EmpModel(models.Model):

	e_id     =models.AutoField(primary_key=True)
	e_name   =models.CharField(max_length=30)
	e_contact=models.IntegerField(unique=True)
	e_salary =models.FloatField()
