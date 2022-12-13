from django import template
register=template.Library()

def isAdmin(user):
    return user.groups.filter(name="admin").exists()

def isCustomer(user):
    return user.groups.filter(name="customer").exists()

register.filter("admin",isAdmin)
register.filter("customer",isCustomer)

def multiply(qty,unit_price):
    return qty*unit_price
register.filter("multiply",multiply)

def calcBill(productlist):
    total=0
    for product in productlist:
        total += product.mobile.mobileprice * product.quantity
    return total

register.filter('calcBill',calcBill)