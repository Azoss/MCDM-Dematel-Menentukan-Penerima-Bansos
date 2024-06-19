## Dematel : Menentukan Penerima Bansos

 Aplikasi menggunakan Streamlit untuk menentukan siapa yang pantas menerima Bansos berdasarkan metode DEMATEL dengan kriteria seperti "Pendapatan", "Jumlah Tanggungan",   "Pengeluaran", dll. Aplikasi ini memungkinkan pengguna untuk menginput data penerima dan menghitung ranking berdasarkan analisis DEMATEL.



### DEMATEL (Decision-Making Trial and Evaluation Laboratory)

DEMATEL adalah metode yang digunakan untuk menganalisis dan memecahkan masalah kompleks dengan memetakan hubungan sebab-akibat antara kriteria atau variabel. Metode ini sangat berguna dalam mengidentifikasi elemen-elemen kunci yang paling berpengaruh dalam suatu sistem.

### Running

1. Instal **Streamlit** jika belum terinstal :

    ```bash
    pip install streamlit
    ```

2. Jalankan aplikasi dengan perintah :

   ```bash
   streamlit run bansos_dematel.py
   ```

### Penjelasan Kode

#### Menghitung Matriks Hubungan Langsung

   
    def calculate_direct_relation_matrix(df):
    n = len(df.columns)
    direct_relation_matrix = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            if i != j:
                direct_relation_matrix[i, j] = np.mean(df.iloc[:, i]) - np.mean(df.iloc[:, j])
    return direct_relation_matrix

Fungsi ini menghitung matriks hubungan langsung (direct_relation_matrix) berdasarkan perbedaan rata-rata nilai antara setiap pasangan kriteria. Matriks ini digunakan untuk memahami seberapa besar satu kriteria mempengaruhi kriteria lainnya secara langsung.

#### Normalisasi Matriks Hubungan Langsung

     def normalize_matrix(matrix):
    return matrix / np.max(matrix)

Fungsi ini menormalkan matriks hubungan langsung agar nilai-nilainya berada dalam rentang yang seragam, sehingga analisis lebih konsisten dan mudah dibandingkan.

#### Menghitung Matriks Hubungan Total

    def calculate_total_relation_matrix(normalized_matrix):
    identity_matrix = np.eye(len(normalized_matrix))
    return np.linalg.inv(identity_matrix - normalized_matrix).dot(normalized_matrix)

Fungsi ini menghitung matriks hubungan total (total_relation_matrix), yang mencakup hubungan langsung dan tidak langsung antara kriteria. Matriks ini diperoleh dengan menggunakan invers dari matriks identitas dikurangi matriks hubungan langsung yang dinormalisasi.
