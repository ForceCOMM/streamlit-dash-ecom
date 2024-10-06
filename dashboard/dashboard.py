import pandas as pd  # Mengimpor pandas untuk manipulasi data
import matplotlib.pyplot as plt  # Mengimpor matplotlib untuk visualisasi data
import seaborn as sns  # Mengimpor seaborn untuk visualisasi yang lebih baik
import streamlit as st  # Mengimpor Streamlit untuk membuat aplikasi web

# Memuat data CSV ke dalam DataFrame
state_year_payment_totals = pd.read_csv('dashboard/state_year_month_day_payment_totals.csv')  # Data total pembayaran berdasarkan negara bagian
most_goods_by_year = pd.read_csv('dashboard/most_goods_by_year.csv')  # Data barang terlaris berdasarkan tahun
average_review_scores = pd.read_csv('dashboard/average_review_score_sorted_with_timestamp.csv')  # Skor rata-rata ulasan produk
rfm = pd.read_csv('rfm.csv')  # Memuat data segmentasi pelanggan RFM

# Mengonversi kolom tanggal ke format datetime
state_year_payment_totals['order_purchase_timestamp'] = pd.to_datetime(
    state_year_payment_totals['order_year'].astype(str) + '-' + state_year_payment_totals['order_month'].astype(str) + '-01'
)
most_goods_by_year['order_purchase_timestamp'] = pd.to_datetime(
    most_goods_by_year['order_year'].astype(str) + '-' + most_goods_by_year['order_month'].astype(str) + '-' + most_goods_by_year['order_day'].astype(str)
)
average_review_scores['order_purchase_timestamp'] = pd.to_datetime(
    average_review_scores['order_year'].astype(str) + '-' + average_review_scores['order_month'].astype(str) + '-' + average_review_scores['order_day'].astype(str)
)

# Menyiapkan aplikasi Streamlit
st.title("Visualisasi Data E-commerce")  # Judul aplikasi

# Menerapkan gaya global untuk semua plot
plt.style.use('seaborn-whitegrid')  # Menggunakan gaya seaborn untuk tampilan yang lebih baik

# Input tanggal untuk memfilter data berdasarkan rentang tanggal
start_date = st.date_input("Pilih tanggal mulai", value=pd.to_datetime("2017-01-01").date())  # Input tanggal mulai
end_date = st.date_input("Pilih tanggal akhir", value=pd.to_datetime("2017-10-24").date())  # Input tanggal akhir

# Mengonversi tanggal ke datetime untuk pemfilteran
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Visualisasi Pertama: Total Pembayaran per Negara Bagian untuk rentang tanggal yang dipilih
st.header(f'Total Pembayaran per Negara Bagian dari {start_date.date()} hingga {end_date.date()}')  # Header visualisasi

# Memfilter data pembayaran untuk rentang tanggal yang dipilih
payment_data_filtered = state_year_payment_totals[
    (state_year_payment_totals['order_purchase_timestamp'] >= start_date) &
    (state_year_payment_totals['order_purchase_timestamp'] <= end_date)
]

if not payment_data_filtered.empty:
    fig, ax = plt.subplots(figsize=(12, 6))  # Membuat figure dan axes
    ax.bar(payment_data_filtered['customer_state'], payment_data_filtered['payment_value'], color="#1f77b4")  # Membuat diagram batang
    ax.set_title(f'Total Pembayaran per Negara Bagian dari {start_date.date()} hingga {end_date.date()}', fontsize=16)  # Judul plot
    ax.set_xlabel('Negara Bagian', fontsize=12)  # Label sumbu x
    ax.set_ylabel('Total Nilai Pembayaran', fontsize=12)  # Label sumbu y
    plt.xticks(rotation=90)  # Memutar label sumbu x
    plt.tight_layout()  # Mengatur tata letak untuk tampilan yang lebih baik
    st.pyplot(fig)  # Menampilkan plot di Streamlit
else:
    st.write(f"Tidak ada data pembayaran yang tersedia untuk rentang tanggal yang dipilih.")  # Pesan jika tidak ada data

# Visualisasi Kedua: 5 Barang Terlaris berdasarkan Kategori Produk untuk rentang tanggal yang dipilih
st.header(f'Total Barang Terjual berdasarkan Kategori Produk dari {start_date.date()} hingga {end_date.date()}')  # Header visualisasi

# Memfilter data barang untuk rentang tanggal yang dipilih
goods_data_filtered = most_goods_by_year[
    (most_goods_by_year['order_purchase_timestamp'] >= start_date) &
    (most_goods_by_year['order_purchase_timestamp'] <= end_date)
]

