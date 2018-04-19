from django.contrib import admin

# Register your models here.
from .models import *

#Part I (Pre-Injection)
admin.site.register(Patient)
#Pre-assessment details
#Pre-injection
#Range of Movement(Upper Limb)
#Range of Movement(Lower Limb)

#Part II (Injection)
admin.site.register(Consents)
admin.site.register(Consentss)
admin.site.register(Dysports)
admin.site.register(MedClerkPreSed)
admin.site.register(ProcReport)

#Part III (Post-Injection)
admin.site.register(PostInject1)
admin.site.register(PostInject2)

#Part IV (Conclusion)
admin.site.register(ConcOfTreatment)