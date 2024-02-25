# project_kasir
---
Andi adalah seorang pemilik supermarket besar di salah satu Indonesia. Andi memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu Andi akan membuat sistem kasir yang self-service di supermarket miliknya. Sehingga customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli dan fitur yang lain.
Sehingga customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut. Setelah Andi melakukan riset, ternyata Andi memiliki masalah, yaitu Andi membutuhkan Programmer untuk membuatkan fitur-fitur agar bisa sistem kasir self-service di supermarket itu bisa berjalan dengan lancar.

---

## Requirements :
1. Customer membuat ID Transaksi sebagai berikut :
   
   Dengan membuat objek dari data kelas trnsct_123 = `Transaction`
3. Customer memasukkan nama belanja, jumlah belanja, harga belanja per item yang akan dibeli
* Customer memasukkan nama item, jumlah item, harga per item yang 
   ingin dibeli
2. Jika customer sudah selesai berbelanja, dengan ketentuan nama belanja, jumlah belanja, dan harga belanja yang diinput sudah benar.
  Maka customer bisa melakukan check order.
  Menggunakan method `check_keranjang()`
  
3. Jika terjadi kesalahan pada saat customer memasukkan nama belanja.
   Maka customer bisa melakukan update nama belanja dengan method : `update_item_nama_belanja()`

4. Jika terjadi kesalahan pada saat customer memasukkan jumlah belanja.
   Maka customer bisa melakukan update jumlah belanja dengan method : `update_item_jumlah_belanja()`

5. Jika terjadi kesalahan pada saat customer memasukkan harga belanja.
   Maka customer bisa melakukan update harga belanja dengan method : `update_item_harga_belanja()`

6.  Jika customer ingin membatalkan transaksi maka bisa melakukan :
   
         a). Menghapus daftar belanja dari nama belanja dengan method : `delete_item()`
    
         b). Jika customer ingin menghapus semua daftar belanja maka dapat menggunakan : `self.keranjang.clear()`

         c). Jika ingin menghapus semua daftar belanja maka dapat menggunakan : `reset_transaction()`

5. Setelah selesai melakukan pengecekan, customer dapat menghitung total belanja yang sudah dibeli.
    Dengan menggunakan method : `total_price()`.
   
   Pada supermarket Andi terdapat ketentuan :
   
      a).Jika total belanja lebih dari Rp 200.000 maka akan mendapatkan diskon 5%
   
      b). Jika total belanja lebih dari Rp 300.000 maka akan mendapatkan diskon 8%
   
      c). Jika total belanja lebih dari Rp 500.000 maka akan mendapatkan diskon 10%


   ## Flowchart

   ![image](https://github.com/Indriyani1507/project_kasir/blob/main/flowchart_kasir.jpg)


   ## Penggunaan Method
   1). `Transaction()`
      
      Membuat kelas transaksi untuk menghimpun data transaksi dan membuat fungsi/method sehingga menghasilkan objek
      
   2). `add_item()`
      
      Digunakan untuk menambahkan nama belanja, jumlah belanja dan harga belanja per item
      
   3). `update_item()`

      Digunakan untuk mengupdate/memperbarui isi keranjang
      
   4). `update_item_nama_belanja()`

      Digunakan untuk memperbarui/mengganti salah satu nama belanja
      
   5). `update_item_jumlah_belanja()`

      Digunakan untuk memperbarui/mengganti salah satu jumlah belanja
      
   6). `update_item_harga_belanja()`

      Digunakan untuk memperbarui/mengganti harga belanja
   
   7). `delete_item()`

      Digunakan untuk menghapus daftar belanja didalam keranjang
   
   8). `reset_keranjang()`

      Digunakan untuk menghapus semua daftar belanja dalam keranjang
   
   9). `cek_keranjang`
       
       Digunakan untuk menghitung isi keranjang
      
   10). `total_price()`
       
       Digunakan untuk untuk menghitung total belanja dari daftar keranjang
      
   

