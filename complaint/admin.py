from django.contrib import admin

# Model complaint
from .models import Complaint


class ComplaintAdmin(admin.ModelAdmin):

    list_display = [
        "id", "complainant_name", "place_event", "complaint_date",
        "event_date_time", "description", "evidence"
    ]

    class Meta:
        model = Complaint


admin.site.register(Complaint, ComplaintAdmin)
