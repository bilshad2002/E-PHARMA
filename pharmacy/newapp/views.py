from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import user,Product,cart,booking
from .forms import PharmaEditForm,UserEditForm,ProductEditForm
from django.contrib.auth.models import User,auth

# Create your views here.

def start(request):
    return render(request,'register.html')

def reg(request):
    if request.method == 'POST':
        UserName = request.POST['UserName']
        Email = request.POST['Email']
        Address = request.POST['Address']
        PhoneNo = request.POST['PhoneNo']
        Password = request.POST['Password']
        data = user.objects.create(UserName=UserName,Email=Email,Address=Address,PhoneNo=PhoneNo,Password=Password,type=1)
        data.save()
        # return HttpResponse("created")
        return redirect(Login)
    else:
        return redirect(reg)
def Login(request):
    if request.method == 'POST':
        UserName = request.POST['UserName']
        Password = request.POST['Password']
        try:
            users = user.objects.get(UserName=UserName,Password=Password)
            if users.type == 1:
                request.session['id'] = users.id
                return redirect(userhome)
            if users.type == 0:
                request.session['id'] = users.id
                return redirect(pharmahome)
            else:
                return HttpResponse('error')
        except Exception as e:
            return HttpResponse('error')
    else:
        return render(request,'login.html')

def pharmahome(request):
    return render(request,'pharmahome.html')

def userhome(request):
    return render(request,'index.html')

def pharmaprofile(request):
    if 'id' in request.session:
        user_id= request.session['id']
        data= user.objects.get(id=user_id)
        return render(request,'pharma_profile.html',{'data':data})

def edit_pharmaprofile(request,id):
    if 'id' in request.session:
        pharma = user.objects.get(id=id)
        print(pharma)
        form = PharmaEditForm(instance=pharma)
        if request.method == 'POST':
            form = PharmaEditForm(request.POST,instance=pharma)
            if form.is_valid():
                form.save()
                return redirect(pharmaprofile)
        else:
            return render(request,'edit_pharmaprofile.html',{'form':form,'user':pharma})

def pharmacyhome(request):
    return render(request,'pharmahome.html')

def userprofile(request):
    if 'id' in request.session:
        user_id = request.session['id']
        data = user.objects.get(id=user_id)
        return render(request, 'userprofile.html', {'data': data})

def edit_userprofile(request,id):
    if 'id' in request.session:
        users = user.objects.get(id=id)
        print(users)
        form = UserEditForm(instance=users)
        if request.method == 'POST':
            form = UserEditForm(request.POST,instance=users)
            if form.is_valid():
                form.save()
                return redirect(userprofile)
        else:
            return render(request,'edit-userprofile.html',{'form':form,'user':users})

def Logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(Login)

def addproduct(request):
    if request.method == 'POST':
        Image = request.FILES['Image']
        MedicineName = request.POST['MedicineName']
        Price = request.POST['Price']
        data1= Product.objects.create(Image=Image,MedicineName=MedicineName,Price=Price)
        data1.save()
        return render(request,'pharmahome.html')

def viewproduct(request):
    data = Product.objects.all()
    print(data)
    return render(request,'pharmaviewproduct.html',{'data1':data})

def deleteproduct(request,id):
    data=Product.objects.get(id=id)
    print(data)
    data.delete()
    return redirect(viewproduct)

def edit_product(request,id):
    if 'id' in request.session:
        products = Product.objects.get(id=id)
        print(products)
        form = ProductEditForm(instance=products)
        if request.method == 'POST':
            form = ProductEditForm(request.POST,request.FILES,instance=products)
            if form.is_valid():
                form.save()
                return redirect(viewproduct)
        else:
            return render(request,'edit-product.html',{'form':form,'products':products})

def userviewproduct(request):
    data = Product.objects.all()
    print(data)
    return render(request,'shop.html',{'data1':data})


def Add_cart(request,id):
    if 'id' in request.session:
        useid=request.session['id']
        user2=user.objects.get(id=useid)
        medicine=Product.objects.get(id=id)
        if cart.objects.filter(Medicineid=medicine,Userid=user2).exists():
            return redirect(erro404)
        else:
            data6 = cart.objects.create(Userid=user2,Medicineid=medicine)
            data6.save()
            data = cart.objects.filter(Userid=user2)
            return render(request,'cart.html',{'cart':data})

def erro404(request):
    return render(request,'Error404.html')

def success(request):
    return render(request,'bookingsuccess.html')

def dummypay(request):
    return render(request,'dummyaccount.html')

def buymedicine(request,id):
    if 'id'in request.session:
        userid=request.session['id']
        user1= user.objects.get(id=userid)
        medicineid=Product.objects.get(id=id)
        if booking.objects.filter(userid=user1,medicineid=medicineid).exists():
            return redirect(erro404)
        else:
            data=booking.objects.create(userid=user1,medicineid=medicineid)
            data.save()
            return redirect(dummypay)

def cartdlt(request,id):
    if 'id' in request.session:
        userid=request.session['id']
        user2=user.objects.get(id=userid)
        data1=cart.objects.get(Medicineid=id,Userid=user2)
        print(data1)
        data1.delete()
        data=cart.objects.filter(Userid=user2)
        return render(request,'cart.html',{'cart':data})


def viewcart(request):
    if 'id' in request.session:
        user1=request.session['id']
        user2=user.objects.get(id=user1)
        view=cart.objects.filter(Userid=user2)
        return render(request,'viewcart.html',{'view':view})

def userhistory(request):
    if 'id' in request.session:
        userid=request.session['id']
        user1=user.objects.get(id=userid)
        history=booking.objects.filter(userid=user1)
        return render(request,'userhistory.html',{'history':history})

def pharmahistory(request):
    data=booking.objects.all()
    return render(request,'pharmahistory.html',{'pharmahist':data})

def searchproduct(request):
    if request.method=='GET':
        result=request.GET.get('search')
        products= Product.objects.all().filter(MedicineName=result)
        return render(request,'search.html',{'products':products})
    else:
        print('no given information')
        return redirect(request,'search.html',{})


