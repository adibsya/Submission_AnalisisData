import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Dashboard
st.title("Dashboard Analisis Data Penyewaan Sepeda")

# Membaca dataset
df = pd.read_csv("day.csv")
df['dteday'] = pd.to_datetime(df['dteday'])  # Konversi kolom tanggal

# Sidebar untuk filter data
st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input('Tanggal Mulai', df['dteday'].min())
end_date = st.sidebar.date_input('Tanggal Akhir', df['dteday'].max())

# Filter berdasarkan tanggal
filtered_df = df[(df['dteday'] >= pd.to_datetime(start_date)) & (df['dteday'] <= pd.to_datetime(end_date))]

# Filter suhu
temp_range = st.sidebar.slider('Rentang Suhu (Normalisasi)', 0.0, 1.0, (0.1, 0.9))
filtered_df = filtered_df[(filtered_df['temp'] >= temp_range[0]) & (filtered_df['temp'] <= temp_range[1])]

# Filter kelembaban
humidity_range = st.sidebar.slider('Rentang Kelembaban (Normalisasi)', 0.0, 1.0, (0.1, 0.9))
filtered_df = filtered_df[(filtered_df['hum'] >= humidity_range[0]) & (filtered_df['hum'] <= humidity_range[1])]

# Menampilkan data yang difilter
st.subheader(f"Data Penyewaan Sepeda dari {start_date} hingga {end_date}")
st.write(filtered_df.head())

# Visualisasi 1: Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda
st.subheader("Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda")
season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
weather_map = {1: 'Good Weather', 2: 'Misty/Cloudy', 3: 'Light Rain/Snow', 4: 'Heavy Rain/Snow'}
filtered_df['season'] = filtered_df['season'].map(season_map)
filtered_df['weathersit'] = filtered_df['weathersit'].map(weather_map)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='season', y='cnt', hue='weathersit', data=filtered_df, ax=ax)
ax.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Musim dan Kondisi Cuaca')
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)

# Visualisasi 2: Hubungan Suhu dengan Pengguna Terdaftar pada Hari Kerja vs Hari Libur
st.subheader("Hubungan Suhu dengan Pengguna Terdaftar pada Hari Kerja vs Hari Libur")
fig, ax = plt.subplots(figsize=(10, 6))
working_days = filtered_df[filtered_df['workingday'] == 1]
non_working_days = filtered_df[filtered_df['workingday'] == 0]
sns.scatterplot(x=working_days['temp'], y=working_days['registered'], label='Hari Kerja', color='blue', ax=ax)
sns.scatterplot(x=non_working_days['temp'], y=non_working_days['registered'], label='Hari Libur', color='red', ax=ax)
ax.set_title('Hubungan Suhu dengan Pengguna Terdaftar')
ax.set_xlabel('Suhu (Normalisasi)')
ax.set_ylabel('Jumlah Pengguna Terdaftar')
ax.legend()
st.pyplot(fig)

# Visualisasi Tambahan: Distribusi Suhu
st.subheader("Distribusi Suhu")
fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(filtered_df['temp'], bins=20, kde=True, ax=ax)
ax.set_title('Distribusi Suhu')
ax.set_xlabel('Suhu (Normalisasi)')
st.pyplot(fig)

# Visualisasi Tambahan: Distribusi Kelembaban
st.subheader("Distribusi Kelembaban")
fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(filtered_df['hum'], bins=20, kde=True, ax=ax)
ax.set_title('Distribusi Kelembaban')
ax.set_xlabel('Kelembaban (Normalisasi)')
st.pyplot(fig)

# Visualisasi Tambahan: Boxplot Penyewaan Berdasarkan Hari Kerja vs Libur
st.subheader("Penyewaan Sepeda pada Hari Kerja vs Hari Libur")
fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(x='workingday', y='cnt', data=filtered_df, ax=ax)
ax.set_title('Penyewaan Sepeda Berdasarkan Hari Kerja vs Hari Libur')
ax.set_xlabel('Hari Kerja (0 = Libur, 1 = Kerja)')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)
