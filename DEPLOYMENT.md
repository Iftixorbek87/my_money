# 🚀 Railway Deployment Guide

## 1. 📋 Tayorlik
- GitHub repository yarating
- Kodlarni GitHub ga yuklang

## 2. 🚀 Railway da Deployment
1. [railway.app](https://railway.app) ga kirish
2. "New Project" → "Deploy from GitHub repo"
3. Repository ni tanlang
4. Django loyiha aniqlanadi

## 3. ⚙️ Environment Variables
`railway.env` faylidan nusxalab quyidagilarni qo'shing:
```
SECRET_KEY=django-insecure-very-long-secret-key-here
DEBUG=0
ALLOWED_HOSTS=railway.app,*.railway.app
```

## 4. 🗄️ Database
1. Railway da "PostgreSQL" service qo'shing
2. Database URL ni oling
3. Environment variables ga qo'shing:
```
DATABASE_URL=postgresql://username:password@host:port/dbname
```

## 5. 🚀 Build Commands
Railway avtomatik aniqlaydi:
- Build: `pip install -r requirements.txt`
- Start: `gunicorn config.wsgi:application`

## 6. ✅ Natija
- Bepul SSL
- Avtomatik deployment
- Custom domain (ixtiyoriy)
- 500MB/oy bepul

## 🎯 Alternativlar:
- **Render.com** - 750MB/oy bepul
- **Heroku** - 550MB/oy bepul
- **Vercel** - Next.js uchun yaxshi
