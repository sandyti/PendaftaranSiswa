from django.contrib import admin
from unfold.admin import ModelAdmin
# Register your models here.
from TesOnline.models import JawabanSiswa, TesOnline
from jadwal_test.models import HasilSeleksi, JadwalTes
from siswa.models import *
from user.models import LogAktivitas, User

admin.site.register(ProgramStudi)
admin.site.register(User)
admin.site.register(LogAktivitas)
admin.site.register(TesOnline)
admin.site.register(JawabanSiswa)
admin.site.register(JadwalTes)
admin.site.register(HasilSeleksi)

class DokumentSiswaInline(admin.TabularInline):
    model = DokumenSiswa

class SiswaAdmin(admin.ModelAdmin):
    inlines = (DokumentSiswaInline,)

admin.site.register(Siswa, SiswaAdmin)