from django.shortcuts import redirect, render
from cartapp.models import *
from orderapp.models import *
from django.contrib import messages
# Create your views here.

def saveadd(request):
    if request.method=="GET":
        return render(request,'summery.html',{'action':'save'})
    elif request.method=="POST":
        phone_number=request.POST['phone_number']
        address=request.POST['address']
        state=request.POST['state']
        city=request.POST['city']
        country=request.POST['country']
        pincode=request.POST['pincode']
        address_obj=Address.objects.create(phone_number=phone_number,address=address,state=state,city=city,country=country,pincode=pincode)
        address_obj.save()
        return redirect('/index/')

def placeorder(request):
    id=request.POST['id']
    amount=request.POST['amount']
    cart=Cart.objects.get(cartid=id)
    order=Order.objects.create(user=request.user,billamount=amount,orderstatus="Order Placed")
    order.productlist.set(cart.productlist.all())
    order.save()
    cart.productlist.clear()
    messages.success(request,"ORDER PLACED SUCCESSFULLY")
    return render(request,"order.html",{"order":order})




def invoice(request):
    mycart=Cart.objects.filter(user=request.user)[0]
    return render(request,'invoice.html',{'mycart':mycart})