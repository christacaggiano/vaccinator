from django.contrib import admin
from django.db import models
from .models import Parent, Doctor, Vaccine, Child, VaccineCompletion
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from phonenumber_field.modelfields import PhoneNumberField


# Register your models here.

class ParentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        PhoneNumberField: {'widget': PhoneNumberPrefixWidget},
    }

admin.site.register(Parent, ParentAdmin)
admin.site.register(Child)
admin.site.register(Doctor)
admin.site.register(Vaccine)
admin.site.register(VaccineCompletion)