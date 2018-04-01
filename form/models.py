from django.db import models
from django.utils import timezone
from .validators import *

YES_NO_NA_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
        ('', 'n/a'),
    )

YES_NO_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )

LEFT_RIGHT_CHOICES = (
    ('left', 'L'),
    ('right', 'R'),
    ('', "n/a"),
)

PAIN_CHOICES = (
    ('no', 'No'),
    ('partial', 'Partial'),
    ('full', "Full"),
)

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,)
    patient_id = models.CharField(max_length=100, validators=[val_pat_id], unique=True)
    date_of_birth = models.DateField(validators=[valid_dob])

    def name(self):
        return str(self.first_name + " " + self.last_name).upper()

    def __str__(self):
        return (self.name() + " " + str(self.patient_id))


class MedClerkPreSed(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=0)
    access_date = timezone.now()
    page = 11
    ABNORMAL_CHOICES = (
        ('normal', 'Normal'),
        ('abnormal', 'Abnormal'),
        ('', "n/a"),
    )
    clinician = models.CharField(max_length=200)
    current_health_status = models.TextField(
        help_text="Please Comment on URTI/Seizures/Flu/Bladder Incontinence/LRTI/Swallowing Difficulty",
        blank=True
    )
    met = models.CharField(
        max_length=3,
        choices=YES_NO_NA_CHOICES,
        default='no',
        blank=True
    )
    met_time = models.DateField()
    record_medication_changes = models.TextField(
        help_text="Record Medication Changes Since Pre-Injection Assessment",
        blank=True
    )
    respiratory_examination_details = models.TextField(
        help_text="Respiratory Examination Details",
        blank=True
    )
    normal = models.CharField(
        max_length=8,
        choices=ABNORMAL_CHOICES,
        default=None,
        blank=True
    )
    fit_for_sedation = models.CharField(
        max_length=3,
        choices=YES_NO_CHOICES,
        default='no',
        blank=True
    )
    oral_sedation_time = models.DateField()
    number_of_ametop_tubes_used = models.PositiveSmallIntegerField(default=0)
    ametop_applied_time = models.DateField()
    reasons_for_cancellation = models.TextField(
        help_text="If Applicable, State Reasons for Cancellation",
        blank = True
    )
    follow_up_arrangements = models.TextField(
        help_text="Outline Follow Up Arrangements Below",
        blank = True
    )

    def __str__(self):
        return "Medical Clerking Pre-Sedation"


class ConcOfTreatment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=0)
    access_date = timezone.now()
    page = 19
    completed_by = models.CharField(max_length=5, help_text="Initials")
    date = models.DateField()
    last_injection = models.DateField()
    summary_and_effectiveness_of_injection = models.TextField(
        help_text="Summary of Injection Results",
        blank=True
    )
    future_treatment_plan = models.TextField(
        help_text="Details of Future Treatment Plan",
        blank=True
    )
    reinjection = models.CharField(
        max_length=3,
        choices=YES_NO_CHOICES,
        default='no',
        blank=True
    )
    if_reinjection_yes = models.TextField(
        help_text="Reason for Re-injection",
        blank=True
    )
    timeframe = models.DateField()
    admin_informed = models.CharField(
        max_length=3,
        choices=YES_NO_CHOICES,
        default='no',
        blank=True
    )
    if_reinjection_no = models.TextField(
        help_text="Reason Re-injection Not Indicated",
        blank=True
    )
    onward_referral_plan = models.TextField(
        blank=True
    )

    def __str__(self):
        return "Conclusion of Treatment"


class ProcReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=0)
    access_date = timezone.now()
    page = 12
    muscle_1 = models.CharField(
        max_length=5,
        choices=LEFT_RIGHT_CHOICES,
        default='',
        blank=True
    )
    muscle_2 = models.CharField(
        max_length=5,
        choices=LEFT_RIGHT_CHOICES,
        default='',
        blank=True
    )
    muscle_3 = models.CharField(
        max_length=5,
        choices=LEFT_RIGHT_CHOICES,
        default='',
        blank=True
    )
    muscle_4 = models.CharField(
        max_length=5,
        choices=LEFT_RIGHT_CHOICES,
        default='',
        blank=True
    )
    muscle_5 = models.CharField(
        max_length=5,
        choices=LEFT_RIGHT_CHOICES,
        default='',
        blank=True
    )
    muscle_6 = models.CharField(
        max_length=5,
        choices=LEFT_RIGHT_CHOICES,
        default='',
        blank=True
    )
    muscle_7 = models.CharField(
        max_length=5,
        choices=LEFT_RIGHT_CHOICES,
        default='',
        blank=True
    )
    muscle_8 = models.CharField(
        max_length=5,
        choices=LEFT_RIGHT_CHOICES,
        default='',
        blank=True
    )
    muscle_9 = models.CharField(
        max_length=5,
        choices=LEFT_RIGHT_CHOICES,
        default='',
        blank=True
    )
    muscle_10 = models.CharField(
        max_length=5,
        choices=LEFT_RIGHT_CHOICES,
        default='',
        blank=True
    )
    muscle_11 = models.CharField(
        max_length=5,
        choices=LEFT_RIGHT_CHOICES,
        default='',
        blank=True
    )
    muscle_12 = models.CharField(
        max_length=5,
        choices=LEFT_RIGHT_CHOICES,
        default='',
        blank=True
    )
    musc_inject_1 = models.TextField(blank=True)
    musc_inject_2 = models.TextField(blank=True)
    musc_inject_3 = models.TextField(blank=True)
    musc_inject_4 = models.TextField(blank=True)
    musc_inject_5 = models.TextField(blank=True)
    musc_inject_6 = models.TextField(blank=True)
    musc_inject_7 = models.TextField(blank=True)
    musc_inject_8 = models.TextField(blank=True)
    musc_inject_9 = models.TextField(blank=True)
    musc_inject_10 = models.TextField(blank=True)
    musc_inject_11 = models.TextField(blank=True)
    musc_inject_12 = models.TextField(blank=True)

    ultrasound_1 = models.CharField(
        max_length=3,
        choices=YES_NO_NA_CHOICES,
        default='',
        blank=True
    )
    ultrasound_2 = models.CharField(
        max_length=3,
        choices=YES_NO_NA_CHOICES,
        default='',
        blank=True
    )
    ultrasound_3 = models.CharField(
        max_length=3,
        choices=YES_NO_NA_CHOICES,
        default='',
        blank=True
    )
    ultrasound_4 = models.CharField(
        max_length=3,
        choices=YES_NO_NA_CHOICES,
        default='',
        blank=True
    )
    ultrasound_5 = models.CharField(
        max_length=3,
        choices=YES_NO_NA_CHOICES,
        default='',
        blank=True
    )
    ultrasound_6 = models.CharField(
        max_length=3,
        choices=YES_NO_NA_CHOICES,
        default='',
        blank=True
    )
    ultrasound_7 = models.CharField(
        max_length=3,
        choices=YES_NO_NA_CHOICES,
        default='',
        blank=True
    )
    ultrasound_8 = models.CharField(
        max_length=3,
        choices=YES_NO_NA_CHOICES,
        default='',
        blank=True
    )
    ultrasound_9 = models.CharField(
        max_length=3,
        choices=YES_NO_NA_CHOICES,
        default='',
        blank=True
    )
    ultrasound_10 = models.CharField(
        max_length=3,
        choices=YES_NO_NA_CHOICES,
        default='',
        blank=True
    )
    ultrasound_11 = models.CharField(
        max_length=3,
        choices=YES_NO_NA_CHOICES,
        default='',
        blank=True
    )
    ultrasound_12 = models.CharField(
        max_length=3,
        choices=YES_NO_NA_CHOICES,
        default='',
        blank=True
    )

    placement_1 = models.TextField(blank=True)
    placement_2 = models.TextField(blank=True)
    placement_3 = models.TextField(blank=True)
    placement_4 = models.TextField(blank=True)
    placement_5 = models.TextField(blank=True)
    placement_6 = models.TextField(blank=True)
    placement_7 = models.TextField(blank=True)
    placement_8 = models.TextField(blank=True)
    placement_9 = models.TextField(blank=True)
    placement_10 = models.TextField(blank=True)
    placement_11 = models.TextField(blank=True)
    placement_12 = models.TextField(blank=True)

    tolerated_1 = models.TextField(blank=True)
    tolerated_2 = models.TextField(blank=True)
    tolerated_3 = models.TextField(blank=True)
    tolerated_4 = models.TextField(blank=True)
    tolerated_5 = models.TextField(blank=True)
    tolerated_6 = models.TextField(blank=True)
    tolerated_7 = models.TextField(blank=True)
    tolerated_8 = models.TextField(blank=True)
    tolerated_9 = models.TextField(blank=True)
    tolerated_10 = models.TextField(blank=True)
    tolerated_11 = models.TextField(blank=True)
    tolerated_12 = models.TextField(blank=True)

    adverse_event = models.CharField(
        max_length=3,
        choices=YES_NO_NA_CHOICES,
        default='',
        blank=True
    )
    adverse_event_yes = models.TextField(blank=True)
    sedation_effective = models.CharField(
        max_length=3,
        choices=YES_NO_NA_CHOICES,
        default='',
        blank=True
    )
    sedation_effective_no = models.TextField(blank=True)
    initials = models.CharField(max_length=5)
    date = models.DateField()
    def __str__(self):
        return "Procedure Report"


