from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout as django_logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Product, Category, ProductHistory, OtherForm
from .forms import AddProduct, AddCategory, SignupForm, NewForm
from django.contrib.auth.decorators import login_required

import json
import requests #used for collect data from api

product_url = 'http://127.0.0.1:8000/api/product/' #product api url
category_url = 'http://127.0.0.1:8000/api/'  #categpru api url
history_url = 'http://127.0.0.1:8000/api/history/'   #history api url


# Create your views here.
def home(request):
    product_url_response = requests.get(product_url) #collecting data from product api url
    product_url_json_data = json.loads(product_url_response.content) #convert into json form
    context = {
        'product': product_url_json_data,
    }
    return render(request, 'index.html', context)

@login_required(login_url='login')
def addproduct(request):
    form = AddProduct(request.POST or None, request.FILES or None) #AddProduct form assing intor form variable
    if form.is_valid(): #check form is valid or not
        name = form.cleaned_data['name'] #retrive data from input, which name is 'name'
        seller_name = form.cleaned_data['seller_name']
        name = name.replace(' ', '')
        seller_name = seller_name.replace(' ', '')
        if name.isalnum()==False:
            messages.error(request, 'Product must be Alphanumeric') #passing messaage if name contain punctuation mark
        elif seller_name.isalpha()==False:
            messages.error(request, 'Seller name must be Alphabet')
        else:
            form.save() #save data into AddProduct table
            return redirect('productlist')
    return render(request, 'add_product.html', {'form': form})

