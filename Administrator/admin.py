from django.contrib import admin

from .models import Tutor,DanceCourses

admin.site.register(DanceCourses)

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
        list_display=("tutor_name",
        "tutor_contact",
        "tutor_email",
        "tutor_gender",
        "tutor_dob",
        "tutor_designation",
        "tutor_dancecategory",
        "tutor_district",
        )