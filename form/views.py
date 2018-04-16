from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext as _

from .forms import *


def current_date():
    return date.today()

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('Your password was successfully updated!'))
            return redirect('/')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'form/change_password.html', {
        'form': form
    })

@login_required
def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            id = patient.patient_id
            patient.access_date = timezone.now()
            patient.save()
            return redirect('../' + str(id))
    else:
        form = PatientForm()
    return render(request, 'form/patient_add.html', {'form': form, 'date': current_date()})

@login_required
def edit_patient(request):
    time = datetime.now()
    patients = Patient.objects.all()
    return render(request, 'form/patient_edit.html', {'patients': patients, 'db_time': time, 'date': current_date()}, )

@login_required
def get_patient_information(request, patient_id):
    pat = get_object_or_404(Patient, patient_id=patient_id)
    return render(request, 'form/patient_information.html', {'patient': pat, 'patient_id':patient_id, 'date': current_date()})

@login_required
def get_patient_dashboard(request):
    time = datetime.now()
    patients = Patient.objects.all()
    return render(request, 'form/patient_dashboard.html', {'patients':patients, 'db_time': time, 'date': current_date()}, )

@login_required
def get_med_clerk_pre_sed(request, patient_id):
    pat = get_object_or_404(Patient, patient_id=patient_id)
    try:
        # fetch MedClerk page for patient pat
        med = MedClerkPreSed.objects.get(patient=pat)
    except Exception:
        # pat has not created a MedClerk page yet
        med = None
    if request.method == "POST":
        # filling in the form
        form = MedClerkPreSedForm(request.POST or None, instance=med)
        if form.is_valid():
            medclerkpresed = form.save(commit=False)
            medclerkpresed.patient = get_object_or_404(Patient, patient_id=patient_id)
            medclerkpresed.access_date = timezone.now()
            medclerkpresed.save()
            return redirect('/'+str(patient_id))
    elif med is not None:
        # view existing/edit
        form = MedClerkPreSedForm(None, instance=med)
    else:
        # create new medclerk form
        form = MedClerkPreSedForm()
    return render(request, 'form/icp/11_medclerk.html', {'form': form, 'patient': pat, 'date': current_date()})

@login_required
def get_post_inject1(request, patient_id):
    pat = get_object_or_404(Patient, patient_id=patient_id)
    try:
        postinj = PostInject1.objects.get(patient=pat)
    except Exception:
        postinj = None
    if request.method == "POST":
        form = PostInject1Form(request.POST or None, instance=postinj)
        if form.is_valid():
            postinj = form.save(commit=False)
            postinj.patient = get_object_or_404(Patient, patient_id=patient_id)
            postinj.access_date = timezone.now()
            postinj.save()
            return redirect('/'+str(patient_id))
    elif postinj is not None:
        form = PostInject1Form(None, instance=postinj)
    else:
        form = PostInject1Form()
    return render(request, 'form/icp/13_post_inject1.html', {'form': form, 'patient': pat, 'date': current_date()})\

@login_required
def get_post_inject2(request, patient_id):
    pat = get_object_or_404(Patient, patient_id=patient_id)
    try:
        postinj2 = PostInject2.objects.get(patient=pat)
    except Exception:
        postinj2 = None
    if request.method == "POST":
        form = PostInject2Form(request.POST or None, instance=postinj2)
        if form.is_valid():
            postinj2 = form.save(commit=False)
            postinj2.patient = get_object_or_404(Patient, patient_id=patient_id)
            postinj2.access_date = timezone.now()
            postinj2.save()
            return redirect('/'+str(patient_id))
    elif postinj2 is not None:
        form = PostInject2Form(None, instance=postinj2)
    else:
        form = PostInject2Form()
    return render(request, 'form/icp/14_post_inject2.html', {'form': form, 'patient': pat, 'date': current_date()})

