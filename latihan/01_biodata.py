nama = input ("Nama : ")
nim = input ("NIM : ")
kelas = input ("Kelas : ")
tahun_lahir = int (input ("Tahun lahir : ") )
TAHUN_SEKARANG = 2026
umur = TAHUN_SEKARANG - tahun_lahir
print ("\n===== KARTU BIODATA =====")
print ( f"Nama : {nama}")
print ( f"NIM : {nim}")
print ( f"Kelas : {kelas}")
print ( f"Tahun Lahir : {tahun_lahir}")
print ( f"Perkiraan umur : {umur} tahun")