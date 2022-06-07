from .models import ariza_E
from rest_framework import serializers

class arizaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ariza_E
        fields = ['pinfl', 'firstname', 'lastname', 'fathersname', 'bank_name', 'bank_inn', 'bank_mfo', 'bank_tr', 'bank_cardnumber', 'ariza_pdf', 'passport_pdf', 'placeofwork_pdf', 'exampaper_pdf','checking',]
