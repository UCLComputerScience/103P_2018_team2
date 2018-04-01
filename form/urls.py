from django.urls import path
from django.contrib import admin
from . import views

import django.contrib.auth.views as auth_views
from django.conf.urls import include, url


urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'form/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^password/$',views.change_password, name='change_password'),
    url(r'^admin/', admin.site.urls),    path('', views.get_patient_dashboard, name='get_patient_dashboard'),
    path('add-patient/', views.add_patient, name='add_patient'),
    path('edit-patient/', views.edit_patient, name='edit_patient'),
    path('<patient_id>/', views.get_patient_information, name='get_patient_information'),
    path('<patient_id>/medical-clerking-pre-sedation', views.get_med_clerk_pre_sed, name='get_med_clerk_pre_sed'),
    path('<patient_id>/procedure-report', views.get_proc_report, name='get_proc_report'),
    path('<patient_id>/post-injection-follow-up-1', views.get_post_inject1, name='get_post_inject1'),
    path('<patient_id>/post-injection-follow-up-2', views.get_post_inject2, name='get_post_inject2'),
    path('<patient_id>/conclusion-of-treatment', views.get_conc_of_treatment, name='get_conc_of_treatment'),
    path('<patient_id>/consent-to-photography-or-video-recording',views.get_consents,name='get_consents'),
    path('<patient_id>/dysport_calculation_sheet',views.get_dysports,name='get_dysports'),
    path('<patient_id>/consent-to-photography-or-video-recording2',views.get_consentss,name='get_consentss'),
]
