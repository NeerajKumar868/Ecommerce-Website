import imp
from django.shortcuts import redirect, render
from account.forms import *
from cartapp.models import Cart
from ecommerceapp.models import Mobile
from.models import *
from django.contrib import messages
from account.templatetags.usertags import *
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/account/login')
def addtocart(request,id):
    cart_obj=Cart.objects.filter(user=request.user)
    if len(cart_obj) == 0:
        cart=Cart.objects.create(user=request.user)
    else:
        cart=cart_obj[0]
    mobile=Mobile.objects.get(mobileid=id)
    product=Product.objects.create(mobile=mobile,quantity=1)
    product.save()
    print("Item Added To Cart")
    cart.productlist.add(product)
    cart.save()
    messages.success(request,f'{mobile.mobilename} Added Suceesfully')
    return redirect('/index')
    
# to delete all product from database ( truncate cartapp_cart_productlist; )
@login_required(login_url='/account/login')
def viewcart(request):
    mycart=Cart.objects.filter(user=request.user)[0]
    return render(request,'cart.html',{'mycart':mycart})

def removefromcart(request,pid):
    product=Product.objects.get(pid=pid)
    product.delete()
    return redirect('/cartapp/view')



@login_required(login_url='/account/login')
def update(request):
    quantity=request.POST['quantity']
    pid=request.POST['pid']
    product=Product.objects.get(pid=pid)
    product.quantity=quantity
    product.save()
    totalamount=multiply(float(product.quantity),float(product.mobile.mobileprice))
    mycart=Cart.objects.filter(user=request.user)[0]
    totalbill=calcBill(mycart.productlist.all())
    jsonobj={'response':'True','totalamount':totalamount,'totalbill':totalbill}
    return JsonResponse(jsonobj)



# def save(request):
#     if request.method=="GET":
#         return render(request,'summery.html',{'action':'save'})
#     elif request.method=="POST":
#         address=request.POST['address']
#         city=request.POST['city']
#         state=request.POST['state']
#         country=request.POST['country']
#         pincode=request.POST['pincode']
#         summery_obj=Profile.objects.create(address=address,city=city,state=state,country=country,pincode=pincode)
#         summery_obj.save()
#         return redirect('/cartapp/view')
