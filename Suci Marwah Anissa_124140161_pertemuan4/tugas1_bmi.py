# ===================================================
# Berkas: tugas1_bmi.py
# Deskripsi: Program Penghitung BMI dan Kategori Berat Badan
# ===================================================

def hitung_bmi(berat: float, tinggi: float) -> float:
    """
    Menghitung nilai BMI berdasarkan berat (kg) dan tinggi (m).
    Parameter:
        berat (float): Berat badan dalam kg.
        tinggi (float): Tinggi badan dalam meter.
    Return:
        float: Nilai BMI hasil perhitungan.
    """
    return berat / (tinggi * tinggi)

def tentukan_kategori(bmi: float) -> str:
    """
    Menentukan kategori berat badan berdasarkan nilai BMI.
    Parameter:
        bmi (float): Nilai BMI.
    Return:
        str: Teks kategori berat badan.
    """
    if bmi < 18.5:
        return "Berat badan kurang"
    elif 18.5 <= bmi < 25:
        return "Berat badan normal"
    elif 25 <= bmi < 30:
        return "Berat badan berlebih"
    else:
        return "Obesitas"

# Program Utama
if __name__ == "__main__":
    print("=" * 40)
    print("--- PROGRAM PENGHITUNG BMI ---")
    print("=" * 40)
    
    try:
        # Menerima input dari pengguna
        input_berat = float(input("Masukkan berat badan (kg) : "))
        input_tinggi = float(input("Masukkan tinggi badan (m) : "))
        
        # Memanggil fungsi yang sudah dibuat
        nilai_bmi = hitung_bmi(input_berat, input_tinggi)
        kategori = tentukan_kategori(nilai_bmi)
        
        # Menampilkan hasil dengan format 2 desimal
        print("\n--- HASIL PERHITUNGAN ---")
        print(f"Nilai BMI Anda : {nilai_bmi:.2f}")
        print(f"Kategori       : {kategori}")
        
    except ValueError:
        print("\n[Error] Input tidak valid! Pastikan memasukkan angka.")