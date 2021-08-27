from django.db import models

# Create your models here.
choice=(
    ('regular','regular'),('medium','medium'),('large','large')
    )
top=(
    ('chicken','chicken'),('mutton','mutton'),('onion','onion'),('tomato','tomato')
)
class Pizza(models.Model):
    name=models.CharField(max_length=200)
    size=models.CharField(choices=choice,max_length=200)
    toppings=models.CharField(choices=top,max_length=200)
    price=models.IntegerField()
    
    def __str__(self):
        return str(self.name)
    