# Membatasi ke 5 kategori teratas berdasarkan total barang terjual
top_goods_data = goods_data_filtered.groupby('product_category_name').sum().nlargest(5, 'total_goods_sold').reset_index()

if not top_goods_data.empty:
    fig, ax = plt.subplots(figsize=(12, 6))  # Membuat figure dan axes
    sns.barplot(data=top_goods_data, x='product_category_name', y='total_goods_sold', ax=ax, color="#1f77b4")  # Membuat diagram batang
    ax.set_title(f'Total Barang Terjual berdasarkan Kategori Produk dari {start_date.date()} hingga {end_date.date()}', fontsize=16)  # Judul plot
    ax.set_xlabel('Kategori Produk', fontsize=12)  # Label sumbu x
    ax.set_ylabel('Total Barang Terjual', fontsize=12)  # Label sumbu y
    plt.xticks(rotation=45, ha='right')  # Memutar label sumbu x
    plt.tight_layout()  # Mengatur tata letak untuk tampilan yang lebih baik
    st.pyplot(fig)  # Menampilkan plot di Streamlit
else:
    st.write(f"Tidak ada data barang yang terjual untuk rentang tanggal yang dipilih.")  # Pesan jika tidak ada data

# Visualisasi Ketiga: Skor Ulasan Rata-rata berdasarkan Kategori Produk untuk periode yang dipilih
st.header(f'Skor Ulasan Rata-rata untuk Kategori Produk untuk periode yang dipilih')  # Header visualisasi

# Memfilter data skor ulasan untuk rentang tanggal yang dipilih
average_review_scores_filtered = average_review_scores[
    (average_review_scores['order_purchase_timestamp'] >= start_date) &
    (average_review_scores['order_purchase_timestamp'] <= end_date)
]

# Mengelompokkan berdasarkan kategori produk dan menghitung skor ulasan rata-rata
average_review_scores_grouped = average_review_scores_filtered.groupby('product_category_name_english')['review_score'].mean()

# Membatasi ke 5 skor ulasan rata-rata teratas
top_average_review_score = average_review_scores_grouped.nlargest(5)

if not top_average_review_score.empty:
    fig, ax = plt.subplots(figsize=(12, 6))  # Membuat figure dan axes
    bars = ax.bar(top_average_review_score.index, top_average_review_score.values, color="#1f77b4")  # Membuat diagram batang
    ax.set_title('Skor Ulasan Rata-rata untuk Kategori Produk', fontsize=16)  # Judul plot
    ax.set_xlabel('Kategori Produk', fontsize=12)  # Label sumbu x
    ax.set_ylabel('Skor Ulasan Rata-rata', fontsize=12)  # Label sumbu y
    plt.xticks(rotation=45, ha='right')  # Memutar label sumbu x

    # Menambahkan label nilai di atas setiap batang
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., height, f'{height:.2f}', ha='center', va='bottom')  # Menampilkan nilai di atas batang

    # Mengatur batas sumbu y dari 0 hingga 5
    ax.set_ylim(0, 5)
    plt.tight_layout()  # Mengatur tata letak untuk tampilan yang lebih baik
    st.pyplot(fig)  # Menampilkan plot di Streamlit
else:
    st.write(f"Tidak ada data skor ulasan rata-rata yang tersedia untuk periode yang dipilih.")  # Pesan jika tidak ada data

# Visualisasi Keempat: Segmentasi Pelanggan Berdasarkan Analisis RFM
st.header(f'Segmentasi Pelanggan Berdasarkan Analisis RFM')  # Header untuk visualisasi RFM

# Membuat plot distribusi segmentasi pelanggan
fig, ax = plt.subplots(figsize=(10, 6))  # Menentukan ukuran figure
sns.countplot(data=rfm, x='Customer_Segment', order=rfm['Customer_Segment'].value_counts().index, palette='Blues', ax=ax)  # Menghitung dan menampilkan jumlah pelanggan di setiap segmen

# Mengkustomisasi plot
ax.set_title('Segmentasi Pelanggan Berdasarkan Analisis RFM', fontsize=16)  # Menambahkan judul
ax.set_xlabel('Segmentasi Pelanggan', fontsize=12)  # Menambahkan label sumbu x
ax.set_ylabel('Jumlah Pelanggan', fontsize=12)  # Menambahkan label sumbu y
plt.xticks(rotation=45, fontsize=10)  # Memutar label sumbu x untuk keterbacaan yang lebih baik

# Menampilkan plot
plt.tight_layout()  # Mengatur tata letak untuk tampilan yang lebih baik
st.pyplot(fig)  # Menampilkan plot di Streamlit
