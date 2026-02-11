from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Sum, Q
from transactions.models import Transaction, Account
from datetime import datetime, timedelta
import json


def register_view(request):
    """Ro'yxatdan o'tish"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        
        if password != password2:
            messages.error(request, 'Parollar bir xil emas!')
            return render(request, 'accounts/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Bu foydalanuvchi nomi band!')
            return render(request, 'accounts/register.html')
        
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        
        # Default hisoblarni yaratish
        Account.objects.create(user=user, name="So'm", currency='UZS', balance=0)
        Account.objects.create(user=user, name="Dollar", currency='USD', balance=0)
        
        login(request, user)
        messages.success(request, 'Ro\'yxatdan muvaffaqiyatli o\'tdingiz!')
        return redirect('dashboard')
    
    return render(request, 'accounts/register.html')


def login_view(request):
    """Tizimga kirish"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Xush kelibsiz!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Login yoki parol xato!')
    
    return render(request, 'accounts/login.html')


@login_required
def logout_view(request):
    """Tizimdan chiqish"""
    logout(request)
    messages.info(request, 'Tizimdan chiqdingiz.')
    return redirect('login')


@login_required
def dashboard_view(request):
    """Asosiy dashboard"""
    user = request.user
    
    # Hisoblar
    accounts = Account.objects.filter(user=user)
    
    # Jami balance
    total_uzs = accounts.filter(currency='UZS').aggregate(total=Sum('balance'))['total'] or 0
    total_usd = accounts.filter(currency='USD').aggregate(total=Sum('balance'))['total'] or 0
    
    # Oxirgi tranzaksiyalar
    recent_transactions = Transaction.objects.filter(user=user).order_by('-date')[:10]
    
    # Statistika uchun ma'lumotlar
    today = datetime.now().date()
    week_ago = today - timedelta(days=7)
    month_ago = today - timedelta(days=30)
    
    # UZS statistika
    income_uzs_month = Transaction.objects.filter(
        user=user,
        currency='UZS',
        transaction_type='income',
        date__gte=month_ago
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    expense_uzs_month = Transaction.objects.filter(
        user=user,
        currency='UZS',
        transaction_type='expense',
        date__gte=month_ago
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    # USD statistika
    income_usd_month = Transaction.objects.filter(
        user=user,
        currency='USD',
        transaction_type='income',
        date__gte=month_ago
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    expense_usd_month = Transaction.objects.filter(
        user=user,
        currency='USD',
        transaction_type='expense',
        date__gte=month_ago
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    # Donut chart uchun ma'lumotlar
    chart_data_uzs = {
        'income': float(income_uzs_month),
        'expense': float(expense_uzs_month),
        'balance': float(total_uzs)
    }
    
    chart_data_usd = {
        'income': float(income_usd_month),
        'expense': float(expense_usd_month),
        'balance': float(total_usd)
    }
    
    context = {
        'accounts': accounts,
        'total_uzs': total_uzs,
        'total_usd': total_usd,
        'recent_transactions': recent_transactions,
        'income_uzs_month': income_uzs_month,
        'expense_uzs_month': expense_uzs_month,
        'income_usd_month': income_usd_month,
        'expense_usd_month': expense_usd_month,
        'chart_data_uzs': json.dumps(chart_data_uzs),
        'chart_data_usd': json.dumps(chart_data_usd),
    }
    
    return render(request, 'accounts/dashboard.html', context)
