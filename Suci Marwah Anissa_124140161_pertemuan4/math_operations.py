# ===================================================
# Berkas: math_operations.py
# Deskripsi: Modul kustom penyedia fungsi matematika
# ===================================================

# Konstanta
PI = 3.14159

def luas_persegi(sisi: float) -> float:
    """
    Menghitung luas persegi.
    Parameter: sisi (float)
    Return: float
    """
    return sisi * sisi

def keliling_persegi(sisi: float) -> float:
    """
    Menghitung keliling persegi.
    Parameter: sisi (float)
    Return: float
    """
    return 4 * sisi

def luas_persegi_panjang(panjang: float, lebar: float) -> float:
    """
    Menghitung luas persegi panjang.
    Parameter: panjang (float), lebar (float)
    Return: float
    """
    return panjang * lebar

def keliling_persegi_panjang(panjang: float, lebar: float) -> float:
    """
    Menghitung keliling persegi panjang.
    Parameter: panjang (float), lebar (float)
    Return: float
    """
    return 2 * (panjang + lebar)

def luas_lingkaran(jari_jari: float) -> float:
    """
    Menghitung luas lingkaran menggunakan konstanta PI.
    Parameter: jari_jari (float)
    Return: float
    """
    return PI * (jari_jari ** 2)

def keliling_lingkaran(jari_jari: float) -> float:
    """
    Menghitung keliling lingkaran.
    Parameter: jari_jari (float)
    Return: float
    """
    return 2 * PI * jari_jari

def celsius_ke_fahrenheit(celsius: float) -> float:
    """
    Konversi suhu Celsius ke Fahrenheit.
    Parameter: celsius (float)
    Return: float
    """
    return (celsius * 9/5) + 32

def celsius_ke_kelvin(celsius: float) -> float:
    """
    Konversi suhu Celsius ke Kelvin.
    Parameter: celsius (float)
    Return: float
    """
    return celsius + 273.15

# Blok testing mandiri modul
if __name__ == "__main__":
    print("[TEST MODUL] Menjalankan uji coba internal math_operations:")
    print("Luas Persegi (sisi=4) :", luas_persegi(4))
    print("Konversi 25C ke F     :", celsius_ke_fahrenheit(25))