## Objectif :
Proyek ini bertujuan untuk membuat sistem kasir supermarket dengan alur sebagai berikut:

   a). Pelanggan memasukkan nama barang, jumlah barang, dan harga 
   
   * Pelanggan memasukkan nama belanja, jumlah belanja, dan harga belanja yang dibeli.

   b). Jika terjadi kesalahan dalam memasukkan nama barang, jumlah

   * Jika terjadi kesalahan dalam memasukkan nama barang, jumlah 
       barang, atau harga barang, pelanggan dapat mengubah atau 
       memperbarui barang tersebut:
        * perbarui nama belanja
        * perbarui jumlah belanja
        * perbarui harga belanja
          
   c). Jika pelanggan membatalkan pembelian suatu barang
   * Jika pelanggan membatalkan pembelian suatu barang, pelanggan dapat menghapus barang tersebut:
        * hapus satu baris 
        * reset semua transaksi
          
   d). Jika pelanggan sudah selesai membeli
   
   *Menampilkan tabel yang berisi semua data pesanan

   e). Jika pelanggan mengalami kesalahan dalam memasukkan nama belanja, Pelanggan dapat memeriksa dengan ditampilkan pesan error
   
   *Mengeluarkan pesan error* :
   
   "Type data yang dimasukkan tidak sesuai dengan keranjang", 
    
   "Nilai yang dimasukkan bukan integer dan tidak sesuai", 
    
   "Transaksi dibatalkan, daftar belanja berhasil dihapus". 
      
        Dalam hal ini berguna untuk pengecekan kembali agar menegtahui kesalahannya.


**Input:**<br />
 ## Test Case 1
**menambahkan item belanja ke dalam keranjang**

trsnct_123.add_item("Beras", 10, 15_000)

trsnct_123.add_item("susu",10, 15_000)

trsnct_123.add_item("gula", 7, 20_000)

trsnct_123.check_keranjang()

**Output:**<br />

![image](https://github.com/Indriyani1507/project_kasir/blob/main/testing%201.jpeg)

 ## Test Case 2

**Input:**<br />
**Mengubah/memperbarui nama belanja setelah mengalami pengupdate an** 

trsnct_123.update_item_nama_belanja("susu", "kopi")

trsnct_123.check_keranjang()

**Output:**<br />

![image](https://github.com/Indriyani1507/project_kasir/blob/main/testing%202.jpeg)

**Input:**<br />
##  Test case 3
**Mengubah/memperbarui nama belanja dengan string**

trsnct_123.update_item_nama_belanja("kopi", 15)

trsnct_123.check_keranjang()
**Output:**<br />

![image](https://github.com/Indriyani1507/project_kasir/blob/main/testing%203.jpeg)

**Input:**<br />
## Test case 4
**Mengubah/memperbarui jumlah belanja setelah mengalami pengupdate an**

trsnct_123.update_item_jumlah_belanja("gula", 9)

trsnct_123.check_keranjang()

**Output:**<br />
![image](https://github.com/Indriyani1507/project_kasir/blob/main/testing%204.jpeg)

**Input:**<br />

## Test Case 5
**memperbarui jumlah belanja dengan menggunakan string**

trsnct_123.update_item_jumlah_belanja("gula", "roti")

trsnct_123.check_keranjang()
**Output:**<br />
![image](https://github.com/Indriyani1507/project_kasir/blob/main/testing%205.jpeg)


**Input:**<br />
## Test Case 6
**Memperbarui/mengupdate harga belanja**

trsnct_123.update_item_harga_belanja("gula", 30_000)

trsnct_123.check_keranjang()
**Output:**<br />
![image](https://github.com/Indriyani1507/project_kasir/blob/main/testing%206.jpeg)

**Input:**<br />
## Test Case 7
**Memperbarui harga belanja menggunakan string**

trsnct_123.update_item_harga_belanja("gula", "mie")

trsnct_123.check_keranjang()
![image](https://github.com/Indriyani1507/project_kasir/blob/main/testing%207.jpeg)

**Input:**<br />
## Test case  8
**Menyatakan apakah belanjaan akan mendapatkan diskon**

trsnct_123.total_price()

trsnct_123.check_keranjang()
![image](https://github.com/Indriyani1507/project_kasir/blob/main/testing%208.jpeg)
