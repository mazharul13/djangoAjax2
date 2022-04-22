from django.shortcuts import render, redirect

from contact.forms import ContactForm
from contact.models import Contact
from django.http import HttpResponse


# Create your views here.

def list_view(request):
    contacts = Contact.objects.all()
    return render(request, "contact_list.html", {'contacts': contacts, 'myValue': 100})


def delete_ajax_cntact(request):
    ename = ""
    id = 0
    if request.method == 'POST':
        id = request.POST['post_id']
        if int(id) > 0:
            try:
                contact = Contact.objects.get(id=id)
                ename = contact.ename
                # contact.delete()
            except:
                pass

    return HttpResponse("Specified Contact of '" + ename + "' has been deleted")
    # render(request, "contact_list.html", {'contacts': contacts, 'ename': ename})




def delete_cntact(request, id):
    ename = ""
    if id > 1:
        try:
            contact = Contact.objects.get(id=id)
            ename = contact.ename
            contact.delete()
        except:
            pass

    contacts = Contact.objects.all()
    return render(request, "contact_list.html", {'contacts': contacts, 'ename': ename})

    # return redirect("/contact/info")


def new_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact/info')
        else:
            # form = ContactForm()
            return render(request, "new_contact.html", {'form':form})
    else:
        form = ContactForm()
        return render(request, "new_contact.html", {'form':form})
