# ===== views.py =====
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ProgramStudi, JalurPendaftaran, SistemKuliah, Pengumuman, TataCara
from .serializers import (
    ProgramStudiSerializer, JalurPendaftaranSerializer, 
    SistemKuliahSerializer, PengumumanSerializer, TataCaraSerializer
)

def home(request):
    """Main pmb_public page"""
    # Hardcoded data for now
    context = {
        'program_studi': ProgramStudi.objects.all(),
        'jalur_pendaftaran': JalurPendaftaran.objects.filter(is_active=True),
        'sistem_kuliah': SistemKuliah.objects.all(),
        'pengumuman': Pengumuman.objects.filter(is_active=True)[:2],
        'tata_cara': TataCara.objects.all()
    }
    return render(request, 'pmb_public/home.html', context)

# API ViewSets
class ProgramStudiViewSet(viewsets.ModelViewSet):
    queryset = ProgramStudi.objects.all()
    serializer_class = ProgramStudiSerializer

class JalurPendaftaranViewSet(viewsets.ModelViewSet):
    queryset = JalurPendaftaran.objects.all()
    serializer_class = JalurPendaftaranSerializer

class SistemKuliahViewSet(viewsets.ModelViewSet):
    queryset = SistemKuliah.objects.all()
    serializer_class = SistemKuliahSerializer

class PengumumanViewSet(viewsets.ModelViewSet):
    queryset = Pengumuman.objects.all()
    serializer_class = PengumumanSerializer

class TataCaraViewSet(viewsets.ModelViewSet):
    queryset = TataCara.objects.all()
    serializer_class = TataCaraSerializer

@api_view(['GET'])
def pmb_public_data(request):
    """API endpoint untuk mendapatkan semua data pmb_public"""
    data = {
        'program_studi': ProgramStudiSerializer(ProgramStudi.objects.all(), many=True).data,
        'jalur_pendaftaran': JalurPendaftaranSerializer(JalurPendaftaran.objects.filter(is_active=True), many=True).data,
        'sistem_kuliah': SistemKuliahSerializer(SistemKuliah.objects.all(), many=True).data,
        'pengumuman': PengumumanSerializer(Pengumuman.objects.filter(is_active=True)[:2], many=True).data,
        'tata_cara': TataCaraSerializer(TataCara.objects.all(), many=True).data
    }
    return Response(data)