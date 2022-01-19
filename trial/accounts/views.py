from django.shortcuts import render ,redirect ,HttpResponse

from accounts.models import CustomUser, websites
from .forms import CustomCreationForm ,WebsiteForm ,ContactForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.forms import inlineformset_factory
from django.core.mail import send_mail,BadHeaderError


# Create your views here.

def registerpage(request):
    form=CustomCreationForm()
    if request.method=="POST":
        form=CustomCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User Register Successfully')
            return redirect('login')
    context={'form':form}
    return render(request,'register.html',context)


def loginpage(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home',id=user.id)

    return render(request,'login.html')


def home(request,id):
    results={}
    user=CustomUser.objects.get(id=id)
    if request.method=="POST":
        website_name=request.POST['websitename']
        results=websites.objects.filter(name__icontains=website_name)
    context={'user':user,
    'results':results}
    return render(request,'home.html',context)

def addWebsite(request,id):
    customer=CustomUser.objects.get(id=id)
    form=WebsiteForm(initial={'userID':id})
    if request.method=="POST":
        form=WebsiteForm(request.POST,initial={'userID':id})
        if form.is_valid():
            form.save()
            return redirect('home',id=id)
    context={'form':form}
    '''
    WebsiteFormSet=inlineformset_factory(parent_model=CustomUser ,model=websites,form=WebsiteForm,fields=('name','username','password','email','recoveremail','phone'),extra=5)
    customer=CustomUser.objects.get(id=id)
    formset=WebsiteFormSet()
    if request.method=="POST":
        formset=WebsiteFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('home',id=id)
    context={'formset':formset}
    '''
    #return render(request,'addwebsite.html',context)
    return render(request,'website.html',context)


def search (request,id):
    if request.method=="POST":
        website_name=request.POST['websitename']
    results=websites.objects.filter(name__icontains=website_name)
    print(results)


def contact(request,id):
    form=ContactForm()
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            fullname=form.cleaned_data['firstname']+form.cleaned_data['secondname']
            subject=form.cleaned_data['subject']
            from_email=form.cleaned_data['from_email']
            body=form.cleaned_data['body']
            message=fullname+'\n'+body
            try:
                send_mail(subject,message,from_email,['ayaelamir189@gmail.com'])
            except BadHeaderError:
                return HttpResponse("Bad Header Error ")
            return redirect('home',id=id)
    return render(request,'contact.html',{'form':form})


def profile(request,id):
    usr=CustomUser.objects.get(id=id)
    websites=usr.websites_set.all()
    form=CustomCreationForm(instance=usr)
    if request.method=='post':
        form=CustomCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form,
            'websites':websites}
    return render(request,'profile.html',context)


def updatewebsite(request,id):
    website=websites.objects.get(id=id)
    form=WebsiteForm(instance=website)
    context={'form':form}
    if request.method=="post":
        form=WebsiteForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect()
        
    return render(request,'update.html',context)


def deletewebsite(request,id):
    website=websites.objects.get(id=id)
    context={'website':website}
    if request.method=="post":
        websites.delete()

    return render(request,'delete.html',context)


