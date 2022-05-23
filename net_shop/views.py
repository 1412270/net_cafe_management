from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import auth
from .models import User, PaidHistory, Computer, Bill, Customer


@login_required(login_url='login')
def index(request):
    # return render(request, 'home.html')
    return render(request, 'home.html')


# Đăng ký người dùng hệ thống
def register(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Kiem tra ten dang nhap
                User.objects.get(username=request.POST['username'])
                return render(request, 'register.html', {'error': 'Tên đăng nhập đã tồn tại!'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'],
                                                email=request.POST['email'], phone=request.POST['phone'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'register.html', {'error': 'Mật khẩu không khớp!'})
    else:
        return render(request, 'register.html')


# Đăng nhập
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


# Đăng xuất
def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        print("logout")
    return redirect('home')


def add_funds(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        update_wallet = int(request.POST['payment']) + int(user.wallet)
        user.wallet = update_wallet
        user.save()

        PaidHistory.objects.create(user=request.user, payment=request.POST['payment'])

        return redirect('home')


# Thêm thiết bị mới
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


# Xem danh sách máy ở cửa hàng
@login_required(login_url='/login/')
def computer_list(request):
    computers = Computer.objects.all()
    return render(request, 'computer_list.html', {'data': computers})


# Tạo hóa đơn mới
@login_required(login_url='/login/')
def new_bill(request):
    if request.method == "POST":
        try:
            customer = Customer.objects.get(username=request.POST['username'])
            computer = Computer.objects.get(pk=request.POST['computer'])
            Bill.objects.create(customer=customer, computer=computer, play_time=request.POST['playtime'],
                                total_payment=request.POST['totalPayment'])
        except Customer.DoesNotExist:
            computers = Computer.objects.all()
            return render(request, 'new_bill.html', {'data': computers, 'error': 'Khách hàng không tồn tại!'})

        return redirect('bill_list')
    else:
        computers = Computer.objects.all()
        return render(request, 'new_bill.html', {'data': computers})


# Xem sách thanh toán
@login_required(login_url='/login/')
def bill_list(request):
    bills = Bill.objects.all()
    return render(request, 'bills_list.html', {'data': bills})


# Xem danh sách khách hàng
@login_required(login_url='/login/')
def get_customers(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'data': customers})


# Tạo một người dùng mới
@login_required(login_url='/login/')
def new_customer(request):
    if request.method == "POST":
        try:
            Customer.objects.get(username=request.POST['username'])
            return render(request, 'new_customers.html', {'error': 'Tên đăng nhập đã tồn tại!'})
        except Customer.DoesNotExist:
            Customer.objects.create(username=request.POST['username'], fullname=request.POST['fullname'],
                                    email=request.POST['email'], phone=request.POST['phone'], wallet=0)
            return redirect('customer_list')
    else:
        return render(request, 'new_customers.html')

