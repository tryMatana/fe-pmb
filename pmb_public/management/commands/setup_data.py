# ===== management/commands/setup_data.py =====
# Buat folder: pmb_public/management/commands/
from django.core.management.base import BaseCommand
from pmb_public.models import (
    ProgramStudi,
    JalurPendaftaran,
    SistemKuliah,
    Pengumuman,
    TataCara,
)


class Command(BaseCommand):
    help = "Setup initial data for pmb_public"

    def handle(self, *args, **options):
        self.stdout.write("Setting up initial data...")

        # Create Sistem Kuliah
        sistem_kuliah_data = [
            {"nama": "Reguler", "kode": "REG"},
            {"nama": "Eksekutif", "kode": "EKS"},
            {"nama": "Karyawan", "kode": "KAR"},
        ]

        for data in sistem_kuliah_data:
            obj, created = SistemKuliah.objects.get_or_create(
                kode=data["kode"], defaults=data
            )
            if created:
                self.stdout.write(f"Created Sistem Kuliah: {obj.nama}")

        # Create Jalur Pendaftaran
        jalur_data = [
            {
                "nama": "Jalur Reguler",
                "kode": "REG",
                "deskripsi": "Jalur pendaftaran reguler",
            },
            {
                "nama": "Jalur Prestasi",
                "kode": "PRES",
                "deskripsi": "Jalur pendaftaran prestasi",
            },
            {
                "nama": "Jalur Beasiswa",
                "kode": "BEAS",
                "deskripsi": "Jalur pendaftaran beasiswa",
            },
            {
                "nama": "Jalur Transfer",
                "kode": "TRANS",
                "deskripsi": "Jalur pendaftaran transfer",
            },
        ]

        for data in jalur_data:
            obj, created = JalurPendaftaran.objects.get_or_create(
                kode=data["kode"], defaults=data
            )
            if created:
                self.stdout.write(f"Created Jalur Pendaftaran: {obj.nama}")

        # Create Program Studi
        program_studi_data = [
            {
                "kode": "S1-MAN",
                "nama": "Manajemen",
                "strata": "S1",
                "deskripsi": "Program Studi Manajemen",
                "tersedia_jalur_pendaftaran": 4,
            },
            {
                "kode": "S1-HOST",
                "nama": "Hospitality Dan Pariwisata",
                "strata": "S1",
                "deskripsi": "Program Studi Hospitality Dan Pariwisata",
                "tersedia_jalur_pendaftaran": 4,
            },
            {
                "kode": "S1-AKU",
                "nama": "Akuntansi",
                "strata": "S1",
                "deskripsi": "Program Studi Akuntansi",
                "tersedia_jalur_pendaftaran": 4,
            },
            {
                "kode": "S1-FIS",
                "nama": "Fisika",
                "strata": "S1",
                "deskripsi": "Program Studi Fisika",
                "tersedia_jalur_pendaftaran": 4,
            },
            {
                "kode": "S1-STAT",
                "nama": "Statistika",
                "strata": "S1",
                "deskripsi": "Program Studi Statistika",
                "tersedia_jalur_pendaftaran": 4,
            },
            {
                "kode": "S2-MAN",
                "nama": "Manajemen",
                "strata": "S2",
                "deskripsi": "Program Studi Magister Manajemen",
                "tersedia_jalur_pendaftaran": 3,
            },
            {
                "kode": "S2-AKU",
                "nama": "Akuntansi",
                "strata": "S2",
                "deskripsi": "Program Studi Magister Akuntansi",
                "tersedia_jalur_pendaftaran": 3,
            },
        ]

        for data in program_studi_data:
            obj, created = ProgramStudi.objects.get_or_create(
                kode=data["kode"], defaults=data
            )
            if created:
                self.stdout.write(f"Created Program Studi: {obj.nama}")

        # Create Pengumuman
        pengumuman_data = [
            {
                "judul": "MATANA UNGGUL - Ujian Saringan Masuk",
                "konten": "Informasi mengenai ujian saringan masuk program MATANA UNGGUL untuk calon mahasiswa baru.",
                "kategori": "Pengumuman",
            },
            {
                "judul": "PRICELIST TAHUN AJARAN 2025/2026",
                "konten": "Daftar biaya kuliah untuk tahun ajaran 2025/2026 seluruh program studi.",
                "kategori": "Pengumuman",
            },
        ]

        for data in pengumuman_data:
            obj, created = Pengumuman.objects.get_or_create(
                judul=data["judul"], defaults=data
            )
            if created:
                self.stdout.write(f"Created Pengumuman: {obj.judul}")

        # Create Tata Cara
        tata_cara_data = [
            {
                "nomor": 1,
                "judul": "Pilih Jalur Pendaftaran",
                "deskripsi": "Terdapat jalur masuk sesuai dengan pilihan dan kebutuhan kampus.",
            },
            {
                "nomor": 2,
                "judul": "Isi Formulir Pendaftaran",
                "deskripsi": "Lengkapi data dan pola formulir secara benar.",
            },
            {
                "nomor": 3,
                "judul": "Bayar Biaya Pendaftaran",
                "deskripsi": "Lakukan pembayaran sesuai petunjuk yang tersedia.",
            },
            {
                "nomor": 4,
                "judul": "Unggah Berkas & Ikuti Seleksi",
                "deskripsi": "Kirim dokumen dan ikuti tahapan seleksi sesuai jadwal.",
            },
        ]

        for data in tata_cara_data:
            obj, created = TataCara.objects.get_or_create(
                nomor=data["nomor"], defaults=data
            )
            if created:
                self.stdout.write(f"Created Tata Cara: {obj.judul}")

        self.stdout.write(self.style.SUCCESS("Successfully setup initial data!"))
