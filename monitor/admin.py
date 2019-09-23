from django.contrib import admin
from .models import Crn
# Register your models here.

@admin.register(Crn)
class CrnAdmin(admin.ModelAdmin):
    list_display = ('id' ,'cr_station' ,'crn_comm_date' ,'crn_clos_date', 'cr_note' ,'cr_cash' ,'cr_status' )
    list_display_links = ('id' , 'cr_note')
    search_fields = ('cr_note' , 'cr_cash' ,'cr_status' , )
    list_per_page = 25
