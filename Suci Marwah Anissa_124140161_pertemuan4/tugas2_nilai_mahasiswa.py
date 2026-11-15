# ===================================================
# Berkas: tugas2_nilai_mahasiswa.py
# Deskripsi: Pengelolaan Nilai Mahasiswa (List & Dictionary)
# ===================================================

def hitung_nilai_akhir(uts: float, uas: float, tugas: float) -> float:
    """
    Menghitung nilai akhir berdasarkan bobot 30% UTS, 40% UAS, 30% Tugas.
    Parameter:
        uts (float): Nilai UTS mahasiswa.
        uas (float): Nilai UAS mahasiswa.
        tugas (float): Nilai Tugas mahasiswa.
    Return:
        float: Nilai akhir hasil perhitungan bobot.
    """
    return (0.30 * uts) + (0.40 * uas) + (0.30 * tugas)

def tentukan_grade(nilai_akhir: float) -> str:
    """
    Menentukan grade A-E berdasarkan nilai akhir.
    Parameter:
        nilai_akhir (float): Total nilai akhir mahasiswa.
    Return:
        str: Huruf grade (A, B, C, D, atau E).
    """
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"

# Program Utama
if __name__ == "__main__":
    # List berisi 5 dictionary data mahasiswa
    data_mahasiswa = [
        {"nama": "Suci", "nim": "12414001", "nilai_uts": 80, "nilai_uas": 85, "nilai_tugas": 90},
        {"nama": "Marwah", "nim": "12414002", "nilai_uts": 60, "nilai_uas": 65, "nilai_tugas": 70},
        {"nama": "Anissa", "nim": "12414003", "nilai_uts": 50, "nilai_uas": 45, "nilai_tugas": 60},
        {"nama": "Diva", "nim": "12414004", "nilai_uts": 90, "nilai_uas": 95, "nilai_tugas": 85},
        {"nama": "Rezki", "nim": "12414005", "nilai_uts": 75, "nilai_uas": 70, "nilai_tugas": 80}
    ]

    print("=" * 65)
    print(f"{'NAMA':<15} | {'NIM':<10} | {'NILAI AKHIR':<12} | {'GRADE':<5}")
    print("=" * 65)

    nilai_tertinggi = -1
    nilai_terendah = 101
    mhs_tertinggi = ""
    mhs_terendah = ""

    # Iterasi data mahasiswa
    for mhs in data_mahasiswa:
        # Panggil fungsi perhitungan
        n_akhir = hitung_nilai_akhir(mhs["nilai_uts"], mhs["nilai_uas"], mhs["nilai_tugas"])
        grade = tentukan_grade(n_akhir)

        # Cetak baris tabel
        print(f"{mhs['nama']:<15} | {mhs['nim']:<10} | {n_akhir:<12.2f} | {grade:<5}")

        # Logika pencarian nilai tertinggi & terendah
        if n_akhir > nilai_tertinggi:
            nilai_tertinggi = n_akhir
            mhs_tertinggi = mhs['nama']
        
        if n_akhir < nilai_terendah:
            nilai_terendah = n_akhir
            mhs_terendah = mhs['nama']

    print("=" * 65)
    print("\n--- INFORMASI TAMBAHAN ---")
    print(f"Mahasiswa Nilai Tertinggi : {mhs_tertinggi} ({nilai_tertinggi:.2f})")
    print(f"Mahasiswa Nilai Terendah  : {mhs_terendah} ({nilai_terendah:.2f})")