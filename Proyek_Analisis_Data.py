import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import streamlit as st

# Membaca data
data = pd.read_csv('https://raw.githubusercontent.com/ssnhm/data/refs/heads/main/day.csv')

# Menentukan Pertanyaan Bisnis
st.title('Analisis Penyewaan Sepeda')
st.write("""
## Pertanyaan Analisis
1. Apakah terdapat hubungan antara suhu dan penyewaan sepeda? Jika iya, bagaimana hubungan antara keduanya? 
2. Bagaimana perbedaan penyewaan sepeda antara hari kerja dan akhir pekan? Strategi apa yang dapat diterapkan untuk meningkatkan keuntungan?
""")

# 1. Analisis Korelasi antara suhu (temp) dan jumlah penyewaan sepeda (cnt)
temp = data['temp']  # suhu
cnt = data['cnt']  # banyak penyewaan sepeda

# Hitung koefisien korelasi Pearson (r)
n = len(temp)
sum_x = np.sum(temp)
sum_y = np.sum(cnt)
sum_xy = np.sum(temp * cnt)
sum_x2 = np.sum(temp**2)
sum_y2 = np.sum(cnt**2)
pembilang = (n * sum_xy) - (sum_x * sum_y)
penyebut = np.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))
r = pembilang / penyebut

# Hitung persamaan garis regresi (y = mx + b)
m = pembilang / (n * sum_x2 - sum_x**2)  # Gradien
b = (sum_y - m * sum_x) / n  # Intersep

# Tampilkan output
st.subheader("Hasil Analisis Korelasi")
st.write(f"Koefisien korelasi (r): {r:.4f}")
st.write(f"Persamaan garis regresi: y = {m:.1f}x + {b:.1f}")

# Insight
insight1 = """
Setelah dilakukan analisis korelasi, diperoleh nilai koefisien korelasi (r) sebesar 0,6275 dan persamaan garis untuk regresinya adalah y = 6640,7x + 1214,6. Persamaan garis ini nanti akan dibuat visualisasi data agar terlihat hubungan antara suhu dan jumlah penyewaan sepeda.
"""
st.write(insight1)

# Plotting Data Pertanyaan 1
plt.figure(figsize=(10, 5))
plt.scatter(temp, cnt, alpha=0.5, color='lightskyblue', edgecolors='black', label='Data Penyewaan')
plt.title('Hubungan Antara Suhu dan Jumlah Penyewaan Sepeda',fontsize=14, fontweight='bold')
plt.xlabel('Suhu yang Dinormalisasi (temp)', fontsize=11)
plt.ylabel('Jumlah Penyewaan Sepeda (cnt)', fontsize=11)

# Tambahkan garis regresi
x_values = np.linspace(temp.min(), temp.max(), 10)  # Membuat titik x
y_values = m * x_values + b  # Menghitung y berdasarkan persamaan regresi
plt.plot(x_values, y_values, color='black', label='Garis Regresi',linewidth=1)

# Finishing dan tampilkan plot
plt.legend()
plt.grid(True, which='both', linewidth=0.4)
st.pyplot(plt)

# 2. Analisis perbedaan penyewaan sepeda antara hari kerja dan akhir pekan
avg_workingday = data[data['workingday'] == 1]['cnt'].mean()  # "1" menandakan itu adalah hari kerja
avg_weekend = data[data['workingday'] == 0]['cnt'].mean()  # "0" menandakan itu adalah akhir pekan

# Tampilkan output
st.subheader("Rata-rata Jumlah Penyewaan Sepeda")
st.write(f"Rata-rata jumlah penyewaan sepeda di hari kerja: {avg_workingday:.2f}")
st.write(f"Rata-rata jumlah penyewaan sepeda di akhir pekan: {avg_weekend:.2f}")

# Plotting pertanyaan 2
mean = [avg_workingday, avg_weekend]
jenis = ['Hari Kerja', 'Akhir Pekan']

# Buat histogram rata-rata jumlah penyewaan sepeda pada hari kerja dan akhir pekan
plt.figure(figsize=(7, 5))
bars = plt.bar(jenis, mean, color=['teal', 'salmon'], edgecolor='black', width=0.4)
plt.title('Rata-rata Jumlah Penyewaan Sepeda Pada Hari Kerja dan Akhir Pekan', fontsize=14, fontweight='bold')
plt.ylabel('Rata-rata Jumlah Penyewaan Sepeda', fontsize=11)
plt.xlabel('Jenis Hari', fontsize=11)

# Tampilkan nilai rata-rata di atas setiap bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval:.2f}', ha='center', va='bottom',fontsize=10)

# Finishing dan tampilkan plot
plt.grid(axis='y', linestyle='--',alpha=0.7)
plt.tight_layout()
st.pyplot(plt)

# Insight
insight2 = """
Dari visualisasi 1 (Hubungan Antara Suhu dan Jumlah Penyewaan Sepeda), terlihat terdapat hubungan positif atau berbanding lurus antara suhu dan penyewaan sepeda. Hal ini juga sesuai dengan besar nilai koefisien korelasi (r) yang diperoleh sebelumnya yaitu 0,6275.
Dari visualisasi 2 (Rata-rata Jumlah Penyewaan Sepeda Pada Hari Kerja dan Akhir Pekan), terlihat rataan penyewaan sepeda pada hari kerja lebih tinggi daripada akhir pekan.
"""
st.write(insight2)

# Conclusion
st.title('Conclusion')
conclusion1 = """
Setelah dilakukan analisis korelasi dan regresi, diperoleh nilai koefisien korelasi (r) sebesar 0,6275 dan persamaan garis untuk regresinya adalah y = 6640,7x + 1214,6. Nilai korelasi yang lebih besar atau sama dengan 0,6 menandakan hubungan yang cukup kuat. Sehingga bisa kita lihat hasil visualisasi data, ketika suhu cenderung hangat jumlah penyewaan sepeda semakin meningkat. Namun, dapat dilihat juga terdapat beberapa titik ketika hampir mendekati suhu normaliasi (41 derajat Celcius), jumlah penyewaan sepeda menurun. Hal ini dapat dikarenakan suhu yang ekstrim (terlalu panas) membuat orang enggan menyewa sepeda.
"""
st.write(conclusion1)

conclusion2 = """
Setelah dilakukan perhitungan rataan untuk jumlah penyewaan sepeda pada hari kerja dan akhir pekan, diperoleh rataan penyewaan sepeda pada hari kerja lebih tinggi daripada akhir pekan. Hal ini menandakan penyewaan sepeda lebih banyak digunakan sebagai alat mobilisasi untuk pekerjaan atau keperluan sehari-hari dibandingkan untuk hiburan ketika akhir pekan.

Strategi yang dapat dilakukan oleh perusahaan penyewa sepeda yaitu lebih menargetkan orang yang tinggal di daerah industri atau perkantoran karena lebih banyak pekerja disana, perusahaan dapat lebih memperbanyak unit sepeda disana. Selain itu, dikarenakan penyewaan sepeda lebih tinggi di hari kerja dibandingkan akhir pekan, perusahaan dapat memberikan promo (penawaran menarik) di akhir pekan agar menarik minat orang-orang.
"""
st.write(conclusion2)
