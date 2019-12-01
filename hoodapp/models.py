from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_regular = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class Regular(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    neighbourhood = models.ManyToManyField (Neighbourhood, related_name='hood_regular')

class Neighbourhood(models.Model):
    neighbourhood = (
        (KAREN,'karen'),
        (LANGATA, 'langata'),
        (RUNDA, 'runda'),
        (MUTHAIGA, 'muthaiga'),
        (WESTLANDS, 'westlands'),
        (KILIMANI,'kilimani'),
        (HURLINGHAM,'hurlingham'),
        (NAIROBIWEST, 'nairobiwest'),
        (UPPERHILL,'upperhill'),
        (SOUTHB, 'southb'),
        (SOUTHC, 'southc'),
        (BURUBURU, 'buruburu'),
        (KASARANI, 'kasarani'),
        (GIGIRI, 'gigiri'),
        (KAHAWAWEST, 'Kahawawest'),
        (EMBAKASI,'embakasi'),
        (EASTLANDS, 'eastlands'),
        (RONGAI,'rongai'),
        (SYOKIMAU, 'syokimau'),
        (KISERIAN, 'kiserian'),

    )
