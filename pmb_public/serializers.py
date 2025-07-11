# ===== serializers.py =====
from rest_framework import serializers
from .models import ProgramStudi, JalurPendaftaran, SistemKuliah, Pengumuman, TataCara

class ProgramStudiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramStudi
        fields = '__all__'

class JalurPendaftaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = JalurPendaftaran
        fields = '__all__'

class SistemKuliahSerializer(serializers.ModelSerializer):
    class Meta:
        model = SistemKuliah
        fields = '__all__'

class PengumumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengumuman
        fields = '__all__'

class TataCaraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TataCara
        fields = '__all__'