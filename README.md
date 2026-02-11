# 💰 Moliyaviy Boshqaruv Tizimi

Django asosida yaratilgan to'liq funksional moliyaviy boshqaruv web ilovasi.

## ✨ Xususiyatlar

- 👤 **Foydalanuvchi tizimi**: Ro'yxatdan o'tish va kirish
- 💵 **Ko'p valyuta**: UZS va USD qo'llab-quvvatlash
- 📊 **Dashboard**: Balans, kirim va chiqimlarni real-time kuzatish
- ➕ **Tranzaksiyalar**: Kirim va chiqimlarni qo'shish, tahrirlash va o'chirish
- 📈 **Statistika**: Donut chart va kategoriya bo'yicha tahlil
- 🔍 **Qidiruv va Filter**: Tranzaksiyalarni turli parametrlar bo'yicha filtrlash
- 📱 **Responsive dizayn**: Mobil va desktop qurilmalarda ishlaydi
- 🎨 **Zamonaviy UI**: Gradient va glassmorphism effektlar

## 🚀 O'rnatish

### 1. Loyihani yuklab olish
```bash
cd expense_tracker
```

### 2. Virtual environment yaratish (ixtiyoriy)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### 3. Kerakli kutubxonalarni o'rnatish
```bash
pip install -r requirements.txt
```

### 4. Ma'lumotlar bazasini migratsiya qilish
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Superuser yaratish (admin panel uchun)
```bash
python manage.py createsuperuser
```

### 6. Serverni ishga tushirish
```bash
python manage.py runserver
```

Brauzerda `http://127.0.0.1:8000` manzilini oching.

## 📖 Foydalanish

### Ro'yxatdan o'tish
1. `/register` sahifasiga o'ting
2. Foydalanuvchi ma'lumotlaringizni kiriting
3. Tizimga avtomatik kirasiz

### Dashboard
- Umumiy balansni ko'ring (UZS va USD)
- Oylik kirim va chiqimlarni ko'ring
- Donut chart orqali statistikani tahlil qiling
- Oxirgi tranzaksiyalarni ko'ring

### Tranzaksiya qo'shish
1. "➕ Qo'shish" tugmasini bosing
2. Tranzaksiya turini tanlang (Kirim/Chiqim)
3. Summa, valyuta va kategoriyani kiriting
4. Tavsif va sanani qo'shing
5. "Saqlash" tugmasini bosing

### Statistika
- Haftalik, oylik yoki yillik hisobotlarni ko'ring
- Kategoriya bo'yicha chiqimlarni tahlil qiling
- Foyda va zarami hisoblang

## 🗂️ Loyiha Strukturasi

```
expense_tracker/
├── config/                 # Django asosiy sozlamalari
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/               # Foydalanuvchi tizimi
│   ├── models.py          # UserProfile modeli
│   ├── views.py           # Login, Register, Dashboard
│   └── urls.py
├── transactions/           # Tranzaksiyalar tizimi
│   ├── models.py          # Account, Transaction, Category
│   ├── views.py           # CRUD operatsiyalar
│   ├── urls.py
│   └── templatetags/      # Custom filters
├── templates/              # HTML shablon fayllar
│   ├── base.html
│   ├── accounts/
│   └── transactions/
├── static/                 # CSS, JS fayllar
├── manage.py
└── requirements.txt
```

## 🎨 Texnologiyalar

- **Backend**: Django 5.0.1
- **Frontend**: HTML5, CSS3, JavaScript
- **Ma'lumotlar bazasi**: SQLite (default)
- **Chart**: Chart.js
- **Styling**: Custom CSS (Glassmorphism)

## 📊 Modellar

### UserProfile
- Foydalanuvchi profili
- UZS va USD balanslari
- Avtomatik yaratiladi

### Account
- Foydalanuvchi hisobi
- Valyuta (UZS/USD)
- Joriy balans

### Transaction
- Tranzaksiya turi (Kirim/Chiqim)
- Summa va valyuta
- Kategoriya va tavsif
- Sana

### Category
- Tranzaksiya kategoriyalari
- Icon qo'llab-quvvatlash

## 🔧 Sozlamalar

`config/settings.py` faylida quyidagilarni o'zgartirishingiz mumkin:

- `SECRET_KEY`: Production uchun yangi key yarating
- `DEBUG`: Production da False qiling
- `ALLOWED_HOSTS`: Domen nomingizni qo'shing
- `DATABASES`: PostgreSQL, MySQL ga o'tkazish mumkin

## 🌐 Production uchun

1. `DEBUG = False` qiling
2. `SECRET_KEY` ni yangilang
3. `ALLOWED_HOSTS` sozlang
4. Static fayllarni to'plang:
   ```bash
   python manage.py collectstatic
   ```
5. HTTPS qo'llang
6. PostgreSQL ga o'ting (ixtiyoriy)

## 📝 Litsenziya

MIT License - bepul va ochiq manba

## 👨‍💻 Muallif

Claude AI yordamida yaratildi

## 🤝 Qo'llab-quvvatlash

Muammolar yoki takliflar bo'lsa, GitHub Issues orqali xabar bering.

---

**Eslatma**: Bu loyiha o'quv va demonstratsion maqsadlarda yaratilgan. Production muhitda ishlatishdan oldin xavfsizlik sozlamalarini tekshiring.