class PostInject1(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=0)
    access_date = timezone.now()

    date = models.DateField(blank=True)
    completed_by = models.CharField(max_length=5)
    local_team_members = models.CharField(max_length=200)

    weeks_postinj1 = models.PositiveSmallIntegerField(default=0)
    attending_clinicians = models.CharField(max_length=200)
    attending_fam_car = models.CharField(max_length=200)

    musc1_inj = models.CharField(max_length=200)
    musc1_inj_n = models.BooleanField()
    musc1_inj_p = models.BooleanField()
    musc1_inj_y = models.BooleanField()

    musc2_inj = models.CharField(max_length=200)
    musc2_inj_n = models.BooleanField()
    musc2_inj_p = models.BooleanField()
    musc2_inj_y = models.BooleanField()

    musc3_inj = models.CharField(max_length=200)
    musc3_inj_n = models.BooleanField()
    musc3_inj_p = models.BooleanField()
    musc3_inj_y = models.BooleanField()

    musc4_inj = models.CharField(max_length=200)
    musc4_inj_n = models.BooleanField()
    musc4_inj_p = models.BooleanField()
    musc4_inj_y = models.BooleanField()

    #face pain-scale options
    pain_0 = models.BooleanField()
    pain_2 = models.BooleanField()
    pain_4 = models.BooleanField()
    pain_6 = models.BooleanField()
    pain_8 = models.BooleanField()
    pain_10 = models.BooleanField()

    goal_1 = models.TextField(blank=True)
    goal_1_y = models.BooleanField()
    goal_1_n = models.BooleanField()
    goal_1_p = models.BooleanField()

    goal_2 = models.TextField(blank=True)
    goal_2_y = models.BooleanField()
    goal_2_n = models.BooleanField()
    goal_2_p = models.BooleanField()

    goal_3 = models.TextField(blank=True)
    goal_3_y = models.BooleanField()
    goal_3_n = models.BooleanField()
    goal_3_p = models.BooleanField()

    goal_4 = models.TextField(blank=True)
    goal_4_y = models.BooleanField()
    goal_4_n = models.BooleanField()
    goal_4_p = models.BooleanField()

    child_fam_goals = models.TextField()
    therapy_intervention = models.TextField()
    physical_activity = models.TextField()
    family_opinions = models.TextField()

    orth_changes_made = models.CharField(
        max_length=3,
        choices=YES_NO_NA_CHOICES,
        blank=True,
    )
    orth_changes = models.TextField(blank=True)

    therapy_implemented_made = models.CharField(
        max_length=3,
        choices=YES_NO_NA_CHOICES,
        blank=True,
    )
    therapy_implemented = models.TextField(blank=True)

    casting_complete_made = models.CharField(
        max_length=3,
        choices=YES_NO_NA_CHOICES,
        default='',
        blank=True,
    )
    casting_complete = models.TextField(blank=True)


    day_case = models.TextField(blank=True)

    side_effects_choices = models.CharField(
        max_length = 3,
        choices=YES_NO_NA_CHOICES,
        default = '',
        blank=True
    )
    side_effects = models.TextField(blank=True)

    pos_effects = models.TextField(blank=True)

    neg_effects = models.TextField(blank=True)

    changes_medical = models.TextField(blank=True)

    date1 = models.DateField()

    completed_by1 = models.CharField(max_length = 5)

    post_inj_examination = models.TextField(blank=True)

    GMFM_A = models.CharField(max_length=20, blank=True)
    GMFM_B = models.CharField(max_length=20, blank=True)
    GMFM_C = models.CharField(max_length=20, blank=True)
    GMFM_D = models.CharField(max_length=20, blank=True)
    GMFM_E = models.CharField(max_length=20, blank=True)

    AHA = models.CharField(max_length=200)

    TUG = models.CharField(max_length=200)
    MFWT= models.CharField(max_length=200)

    post_inj_summary = models.TextField(blank=True)

    date2 = models.DateField(blank=True)
    completed_by2 = models.CharField(max_length=5)

    def __str__(self):
        return "Post Injection Follow up 1"

