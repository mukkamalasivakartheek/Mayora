from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'Home.html',{'title':'Home'})
def Aboutus(request):
    return render(request,'Aboutus.html')
def Contactus(request):
    return render(request,'contactus.html')
def Services(request):
    return render(request,'services.html')
def SocialMedia(request):
    return render(request,'social_media.html')
def Web_dev(request):
    return render(request,'web_dev.html')
def CreativeDesign(request):
    return render(request,'creative_design.html')