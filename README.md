# Personality-Prediction-Using-PbSC

> Berisi 4 Folder untuk melakukan klasifikasi kepribadian dengan menggunakan metode PbSC.

Aplikasi terdiri dari 4 folder dimana setiap folder memiliki fungsinya masing-masing.
1. Crawl, Bertujuan untuk mengumpulkan tweet dari masing-masing user
2. Preprocessing, Bertujuan untuk membersihkan hasil tweet yang sudah di crawl
3. PbSC, Bertujuan untuk melakukan klasifikasi kepribadian user berdasarkan hasil tweet
4. GUI, Folder tambahan berisi keseluruhan aplikasi yang dibuat versi GUI nya.

## Library Installation

Mac OS:

```sh
$ pip install tweepy
$ pip install -U scikit-learn
$ pip install pandas
$ pip install jupyter
$ pip install csv
$ pip install numpy
$ pip install nltk
$ pip install textblob
```

Windows:

```sh
pip install tweepy
pip install -U scikit-learn
pip install pandas
pip install jupyter
pip install csv
pip install numpy
pip install nltk
pip install textblob
```

## Usage example (Alur Program)

1. Download/Clone semua file yang ada dalam repositori ini  

2. Buka Folder __Crawl__  
   a. Buka file .ipynb lewat jupyter notebook    
   b. Pada blok ke 4 terdapat code  
   ```sh
   if __name__ == '__main__':
      username = ['@jooshpn']  # masukkan username target
      for uname in username:
         get_tweets(uname)
   ```
   Ubah username target username kalian    
   ```
      username = ['@jooshpn'] 
   ``` 
   c. Run Semua blok dari awal sampai akhir  
   d. Setelah selesai di run maka akan didapatkan file result ```username.csv```  
   e. Copy file tersebut dan paste ke Folder __Preprocessing__  
   
3. Buka Folder __Preprocessing__  
   a. Didalam folder terdapat file ```clean1.ipynb``` dan ```clean2.ipynb```  
   b. Buka file tersebut secara berurutan mulai dari ```clean1.ipynb``` terlebih dahulu   
   c. Ubah semua ```uname = ['@jooshpn']``` isi variabel username menjadi username target yg sebelumnya anda isi pada folder __Crawl__   
   c. File ```clean1.ipynb``` bertujuan untuk membersihkan __special character__, __convert emoji__, dan __case folding__  
   d. Sementara ```clean2.ipynb``` bertujuan untuk membersihkan URL  
   e. Setelah 2 File tersebut selesai di run pindahkan file hasil ```username.csv``` ke folder __PbSC__  
   
4. Buka Folder __PbSC__  
   a. Didalam Folder terdapat file ```pbsc_ruled_based.ipynb```  
   b. Buka folder dan jangan lupa ganti ```uname = ['@jooshpn']``` menjadi username target yang sebelumnya anda isi.  
   c. Run Program dari awal sampai akhir untuk melihat hasil klasifikasi.  
   
5. GUI APPS  
   Folder __GUI__ Berisi aplikasi PbSC yang sudah dibuatkan versi GUInya agar user bisa langsung berinteraksi dengan program.  
   
   a. Buka Folder __GUI__ dan didalamnya terdapat file ```main.py```  
   b. Jalankan file ```main.py``` dan anda sudah bisa berinteraksi dengan __Sistem Klasifikasi Kepribadian berbasis Twitter dengan Algoritma PbSC__    
      ```sh
      python3 main.py #buka lewat CMD
      ```
   c. Sistem yang berjalan sudah melewati proses __crawling__, __preprocessing__ dan __klasifikasi__ yang sudah anda coba sebelumnya dalam __Alur 1-4__
   
   
## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
