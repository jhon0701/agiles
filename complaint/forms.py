import datetime

from django import forms
# models
from .models import Complaint

# Template classes

today = datetime.date.today()
today = today.strftime('%d/%m/%Y')

attrs_template = {'class': 'form-control'}
attrs_blocked = {'class': 'form-control', 'readonly': 'True'}
attrs_date = {
    'class': 'form-control',
    'id': 'datepicker',
    'placeholder': 'M/D/A',
    'value': today
}
attrs_time = {
    'class': 'form-control',
    'id': 'timepicker2',
    'placeholder': 'HH:MM',
}


class ComplaintForm(forms.Form):

    FORM_TITLE = "Formulario de denuncia"

    complainant_name = forms.CharField(
        max_length=120,
        widget=forms.TextInput(attrs=attrs_template)
    )
    place_event = forms.CharField(
        max_length=120,
        widget=forms.TextInput(attrs=attrs_template)
    )
    event_date = forms.DateField(
        widget=forms.DateInput(attrs=attrs_date),
        input_formats=['%d/%m/%Y']
    )
    event_time = forms.TimeField(
        widget=forms.TimeInput(attrs=attrs_time)
    )
    description = forms.CharField(
        max_length=255,
        widget=forms.Textarea(attrs=attrs_template)
    )
    evidence = forms.FileField(
        required=False
    )

    def register(self):
        complainant_name = self.cleaned_data['complainant_name']
        place_event = self.cleaned_data['place_event']
        event_date = self.cleaned_data['event_date']
        event_time = self.cleaned_data['event_time']
        description = self.cleaned_data['description']

        new_complaint = Complaint.objects.create(
            complainant_name=complainant_name,
            place_event=place_event,
            event_date=event_date,
            event_time=event_time,
            description=description,
            # evidence=evidence
        )

        return new_complaint
