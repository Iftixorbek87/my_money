from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    """Foydalanuvchi hisobi (So'm, Dollar)"""
    CURRENCY_CHOICES = [
        ('UZS', 'So\'m'),
        ('USD', 'Dollar'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    name = models.CharField(max_length=100)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Hisob'
        verbose_name_plural = 'Hisoblar'
        unique_together = ['user', 'currency']

    def __str__(self):
        return f"{self.user.username} - {self.name} ({self.currency})"


class Transaction(models.Model):
    """Tranzaksiya (Kirim/Chiqim)"""
    TRANSACTION_TYPES = [
        ('income', 'Kirim'),
        ('expense', 'Chiqim'),
    ]
    
    CURRENCY_CHOICES = [
        ('UZS', 'So\'m'),
        ('USD', 'Dollar'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    category = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Tranzaksiya'
        verbose_name_plural = 'Tranzaksiyalar'
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.get_transaction_type_display()} - {self.amount} {self.currency}"

    def save(self, *args, **kwargs):
        """Tranzaksiya saqlananda balansni yangilash"""
        from decimal import Decimal
        
        is_new = self.pk is None
        
        if is_new:
            # Yangi tranzaksiya
            if self.transaction_type == 'income':
                self.account.balance = Decimal(str(self.account.balance)) + Decimal(str(self.amount))
            else:
                self.account.balance = Decimal(str(self.account.balance)) - Decimal(str(self.amount))
            self.account.save()
        
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Tranzaksiya o'chirilganda balansni yangilash"""
        from decimal import Decimal
        
        if self.transaction_type == 'income':
            self.account.balance = Decimal(str(self.account.balance)) - Decimal(str(self.amount))
        else:
            self.account.balance = Decimal(str(self.account.balance)) + Decimal(str(self.amount))
        self.account.save()
        
        super().delete(*args, **kwargs)


class Category(models.Model):
    """Tranzaksiya kategoriyalari"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=10, choices=Transaction.TRANSACTION_TYPES)
    icon = models.CharField(max_length=50, blank=True, default='💰')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
        unique_together = ['user', 'name', 'transaction_type']

    def __str__(self):
        return f"{self.name} ({self.get_transaction_type_display()})"
