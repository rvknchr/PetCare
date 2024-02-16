from django.db import models

class Pets(models.Model):
    petid = models.IntegerField(primary_key=True)
    petname = models.CharField(max_length=100)
    petgender = models.CharField(max_length=100)
    petage = models.IntegerField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return str(self.petid)
