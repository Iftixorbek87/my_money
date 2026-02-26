# 🚀 Render.com Deployment Guide

## 1. 📋 Tayorlik
- GitHub repository tayyor (✅ allaqachon bor)

## 2. 🚀 Render.com da Deployment
1. [render.com](https://render.com) ga kirish
2. "New" → "Web Service"
3. "Connect GitHub repository"
4. "Iftixorbek87/my_money" ni tanlang

## 3. ⚙️ Build va Start Commands
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`

## 4. 🗄️ Database
1. "New" → "PostgreSQL"
2. Database yarating
3. Database URL ni oling
4. Web service ga ulang

## 5. 🔧 Environment Variables
```
SECRET_KEY=django-insecure-very-long-secret-key-here
DEBUG=0
ALLOWED_HOSTS=onrender.com,*.onrender.com
DATABASE_URL=postgresql://user:pass@host:port/dbname
```

## 6. ✅ Natija
- **750MB/oy bepul**
- **SSL bepul** (https://)
- **Custom domain**
- **24/7 ishlaydi**

## 🎯 URL: `https://your-app.onrender.com`
