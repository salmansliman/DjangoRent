from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cars
from .models import Customer
from .models import Rent
import phonenumbers

# Create your views here.
def index(request):
    car=Cars.objects.all()
    cos=Customer.objects.all()
    rent=Rent.objects.all()
    return render(request,'index.html',{'car':car,'cos':cos,'rent':rent})
def add(request):
    return render(request,'add.html')
def addrec(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        price = request.POST.get('price')

        # Check if 'rented' checkbox is checked
        rented = request.POST.get('rented') == 'on'

        car = Cars(brand=brand, model=model, price=price, rented=rented)
        car.save()

        return redirect("/")  

    return render(request, 'add.html')
def delete(request,id):
    car=Cars.objects.get(id=id)
    car.delete()
    return redirect("/")
def update(request,id):
    car=Cars.objects.get(id=id)
    return render(request,'update.html',{'car':car})
def uprec(request,id):
    brand = request.POST.get('brand')
    model = request.POST.get('model')
    price = request.POST.get('price')
    rented = request.POST.get('rented') == 'on'
    car=Cars.objects.get(id=id)
    car.brand=brand
    car.model=model
    car.price=price
    car.rented=rented
    car.save()
    return redirect("/")
def addC(request):
    return render(request,'addC.html')
def addCrec(request):
    if request.method == 'POST':
        first = request.POST.get('first')
        last = request.POST.get('last')
        phone = request.POST.get('phone')

        try:
            # Attempt to parse the input as a phone number
            parsed_phone = phonenumbers.parse(phone, 'US')
            if not phonenumbers.is_valid_number(parsed_phone):
                raise ValueError('Invalid phone number')

            customer = Customer(first=first, last=last, phone=phone)
            customer.save()

            return redirect("/")  
        except ValueError as e:
            messages.error(request, str(e))  

    return render(request, 'addC.html')
def deleteC(request,id):
    cus=Customer.objects.get(id=id)
    cus.delete()
    return redirect("/")
def updateC(request,id):
    cos=Customer.objects.get(id=id)
    return render(request,'updateC.html',{'cos':cos})
def upCrec(request,id):
    if request.method == 'POST':
        first_name = request.POST.get('first')
        last_name = request.POST.get('last')
        phone = request.POST.get('phone')
        customer = Customer.objects.get(id=id)
        try:
            
            parsed_phone = phonenumbers.parse(phone, 'US')
            if not phonenumbers.is_valid_number(parsed_phone):
                raise ValueError('Invalid phone number')

            
            customer.first = first_name
            customer.last = last_name
            customer.phone = phone
            customer.save()

            return redirect("/")  
        except ValueError as e:
            messages.error(request, str(e))  
   
    return render(request, 'updateC.html', {'cos': Customer.objects.get(id=id)})
def rent(request):
    rent=Rent.objects.all()
    car=Cars.objects.all()
    cos=Customer.objects.all()
    return render(request,'rent.html',{'rent':rent,'car':car,'cos':cos})
def addRent(request):
    if request.method == 'POST':
        car_id=request.POST.get('car')
        cos_id=request.POST.get('customer')
        startDate=request.POST.get('startDate')
        endDate=request.POST.get('endDate')
        car_instance = Cars.objects.get(id=car_id)
        cos_instance = Customer.objects.get(id=cos_id)
        new_Rent=Rent(id_car=car_instance,id_cos=cos_instance,startDate=startDate,endDate=endDate)
        new_Rent.save()
        return redirect("/")
def deleteR(request,id_rent):
    rent=Rent.objects.get(id_rent=id_rent)
    rent.delete()
    return redirect("/")
