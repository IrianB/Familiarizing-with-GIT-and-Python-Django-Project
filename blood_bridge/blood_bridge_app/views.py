from django.shortcuts import render
from .models import Donor

def donor_list(request):
    donors = Donor.objects.all()
    return render(request, "app_name/donor_list.html", {"donors": donors})
