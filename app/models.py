from django.db import models
from slugger import AutoSlugField

# Create your models here.


class Category(models.Model):

    category = models.CharField(max_length=200)

    def __str__(self) -> str:
        
        return self.category

class Location(models.Model):

    location = models.CharField(max_length=200)

    def __str__(self) -> str:
        
        return self.location

class InventoryItem(models.Model):

    EXLNT = 'Excellent'
    GD = 'Good'
    AVG = 'Average'
    BD = 'Bad'
    PR = 'Poor'

    L = 'Liters (L)'
    ml = 'Milliliters (ml)'
    Kg = 'Kilograms (Kg)'
    g = 'Grams (g)'
    P_ = 'Pairs (P_)'
    m = 'Meters (m)'
    ft = 'Feet (ft)'
    s = 'Singel Object(s)'

    MEASUREMENT_IN_CHOICES = [
        (L, 'Liters'),
        (ml, 'Milliliters'),
        (Kg, 'Kilograms'),
        (g, 'Grams'),
        (P_, 'Pairs'),
        (m, 'Meters'),
        (ft, 'Feet'),
        (s, 'Single object(s)'),
    ]

    CONDITION_CHOICES = [
        (EXLNT, 'Excellent'),
        (GD, 'Good'),
        (AVG, 'Average'),
        (BD, 'Bad'),
        (PR, 'Poor'),
    ]

    name = models.CharField(max_length=200, blank=False, null=False)

    slug = AutoSlugField(populate_from='name')
    
    category = models.ForeignKey(Category, related_name='inventory_item', on_delete=models.CASCADE, blank=False, null=False)
    
    location = models.ForeignKey(Location, related_name='inventory_item', on_delete=models.CASCADE, blank=False, null=False)

    quantity_mass_volume = models.PositiveIntegerField(default=0)

    measurement_in =  models.CharField(max_length=50, choices=MEASUREMENT_IN_CHOICES, default=s, blank=False, null=False)

    condition = models.CharField(max_length=50, choices=CONDITION_CHOICES, default=AVG, blank=False, null=False)

    type_make_model = models.CharField(max_length=200, blank=False, null=False)

    more_details = models.TextField( blank=False, null=False)

    archived_on = models.DateTimeField(auto_now_add=True)

    last_modified = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ['-archived_on']

    def __str__(self) -> str:
        
        return self.name
