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
```

Windows:

```sh
pip install tweepy
pip install -U scikit-learn
pip install pandas
pip install jupyter
```

## Usage example

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
      ubah semua ```uname = ['@jooshpn']``` isi variabel username menjadi username target   
   c. File ```clean1.ipynb``` bertujuan untuk membersihkan __special character__, __convert emoji__, dan __case folding__  
   d. Sementara ```clean2.ipynb``` bertujuan untuk membersihkan URL  
   e. Setelah 2 File tersebut selesai di run pindahkan file hasil ```username.csv``` ke folder __PbSC__   
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
