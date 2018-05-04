from django.contrib import admin
from django.urls import path

# Views
from complaint.views import (
    complaint_view,
    complaint_publication_view
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('complaint', complaint_view, name="complaint"),
    path('complaint/publications', complaint_publication_view,
         name="complaint_publication"),
]
