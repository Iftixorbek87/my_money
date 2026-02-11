# 🚀 Loyihani Ishga Tushirish Yo'riqnomasi

## Tizim Talablari

- Python 3.8 yoki undan yuqori
- pip (Python package manager)
- Git (ixtiyoriy)

## Qadam-baqadam O'rnatish

### 1️⃣ Pythonni Tekshirish

Terminal yoki CMD da:
```bash
python --version
# yoki
python3 --version
```

Agar Python o'rnatilmagan bo'lsa, [python.org](https://python.org) dan yuklab oling.

### 2️⃣ Loyiha Papkasiga O'tish

```bash
cd expense_tracker
```

### 3️⃣ Virtual Environment Yaratish (Tavsiya etiladi)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Virtual environment faol bo'lganda terminal oldida `(venv)` ko'rinadi.

### 4️⃣ Kerakli Kutubxonalarni O'rnatish

```bash
pip install -r requirements.txt
```

Agar xatolik bo'lsa:
```bash
pip install Django==5.0.1
pip install djangorestframework==3.14.0
pip install django-cors-headers==4.3.1
pip install Pillow==10.2.0
pip install python-decouple==3.8
```

### 5️⃣ Ma'lumotlar Bazasini Sozlash

```bash
python manage.py makemigrations accounts
python manage.py makemigrations transactions
python manage.py migrate
```

### 6️⃣ Superuser Yaratish (Admin Panel uchun)

```bash
python manage.py createsuperuser
```

Keyin:
- Username: (masalan: admin)
- Email: (ixtiyoriy)
- Password: (xavfsiz parol kiriting)
- Password (again): (parolni tasdiqlang)

### 7️⃣ Serverni Ishga Tushirish

```bash
python manage.py runserver
```

Muvaffaqiyatli ishga tushsa:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### 8️⃣ Brauzerda Ochish

Brauzeringizda quyidagi manzillardan birini oching:
- Asosiy sahifa: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## 🎯 Birinchi Kirish

1. **Ro'yxatdan o'tish**: http://127.0.0.1:8000/register/
   - Ism va familiyangizni kiriting
   - Username tanlang
   - Parol o'rnating

2. **Tizimga kirish**: Avtomatik tizimga kirasiz yoki http://127.0.0.1:8000/login/

3. **Dashboard**: Bosh sahifada balans va statistikani ko'rasiz

4. **Tranzaksiya qo'shish**: "➕ Qo'shish" tugmasini bosing

## ❗ Keng Tarqalgan Muammolar va Yechimlar

### Muammo 1: "No module named 'django'"
**Yechim:**
```bash
pip install Django
```

### Muammo 2: "python: command not found"
**Yechim:** Python o'rnatilmagan. [python.org](https://python.org) dan yuklab oling.

### Muammo 3: "Port already in use"
**Yechim:** Boshqa portda ishga tushiring:
```bash
python manage.py runserver 8080
```

### Muammo 4: Migration xatoliklari
**Yechim:**
```bash
# Ma'lumotlar bazasini tozalash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Muammo 5: Static fayllar yuklanmaydi
**Yechim:**
```bash
python manage.py collectstatic
```

## 🔧 Qo'shimcha Sozlamalar

### Port O'zgartirish
```bash
python manage.py runserver 8080
```

### Tashqi Qurilmalardan Kirish
```bash
python manage.py runserver 0.0.0.0:8000
```

### Debug Rejimini O'chirish
`config/settings.py` da:
```python
DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
```

## 📱 Test Ma'lumotlari

Tezda test qilish uchun:

**Test User:**
- Username: testuser
- Password: test123456

**Tranzaksiya Misollari:**
- Kirim: Maosh - 5,000,000 so'm
- Chiqim: Oziq-ovqat - 500,000 so'm
- Kirim: Freelance - 200 USD

## 🛑 Serverni To'xtatish

Terminal da: `CTRL + C`

Virtual environment dan chiqish: `deactivate`

## 📚 Qo'shimcha Resurslar

- [Django Documentation](https://docs.djangoproject.com/)
- [Python Documentation](https://docs.python.org/)
- [Chart.js Documentation](https://www.chartjs.org/docs/)

## 💡 Yordam Kerakmi?

Muammolar yoki savollar bo'lsa:
1. README.md faylini o'qing
2. Django dokumentatsiyasini tekshiring
3. Google da xatolik xabarini qidiring

---

**Muvaffaqiyatli ishlatishingizni tilaymiz! 🎉**