class PostInject2(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=0)
    access_date = timezone.now()

    date = models.DateField(blank=True)
    completed_by = models.CharField(max_length=5)
    local_team_members = models.CharField(max_length=200)

    weeks_postinj1 = models.PositiveSmallIntegerField(default=0)
    attending_clinicians = models.CharField(max_length=200)
    attending_fam_car = models.CharField(max_length=200)

    musc1_inj = models.CharField(max_length=200)
    musc1_inj_n = models.BooleanField()
    musc1_inj_p = models.BooleanField()
    musc1_inj_y = models.BooleanField()

    musc2_inj = models.CharField(max_length=200)
    musc2_inj_n = models.BooleanField()
    musc2_inj_p = models.BooleanField()
    musc2_inj_y = models.BooleanField()

    musc3_inj = models.CharField(max_length=200)
    musc3_inj_n = models.BooleanField()
    musc3_inj_p = models.BooleanField()
    musc3_inj_y = models.BooleanField()

    musc4_inj = models.CharField(max_length=200)
    musc4_inj_n = models.BooleanField()
    musc4_inj_p = models.BooleanField()
    musc4_inj_y = models.BooleanField()

    #face pain-scale options
    pain_0 = models.BooleanField()
    pain_2 = models.BooleanField()
    pain_4 = models.BooleanField()
    pain_6 = models.BooleanField()
    pain_8 = models.BooleanField()
    pain_10 = models.BooleanField()

    goal_1 = models.TextField(blank=True)
    goal_1_y = models.BooleanField()
    goal_1_n = models.BooleanField()
    goal_1_p = models.BooleanField()

    goal_2 = models.TextField(blank=True)
    goal_2_y = models.BooleanField()
    goal_2_n = models.BooleanField()
    goal_2_p = models.BooleanField()

    goal_3 = models.TextField(blank=True)
    goal_3_y = models.BooleanField()
    goal_3_n = models.BooleanField()
    goal_3_p = models.BooleanField()

    goal_4 = models.TextField(blank=True)
    goal_4_y = models.BooleanField()
    goal_4_n = models.BooleanField()
    goal_4_p = models.BooleanField()

    child_fam_goals = models.TextField()
    therapy_intervention = models.TextField()
    physical_activity = models.TextField()
    family_opinions = models.TextField()

    orth_changes_made = models.CharField(
        max_length=3,
        choices=YES_NO_NA_CHOICES,
        blank=True,
    )
    orth_changes = models.TextField(blank=True)

    therapy_implemented_made = models.CharField(
        max_length=3,
        choices=YES_NO_NA_CHOICES,
        blank=True,
    )
    therapy_implemented = models.TextField(blank=True)

    casting_complete_made = models.CharField(
        max_length=3,
        choices=YES_NO_NA_CHOICES,
        default='',
        blank=True,
    )
    casting_complete = models.TextField(blank=True)


    day_case = models.TextField(blank=True)

    side_effects_choices = models.CharField(
        max_length = 3,
        choices=YES_NO_NA_CHOICES,
        default = '',
        blank=True
    )
    side_effects = models.TextField(blank=True)

    pos_effects = models.TextField(blank=True)

    neg_effects = models.TextField(blank=True)

    changes_medical = models.TextField(blank=True)

    date1 = models.DateField()

    completed_by1 = models.CharField(max_length = 5)

    post_inj_examination = models.TextField(blank=True)

    GMFM_A = models.CharField(max_length=20, blank=True)
    GMFM_B = models.CharField(max_length=20, blank=True)
    GMFM_C = models.CharField(max_length=20, blank=True)
    GMFM_D = models.CharField(max_length=20, blank=True)
    GMFM_E = models.CharField(max_length=20, blank=True)

    AHA = models.CharField(max_length=200)

    TUG = models.CharField(max_length=200)
    MFWT= models.CharField(max_length=200)

    post_inj_summary = models.TextField(blank=True)

    date2 = models.DateField(blank=True)
    completed_by2 = models.CharField(max_length=5)

    def __str__(self):
        return "Post Injection Follow up 1"


