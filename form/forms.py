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
    patient = PostInject1.patient

    class Meta:
        model = PostInject1
        fields = '__all__'
        exclude = ['patient']
        widgets = {
            'date': DateInput(),

            'musc1_inj': forms.TextInput(attrs={'style':"width:100%;border:none;"}),
            'musc2_inj': forms.TextInput(attrs={'style':"width:100%;border:none;"}),
            'musc3_inj': forms.TextInput(attrs={'style':"width:100%;border:none;"}),
            'musc4_inj': forms.TextInput(attrs={'style':"width:100%;border:none;"}),

            'goal_1': forms.Textarea(attrs={'style':"width:100%;height:100px;border:none;"}),
            'goal_2': forms.Textarea(attrs={'style':"width:100%;height:100px;border:none;"}),
            'goal_3': forms.Textarea(attrs={'style':"width:100%;height:100px;border:none;"}),
            'goal_4': forms.Textarea(attrs={'style':"width:100%;height:100px;border:none;"}),


            'child_fam_goals': forms.Textarea(attrs={'style':"width:80%;height:200px"}),
            'therapy_intervention': forms.Textarea(attrs={'style':"width:80%;height:200px"}),
            'physical_activity': forms.Textarea(attrs={'style':"width:80%;height:200px"}),
            'family_opinions': forms.Textarea(attrs={'style':"width:80%;height:200px"}),

            'orth_changes_made': forms.RadioSelect,
            'orth_changes': forms.Textarea(attrs={'placeholder': 'If yes, please specify changes made','style':"width:80%;height:200px"}),
            'therapy_implemented_made': forms.RadioSelect,
            'therapy_implemented': forms.Textarea(attrs={'placeholder': 'If yes, please specify details','style':"width:80%;height:200px"}),
            'casting_complete_made': forms.RadioSelect,
            'casting_complete': forms.Textarea(attrs={'placeholder': 'If yes, please specify outcome','style':"width:80%;height:200px"}),

            'day_case': forms.Textarea(attrs={'style':"width:80%;height:200px"}),
            'side_effects_choices': forms.RadioSelect,
            'side_effects': forms.Textarea(attrs={'style':"width:80%;height:200px"}),
            'pos_effects': forms.Textarea(attrs={'style':"width:80%;height:200px"}),
            'neg_effects': forms.Textarea(attrs={'style':"width:80%;height:200px"}),
            'changes_medical': forms.Textarea(attrs={'style':"width:80%;height:200px"}),
            'date1': DateInput(),

            'post_inj_examination': forms.Textarea(attrs={'style':"width:80%;height:400px"}),

            'GMFM_A': forms.TextInput(attrs={'style': "width:100%;border:none;"}),
            'GMFM_B': forms.TextInput(attrs={'style': "width:100%;border:none;"}),
            'GMFM_C': forms.TextInput(attrs={'style': "width:100%;border:none;"}),
            'GMFM_D': forms.TextInput(attrs={'style': "width:100%;border:none;"}),
            'GMFM_E': forms.TextInput(attrs={'style': "width:100%;border:none;"}),

            'AHA': forms.TextInput(attrs={'size':"30"}),

            'post_inj_summary': forms.Textarea(attrs={'style':"width:80%;height:400pxs"}),

            'date2': DateInput()

        }

class PostInject2Form(forms.ModelForm):
    patient = PostInject2.patient

    class Meta:
        model = PostInject2
        fields = '__all__'
        exclude = ['patient']
        widgets = {
            'date': DateInput(),

            'musc1_inj': forms.TextInput(attrs={'style':"width:100%;border:none;"}),
            'musc2_inj': forms.TextInput(attrs={'style':"width:100%;border:none;"}),
            'musc3_inj': forms.TextInput(attrs={'style':"width:100%;border:none;"}),
            'musc4_inj': forms.TextInput(attrs={'style':"width:100%;border:none;"}),

            'goal_1': forms.Textarea(attrs={'style':"width:100%;height:100px;border:none;"}),
            'goal_2': forms.Textarea(attrs={'style':"width:100%;height:100px;border:none;"}),
            'goal_3': forms.Textarea(attrs={'style':"width:100%;height:100px;border:none;"}),
            'goal_4': forms.Textarea(attrs={'style':"width:100%;height:100px;border:none;"}),


            'child_fam_goals': forms.Textarea(attrs={'style':"width:80%;height:200px"}),
            'therapy_intervention': forms.Textarea(attrs={'style':"width:80%;height:200px"}),
            'physical_activity': forms.Textarea(attrs={'style':"width:80%;height:200px"}),
            'family_opinions': forms.Textarea(attrs={'style':"width:80%;height:200px"}),

            'orth_changes_made': forms.RadioSelect,
            'orth_changes': forms.Textarea(attrs={'placeholder': 'If yes, please specify changes made','style':"width:80%;height:200px"}),
            'therapy_implemented_made': forms.RadioSelect,
            'therapy_implemented': forms.Textarea(attrs={'placeholder': 'If yes, please specify details','style':"width:80%;height:200px"}),
            'casting_complete_made': forms.RadioSelect,
            'casting_complete': forms.Textarea(attrs={'placeholder': 'If yes, please specify outcome','style':"width:80%;height:200px"}),

            'day_case': forms.Textarea(attrs={'style':"width:80%;height:200px"}),
            'side_effects_choices': forms.RadioSelect,
            'side_effects': forms.Textarea(attrs={'style':"width:80%;height:200px"}),
            'pos_effects': forms.Textarea(attrs={'style':"width:80%;height:200px"}),
            'neg_effects': forms.Textarea(attrs={'style':"width:80%;height:200px"}),
            'changes_medical': forms.Textarea(attrs={'style':"width:80%;height:200px"}),
            'date1': DateInput(),

            'post_inj_examination': forms.Textarea(attrs={'style':"width:80%;height:400px"}),

            'GMFM_A': forms.TextInput(attrs={'style': "width:100%;border:none;"}),
            'GMFM_B': forms.TextInput(attrs={'style': "width:100%;border:none;"}),
            'GMFM_C': forms.TextInput(attrs={'style': "width:100%;border:none;"}),
            'GMFM_D': forms.TextInput(attrs={'style': "width:100%;border:none;"}),
            'GMFM_E': forms.TextInput(attrs={'style': "width:100%;border:none;"}),

            'AHA': forms.TextInput(attrs={'size':"30"}),

            'post_inj_summary': forms.Textarea(attrs={'style':"width:80%;height:400pxs"}),

            'date2': DateInput()

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


class DysportForm(forms.ModelForm):
    patient = Dysports.patient
    class Meta:
        model = Dysports
        fields = '__all__'
        exclude = ['patient']
        widgets = {
            'date': DateInput(),
            'expirydate': DateInput(),
        }

class ConsentForm(forms.ModelForm):
    patient = Consents.patient
    class Meta:
        model = Consents
        fields = '__all__'
        exclude = ['patient']
        widgets = {
            'date': DateInput(),
        }

class ConsentForm2(forms.ModelForm):
    patient = Consentss.patient
    class Meta:
        model = Consentss
        fields = '__all__'
        exclude = ['patient']
        widgets = {
            'date': DateInput(),
        }
