# ===== models.py =====
from django.db import models
from django.utils import timezone

class ProgramStudi(models.Model):
    STRATA_CHOICES = [
        ('S1', 'Strata 1'),
        ('S2', 'Strata 2'),
        ('S3', 'Strata 3'),
    ]
    
    kode = models.CharField(max_length=10, unique=True)
    nama = models.CharField(max_length=100)
    strata = models.CharField(max_length=2, choices=STRATA_CHOICES)
    deskripsi = models.TextField(blank=True)
    tersedia_jalur_pendaftaran = models.IntegerField(default=4)
    
    def __str__(self):
        return f"{self.strata} - {self.nama}"
    
    class Meta:
        verbose_name = "Program Studi"
        verbose_name_plural = "Program Studi"

class JalurPendaftaran(models.Model):
    nama = models.CharField(max_length=100)
    kode = models.CharField(max_length=20, unique=True)
    deskripsi = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name = "Jalur Pendaftaran"
        verbose_name_plural = "Jalur Pendaftaran"

class SistemKuliah(models.Model):
    nama = models.CharField(max_length=50)
    kode = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name = "Sistem Kuliah"
        verbose_name_plural = "Sistem Kuliah"

class Pengumuman(models.Model):
    judul = models.CharField(max_length=200)
    konten = models.TextField()
    tanggal = models.DateTimeField(default=timezone.now)
    gambar = models.ImageField(upload_to='pengumuman/', blank=True, null=True)
    kategori = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.judul
    
    class Meta:
        verbose_name = "Pengumuman"
        verbose_name_plural = "Pengumuman"
        ordering = ['-tanggal']

class TataCara(models.Model):
    nomor = models.IntegerField()
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    
    def __str__(self):
        return f"{self.nomor}. {self.judul}"
    
    class Meta:
        verbose_name = "Tata Cara"
        verbose_name_plural = "Tata Cara"
        ordering = ['nomor']