from django.shortcuts import render

# Create your views here.
def contact_details(request):
    return render(request, template_name='contacts/contacts.html')