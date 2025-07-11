# ===== Panduan Setup =====
"""
LANGKAH-LANGKAH SETUP DJANGO PORTAL:

1. Buat Virtual Environment:
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows

2. Install Dependencies:
   pip install -r requirements.txt

3. Buat Project Django:
   django-admin startproject fe_pmb
   cd fe_pmb

4. Buat App Portal:
   python manage.py startapp portal

5. Konfigurasi Settings:
   - Copy konfigurasi settings.py dari artifact
   - Tambahkan 'portal' ke INSTALLED_APPS

6. Buat Models:
   - Copy models.py dari artifact
   - Buat folder management/commands/ di dalam app portal
   - Copy setup_data.py ke portal/management/commands/

7. Buat dan Jalankan Migrations:
   python manage.py makemigrations
   python manage.py migrate

8. Setup Data Awal:
   python manage.py setup_data

9. Buat Superuser (optional):
   python manage.py createsuperuser

10. Buat Folder Templates:
    mkdir templates
    mkdir templates/portal
    - Copy template HTML ke templates/portal/home.html

11. Buat Folder Static:
    mkdir static
    mkdir static/css
    mkdir static/js
    mkdir static/images

12. Copy Views, URLs, Serializers:
    - Copy semua kode dari artifact ke file yang sesuai

13. Jalankan Server:
    python manage.py runserver

14. Akses Portal:
    http://127.0.0.1:8000/

15. Akses Admin (optional):
    http://127.0.0.1:8000/admin/

16. Akses API:
    http://127.0.0.1:8000/api/portal-data/
    http://127.0.0.1:8000/api/program-studi/
    http://127.0.0.1:8000/api/pengumuman/

STRUCTURE FOLDER:
fe_pmb/
├── manage.py
├── requirements.txt
├── fe_pmb/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── portal/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│   ├── migrations/
│   └── management/
│       └── commands/
│           └── setup_data.py
├── templates/
│   └── portal/
│       └── home.html
├── static/
│   ├── css/
│   ├── js/
│   └── images/
└── media/
"""