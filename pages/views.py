import requests

from django.shortcuts import render,redirect
from django.http import HttpResponse

from .generate_pdf import pdf_generator
from .forms import ConsultationForm

def consultation(request):
    if request.method == "GET":#how do we know the request is get or post
        form = ConsultationForm()
        context = {}
        context["form"] = form
        return render(request, "pages/index.html", context)
    if request.method == "POST":
        form = ConsultationForm(request.POST)
        if form.is_valid():
            new_consultation = form.save()
            output_file_path, filename = pdf_generator(new_consultation)
            new_consultation.pdf_form.name = output_file_path
            new_consultation.save()
            media_url = "/media/generatedPdfs/{}".format(filename)
            return redirect(media_url)