@login_required(login_url='login')
def addcategory(request):
    form = AddCategory(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        name=name.replace(' ','')
        if name.isalnum():
            form.save()
            return redirect('categorylist')
        else:
            messages.error(request, 'Product must be Alphanumeric')
    return render(request, 'add_category.html', {'form': form})

@login_required(login_url='login')
def productdetails(request, id):
    response = requests.get(product_url)
    json_data = json.loads(response.content)
    context = {}
    b = False
    for i in json_data:
        if i['id'] == id: #check product id and perameter id is equal or not
            for j in i:
                context[j] = i[j] #add product into context which match the perameter id
                b = True
        if b:
            break
    return render(request, 'product_details.html', {'context': context})

@login_required(login_url='login')
def checkout(request):
    if request.method == 'POST':
        pid = request.POST.get('pid') #return none if pid not found
        name = request.POST.get('name')
        quantity = int(request.POST.get('select_quantity')) #convert str to int
        unit_price = int(request.POST.get('price'))
        total_price = unit_price * quantity
        #print(pid)
        # print(unit_price,type(unit_price),quantity,type(quantity),total_price,type(total_price))
        context = {
            'pid': pid,
            'name': name,
            'quantity': quantity,
            'unit_price': unit_price,
            'total_price': total_price
        }
        return render(request, 'checkout.html', context)


@login_required(login_url='login')
def placeorder(request):
    if request.method == 'POST':
        pid = request.POST.get('pid')
        select_qantity = int(request.POST.get('quantity'))
        total_price = request.POST.get('total_price')
        quantity = Product.objects.get(id=pid) #select * from Porduct where id=pid (it's not iteretive)
        quantity.available_quantity = quantity.available_quantity - select_qantity #assing update availabel quantity into Product table
        current_email = request.user
        history = ProductHistory(email=current_email.email, product_name=quantity.name,
                                 unit_price=quantity.price, select_quantity=select_qantity, total_price=total_price)
        quantity.save()  # save and update the available_quantity
        history.save()
        context = {
            'select_quantity': select_qantity,
            'total_price': total_price,
            'quantity': quantity
        }
        # print(quantity.available_quantity,type(quantity.available_quantity))

        return render(request, 'placeorder.html', context)


@login_required(login_url='login')
def updateproduct(request, id):
    post = get_object_or_404(Product, pk=id) #return 404 error if Product not found by id
    form = AddProduct(request.POST or None, request.FILES or None, instance=post)  # this instance is inbuilt
    if form.is_valid():
        name = form.cleaned_data['name']
        seller_name = form.cleaned_data['seller_name']
        name = name.replace(' ', '')
        seller_name = seller_name.replace(' ', '')
        if name.isalnum() == False:
            messages.error(request, 'Product must be Alphanumeric')
        elif seller_name.isalpha() == False:
            messages.error(request, 'Seller name must be Alphabet')
        else:
            instance = form.save(commit=False)
            instance.save()
            return redirect('productlist')
    return render(request, 'add_product.html', {'form': form})

@login_required(login_url='login')
def deleteproduct(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('productlist')


@login_required(login_url='login')
def updatecategory(request, id):
    post = get_object_or_404(Category, pk=id)
    form = AddCategory(request.POST or None, instance=post)  # this instance is inbuilt
    if form.is_valid():
        name = form.cleaned_data['name']
        name = name.replace(' ', '')
        if name.isalnum():
            form.save()
            return redirect('categorylist')
        else:
            messages.error(request, 'Product must be Alphanumeric')
    return render(request, 'add_category.html', {'form': form})


@login_required(login_url='login')
def deletecategory(request, id):
    category = Category.objects.get(pk=id)
    category.delete() #delete from Category table
    return redirect('categorylist')



def signup(request):
    form = SignupForm(request.POST or None)
    otherform = NewForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        other = otherform.save(commit=False)
        name = form.cleaned_data['username']
        password = form.cleaned_data['password']
        confirm_password = form.cleaned_data['confirm_password']
        mobile_no = otherform.cleaned_data['mobile_no']
        account_type = otherform.cleaned_data['account_type']
        if len(mobile_no) < 11:
            messages.error(request, 'Mobile number must be 11 digit')
        elif mobile_no[0] != '0' or mobile_no[1] != '1' or mobile_no.isdigit() == False:
            messages.error(request, 'Mobile number is not valid')
        elif password == confirm_password:
            if len(password) < 8 or password.isdigit():
                messages.error(request, 'Password length must be 8 and contain at least one character')
            else:
                user.set_password(password)
                user.save()
                other=OtherForm(name=name,mobile_no=mobile_no,account_type=account_type)
                other.save()
                if user is not None: #check user available or not
                    if user.is_active: #check user is active or not
                        return redirect('home')
        else:
            messages.error(request, 'Password are not match')
    return render(request,'signup.html', {'form': form,'otherform':otherform})


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['user']  # request.POST['user'] it's return keyword if 'user' not found
            password = request.POST['pass']
            auth = authenticate(request, username=username, password=password)
            all = OtherForm.objects.all()
            type = ''
            for i in all:
                #print(i.name,i.account_type)
                if i.name == username: #check OtherForm table name and username is equal or not
                    type = i.account_type
                    break
            #print(type)
            #print(auth)
            if auth is not None:
                #print('login',type)
                auth_login(request, auth)
                request.session["name"]=type #create session variable
                #print(request.session["name"],type)
                if type=='BUYER':
                    #print(type)
                    return redirect('buyerprofile')
                else:
                    #print(type)
                    return redirect('productlist')
            else:
                messages.error(request, 'Username or Password are not match')
    return render(request, 'login.html')


@login_required(login_url='login')
def productlist(request):
    response = requests.get(product_url)
    json_data = json.loads(response.content)
    return render(request, 'productlist.html', {'product': json_data})

@login_required(login_url='login')
def categorylist(request):
    response = requests.get(category_url)
    json_data = json.loads(response.content)
    return render(request, 'categorylist.html', {'category': json_data})



@login_required(login_url='login')
def buyerprofile(request):
    response = requests.get(history_url)
    json_data = json.loads(response.content)
    j = 0
    history = []
    current_email = request.user
    for h in json_data:
        # print(h['email'])
        if h['email'] == current_email.email:
            history += [json_data[j]]
            # print(json_data[j], end='\n\n')
        j += 1
    return render(request, 'buyerprofile.html', {'history': history,'name':request.session['name']})

@login_required(login_url='login')
def historydetails(request,id):
    response = requests.get(history_url)
    json_data = json.loads(response.content)
    j=0
    for h in json_data:
        if h['id']==id:
            history = json_data[j]
            break
        j+=1
    return render(request, 'historydetails.html', {'history': history})

@login_required(login_url='login')
def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            user=form.save(commit=False)
            password = form.cleaned_data['new_password1']
            user.set_password(password)
            user.save()
            update_session_auth_hash(request, form.user) #stay session is active
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request,'changepassword.html',{'form':form})



def logout(request):
    django_logout(request)
    return redirect('login')