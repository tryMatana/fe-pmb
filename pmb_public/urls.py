# ===== urls.py (pmb_public app) =====
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'program-studi', views.ProgramStudiViewSet)
router.register(r'jalur-pendaftaran', views.JalurPendaftaranViewSet)
router.register(r'sistem-kuliah', views.SistemKuliahViewSet)
router.register(r'pengumuman', views.PengumumanViewSet)
router.register(r'tata-cara', views.TataCaraViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('api/pmb_public-data/', views.pmb_public_data, name='pmb_public-data'),
]