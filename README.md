# project_kasir
---
Andi adalah seorang pemilik supermarket besar di salah satu Indonesia. Andi memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu Andi akan membuat sistem kasir yang self-service di supermarket miliknya. Sehingga customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli dan fitur yang lain.
Sehingga customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut. Setelah Andi melakukan riset, ternyata Andi memiliki masalah, yaitu Andi membutuhkan Programmer untuk membuatkan fitur-fitur agar bisa sistem kasir self-service di supermarket itu bisa berjalan dengan lancar.

---

## Requirements :
1. Customer memasukkan nama belanja, jumlah belanja, harga belanja per item yang akan dibeli
* Customer memasukkan nama item, jumlah item, harga per item yang 
   ingin dibeli
2. Jika customer sudah selesai berbelanja, dengan ketentuan nama belanja, jumlah belanja, dan harga belanja yang diinput sudah benar. Maka customer bisa melakukan check order.
   Menggunakan method check_keranjang()
     dengan ketentuan :
* Jika customer sudah selesai dengan belanjanya, apabila nama belanja, jumlah belanja, dan harga belanja yang diinput sudah benar.
* Maka customer bisa melakukan check order. Menggunakan method check_keranjang()
* 
    b). Jika terdapat kesalahan input maka akan mengeluarkan pesan 
    * Jika terdapat kesalahan input maka akan mengeluarkan pesan 
        “terdapat kesalahan input data” dan bisa melakukan update item

3. Jika terjadi kesalahan pada saat customer memasukkan nama belanja,   
* Jika terjadi kesalahan pada saat customer memasukkan nama belanja,   
   jumlah belanja, atau harga belanja per item tetapi tidak ingin menghapus 
   itemnya, maka customer dapat melakukan update :
   a). Update nama belanja dengan method :
   * Update nama item dengan method :
       update_item_nama_belanja
   b). Update jumlah item dengan method :
   * Update jumlah item dengan method :
       update_item_jumlah_belanja
   c). Update harga per item dengan method :
   * Update harga per item dengan method :
       update_item_harga_belanja

4.  Jika customer ingin membatalkan transaksi maka bisa melakukan :
   a). Menghapus salah satu item dari nama belanja dengan method
      self.keranjang.remove(item)
* Jika customer ingin menghapus semua daftar belanja maka bisa melakukan :
   * Menghapus semua item  dengan method
        self.keranjang.clear()

   b). Jika ingin menghapus semua transaksi maka dapat menggunakan 
   * Jika ingin menghapus semua transaksi maka dapat menggunakan 
       method
      reset_transaction()

5. Setelah selesai melakukan pengecekan,customer dapat menghitung total belanja yang sudah dibeli. Dengan menggunakan method total_harga(). Pada supermarket ini terdapat ketentuan :
   a). Jika total belanja customer diatas Rp 200.000 maka akan 
* Setelah selesai melakukan pengecekan,customer dapat menghitung total belanja yang sudah dibeli. Dengan menggunakan method total_harga(). Pada supermarket ini terdapat 
  ketentuan :
   * Jika total belanja customer diatas Rp 200.000 maka akan 
       mendapatkan diskon 5%
   b). Jika total belanja customer diatas Rp 300.000 maka akan 
   * Jika total belanja customer diatas Rp 300.000 maka akan 
       mendapatkan diskon 8%
   c). Jika total belanja customer diatas Rp 500.000 maka akan 
   * Jika total belanja customer diatas Rp 500.000 maka akan 
       mendapatkan diskon 10%

## Objectif :
Proyek ini bertujuan untuk membuat sistem kasir supermarket dengan alur sebagai berikut:
   a). Pelanggan memasukkan nama barang, jumlah barang, dan harga 
   * Pelanggan memasukkan nama barang, jumlah barang, dan harga 
       barang yang dibeli.
   b). Jika terjadi kesalahan dalam memasukkan nama barang, jumlah 
   * Jika terjadi kesalahan dalam memasukkan nama barang, jumlah 
       barang, atau harga barang, pelanggan dapat mengubah atau 
       memperbarui barang tersebut:
        * perbarui nama item
        * perbarui jumlah item
        * perbarui harga barang
   c). Jika pelanggan membatalkan pembelian suatu barang, pelanggan 
   * Jika pelanggan membatalkan pembelian suatu barang, pelanggan 
       dapat menghapus barang tersebut:
        * hapus satu baris 
        * reset semua transaksi
   d). Jika pelanggan sudah selesai membeli, namun masih ragu apakah 
   * Jika pelanggan sudah selesai membeli, namun masih ragu apakah 
       harga barang dan nama     yang dimasukkan sudah benar, 
       pelanggan dapat memeriksa pesanan dengan output sebagai 
       berikut:
@@ -64,7 +62,11 @@ Proyek ini bertujuan untuk membuat sistem kasir supermarket dengan alur sebagai
        * Mengeluarkan pesan “Ada kesalahan input data” jika terjadi 
          kesalahan input.
        * Menampilkan tabel yang berisi semua data pesanan.
    
       #test case dalam pengoperasian code**
     ## Test Case 1 

**Input:**<br />
**menambahkan item belanja ke dalam keranjang**

trsnct_123.add_item("Beras", 10, 15_000)

trsnct_123.add_item("susu",10, 15_000)

trsnct_123.add_item("gula", 7, 20_000)

trsnct_123.check_keranjang()

**Output:**<br />

![image](https://github.com/Indriyani1507/project_kasir/blob/main/testing%201.jpeg)

 ## Test Case 2

**Input:**<br />
**mengubah nama belanja** 

trsnct_123.update_item_nama_belanja("susu", "kopi")

trsnct_123.check_keranjang()

**Output:**<br />

![image](https://github.com/Indriyani1507/project_kasir/blob/main/testing%202.jpeg)

**Input:**<br />
##  Test case 3
**mengubah/memperbarui nama belanja dengan string**

trsnct_123.update_item_nama_belanja("kopi", 15)

trsnct_123.check_keranjang()
**Output:**<br />

![image](https://github.com/Indriyani1507/project_kasir/blob/main/testing%203.jpeg)

**Input:**<br />
## Test case 4
**Mengubah/memperbarui jumlah belanja**

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
