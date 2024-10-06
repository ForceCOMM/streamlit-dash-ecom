# Analisis Data dengan Python by dicoding

## Ikhtisar
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)

## Overview
Projek ini berisi implementasi real dari projek akhir analisa data dengan python dengan dataset E-Commerce untuk mempelajari pengimplmetasian dari Course tersebut

## Struktur Paket
- `dashboard/`: Dashboard dengan streamlit beserta dengan datanya
- `data/`: Direktori yang mengandung data
- `notebook.ipynb`: Notebook dalam bentuk .ipynb.
- `README.md`: Dokumentasi File.

## Instalasi
1. Clone kedalam local
```
git clone ...
```
2. Change directory (cd) ke folder projek
```
cd submission
```
3. Install semua dependecies atau library yang dibutuhkan
```
pip install -r requirements.txt
```

## Keterangan
1. **Data Wrangling**: Data wrangling merupakan tahapan melakukan penilaian terhadap data, untuk tahapan ini bisa dilihat pada notebook.ipynb

2. **Exploratory Data Analysis (EDA)**: Eksplorasi Analisi data berisi pencaritahuan konteks data

3. **Visualization**: Melakukan Visualisasi Data

Untuk melakukan visualisasi data dapat dijalankan dengan argumen-argumen berikut ini
```
cd submission/dasboard
streamlit run dashboard.py
```
Untuk melihat dashboard yang dibuat akses pada `http://localhost:8501` atau keterangan pada terminal ketika argumen dijalankan, contoh: `Local URL: http://localhost:8501 Network URL: http://192.168.115.185:8501`

## Data Sources
Data didapat dari course Analisis Data dengan Python by dicoding