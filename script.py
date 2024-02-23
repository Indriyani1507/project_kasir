# -*- coding: utf-8 -*-
"""Project Kasir.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f_SLWem8ehAryK89kz0bQiTPUN9rzb55
"""

from tabulate import tabulate

#membuat kelas Transaksi
class Transaction:

  #penginisialisasian method init
  def __init__ (self):
    """
    Membuat class Transaction untuk membuat transaksi belanja

    """
    #menginisialisasi list kosong untuk class Transaction
    self.keranjang = []

  #method untuk menambahkan item kedalam keranjang
  def add_item(self, nama_belanja, jumlah_belanja, harga_belanja):
    """
    Merupakan method untuk menambahkan item didalam keranjang.

    parameter :
    -----------

      nama_belanja : str
            merupakan nama belanja yang dimasukkan didalam keranjang.

      jumlah_belanja : int
            merupakan jumlah belanja yang dimasukkan ke dalam keranjang.

      harga_belanja : int
            merupakan harga satuan belanja yang akan dibeli.

    return :
    -------
        None

    """
    #mengecek data yang akan dimasukkan apakah sudah benar
    try:

      #membuat data dictionary untuk daftar belanja
      data = {"nama_belanja" : str(nama_belanja),
            "jumlah_belanja" : int(jumlah_belanja),
            "harga_belanja" : int(harga_belanja),
            "total_harga" : int(jumlah_belanja * harga_belanja)
              }

      #menginput data belanja ke dalam keranjang
      self.keranjang.append(data)

      #mengecek daftar belanja ke dalam keranjang
      self.check_keranjang

    #pesan eror apabila data tidak sesuai
    except TypeError:
      print("Type data tidak sesuai dengan keranjang")

  #method untuk memperbarui/mengganti salah satu nama belanja
  def update_item_nama_belanja(self, nama_belanja, nama_belanja_baru):

      """
      Merupakan method untuk memperbarui salah satu nama belanja lama dengan nama
      belanja baru.

      parameter :
      --------

        nama belanja : str
              nama belanja sebelum diupdate (nama belanja lama).
        nama belanja baru : str
              nama belanja yang sudah diupdate/diperbarui.

      return :
      -------
            None

      """

      #perulangan dalam pengupgrade an nama belanja
      for item in self.keranjang:

        #kondisi nama belanja sama dengan nama belanja
        if item ["nama_belanja"] == nama_belanja:

          #cek kondisi nama belanja baru harus berupa string
          if type(nama_belanja_baru) != str:

            #pesan error apabila Value yang dimasukkan bukan string
            raise ValueError("Nilai yang dimasukkan bukan string")

          #kondisi nama belanja menggunakan string
          else:
            item["nama_belanja"] = str(nama_belanja_baru)

  #method untuk memperbarui/mengganti salah satu jumlah belanja
  def update_item_jumlah_belanja(self, nama_belanja, jumlah_belanja_baru):

    """
    Merupakan method untuk mengupdate/memperbarui jumlah belanja dengan
    jumlah belanja baru.

    parameter :
    ------

      jumlah belanja : int
            jumlah belanja sebelum diupdate/diperbarui.

      jumlah belanja baru : int
            jumlah belanja yang sudah diupdate/diperbarui.

    return :
    ------
          None

    """
    #perulangan pengupdate an jumlah belanja
    for item in self.keranjang :

      #cek kondisi jumlah belanja sama
      if item ["nama_belanja"] == nama_belanja:

        #jumlah belanja sama dengan jumlah belanja baru
        item ["jumlah_belanja"] = jumlah_belanja_baru

        #cek kondisi jumlah belanja adalah integer
        if type(jumlah_belanja_baru) != int:

          #pesan eror yang akan ditampilkan apabila value yang dimasukkan bukan integer
          raise ValueError("Nilai yag dimasukkan bukan integer dan tidak sesuai")

        #total harga merupakan hasil dari jumlah * harga
        item ["total_harga"] = jumlah_belanja_baru * item["harga_belanja"]

  #method untuk memperbarui/mengubah harga belanja
  def update_item_harga_belanja(self, nama_belanja, harga_belanja_baru):

    """
    Merupakan method untuk mengupdate/memperbarui harga belanja dengan
    harga belanja baru.

    parameter :
    ------

      harga belanja : int
            harga belanja sebelum diupdate/diperbarui.

      harga belanja baru : int
            harga belanja yang sudah diupdate/diperbarui.

    return :
    ------
          None

    """

    #perulangan dalam pengupgrade an harga belanja
    for item in self.keranjang:

      #cek kondisi harga belanja sam dengan harga belanja
      if item ["nama_belanja"] == nama_belanja:

        #harga belanja merupakan harga belanja baru yang sudah mengalami pengupgrade an
        item ["harga_belanja"] = harga_belanja_baru

        #cek kondisi harga belanja adalah integer
        if type(harga_belanja_baru)!= int:

          #pesan eror yang akan ditampilkan apabila value yang dimasukkan bukan integer
          raise ValueError ("Nilai yang dimasukkan bukan integer dan tidak sesuai")

        #total harga merupakan jumlah belanja dikalikan harga belanja baru
        item["total_harga"] = item["jumlah_belanja"] * harga_belanja_baru


  #mwthod untuk menghapus daftar belanja dalam keranjang
  def delete_item(self, nama_belanja):

    """
    Merupakan method untuk menghapus daftar belanja yang sudah dimasukkan
    kedalam keranjang.

    parameter :
    -------
      nama belanja : str
            nama belanja yang akan dihapus.

      return :
    -------
    None

    """

    #perulangan pada penghapusan daftar belanja
    for item in self.keranjang:

      #cek kondisi nama belanja yang akan dihapus
      if item["nama_belanja"] == nama_belanja:

        #menghapus daftar belanja yang dipilih
        self.keranjang.remove(item)

  #method untuk menghapus semua daftar belanja dalam keranjang
  def reset_keranjang(self):

      """
      Merupakan method untuk mereset daftar belanja dalam keranjang.
      Mengembalikan keranjang dengan keadaan kosong.

      parameter :
      -----
          reset = 0

      return :
      -----
        None

      """
      #perulangan untuk menghapus semua daftar belanja dalam keranjang
      for item in self.keranjang:

        #perintah untuk menghapus semua daftar belanja keranjang
        self.keranjang.clear()

        #menampilkan pesan keranjang belanja berhasil direset
        print("Transaksi dibatalkan, daftar belanja berhasil dihapus")

  #method untuk menghitung isi keranjang
  def check_keranjang(self):
      """
      Merupakan method untuk menghitung isi keranjang.

      """
      #membuat header pada tabel daftar keranjang
      headers = ["Nama Belanja", "Jumlah Belanja", "Harga Belanja", "Total Belanja"]

      #membuat isi pada tabel daftar keranjang
      rows = [[item["nama_belanja"], item["jumlah_belanja"], item["harga_belanja"],
            item["total_harga"]] for item in self.keranjang]

      #menampilkan  isi daftar keranjang kedalam bentuk tabel
      print(tabulate(rows, headers = headers, tablefmt = "grid"))

  #method untuk menghitung total belanja dari daftar keranjang
  def total_price(self):

      """
      Merupakan method untuk menghitung total semua belanja.

      """
      #melakukan perkalian jumlah belanja * harga belanja
      total_price = sum(item["jumlah_belanja"] * item["harga_belanja"] for item in self.keranjang)

      #cek kondisi total belanja lebih dari Rp. 200.000
      if total_price > 200_000:

        #menghitung total belanja dengan mendapatkan diskon 5%
        total_bayar = total_price - (total_price * 0.05)

        #menampilkan pesan bahwa mendapatkan diskon 5%
        print(f"Selamat Anda mendapatkan diskon 5%, dengan total belanjaan {total_bayar}")

      #cek kondisi total belanja lebih dari Rp. 300.000
      elif total_price > 300_000:

        #menghitung total belanja dengan mendapatkan diskon 8%
        total_bayar = total_price - (total_price * 0.08)

        #menampilkann pesan bahwa mendapatkan diskon 8%
        print(f"Selamat Anda mendapatkan diskon 8%, dengan total belanjaan {total_bayar}")

      #cek kondisi total belanja lebih dari Rp. 500.000
      elif total_price > 500_000:

        #menghitung total belanja dengan mendapatkan diskon 10%
        total_bayar = total_price - (total_price * 0.1)

        #menampilakn pesan bahwa mendapatkan diskon 10%
        print(f"Selamat Anda mendapatkan diskon 10%, dengan total belanjaan {total_bayar}")

      #kondisi jika tidak mendapatkan diskon, total bayar = total belanja
      else :
        total_bayar = total_price