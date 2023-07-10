from django.db import models

class Partita(models.Model):
    squadra1=models.CharField(max_length=100)
    squadra2=models.CharField(max_length=200)
    goal1=models.IntegerField()
    goal2=models.IntegerField()
    

class Meta:
        db_table='partite'
    

   
