from django.db import models

from siswa.models import Siswa

# Create your models here.
class TesOnline(models.Model):
    judul_tes = models.CharField(max_length=255)
    deskripsi = models.TextField()
    tanggal_mulai = models.DateTimeField()
    tanggal_selesai = models.DateTimeField()

    def __str__(self):
        return self.judul_tes

class SoalTes(models.Model):
    tes = models.ForeignKey(TesOnline, on_delete=models.CASCADE)
    pertanyaan = models.TextField()
    jawaban_benar = models.CharField(max_length=255)

    def __str__(self):
        return f"Soal pada {self.tes.judul_tes}"
    
class JawabanSiswa(models.Model):
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)  # ForeignKey ke model Siswa
    soal = models.ForeignKey(SoalTes, on_delete=models.CASCADE)
    jawaban_siswa = models.CharField(max_length=255)
    benar = models.BooleanField()
    status_jawaban = models.CharField(
        max_length=20,
        choices=[('Benar', 'Benar'), ('Salah', 'Salah')],
        default='Salah'
    )

    def __str__(self):
        return f"Jawaban {self.siswa.nama} untuk soal {self.soal.id} - {self.status_jawaban}"
