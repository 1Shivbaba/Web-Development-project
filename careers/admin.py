from django.contrib import admin
from careers.models import Careers

# Register your models here.
class CareerAdmin(admin.ModelAdmin):
    list_display = ('candidate_name',
                    'candidate_mail',
                    'candidate_phone',
                    'candidate_quali',
                    'candidate_post' , 
                    'condidate_address',
                    'condidate_message',
                    'condidate_cv',
                    )
    
admin.site.register( Careers, CareerAdmin)