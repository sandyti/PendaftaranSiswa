from django.db import models

from siswa.models import Siswa

# Create your models here.
# Model untuk Jadwal Tes
class JadwalTes(models.Model):
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    tanggal_tes = models.DateField()
    lokasi_tes = models.CharField(max_length=255)

    def __str__(self):
        return f"Tes untuk {self.siswa.nama} pada {self.tanggal_tes}"

# Model untuk Hasil Seleksi
class HasilSeleksi(models.Model):
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    nilai_tes = models.DecimalField(max_digits=5, decimal_places=2)
    status_kelulusan = models.CharField(
        max_length=20,
        choices=[('Lulus', 'Lulus'), ('Tidak Lulus', 'Tidak Lulus')],
        default='Tidak Lulus'
    )

    def __str__(self):
        return f"Hasil untuk {self.siswa.nama} - {self.status_kelulusan}"
