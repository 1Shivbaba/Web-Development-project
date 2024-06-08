from django.contrib import admin
from contact_inquiry.models import Contact_Inquiry


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_name',
                    'contact_mail',
                    'contact_phone',
                    'contact_subject',
                    'contact_message' 
                    )
    
admin.site.register(Contact_Inquiry, ContactAdmin)