from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
# Form
from .forms import ComplaintForm
from .models import Complaint


class ComplaintView(View):

    template_name = "complaint/complaint.html"
    form = ComplaintForm()
    TITLE = "Denuncia de transito"

    def get(self, request):
        url = reverse("complaint")
        context = {
            'url': url,
            'form': self.form,
            'title': self.TITLE
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.register()
        return redirect("complaint")


complaint_view = ComplaintView.as_view()


class ComplaintPublicationView(View):

    template_name = "complaint/complaint_publication.html"
    TITLE = "Denuncias"

    def get(self, request):
        url = reverse("complaint_publication")
        denuncias = Complaint.objects.all()
        print (denuncias)
        for d in denuncias:
            d_name = d.complainant_name
            d_place = d.place_event
            d_complaint_date = d.complaint_date
            d_date = d.event_date
            d_time = d.event_time
            d_description = d.description
            d_license = d.license_plate
            d_evidence = d.evidence
            d_ranking = d.ranking

        context = {
            'url': url,
            'title': self.TITLE,
            "denuncias" :denuncias,
            "d_name" :d_name,
            "d_place" :d_place,
            "d_complaint_date" :d_complaint_date,
            "d_date" :d_date,
            "d_time" :d_time,
            "d_description" :d_description,
            "d_license" :d_license,
            "d_evidence" :d_evidence,
            "d_ranking" :d_ranking
        }

        return render(request, self.template_name, context)


complaint_publication_view = ComplaintPublicationView.as_view()
