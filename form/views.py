from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Member
from django.conf import settings
import os
import uuid

def membership_form(request):
    if request.method == 'POST':
        # Process form data
        full_name = request.POST.get('fullName')
        state_of_origin = request.POST.get('stateOfOrigin')
        lga = request.POST.get('lga')
        membership_no = request.POST.get('membershipNo')
        
        # Handle file upload
        passport_photo = request.FILES.get('passportPhoto')
        if passport_photo:
            # Create passports directory if it doesn't exist
            os.makedirs(os.path.join(settings.MEDIA_ROOT, 'passports'), exist_ok=True)
            
            # Generate unique filename
            ext = passport_photo.name.split('.')[-1]
            filename = f"{uuid.uuid4()}.{ext}"
            photo_path = os.path.join(settings.MEDIA_ROOT, 'passports', filename)
            
            # Save the file
            with open(photo_path, 'wb+') as destination:
                for chunk in passport_photo.chunks():
                    destination.write(chunk)
            
            photo_url = os.path.join('passports', filename)  # Changed to relative path
        else:
            photo_url = None
        
        # Create member (you should add validation and error handling)
        member = Member.objects.create(
            full_name=full_name,
            state_of_origin=state_of_origin,
            lga=lga,
            membership_no=membership_no,
            passport_photo=photo_url,  # This should match your model's FileField/ImageField
            # add all other fields here
        )
        
        # Redirect to receipt page with member ID
        return redirect('membership_receipt', member_id=member.id)
    
    # Changed template path to match your directory structure
    return render(request, 'form/form.html')

def membership_receipt(request, member_id):
    member = Member.objects.get(id=member_id)
    # Changed template path to match your directory structure
    return render(request, 'form/receipt.html', {'member': member})