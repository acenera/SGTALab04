from django.contrib import admin
from .models import filmak_filma, filmak_bozkatzailea, Bozkatzailea

# Register your models here.
admin.site.register(filmak_filma)
admin.site.register(filmak_bozkatzailea)
admin.site.register(Bozkatzailea)