from datetime import datetime
from django.shortcuts import render
from .models import ContactForm

# Create your views here.
def home(request):
    context = {"name": "Om"}
    return render(request, "home/home.html", context)

def under(request):
    return render(request, "home/under.html")

def submitForm(request):
    if request.method == "POST":
        contact_form = ContactForm()
        contact_form.name = request.POST["name"]
        contact_form.email = request.POST["email"]
        contact_form.phone = request.POST["phone"]
        contact_form.message = request.POST["message"]
        contact_form.date = datetime.now()
        contact_form.save()
    return render(request, "home/home.html")