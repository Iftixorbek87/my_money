# 🚀 Heroku Deployment Guide

## 1. 📋 Tayorlik
- GitHub repository tayyor (✅ allaqachon bor)
- Heroku CLI o'rnatilgan bo'lishi kerak

## 2. 🚀 Heroku da Deployment
1. [heroku.com](https://heroku.com) ga kirish
2. "Create new app"
3. App name tanlang (masalan: my-expense-tracker)
4. GitHub deployment metodini tanlang

## 3. ⚙️ Build va Start Commands
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`

## 4. 🗄️ Database
1. "Resources" → "Add-ons"
2. "Heroku Postgres" (Hobby-dev - bepul)
3. Database yarating

## 5. 🔧 Environment Variables
```
SECRET_KEY=django-insecure-very-long-secret-key-here
DEBUG=0
ALLOWED_HOSTS=herokuapp.com,*.herokuapp.com
```

## 6. 🚀 Deployment Commands
```bash
heroku login
heroku git:remote -a your-app-name
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

## 7. ✅ Natija
- **550MB/oy bepul**
- **SSL bepul** (https://)
- **PostgreSQL bepul**
- **24/7 ishlaydi**

## 🎯 URL: `https://your-app.herokuapp.com`
