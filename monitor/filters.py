import django_filters
from . models import Crn
from datetime import datetime
from django_filters import DateFromToRangeFilter
from django_filters import FilterSet, filters
from django import forms
from django_filters.widgets import RangeWidget, SuffixedMultiWidget
from django_select2.forms import  Select2Widget
from station.models import Station
from django import forms




class CRNFilter(FilterSet):


    created_at = filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': 'YYYY/MM/DD', 'type': 'date'}),label='CRN Date Between')

    #cr_station = forms.ModelChoiceField(queryset=Station.objects.all().order_by('station_name'),  widget=Select2Widget(attrs={'class': 'select2-selection select2-selection--single', }))

    class Meta:
        model = Crn

        fields = ('cr_station', 'created_at')


