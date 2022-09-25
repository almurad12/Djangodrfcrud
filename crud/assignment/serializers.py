from dataclasses import field
from pyexpat import model
from django.db.models import fields
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields= ('name','amount','productDetails')