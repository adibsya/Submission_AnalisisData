# Proyek Analisis Data Penyewaan Sepeda

Proyek ini bertujuan untuk menganalisis data penyewaan sepeda menggunakan dataset *Bike Sharing*. Analisis dilakukan untuk menjawab beberapa pertanyaan bisnis yang relevan, serta menyediakan visualisasi interaktif melalui dashboard berbasis **Streamlit**.

---

## **1. Deskripsi Proyek**
Proyek ini mencakup:
- Analisis data penyewaan sepeda berdasarkan musim, kondisi cuaca, suhu, dan hari kerja/libur.
- Pembuatan visualisasi data untuk menjawab pertanyaan bisnis.
- Dashboard interaktif untuk eksplorasi data secara dinamis.

---

## **2. Pertanyaan Bisnis**
1. Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda di setiap musim?
2. Apakah suhu memengaruhi jumlah pengguna terdaftar pada hari kerja dibandingkan hari libur?

---

## **3. Cara Menjalankan Dashboard**
Dashboard interaktif dibuat menggunakan **Streamlit**. Ikuti langkah-langkah berikut untuk menjalankannya:

### **Langkah 1: Instalasi Dependensi**
Pastikan semua library yang diperlukan telah diinstal. Gunakan perintah berikut untuk menginstal dependensi:
pip install -r requirements.txt


### **Langkah 2: Jalankan Dashboard**
Jalankan file `dashboard_app.py` menggunakan perintah berikut:
- masuk ke direktori Dashboard Streamlit dengan ketik : cd '.\Dashboard Streamlit\'
jalankan dulu virtual environment : .\.venv\Scripts\activate.ps1 (jika pakai powershel) 
lalu jalankan : streamlit run ./dashboard_app.py


### **Langkah 3: Interaksi dengan Dashboard**
Setelah dijalankan, dashboard akan terbuka di browser Anda. Anda dapat menggunakan berbagai filter (seperti rentang tanggal, suhu, kelembaban) untuk mengeksplorasi data.

---

## **5. Dataset**
Dataset yang digunakan adalah *Bike Sharing Dataset* (`day.csv`) yang berisi informasi harian terkait penyewaan sepeda, termasuk:
- **Tanggal (`dteday`)**: Tanggal pencatatan.
- **Musim (`season`)**: Musim (1 = Spring, 2 = Summer, 3 = Fall, 4 = Winter).
- **Kondisi Cuaca (`weathersit`)**: Kondisi cuaca (1 = Clear/Partly Cloudy, 2 = Mist/Cloudy, 3 = Light Snow/Rain, 4 = Heavy Rain/Snow).
- **Suhu (`temp`)**: Suhu normalisasi.
- **Jumlah Penyewaan (`cnt`)**: Total penyewaan sepeda.

Dataset dapat ditemukan di folder `data/`.

---

## **6. Hasil Analisis**
### Pertanyaan Bisnis 1:
**Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda di setiap musim?**
- Penyewaan sepeda tertinggi terjadi pada kondisi cuaca baik (*Good Weather*) di semua musim.
- Musim gugur (*Fall*) memiliki rata-rata penyewaan tertinggi dibandingkan musim lainnya.

### Pertanyaan Bisnis 2:
**Apakah suhu memengaruhi jumlah pengguna terdaftar pada hari kerja dibandingkan hari libur?**
- Terdapat korelasi positif antara suhu dan jumlah pengguna terdaftar.
- Pengguna terdaftar lebih aktif pada hari kerja dibandingkan hari libur untuk suhu yang sama.

---

## **7. Teknologi yang Digunakan**
Proyek ini menggunakan teknologi berikut:
- Python (pandas, matplotlib, seaborn)
- Streamlit (untuk pembuatan dashboard)
- Jupyter Notebook (untuk analisis data)

---

## **8. Kontributor**
- Nama: Ahmad Adib Syaifulloh
- Email: ahmadadibsyaifulloh@gmail.com
- Username: adib_syaa

