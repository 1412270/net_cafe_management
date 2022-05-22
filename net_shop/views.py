from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import auth
from .models import User, PaidHistory, Computer, Bill
from .serializers import UserSerializer


@login_required(login_url='login')
def index(request):
    # return render(request, 'home.html')
    return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request, 'register.html', {'error': 'Tên đăng nhập đã tồn tại!'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], first_name=request.POST['firstname'],
                                                last_name=request.POST['lastname'], password=request.POST['password1'],
                                                email=request.POST['email'], phone=request.POST['phone'], wallet=0)
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'register.html', {'error': 'Mật khẩu không khớp!'})
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Username or password is incorrect!'})
    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        print("logout")
    return redirect('home')


def add_funds(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        update_wallet = int(request.POST['payment']) + int(user.wallet)
        print(update_wallet)
        user.wallet = update_wallet
        user.save()

        PaidHistory.objects.create(user=request.user, payment=request.POST['payment'])

        return redirect('home')


@login_required(login_url='/login/')
def new_computer(request):
    if request.method == "POST":
        try:
            Computer.objects.get(ip_address=request.POST['ipAddress'])
            return render(request, 'new_computer.html', {'error': 'IP đã được đăng ký!'})
        except Computer.DoesNotExist:
            Computer.objects.create(name=request.POST['computerName'], ip_address=request.POST['ipAddress'],
                                    location=request.POST['location'])
            return redirect('computer_list')
    else:
        return render(request, 'new_computer.html')


@login_required(login_url='/login/')
def computer_list(request):
    computers = Computer.objects.all()
    return render(request, 'computer_list.html', {'data': computers})


@login_required(login_url='/login/')
def new_bill(request):
    if request.method == "POST":
        user = User.objects.get(username=request.POST['username'])
        computer = Computer.objects.get(pk=request.POST['computer'])
        Bill.objects.create(user=user, computer=computer, play_time=request.POST['playtime'].text(),
                            total_payment=request.POST['totalPayment'])
        return redirect('bill_list')
    else:
        computers = Computer.objects.all()
        return render(request, 'new_bill.html', {'data': computers})


@login_required(login_url='/login/')
def bill_list(request):
    bills = Bill.objects.all()
    return render(request, 'bills_list.html', {'data': bills})


@login_required(login_url='/login/')
def get_users(request):
    customers = User.objects.all()
    return render(request, 'customer_list.html', {'data': customers})

