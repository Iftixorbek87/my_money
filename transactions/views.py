from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Q
from .models import Transaction, Account, Category
from datetime import datetime, timedelta
import json


@login_required
def add_transaction_view(request):
    """Tranzaksiya qo'shish"""
    if request.method == 'POST':
        transaction_type = request.POST.get('transaction_type')
        from decimal import Decimal
        amount = Decimal(request.POST.get('amount'))
        currency = request.POST.get('currency')
        category = request.POST.get('category', '')
        description = request.POST.get('description', '')
        date_str = request.POST.get('date', datetime.now().date())
        
        # Hisobni topish yoki yaratish
        account, created = Account.objects.get_or_create(
            user=request.user,
            currency=currency,
            defaults={'name': 'So\'m' if currency == 'UZS' else 'Dollar'}
        )
        
        # Tranzaksiya yaratish
        transaction = Transaction.objects.create(
            user=request.user,
            account=account,
            transaction_type=transaction_type,
            amount=amount,
            currency=currency,
            category=category,
            description=description,
            date=date_str
        )
        
        messages.success(request, 'Tranzaksiya muvaffaqiyatli qo\'shildi!')
        return redirect('dashboard')
    
    # Kategoriyalarni olish
    income_categories = Category.objects.filter(
        Q(user=request.user) | Q(user__isnull=True),
        transaction_type='income'
    )
    expense_categories = Category.objects.filter(
        Q(user=request.user) | Q(user__isnull=True),
        transaction_type='expense'
    )
    
    context = {
        'income_categories': income_categories,
        'expense_categories': expense_categories,
    }
    
    return render(request, 'transactions/add_transaction.html', context)


@login_required
def transaction_list_view(request):
    """Barcha tranzaksiyalar ro'yxati"""
    transactions = Transaction.objects.filter(user=request.user)
    
    # Filter by type
    transaction_type = request.GET.get('type')
    if transaction_type:
        transactions = transactions.filter(transaction_type=transaction_type)
    
    # Filter by currency
    currency = request.GET.get('currency')
    if currency:
        transactions = transactions.filter(currency=currency)
    
    # Filter by date range
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    if date_from:
        transactions = transactions.filter(date__gte=date_from)
    if date_to:
        transactions = transactions.filter(date__lte=date_to)
    
    context = {
        'transactions': transactions,
    }
    
    return render(request, 'transactions/transaction_list.html', context)


@login_required
def delete_transaction_view(request, pk):
    """Tranzaksiyani o'chirish"""
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    
    if request.method == 'POST':
        transaction.delete()
        messages.success(request, 'Tranzaksiya o\'chirildi!')
        return redirect('transaction_list')
    
    return render(request, 'transactions/delete_transaction.html', {'transaction': transaction})


@login_required
def statistics_view(request):
    """Statistika sahifasi"""
    user = request.user
    
    # Vaqt oralig'ini olish
    period = request.GET.get('period', 'month')
    today = datetime.now().date()
    
    if period == 'week':
        start_date = today - timedelta(days=7)
    elif period == 'month':
        start_date = today - timedelta(days=30)
    elif period == 'year':
        start_date = today - timedelta(days=365)
    else:
        start_date = today - timedelta(days=30)
    
    # UZS statistika
    transactions_uzs = Transaction.objects.filter(
        user=user,
        currency='UZS',
        date__gte=start_date
    )
    
    income_uzs = transactions_uzs.filter(transaction_type='income').aggregate(
        total=Sum('amount')
    )['total'] or 0
    
    expense_uzs = transactions_uzs.filter(transaction_type='expense').aggregate(
        total=Sum('amount')
    )['total'] or 0
    
    # USD statistika
    transactions_usd = Transaction.objects.filter(
        user=user,
        currency='USD',
        date__gte=start_date
    )
    
    income_usd = transactions_usd.filter(transaction_type='income').aggregate(
        total=Sum('amount')
    )['total'] or 0
    
    expense_usd = transactions_usd.filter(transaction_type='expense').aggregate(
        total=Sum('amount')
    )['total'] or 0
    
    # Kategoriya bo'yicha statistika
    category_stats_uzs = transactions_uzs.filter(
        transaction_type='expense'
    ).values('category').annotate(
        total=Sum('amount')
    ).order_by('-total')[:5]
    
    category_stats_usd = transactions_usd.filter(
        transaction_type='expense'
    ).values('category').annotate(
        total=Sum('amount')
    ).order_by('-total')[:5]
    
    context = {
        'period': period,
        'start_date': start_date,
        'income_uzs': income_uzs,
        'expense_uzs': expense_uzs,
        'profit_uzs': income_uzs - expense_uzs,
        'income_usd': income_usd,
        'expense_usd': expense_usd,
        'profit_usd': income_usd - expense_usd,
        'category_stats_uzs': category_stats_uzs,
        'category_stats_usd': category_stats_usd,
    }
    
    return render(request, 'transactions/statistics.html', context)
