# 🚀 Render.com To'liq Sozlash

## ✅ Loyiha Tayyorligi
- ✅ Production settings sozlandi
- ✅ DEBUG=False
- ✅ ALLOWED_HOSTS to'g'ri
- ✅ Security settings qo'shildi
- ✅ Environment variables tayyor

## 🚀 Render.com da Deployment

### 1. **[render.com](https://render.com) ga kirish**
- Hisob yarating yoki kiring

### 2. **Yangi Web Service:**
- "New" → "Web Service"
- "Connect a repository"
- GitHub: `Iftixorbek87/my_money`

### 3. **Environment:**
- **Name:** `my-expense-tracker`
- **Region:** Eng yaqin region
- **Branch:** `main`
- **Runtime:** Python 3

### 4. **Build Settings:**
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`

### 5. **Database:**
- "New" → "PostgreSQL"
- **Name:** `my-expense-tracker-db`
- **Version:** PostgreSQL 14
- Web service ga ulang

### 6. **Environment Variables:**
```
SECRET_KEY=django-insecure-production-secret-key-change-this
DEBUG=0
ALLOWED_HOSTS=onrender.com,*.onrender.com
```

### 7. **Deploy:**
- "Create Web Service" tugmasini bosing
- 2-3 daqiqa kuting

## 🎯 **Natija:**
- **URL:** `https://my-expense-tracker.onrender.com`
- **750MB/oy bepul**
- **SSL bepul**
- **PostgreSQL bepul**
- **24/7 ishlaydi**

## 📱 **Mobile Ready:**
- ✅ Responsive design
- ✅ Touch-friendly
- ✅ Hamburger menyu

**Endi Render.com ga kiring va deployment boshlang!** 🚀
