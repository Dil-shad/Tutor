from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
import os


# Create your views here.


def Home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        uname = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']
        cpwd = request.POST['cpassword']

        # auth_user_fields_on_top

        address = request.POST['addr']
        gender = request.POST['gen']
        phone = request.POST['ph']
        if request.FILES.get('file') is not None:
            image = request.FILES['file']
        else:
            image = "/static/image/default.png"
        if pwd == cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'username already exists...!!')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already registerd..!!')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    username=uname,
                    password=pwd,
                    email=email,
                )
                user.save()
                u = User.objects.get(id=user.id)  # for fkey
                extra = UserExtra(
                    user=u,  # fkey
                    address=address,
                    gender=gender,
                    mobile=phone,
                    image=image,
                )
                extra.save()
                return redirect('login')
        else:
            messages.info(request, 'paswd doesnt match..!!')
            return redirect('signup')

    return render(request, 'signup.html')


def login(request):
    try:
        if request.method == 'POST':
            uname = request.POST['username']
            pwd = request.POST['password']
            user = auth.authenticate(username=uname, password=pwd)

            if user is not None:
                if user.is_superuser:
                    request.session['uid'] = user.id
                    auth.login(request, user)
                    return redirect('dash')
                else:
                    request.session['uid'] = user.id
                    auth.login(request, user)
                    #messages.info(request, f'Welcome{uname}')
                    return redirect('profile')
            else:
                messages.info(
                    request, 'Invalid Username or Password. Try Again.IN')
                return redirect('login')

        return render(request, 'login.html')
    except:
        messages.info(request, 'Invalid username or password')
        return render(request, 'login.html')


def dash(request):
    if 'uid' in request.session:
        var = request.user

        x = UserExtra.objects.all()
        context = {
            'lst': x,
            'var': var

        }

        return render(request, 'dash.html', context)
    return redirect('login')


def profile(request):
    if 'uid' in request.session:
        usr = UserExtra.objects.filter(user=request.user)
        # var = request.user
        print(list(usr))

        context = {
            'dic': usr,
            # 'var': var
        }

        return render(request, 'profile.html', context)
    return redirect('login')


def about(request):
    if 'uid' in request.session:
        return render(request, 'about.html')

    return redirect('login')


'''def edit(request, pk):
    if not request.user.is_staff:
        raise PermissionDenied'''


def logout(request):
    request.session['uid'] = ''
    auth.logout(request)
    return redirect('/')



def edit(request,pk):

    if request.method=='POST':
        usr=UserExtra.objects.get(id=pk)
        usr.user.first_name=request.POST.get('fname')
        usr.address=request.POST.get('uaddress')
        usr.mobile=request.POST.get('nnumber')
        if request.FILES.get('file') is not None:
            usr.image = request.FILES.get('file')

        else:
            pass
        usr.save()
        return redirect('dash')

    idd=UserExtra.objects.get(id=pk)
    return render(request,'edit.html',{'idd':idd})



def delete(request,pk):
    dell = UserExtra.objects.get(id=pk)
    if dell.image is not None:
        if not dell.image == "/static/image/default.png":
            os.remove(dell.image.path)
        else:
            pass
    dell.delete()
    return redirect('dash')
