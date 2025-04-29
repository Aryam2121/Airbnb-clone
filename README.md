This project is a full-stack Airbnb clone for listing rentals using:
- Backend: Django + DRF + MySQL
- Scraper: Scrapy + Requests
- Frontend: Next.js + Tailwind CSS



## 🧩 Features
- Scrapes Airbnb listings and stores them in MySQL
- GET & POST APIs for listings
- User-friendly frontend to display and search listings

## 🚀 Getting Started
```bash
# Backend
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Frontend
cd frontend
npm install
npm run dev

# Scraper
cd scraper
scrapy crawl airbnb
```
