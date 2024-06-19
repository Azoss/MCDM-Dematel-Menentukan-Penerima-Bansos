import numpy as np
import pandas as pd
import streamlit as st

# Fungsi untuk menghitung matriks hubungan langsung
def calculate_direct_relation_matrix(df):
    n = len(df.columns)
    direct_relation_matrix = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            if i != j:
                direct_relation_matrix[i, j] = np.mean(df.iloc[:, i]) - np.mean(df.iloc[:, j])
    
    return direct_relation_matrix

# Normalisasi matriks hubungan langsung
def normalize_matrix(matrix):
    return matrix / np.max(matrix)

# Menghitung matriks hubungan total
def calculate_total_relation_matrix(normalized_matrix):
    identity_matrix = np.eye(len(normalized_matrix))
    return np.linalg.inv(identity_matrix - normalized_matrix).dot(normalized_matrix)

# Menghitung nilai Prominence dan Relation
def calculate_prominence_relation(total_relation_matrix):
    D = np.sum(total_relation_matrix, axis=1)
    R = np.sum(total_relation_matrix, axis=0)
    Prominence = D + R
    Relation = D - R
    
    return Prominence, Relation

# Fungsi utama Streamlit
def main():
    st.title("Sistem Pendukung Keputusan Penerima Bansos dengan DEMATEL")
    
    # Unggah file CSV
    uploaded_file = st.file_uploader("Unggah file CSV", type=["csv"])
    
    if uploaded_file is not None:
        # Baca file CSV
        df = pd.read_csv(uploaded_file)
        
        if not all(column in df.columns for column in ["Nama", "Pendapatan", "Jumlah Tanggungan", "Pengeluaran"]):
            st.error("File CSV harus memiliki kolom: Nama, Pendapatan, Jumlah Tanggungan, Pengeluaran")
        else:
            st.success("File berhasil diunggah dan diproses!")
            st.subheader("Data Penerima Bansos")
            st.write(df)
            
            # Analisis DEMATEL
            criteria_df = df[["Pendapatan", "Jumlah Tanggungan", "Pengeluaran"]]
            direct_relation_matrix = calculate_direct_relation_matrix(criteria_df)
            normalized_matrix = normalize_matrix(direct_relation_matrix)
            total_relation_matrix = calculate_total_relation_matrix(normalized_matrix)
            Prominence, Relation = calculate_prominence_relation(total_relation_matrix)
            
            st.subheader("Hasil Analisis DEMATEL")
            ranking = Prominence.argsort()[::-1]
            ranked_data = df.iloc[ranking]
            
            st.write("Ranking Penerima Bansos Berdasarkan DEMATEL:")
            st.write(ranked_data)
            st.write("Prominence:", Prominence)
            st.write("Relation:", Relation)

            st.subheader("Penjelasan Berdasarkan Ranking")
            for i, (nama, prominence, relation) in enumerate(zip(ranked_data["Nama"], Prominence[ranking], Relation[ranking])):
                st.write(f"**{i+1}. {nama}**")
                st.write(f"  - **Prominence**: {prominence:.2f}")
                st.write(f"  - **Relation**: {relation:.2f}")
                if relation > 0:
                    st.write(f"  - **Penjelasan**: {nama} lebih banyak memberikan pengaruh ke kriteria lain, sehingga dianggap sebagai penyebab utama dalam sistem.")
                else:
                    st.write(f"  - **Penjelasan**: {nama} lebih banyak menerima pengaruh dari kriteria lain, sehingga dianggap sebagai akibat utama dalam sistem.")

# Jalankan aplikasi Streamlit
if __name__ == "__main__":
    main()
