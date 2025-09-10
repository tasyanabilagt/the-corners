Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). 

-> Langkah pertama saya membuat repositori GitHub bernama **the-corners**, lalu membuat folder lokal yang dihubungkan ke repositori tersebut. Di dalam folder ini saya mengaktifkan virtual environment, menginstall Django, dan menjalankan **django-admin startproject** untuk membuat project utama. Setelah project berhasil dibuat, saya langsung mendeploy project ke **PWS (Pacil Web Service)** dan menambahkan URL deployment ke dalam ALLOWED_HOSTS di settings.py.

Selanjutnya saya membuat aplikasi baru bernama **main** dan menambahkannya ke **INSTALLED_APPS** pada **settings.py** agar terhubung dengan database. Pada aplikasi ini saya membuat model Product dengan field name, price, description, thumbnail, category, dan is_featured. Kategori produk saya batasi menjadi beberapa pilihan, seperti bola, sepatu, jersey, aksesoris, dan bundle. Setelah mendefinisikan model, saya menjalankan **python manage.py makemigrations** dan **python manage.py migrate** untuk menyimpan perubahan ke database.

Berikutnya, saya membuat fungsi **show_main** di **views.py** yang merender template **main.html**. Template ini menampilkan nama aplikasi, serta identitas diri saya (nama, NPM, dan kelas). Agar halaman ini bisa diakses, saya membuat file **urls.py** di dalam app main untuk memetakan path ke fungsi tersebut, lalu menambahkan routing di **urls.py** project utama. Dengan begitu, setiap request yang masuk ke URL tertentu bisa diarahkan ke view yang sesuai dan ditampilkan melalui template.

Untuk memastikan fungsionalitas berjalan dengan baik, saya menambahkan test.py yang digunakan untuk mengetes apakah URL bisa diakses, apakah view menggunakan template yang benar, apakah object **Product** dapat dibuat dengan atribut yang sesuai, serta apakah field default tersimpan dengan benar.

Setelah semua selesai dan aplikasi berjalan baik secara lokal maupun di PWS, saya melakukan **git add**, **git commit**, dan **git push** ke GitHub dan ke PWS agar project saya terdokumentasi dengan rapi.

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. 
![alt text](baganMVT.jpg)

Jelaskan peran settings.py dalam proyek Django!
-> setting.py dalam Django berperan sebagai pusat pengaturan project Django. File tersebut berisi seluruh pengaturan utama project, seperti  pengaturan database yang dipakai, daftar aplikasi yang aktif, lokasi template dan file lainnya yang bersifat statis. Selain itu terdapat keamanan berupa secret key, allowed host untuk membatasi akses, dan lain lain.

Bagaimana cara kerja migrasi database di Django?
-> migrasi dapat dilakukan dengan menjalani kode **makemigrations** dan Django akan membuat file migrasi yang berisi instruksi perubahan, seperti membuat tabel baru, menambah kolom, atau menghapus dan mengubah field pada model. File tersebut dapat dikatakan sebagai **blueprint** pada perubahan database. Selanjutnya Django akan membaca file migrasi tersebut ketika kode **migrate** dijalankan. Setelah dibaca, Django akan langung menerapkannya ke dalam database, sehingga struktur database dapat tetap sinkron dengan model yang telah diubah. Hal ini membuat setiap kali ada perubahan dalam **models.py** perlu dilakukan 2 langkah migrasi tersebut agar database dapat terupdate dengan baik.

Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
-> Menurut saya framework Django dapat dipilih sebagai permulaan pembelajaran karena menggunakan bahasa python yang sudah pernah dipelajari sebelumnya. Selain itu, framework ini juga terstruktur karena terdapat konsep MVT (Model, View, Template) yang mudah dipahami.

Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
-> Sejauh ini, saya tidak memiliki kendala dalam mengerjakan tutorial. Asisten dosen pun selalu stand by untuk membantu dan menjawab pertanyaan. Dokumen instruksi juga sangat jelas dan mudah dipahami.