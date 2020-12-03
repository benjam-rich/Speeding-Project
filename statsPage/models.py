from django.db import models
from datetime import datetime, timedelta

class Ticket(models.Model) :
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    date = models.DateField(default=datetime.today)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    locationStreet = models.CharField(max_length=50, blank=True)
    locationCity = models.CharField(max_length=50)
    speedMPH = models.CharField(max_length=5, blank=True)


    # def __str__(self):

    #     return(self.fname + "paid " + self.amount)