@login_required
def get_proc_report(request, patient_id):
    pat = get_object_or_404(Patient, patient_id=patient_id)
    try:
        proc = ProcReport.objects.get(patient=pat)
    except Exception:
        proc = None
    if request.method == "POST":
        form = ProcReportForm(request.POST or None, instance=proc)
        if form.is_valid():
            proc = form.save(commit=False)
            proc.patient = get_object_or_404(Patient, patient_id=patient_id)
            proc.access_date = timezone.now()
            proc.save()
            return redirect('/'+str(patient_id))
    elif proc is not None:
        form = ProcReportForm(None, instance=proc)
    else:
        form = ProcReportForm()
    return render(request, 'form/icp/12_procedure_report.html', {'form': form, 'patient': pat, 'date': current_date()})

@login_required
def get_conc_of_treatment(request, patient_id):
    pat = get_object_or_404(Patient, patient_id=patient_id)
    try:
        conc = ConcOfTreatment.objects.get(patient=pat)
    except Exception:
        conc = None
    if request.method == "POST":
        form = ConcOfTreatmentForm(request.POST or None, instance=conc)
        if form.is_valid():
            concoftreat = form.save(commit=False)
            concoftreat.patient = get_object_or_404(Patient, patient_id=patient_id)
            concoftreat.access_date = timezone.now()
            concoftreat.save()
            return redirect('/'+str(patient_id))
    elif conc is not None:
        form = ConcOfTreatmentForm(None, instance=conc)
    else:
        form = ConcOfTreatmentForm()
    return render(request, 'form/icp/19_conclusion_of_treatment.html', {'form': form, 'patient': pat, 'date': current_date()})

@login_required
def get_dysports(request,patient_id):
    pat = get_object_or_404(Patient,patient_id=patient_id)
    try:
        dys = Dysports.objects.get(patient=pat)
    except Exception:
        dys = None
    if request.method == "POST":
        form = DysportForm(request.POST or None,instance=dys)
        if form.is_valid():
            dysportform = form.save(commit=False)
            dysportform.patient = get_object_or_404(Patient,patient_id=patient_id)
            dysportform.date = timezone.now()
            dysportform.save()
            return redirect('/'+str(patient_id))
    elif dys is not None:
        form = DysportForm(None,instance=dys)
    else:
        form = DysportForm()

    return render(request,'form/icp/9_dysport_calculation_sheet.html',{'form':form,'patient':pat, 'date': current_date()})

@login_required
def get_consents(request,patient_id):
    pat = get_object_or_404(Patient,patient_id=patient_id)
    try:
        cons = Consents.objects.get(patient=pat)
    except Exception:
        cons = None
    if request.method == "POST":
        form = ConsentForm(request.POST or None,instance=cons)
        if form.is_valid():
            consentform = form.save(commit=False)
            consentform.patient = get_object_or_404(Patient,patient_id=patient_id)
            consentform.date = timezone.now()
            consentform.save()
    elif cons is not None:
        form = ConsentForm(None,instance=cons)
    else:
        form = ConsentForm()

    return render(request,'form/icp/8_consent_to_photography_or_video_recording.html',{'form':form,'patient':pat, 'date': current_date()})

@login_required
def get_consentss(request,patient_id):
    pat = get_object_or_404(Patient,patient_id=patient_id)
    try:
        conss = Consentss.objects.get(patient=pat)
    except Exception:
        conss = None
    if request.method == "POST":
        form = ConsentForm2(request.POST or None,instance=conss)
        if form.is_valid():
            consentform2 = form.save(commit=False)
            consentform2.patient = get_object_or_404(Patient,patient_id=patient_id)
            consentform2.date = timezone.now()
            consentform2.save()
            return redirect('/'+str(patient_id))
    elif conss is not None:
        form = ConsentForm2(None,instance=conss)
    else:
        form = ConsentForm2()

    return render(request,'form/icp/8_2_consent_to_photography_or_video_recording.html',{'form':form,'patient':pat, 'date': current_date()})