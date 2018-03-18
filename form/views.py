from django.shortcuts import render, get_object_or_404
from .forms import *

from django.http import *
from django.shortcuts import render_to_response,redirect, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
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
            patient.access_date = timezone.now()
            patient.save()
    else:
        form = PatientForm()
    return render(request, 'form/patient_add.html', {'form': form})

@login_required
def edit_patient(request):
    patients = Patient.objects.all()
    return render(request, 'form/patient_edit.html', {'patients': patients})

@login_required
def get_patient_information(request, patient_id):
    pat = get_object_or_404(Patient, patient_id=patient_id)
    return render(request, 'form/patient_information.html', {'patient': pat, 'patient_id':patient_id})

@login_required
def get_patient_dashboard(request):
    patients = Patient.objects.all()
    return render(request, 'form/patient_dashboard.html', {'patients':patients})

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
    elif med is not None:
        # view existing/edit
        form = MedClerkPreSedForm(None, instance=med)
    else:
        # create new medclerk form
        form = MedClerkPreSedForm()
    return render(request, 'form/icp/11_medclerk.html', {'form': form, 'patient': pat})

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
    elif proc is not None:
        form = ProcReportForm(None, instance=proc)
    else:
        form = ProcReportForm()
    return render(request, 'form/icp/12_procedure_report.html', {'form': form, 'patient': pat})

@login_required
def get_post_inject1(request, patient_id):
    pat = get_object_or_404(Patient, patient_id=patient_id)
    try:
        # fetch MedClerk page for patient pat
        postinj1 = PostInject1.objects.get(patient=pat)
    except Exception:
        # pat has not created a MedClerk page yet
        postinj1 = None
    if request.method == "POST":
        # filling in the form
        form = PostInject1Form(request.POST or None, instance=postinj1)
        if form.is_valid():
            postinject1 = form.save(commit=False)
            postinject1.patient = get_object_or_404(Patient, patient_id=patient_id)
            postinject1.access_date = timezone.now()
            postinject1.save()
    elif postinj1 is not None:
        # view existing/edit
        form = PostInject1Form(None, instance=postinj1)
    else:
        # create new medclerk form
        form = PostInject1Form()
    return render(request, 'form/icp/13_postinject1.html', {'form': form, 'patient': pat})

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
    elif conc is not None:
        form = ConcOfTreatmentForm(None, instance=conc)
    else:
        form = ConcOfTreatmentForm()
    return render(request, 'form/icp/19_conclusion_of_treatment.html', {'form': form, 'patient': pat})
