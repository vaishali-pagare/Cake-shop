from django.shortcuts import render,redirect
from adminApp.models import Category,Product,userInfo,Payment
from userApp.models import MyCart,OrderMaster
from django.contrib import messages

# Create your views here.
def homepage(request):
    cats = Category.objects.all()
    cakes = Product.objects.all()
    return render(request,"homepage.html",{"cats":cats,"cakes":cakes})

def login(request):
    if(request.method=="GET"):
        cats = Category.objects.all()
        return render(request,"login.html",{"cats":cats,})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        try:
            id = userInfo.objects.get(uname=uname,password=pwd)
            messages.success(request, "Login sucessful")
            return redirect(login)
        except:
            messages.success(request, "Invalid Login")
            return redirect(login)
        else:
            request.session["uname"] = uname
            return redirect(homepage)
  


def signup(request):
    if(request.method=="GET"):
        return render(request,"signup.html",{})
    
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        email = request.POST["email"]
        user = userInfo(uname,pwd,email)
        user.save()
        return redirect(homepage)

def logout(request):
    request.session.clear()
    return redirect(homepage)
   

def showcakes(request,id):
    #id = Category.objects.get(id = id)
    #print(id)
    cakes = Product.objects.filter(cat = id)
    print(cakes)
    cats = Category.objects.all()
    return render(request,"homepage.html",{"cats":cats,"cakes":cakes})

def cakeDetails(request,id):
    cake = Product.objects.get(id = id)
    cats = Category.objects.all()
    return render(request,"cakeDetails.html",{"cake":cake,"cats":cats,})

def addtocart(request):
    if(request.method=="POST"):
        if("uname" in request.session):
            user = request.session["uname"]
            cakeid = request.POST["cakeid"]
            qty = request.POST["qty"]
            userid = userInfo.objects.get(uname= user)
            cake = Product.objects.get(id = cakeid)
            
            try:
                cart = MyCart.objects.get(cake = cake,user = userid)
            except:
                cart = MyCart()
                cart.cake = cake
                cart.user = userid
                cart.qty = qty
                cart.save()
            else:
                pass
            return redirect(homepage)

        else:
            return redirect(login)

def showAll(request):
    uname = request.session["uname"]
    if(request.method=="GET"):
        cats = Category.objects.all()
        
        user = userInfo.objects.get(uname=uname)
        cart = MyCart.objects.filter(user= user)
        total = 0
        for item in cart:
            total += int(item.qty)*item.cake.price
        request.session["total"] = total
        return render(request,"showall.html",{"mycart" : cart,"cats":cats})
    else:
        uname = request.session["uname"]

        cake = request.POST["cakeid"]
        cake = Product.objects.get(id = cake)
        id = MyCart.objects.get(cake=cake,user=uname)

        qty = request.POST["qty"]
        id.qty = qty
        id.save()

        return redirect(showAll)

def removeItem(request):
    uname = request.session["uname"]
    cake = request.POST["cakeid"]
    cake = Product.objects.get(id = cake)
    id = MyCart.objects.get(cake=cake,user=uname)

    id.delete()
    return redirect(showAll)



    


def remove(request,id):
    if(request.method=="GET"):
        return render(request,"remove.html",{})
    else:
        result = request.POST["action"]
        id = MyCart.objects.get(id = id)
        if(result=="yes"):
            id.delete()
        return redirect(showAll)
        
        
        

def payment(request):
    if(request.method == "GET"):
        return render(request,"payment.html",{})
    else:
        cardno = request.POST["cardno"]
        cvv = request.POST["cvv"]
        expiry = request.POST["expiry"]
        try:
            buyer = Payment.objects.get(cardno=cardno,cvv=cvv,expiry=expiry)
        except:
            return redirect(payment)
        else:
            owner = Payment.objects.get(cardno='111',cvv='111',expiry='12/2022')
            owner.balance += request.session["total"]
            buyer.balance -=  request.session["total"]
            owner.save()
            buyer.save()
            uname = request.session["uname"]
            user = userInfo.objects.get(uname=uname)
            order = OrderMaster()
            order.user = user
            order.amount = request.session["total"]
            details = ""
            items = MyCart.objects.filter(user=user)
            for item in items:
                details += item.cake.pname+" "
                item.delete()
                
            order.details = details
            order.save()

            return redirect(homepage)

def demo(request):
    return render(request, "demo.html",{})

def pagedemo(request):
    cakes = Product.objects.all()
    if("count" not in request.session):
        request.session["count"] = 0
    else:
        request.session["count"] += 1
    count = request.session["count"]
    return render(request, "page.html",{"cakes":cakes[count]})