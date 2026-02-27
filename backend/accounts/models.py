from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """Foydalanuvchi profili va balance ma'lumotlari"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    balance_uzs = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    balance_usd = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Foydalanuvchi Profili'
        verbose_name_plural = 'Foydalanuvchi Profillari'

    def __str__(self):
        return f"{self.user.username} - Profile"

    def get_total_income_uzs(self):
        """UZS da jami kirim"""
        from transactions.models import Transaction
        return Transaction.objects.filter(
            user=self.user,
            currency='UZS',
            transaction_type='income'
        ).aggregate(total=models.Sum('amount'))['total'] or 0

    def get_total_expense_uzs(self):
        """UZS da jami chiqim"""
        from transactions.models import Transaction
        return Transaction.objects.filter(
            user=self.user,
            currency='UZS',
            transaction_type='expense'
        ).aggregate(total=models.Sum('amount'))['total'] or 0

    def get_total_income_usd(self):
        """USD da jami kirim"""
        from transactions.models import Transaction
        return Transaction.objects.filter(
            user=self.user,
            currency='USD',
            transaction_type='income'
        ).aggregate(total=models.Sum('amount'))['total'] or 0

    def get_total_expense_usd(self):
        """USD da jami chiqim"""
        from transactions.models import Transaction
        return Transaction.objects.filter(
            user=self.user,
            currency='USD',
            transaction_type='expense'
        ).aggregate(total=models.Sum('amount'))['total'] or 0


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Yangi user yaratilganda avtomatik profil yaratish"""
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """User saqlanganda profilni ham saqlash"""
    if hasattr(instance, 'profile'):
        instance.profile.save()
