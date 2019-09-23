from django.contrib import admin
from .models import Station

# Register your models here.
@admin.register(Station)

class StationAdmin(admin.ModelAdmin):
    list_display = ('id' ,'station_name')
    search_fields = ('station_name' ,  )
    list_per_page = 25
