# ===== admin.py =====
from django.contrib import admin
from .models import ProgramStudi, JalurPendaftaran, SistemKuliah, Pengumuman, TataCara

@admin.register(ProgramStudi)
class ProgramStudiAdmin(admin.ModelAdmin):
    list_display = ['kode', 'nama', 'strata', 'tersedia_jalur_pendaftaran']
    list_filter = ['strata']
    search_fields = ['nama', 'kode']

@admin.register(JalurPendaftaran)
class JalurPendaftaranAdmin(admin.ModelAdmin):
    list_display = ['nama', 'kode', 'is_active']
    list_filter = ['is_active']
    search_fields = ['nama', 'kode']

@admin.register(SistemKuliah)
class SistemKuliahAdmin(admin.ModelAdmin):
    list_display = ['nama', 'kode']
    search_fields = ['nama', 'kode']

@admin.register(Pengumuman)
class PengumumanAdmin(admin.ModelAdmin):
    list_display = ['judul', 'tanggal', 'kategori', 'is_active']
    list_filter = ['kategori', 'is_active', 'tanggal']
    search_fields = ['judul', 'konten']
    date_hierarchy = 'tanggal'

@admin.register(TataCara)
class TataCaraAdmin(admin.ModelAdmin):
    list_display = ['nomor', 'judul']
    ordering = ['nomor']