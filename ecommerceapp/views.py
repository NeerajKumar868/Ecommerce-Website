import re
from django.shortcuts import redirect, render
from ecommerceapp.models import Mobile


# Create your views here.
def index(request):
    mobile_list=Mobile.objects.all()
    return render(request,'index.html',{'mobile_list':mobile_list})

def delete(request,id):
    mobile_list=Mobile.objects.get(mobileid=id)
    mobile_list.delete()
    return redirect('/index')

def save(request):
    if request.method=="GET":
        return render(request,'form.html',{'action':'save'})
    elif request.method=="POST":
        mobilename=request.POST['mobilename']
        mobileprice=request.POST['mobileprice']
        mobilediscription=request.POST['mobilediscription']
        mobileoffer=request.POST['mobileoffer']
        mobiledeliver=request.POST['mobiledeliver']
        mobileimage=request.FILES['mobileimage']
        mobile_obj=Mobile.objects.create(mobilename=mobilename,mobileprice=mobileprice,mobilediscription=mobilediscription,image=mobileimage,mobileoffer=mobileoffer,mobiledeliver=mobiledeliver)
        mobile_obj.save()
        return redirect('/index')

def edit(request,id):
     mobile_list=Mobile.objects.get(mobileid=id)
     return render(request,'form.html',{'action':'Update','mobile_list':mobile_list})

def update(request):
    if request.method=="POST":
        mobileid=request.POST['mobileid']
        mobilename=request.POST['mobilename']
        mobileprice=request.POST['mobileprice']
        mobilediscription=request.POST['mobilediscription']
        mobileoffer=request.POST['mobileoffer']
        mobiledeliver=request.POST['mobiledeliver']
        mobileimage=request.FILES['mobileimage']
        mobile=Mobile.objects.filter(mobileid=mobileid)
        mobile.update(mobileid=mobileid,mobilename=mobilename,mobileprice=mobileprice,mobilediscription=mobilediscription,image=mobileimage,mobileoffer=mobileoffer,mobiledeliver=mobiledeliver)
        return redirect('/index')

