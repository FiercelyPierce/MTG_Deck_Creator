from django.db import models

class Cards(models.Model):
    name = models.CharField(max_length=100)
    color = models.TextChoices('Colors', 'WHITE RED BLACK BLUE GREEN')
    card_type = models.CharField(max_length=50)
    card_subtype = models.CharField(max_length=50)
    rarity = models.TextChoices('Rarity','COMMON UNCOMMON RARE LEGENDARY MYTHIC')
    description = models.TextField()
    image = models.FilePathField(path="/img")
