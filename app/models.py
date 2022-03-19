from django.db import models
from slugger import AutoSlugField

# Create your models here.
class InventoryItem(models.Model):

    # condition
    EXLNT = 'Excellent'
    GD = 'Good'
    AVG = 'Average'
    BD = 'Bad'
    PR = 'Poor'

    # measurement
    L = 'Liters (L)'
    ml = 'Milliliters (ml)'
    Kg = 'Kilograms (Kg)'
    g = 'Grams (g)'
    P_ = 'Pairs (P_)'
    m = 'Meters (m)'
    ft = 'Feet (ft)'
    s = 'Singel Object(s)'

    # categories
    _plumbing = 'Plumbing'
    _construction = 'Construction'
    _animal = 'Animal'
    _farm = 'Farm'
    _indoor = 'Indoor'
    _misc = 'Miscellenious'

    # locations
    EWS = 'East Wing Store'
    WWS = 'West Wing Store'

    CATEGORY_CHOICES = [
        (_plumbing, 'Plumbing'),
        (_construction, 'Construction'),
        (_animal, 'Animal'),
        (_farm, 'Farm'),
        (_indoor, 'Indoor'),
        (_misc, 'Miscellenious'),
    ]

    LOCATION_CHOICES = [
        (EWS, 'East Wing Store'),
        (WWS, 'West Wing Store'),
    ]

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
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES)

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
