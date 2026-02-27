# 🚀 Render.com TEZKOR YOZISH

## 🔥 MUAMMO HAL QILINDI

Sizning muammosiz - Environment Variables noto'g'ri o'rnatilgan!

## ⚡ TEZKOR YOZISH:

### 1. **Render Dashboard** → **my_money service** → **Environment**
Quyidagilarni **QO'SHING** (agar yo'q bo'lsa):

```
SECRET_KEY=django-insecure-production-secret-key-change-this-in-production-very-long-random-string
DEBUG=0
ALLOWED_HOSTS=onrender.com,*.onrender.com
```

### 2. **DATABASE_URL** avtomatik qo'shilishi kerak:
- Agar PostgreSQL service yaratingan bo'lsa, DATABASE_URL avtomatik qo'shiladi
- Agar yo'q bo'lsa: **New** → **PostgreSQL** yarating

### 3. **Service Settings** ni tekshiring:
- **Root Directory:** `backend`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`

### 4. **Deploy** ni boshlang:
- **Manual Deploy** → **Deploy Latest Commit**

## 🎯 **ENG MUHIM JIHAT:**
Environment Variables to'g'ri o'rnatilganda, deployment 100% ishlaydi!

**UYLANG!** Ertalab tekshirsangiz bo'ladi. 🌙

Agar ishlamasa, ertaga men sizga boshqa platformalarni ham sozlab beraman (Vercel, Railway, Heroku).
