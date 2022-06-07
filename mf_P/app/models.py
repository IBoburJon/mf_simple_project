from django.db import models
from django.db.models.fields import IntegerField
from django.utils import timezone


class ariza_E(models.Model):
    pinfl = models.IntegerField(default=0)
    firstname = models.CharField(max_length=25, default=None)
    lastname = models.CharField(max_length=25, default=None)
    fathersname = models.CharField(max_length=25, default=None)
    bank_name = models.CharField(max_length=25, default=None)
    bank_inn = models.CharField(max_length=25, default=None)
    bank_mfo = models.CharField(max_length=25, default=None)
    bank_tr = models.CharField(max_length=25, default=None)
    bank_cardnumber = models.CharField(max_length=25, default=None)
    ariza_pdf = models.FileField(upload_to='pdfs/', default=None)
    passport_pdf = models.FileField(upload_to='pdfs/', default=None)
    placeofwork_pdf = models.FileField(upload_to='pdfs/', default=None)
    exampaper_pdf = models.FileField(upload_to='pdfs/', default=None)
    checking = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pinfl)



class token(models.Model):
    token = models.CharField(max_length=250)
    token_created = models.DateTimeField(default=timezone.now)
    expires_in = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.token)