class Dysports(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=0)
    date = models.DateField()
    page = 9
    initials = models.CharField(max_length=100)
    childweight = models.DecimalField(max_digits=10,decimal_places=2)
    batchnumber = models.CharField(max_length=100)
    expirydate = models.DateField()
    muscle1 = models.CharField(max_length=100,blank=True)
    dysportunit1 = models.DecimalField(max_digits=100,decimal_places=2,null=True)
    Totaldysport1 = models.DecimalField(max_digits=100,decimal_places=2,null=True)
    mls1 = models.DecimalField(max_digits=100,decimal_places=2,null=True)
    circle_side11 = models.TextField(blank=True)
    circle_side12 = models.TextField(blank=True)
    circle_side13 = models.TextField(blank=True)
    muscle2 = models.CharField(max_length=100,blank=True)
    dysportunit2 = models.DecimalField(max_digits=100,decimal_places=2,null=True)
    Totaldysport2 = models.DecimalField(max_digits=100,decimal_places=2,null=True)
    mls2 = models.DecimalField(max_digits=100,decimal_places=2,null=True)
    circle_side21 = models.TextField(blank=True)
    circle_side22 = models.TextField(blank=True)
    circle_side23 = models.TextField(blank=True)
    muscle3 = models.CharField(max_length=100,blank=True)
    dysportunit3 = models.DecimalField(max_digits=100,decimal_places=2,null=True)
    Totaldysport3 = models.DecimalField(max_digits=100,decimal_places=2,null=True)
    mls3 = models.DecimalField(max_digits=100,decimal_places=2,null=True)
    circle_side31 = models.TextField(blank=True)
    circle_side32 = models.TextField(blank=True)
    circle_side33 = models.TextField(blank=True)
    muscle4 = models.CharField(max_length=100,blank=True)
    dysportunit4 = models.DecimalField(max_digits=100,decimal_places=2,null=True)
    Totaldysport4 = models.DecimalField(max_digits=100,decimal_places=2,null=True)
    mls4 = models.DecimalField(max_digits=100,decimal_places=2,null=True)
    circle_side41 = models.TextField(blank=True)
    circle_side42 = models.TextField(blank=True)
    circle_side43 = models.TextField(blank=True)
    muscle5 = models.CharField(max_length=100,blank=True)
    dysportunit5 = models.DecimalField(max_digits=100,decimal_places=2,null=True)
    Totaldysport5 = models.DecimalField(max_digits=100,decimal_places=2,null=True)
    mls5 = models.DecimalField(max_digits=100,decimal_places=2,null=True)
    circle_side51 = models.TextField(blank=True)
    circle_side52 = models.TextField(blank=True)
    circle_side53 = models.TextField(blank=True)

    totaldose = models.DecimalField(max_digits=100,decimal_places=2,null=True)
    totalunits = models.DecimalField(max_digits=100,decimal_places=2,null=True)


    def __str__(self):
        return "Dysport Calculation Sheet"


class Consents(models.Model):
    Clinician_name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=50)
    Clinician_signature = models.CharField(max_length=100)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=0)
    date = models.DateField()

    def __str__(self):
        return "Consent to Photography or Video Recording"


class Consentss(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=0)
    consent_1 = models.BooleanField(help_text="I consent to photographs/video recordings being taken at for my/my child’s personal medical case-notes.")
    consent_2 = models.BooleanField(help_text="I consent to photographs/video recordings being made available for teaching in the Healthcare context as described above.")
    consent_3 = models.BooleanField(help_text="I consent to photographs/video recordings being published for the specific purpose described below. This consent does not extend to any further publications. ")
    patient_signature = models.CharField(max_length=100)
    parent = models.CharField(max_length=100)
    date = models.DateField()
    relations = models.TextField(blank=True)

    def __str__(self):
        return "Consent to Photography or Video Recording(2)"
