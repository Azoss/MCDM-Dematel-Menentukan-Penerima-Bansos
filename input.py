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
    
    # Input form
    with st.form(key='input_form'):
        nama = st.text_input("Nama")
        pendapatan = st.slider("Pendapatan (dalam ribuan)", min_value=0, max_value=10000, step=500) * 1000
        jumlah_tanggungan = st.number_input("Jumlah Tanggungan", min_value=0)
        pengeluaran = st.slider("Pengeluaran (dalam ribuan)", min_value=0, max_value=10000, step=500) * 1000
        submit_button = st.form_submit_button(label='Submit')
        
        if submit_button:
            if 'data' not in st.session_state:
                st.session_state.data = pd.DataFrame(columns=["Nama", "Pendapatan", "Jumlah Tanggungan", "Pengeluaran"])
            
            new_data = pd.DataFrame({
                "Nama": [nama],
                "Pendapatan": [pendapatan],
                "Jumlah Tanggungan": [jumlah_tanggungan],
                "Pengeluaran": [pengeluaran]
            })
            
            st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)
            st.success("Data berhasil ditambahkan!")
    
    # Display data
    if 'data' in st.session_state and not st.session_state.data.empty:
        st.subheader("Data Penerima Bansos")
        st.write(st.session_state.data)
        
        criteria_df = st.session_state.data[["Pendapatan", "Jumlah Tanggungan", "Pengeluaran"]]
        direct_relation_matrix = calculate_direct_relation_matrix(criteria_df)
        normalized_matrix = normalize_matrix(direct_relation_matrix)
        total_relation_matrix = calculate_total_relation_matrix(normalized_matrix)
        Prominence, Relation = calculate_prominence_relation(total_relation_matrix)
        
        st.subheader("Hasil Analisis DEMATEL")
        ranking = Prominence.argsort()[::-1]
        ranked_data = st.session_state.data.iloc[ranking]
        
        st.write("Ranking Penerima Bansos Berdasarkan DEMATEL:")
        st.write(ranked_data)
        st.write("Prominence:", Prominence)
        st.write("Relation:", Relation)

# Jalankan aplikasi Streamlit
if __name__ == "__main__":
    main()
