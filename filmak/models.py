from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bozkatzailea(models.Model):
    # Beharrezko eremua
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class filmak_filma(models.Model):
    izenburua = models.CharField(max_length=100)
    zuzendaria = models.CharField(max_length=60)
    urtea = models.IntegerField()
    generoa = models.CharField(max_length=2)
    sinopsia = models.CharField(max_length=500)
    bozkak = models.IntegerField(default=0)

    def __str__(self):
        return self.izenburua

class filmak_bozkatzailea(models.Model):
    erabiltzailea = models.ForeignKey(Bozkatzailea, on_delete=models.CASCADE)
    filma = models.ForeignKey(filmak_filma, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
