from django.urls import path

from . import views

import django.contrib.auth.views as auth_views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'form/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^password/$',views.change_password,  name='change_password'),
    path('', views.get_patient_dashboard, name='get_patient_dashboard'),
    path('add-patient/', views.add_patient, name='add_patient'),
    path('edit-patient/', views.edit_patient, name='edit_patient'),
    path('<int:patient_id>/', views.get_patient_information, name='get_patient_information'),
    path('<int:patient_id>/medical-clerking-pre-sedation', views.get_med_clerk_pre_sed, name='get_med_clerk_pre_sed'),
    path('<int:patient_id>/procedure-report', views.get_proc_report, name='get_proc_report'),
    path('<int:patient_id>/post-inject1', views.get_post_inject1, name='get_post_inject1'),
    path('<int:patient_id>/conclusion-of-treatment', views.get_conc_of_treatment, name='get_conc_of_treatment'),
]
