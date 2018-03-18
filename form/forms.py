from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'
    
class JQueryUIDatepickerWidget(forms.DateInput):
    def __init__(self, **kwargs):
        super(forms.DateInput, self).__init__(attrs={"size":10, "class": "dateinput"}, **kwargs)

    class Media:
        css = {"all":("http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.6/themes/redmond/jquery-ui.css",)}
        js = ("http://ajax.googleapis.com/ajax/libs/jquery/1.4.3/jquery.min.js",
              "http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.6/jquery-ui.min.js",)


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'date_of_birth': DateInput(),
        }

class MedClerkPreSedForm(forms.ModelForm):
    patient = MedClerkPreSed.patient

    class Meta:
        model = MedClerkPreSed
        fields = '__all__'
        exclude = ['patient']
        widgets = {
            'met_time': DateInput(),
            'oral_sedation_time': DateInput(),
            'ametop_applied_time': DateInput(),
        }


class ProcReportForm(forms.ModelForm):
    patient = ProcReport.patient

    class Meta:
        model = ProcReport
        fields = '__all__'
        exclude = ['patient']
        widgets = {
            'date': DateInput(),
            'ultrasound_1': forms.RadioSelect,
            'ultrasound_2': forms.RadioSelect,
            'ultrasound_3': forms.RadioSelect,
            'ultrasound_4': forms.RadioSelect,
            'ultrasound_5': forms.RadioSelect,
            'ultrasound_6': forms.RadioSelect,
            'ultrasound_7': forms.RadioSelect,
            'ultrasound_8': forms.RadioSelect,
            'ultrasound_9': forms.RadioSelect,
            'ultrasound_10': forms.RadioSelect,
            'ultrasound_11': forms.RadioSelect,
            'ultrasound_12': forms.RadioSelect,
            'adverse_event': forms.RadioSelect,
            'adverse_event_yes': forms.Textarea(attrs={'placeholder': 'If yes, then details of adverse event'}),
            'sedation_effective': forms.RadioSelect,
            'sedation_effective_no': forms.Textarea(attrs={'placeholder': 'If no, then details of ineffective sedation'}),
        }

class PostInject1Form(forms.ModelForm):
    patient  = PostInject1.patient

    class Meta:
        model = PostInject1
        fields = '__all__'
        exclude = ['patient']
        widgets = {
            'date': DateInput(),

        }

class ConcOfTreatmentForm(forms.ModelForm):
    patient = ConcOfTreatment.patient

    class Meta:
        model = ConcOfTreatment
        fields = '__all__'
        exclude = ['patient']
        widgets = {
            'date': DateInput(),
            'last_injection': DateInput(),
            'timeframe': DateInput(),
        }
