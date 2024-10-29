from django.db import models

# Create your models here.
from django.utils import timezone


# Model untuk Program Studi
class ProgramStudi(models.Model):
    nama_program = models.CharField(max_length=255)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama_program

# Model untuk Siswa
class Siswa(models.Model):
    nama = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telepon = models.CharField(max_length=20)
    tanggal_lahir = models.DateField()
    alamat = models.TextField()
    status_pendaftaran = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Terverifikasi', 'Terverifikasi'), ('Ditolak', 'Ditolak')],
        default='Pending'
    )
    program_studi = models.ForeignKey(ProgramStudi, on_delete=models.CASCADE)
    tanggal_pendaftaran = models.DateTimeField(auto_now_add=True)
    verifikasi_dokumen = models.BooleanField(default=False)

    def __str__(self):
        return self.nama

# Model untuk Dokumen Siswa
class DokumenSiswa(models.Model):
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    jenis_dokumen = models.CharField(max_length=255)
    file_dokumen = models.FileField(upload_to='dokumen_siswa/')
    status_verifikasi = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.jenis_dokumen} - {self.siswa.nama}"
