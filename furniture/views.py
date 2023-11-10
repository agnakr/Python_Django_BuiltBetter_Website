from django.shortcuts import render
from furniture.models import contact
# from furniture.models import register
# Create your views here.
def home(request):
    return render(request, "index.html")
def contactpage(request):
    if request.method == "POST":
        a=contact()
        a.name=request.POST.get("name")
        a.email=request.POST.get("email")
        a.message=request.POST.get("message")
        a.save()
        return render(request,"index.html")
def contact_view(request):
    b = contact.objects.all()
    return render(request, "contact_data.html", {'info':b})
def delete(request, id):
    c = contact.objects.get(id=id)
    c.delete()
    b = contact.objects.all()
    return render(request, "contact_data.html", {'info': b})

# def registerview(request):
#     if request.method == "POST":
#         d=register()
#         d.fname=request.POST.get("fname")
#         d.eml=request.POST.get("eml")
#         d.psw=request.POST.get("psw")
#         d.save()
#         return render(request,"registration.html")







