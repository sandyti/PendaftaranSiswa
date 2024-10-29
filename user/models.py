from django.db import models

# Create your models here.
# Model untuk User (Admin dan Siswa)
class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)  # Should be hashed
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=10,
        choices=[('Admin', 'Admin'), ('Siswa', 'Siswa')],
        default='Siswa'
    )

    def __str__(self):
        return f"{self.username} ({self.role})"

# Model untuk Log Aktivitas
class LogAktivitas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    aktivitas = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log - {self.user.username} - {self.aktivitas}"
