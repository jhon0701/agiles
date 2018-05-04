from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
# Form
from .forms import ComplaintForm


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
        context = {
            'url': url,
            'title': self.TITLE
        }
        return render(request, self.template_name, context)


complaint_publication_view = ComplaintPublicationView.as_view()
