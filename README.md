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

#### 1. Menghitung Matriks Hubungan Langsung

Matriks Hubungan Langsung: Ini adalah langkah pertama dalam analisis DEMATEL. Matriks ini menunjukkan pengaruh langsung antara kriteria yang diidentifikasi.
Misalnya, jika kita memiliki kriteria Pendapatan (X1), Jumlah Tanggungan (X2), dan Pengeluaran (X3), maka matriks hubungan langsung bisa terlihat seperti ini:

     
    | X1 (Pendapatan) | X2 (Jumlah Tanggungan) | X3 (Pengeluaran)           |
    -------------------------------------------------------------------
    X1    |       0         |      Hubungan X1 -> X2 |   Hubungan X1 -> X3  |
    -------------------------------------------------------------------
    X2    |  Hubungan X2 -> X1 |        0              |   Hubungan X2 -> X3|
    -------------------------------------------------------------------
    X3    |  Hubungan X3 -> X1 |  Hubungan X3 -> X2    |        0           |
    -------------------------------------------------------------------

Di sini, "Hubungan X1 -> X2" menunjukkan pengaruh Pendapatan terhadap Jumlah Tanggungan, dan seterusnya.


#### 2. Normalisasi Matriks Hubungan Langsung

Normalisasi: Setelah matriks hubungan langsung dibentuk, nilai-nilainya dinormalkan untuk menghasilkan matriks yang memiliki rentang nilai yang seragam (biasanya dari 0 hingga 1 atau -1 hingga 1). Ini mempermudah perbandingan antara kriteria yang berbeda.

    | X1 (Pendapatan) | X2 (Jumlah Tanggungan) | X3 (Pengeluaran)     |
     -------------------------------------------------------------------
     X1               |       0                | Nilai Norm X1 -> X2  |   Nilai Norm X1 -> X3 |
     -------------------------------------------------------------------
     X2               |  Nilai Norm X2 -> X1   |        0             |   Nilai Norm X2 -> X3 |
     -------------------------------------------------------------------
     X3               |  Nilai Norm X3 -> X1   |  Nilai Norm X3 -> X2 |        0              |
     -------------------------------------------------------------------
     

#### 3. Menghitung Matriks Hubungan Total

Matriks Hubungan Total: Setelah normalisasi, matriks hubungan total dibentuk. Ini mencakup pengaruh langsung dan tidak langsung antara kriteria.

    | X1 (Pendapatan) | X2 (Jumlah Tanggungan) | X3 (Pengeluaran)       | 
      -------------------------------------------------------------------
      X1              |       1                | Total Hubungan X1      |   Total Hubungan X1 |
      -------------------------------------------------------------------
      X2              |  Total Hubungan X2     |          1             |   Total Hubungan X2 |
      -------------------------------------------------------------------
      X3              |  Total Hubungan X3     |  Total Hubungan X3     |        1            |
      -------------------------------------------------------------------


Matriks ini menunjukkan pengaruh total (langsung dan tidak langsung) dari setiap kriteria terhadap yang lain.
