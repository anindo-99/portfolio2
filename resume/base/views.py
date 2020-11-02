from django.shortcuts import render,redirect
from base.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'base/home.html')
# def contact(request):
#     return render(request,'base/contact.html')

def contact(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip_code']
        content = request.POST['content']

        if len(first_name) < 2 or len(first_name) < 2 or len(last_name) < 2 or len(email) < 4 or len(phone) < 7 or len(city) < 2 or len(state) < 3 or len(zip_code) < 6 or len(content) < 4:
            messages.error(request, "Please fill up the form correctly!")

        else:

            contact = Contact(first_name=first_name, last_name=last_name, email=email,
                              phone=phone, city=city, state=state, zip_code=zip_code, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent.")
            return redirect(home)
    return render(request, 'base/contact.html')
