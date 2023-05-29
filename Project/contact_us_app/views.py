from django.shortcuts import render
from .models import contact as ContactModel

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_info = request.POST.get('contact')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name, email, contact_info, subject, message) 
        cont = ContactModel.objects.create(
            name=name,
            Email=email,
            contact_no=contact_info,
            subject=subject,
            message=message
        )
        # cont.save()  # Saving is not necessary when using create()
    return render(request, 'contact.html')
