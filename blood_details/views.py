from django.shortcuts import render, redirect
from .models import DonorDetails


def all_donor(request):
    donors = DonorDetails.objects.all()
    return render(request, 'blood_details/donors.html', context={'donors': donors})


def add_donor(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        blood_group = request.POST.get('blood_group')
        contact_no = request.POST.get('contact_no', '')
        email = request.POST.get('email', '')
        try:
            donor_obj = DonorDetails.objects.create(name=name, blood_group=blood_group, contact_no=contact_no, email=email)
            donor_obj.save()
            return redirect('/')
        except:
            return redirect('/')
    return render(request, 'blood_details/add_donor.html')
