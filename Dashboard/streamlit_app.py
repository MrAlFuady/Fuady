import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Fungsi untuk memuat data
@st.cache_data
def load_data():
    # Ganti path dengan path file CSV Anda
    df_day = pd.read_csv("Data Set/day.csv")
    return df_day

# Memuat data
df_day = load_data()

# Judul dashboard
st.title('Dashboard Persewaan Sepeda')

# Visualisasi 1: Scatter plot suhu vs jumlah peminjaman sepeda
st.subheader('Pengaruh Suhu Terhadap Jumlah Peminjaman Sepeda')
fig1, ax1 = plt.subplots(figsize=(14, 6))
sns.scatterplot(x='temp', y='cnt', data=df_day, ax=ax1)
st.pyplot(fig1)

# Visualisasi 2: Scatter plot kecepatan angin vs jumlah peminjaman sepeda
st.subheader('Korelasi Antara Kecepatan Angin dan Jumlah Peminjaman Sepeda')
fig2, ax2 = plt.subplots(figsize=(14, 6))
sns.scatterplot(x='windspeed', y='cnt', data=df_day, ax=ax2)
st.pyplot(fig2)

# Visualisasi 3: Bar plot jumlah peminjaman pada hari libur
st.subheader('Jumlah Peminjaman pada Hari Libur')
fig3, ax3 = plt.subplots(figsize=(14, 6))
sns.barplot(y=df_day["holiday"], x=df_day["cnt"], orient="h", color='blue', ax=ax3)
plt.xlabel("Jumlah Penyewa")
plt.ylabel("Hari Libur")
plt.title("Jumlah Peminjaman pada Hari Libur")
st.pyplot(fig3)

# Visualisasi 4: Bar plot pengaruh cuaca terhadap konsumen
st.subheader('Pengaruh Cuaca Terhadap Konsumen')
fig4, ax4 = plt.subplots(figsize=(14, 6))
sns.barplot(y=df_day["weathersit"], x=df_day["cnt"], orient="h", color='blue', ax=ax4)
plt.xlabel("Jumlah Penyewa")
plt.ylabel("Cuaca")
plt.title("Pengaruh Cuaca terhadap Konsumen")
st.pyplot(fig4)

# Visualisasi 5: Bar plot jumlah penyewa terdaftar pada tiap bulan
st.subheader('Jumlah Penyewa Terdaftar pada Tiap Bulan')
fig5, ax5 = plt.subplots(figsize=(14, 6))
sns.barplot(y=df_day["mnth"], x=df_day["registered"], orient="h", color='blue', ax=ax5)
plt.xlabel("Jumlah Penyewa Terdaftar")
plt.ylabel("Bulan")
plt.title("Jumlah Penyewa Terdaftar pada Tiap Bulan")
st.pyplot(fig5)
