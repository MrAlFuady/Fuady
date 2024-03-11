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
st.title('Analisis Kinerja Rental Sepeda')

# Sidebar untuk memilih jenis analisis
analysis_options = {
    "Analisis Harian": "Analisis statistik tentang jumlah peminjaman sepeda harian, termasuk pengaruh suhu dan kecepatan angin.",
    "Performa Produk": "Analisis performa produk berdasarkan jumlah peminjaman dan penjualan harian.",
    "Analisis Cuaca": "Pengaruh cuaca terhadap jumlah peminjaman sepeda, dipisahkan berdasarkan jenis cuaca.",
}
selected_analysis = st.sidebar.selectbox('Pilih Jenis Analisis', list(analysis_options.keys()))

# Visualisasi 1: Scatter plot suhu vs jumlah peminjaman sepeda
if selected_analysis == "Analisis Harian":
    st.subheader('Pengaruh Suhu Terhadap Jumlah Peminjaman Sepeda')
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='temp', y='cnt', data=df_day, ax=ax1, color='skyblue')
    ax1.set_xlabel("Suhu (Celsius)")
    ax1.set_ylabel("Jumlah Peminjaman")
    ax1.set_title("Pengaruh Suhu Terhadap Jumlah Peminjaman Sepeda")
    ax1.grid(True)
    st.pyplot(fig1)

# Visualisasi 2: Scatter plot kecepatan angin vs jumlah peminjaman sepeda
if selected_analysis == "Analisis Harian":
    st.subheader('Korelasi Antara Kecepatan Angin dan Jumlah Peminjaman Sepeda')
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='windspeed', y='cnt', data=df_day, ax=ax2, color='salmon')
    ax2.set_xlabel("Kecepatan Angin (km/h)")
    ax2.set_ylabel("Jumlah Peminjaman")
    ax2.set_title("Korelasi Antara Kecepatan Angin dan Jumlah Peminjaman Sepeda")
    ax2.grid(True)
    st.pyplot(fig2)

# Visualisasi 3: Bar plot jumlah peminjaman pada hari libur
elif selected_analysis == "Performa Produk":
    st.subheader('Jumlah Peminjaman pada Hari Libur')
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.barplot(x='cnt', y='holiday', data=df_day, orient="h", color='lightgreen')
    ax3.set_xlabel("Jumlah Peminjaman")
    ax3.set_ylabel("Hari Libur")
    ax3.set_title("Jumlah Peminjaman pada Hari Libur")
    ax3.grid(True)
    st.pyplot(fig3)

# Visualisasi 4: Bar plot pengaruh cuaca terhadap konsumen
elif selected_analysis == "Analisis Cuaca":
    weather_options = {
        1: "Cerah, Sedikit awan, Berawan sebagian",
        2: "Kabut + Berawan, Kabut + Awan pecah, Kabut + Sedikit awan, Kabut",
        3: "Salju Ringan, Hujan Ringan + Badai Petir + Awan berserakan, Hujan Ringan + Awan berserakan"
    }
    selected_weather = st.sidebar.selectbox('Pilih Jenis Cuaca', list(weather_options.values()))

    # Mencari kunci (angka) berdasarkan nilai (teks) yang dipilih
    selected_weather_key = [key for key, value in weather_options.items() if value == selected_weather][0]

    st.subheader('Pengaruh Cuaca Terhadap Jumlah Peminjaman Sepeda')
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    sns.barplot(x='cnt', hue='weathersit', data=df_day[df_day['weathersit'] == selected_weather_key], orient="h", palette="muted", legend=False, ax=ax4)
    ax4.set_xlabel("Jumlah Peminjaman")
    ax4.set_ylabel("Cuaca")
    ax4.set_title("Pengaruh Cuaca Terhadap Jumlah Peminjaman Sepeda")
    ax4.grid(True)

    # Menampilkan informasi cuaca terkait
    st.info(f"Informasi Cuaca: {selected_weather}")

    st.pyplot(fig4)

# Visualisasi 5: Bar plot jumlah penyewa terdaftar pada tiap bulan
if selected_analysis == "Analisis Harian":
    st.subheader('Jumlah Penyewa Terdaftar pada Tiap Bulan')
    fig5, ax5 = plt.subplots(figsize=(10, 6))
    sns.barplot(x='registered', y='mnth', data=df_day, orient="h", color='lightblue', ax=ax5)
    ax5.set_xlabel("Jumlah Penyewa Terdaftar")
    ax5.set_ylabel("Bulan")
    ax5.set_title("Jumlah Penyewa Terdaftar pada Tiap Bulan")
    ax5.grid(True)
    st.pyplot(fig5)
