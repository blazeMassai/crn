from django import forms
from monitor.models import Crn
from station.models import Station
from django_select2.forms import Select2MultipleWidget, Select2Widget

    

class CrnForm(forms.ModelForm):
    

    cr_station = forms.ModelChoiceField(queryset=Station.objects.all().order_by('station_name'),  widget=Select2Widget)

    
    crn_comm_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )

    crn_clos_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )
    cr_note = forms.TextInput(attrs={'class': 'form-control' ,'placeholder':'Enter Cr-Note'})
    cr_cash = forms.TextInput(attrs={'class': 'form-control' ,'placeholder':'Enter Amount'})
    cr_status = forms.TextInput(attrs={'class': 'form-control' ,'placeholder':'Enter Status'})

    class Meta():
        model = Crn
        fields = ('cr_station', 'crn_comm_date', 'crn_clos_date', 'cr_note', 'cr_cash', 'cr_status',
                  )
