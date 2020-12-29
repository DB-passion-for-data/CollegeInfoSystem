from django.shortcuts import render

def Homepage(request):
    return render(request,"Homepage.html")
def TeachersData(request):
    return render(request,"TeachersData.html")
def About(request):
    return render(request,"About.html")
def Contactus(request):
    return render(request,"Contact.html")