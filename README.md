# Tugas 2

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). 

-> Langkah pertama saya membuat repositori GitHub bernama **the-corners**, lalu membuat folder lokal yang dihubungkan ke repositori tersebut. Di dalam folder ini saya mengaktifkan virtual environment, menginstall Django, dan menjalankan **django-admin startproject** untuk membuat project utama. Setelah project berhasil dibuat, saya langsung mendeploy project ke **PWS (Pacil Web Service)** dan menambahkan URL deployment ke dalam ALLOWED_HOSTS di settings.py.

Selanjutnya saya membuat aplikasi baru bernama **main** dan menambahkannya ke **INSTALLED_APPS** pada **settings.py** agar terhubung dengan database. Pada aplikasi ini saya membuat model Product dengan field name, price, description, thumbnail, category, dan is_featured. Kategori produk saya batasi menjadi beberapa pilihan, seperti bola, sepatu, jersey, aksesoris, dan bundle. Setelah mendefinisikan model, saya menjalankan **python manage.py makemigrations** dan **python manage.py migrate** untuk menyimpan perubahan ke database.

Berikutnya, saya membuat fungsi **show_main** di **views.py** yang merender template **main.html**. Template ini menampilkan nama aplikasi, serta identitas diri saya (nama, NPM, dan kelas). Agar halaman ini bisa diakses, saya membuat file **urls.py** di dalam app main untuk memetakan path ke fungsi tersebut, lalu menambahkan routing di **urls.py** project utama. Dengan begitu, setiap request yang masuk ke URL tertentu bisa diarahkan ke view yang sesuai dan ditampilkan melalui template.

Untuk memastikan fungsionalitas berjalan dengan baik, saya menambahkan test.py yang digunakan untuk mengetes apakah URL bisa diakses, apakah view menggunakan template yang benar, apakah object **Product** dapat dibuat dengan atribut yang sesuai, serta apakah field default tersimpan dengan benar.

Setelah semua selesai dan aplikasi berjalan baik secara lokal maupun di PWS, saya melakukan **git add**, **git commit**, dan **git push** ke GitHub dan ke PWS agar project saya terdokumentasi dengan rapi.

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. 
![alt text](baganMVT.jpg)

### Jelaskan peran settings.py dalam proyek Django!
-> setting.py dalam Django berperan sebagai pusat pengaturan project Django. File tersebut berisi seluruh pengaturan utama project, seperti  pengaturan database yang dipakai, daftar aplikasi yang aktif, lokasi template dan file lainnya yang bersifat statis. Selain itu terdapat keamanan berupa secret key, allowed host untuk membatasi akses, dan lain lain.

### Bagaimana cara kerja migrasi database di Django?
-> migrasi dapat dilakukan dengan menjalani kode **makemigrations** dan Django akan membuat file migrasi yang berisi instruksi perubahan, seperti membuat tabel baru, menambah kolom, atau menghapus dan mengubah field pada model. File tersebut dapat dikatakan sebagai **blueprint** pada perubahan database. Selanjutnya Django akan membaca file migrasi tersebut ketika kode **migrate** dijalankan. Setelah dibaca, Django akan langung menerapkannya ke dalam database, sehingga struktur database dapat tetap sinkron dengan model yang telah diubah. Hal ini membuat setiap kali ada perubahan dalam **models.py** perlu dilakukan 2 langkah migrasi tersebut agar database dapat terupdate dengan baik.

### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
-> Menurut saya framework Django dapat dipilih sebagai permulaan pembelajaran karena menggunakan bahasa python yang sudah pernah dipelajari sebelumnya. Selain itu, framework ini juga terstruktur karena terdapat konsep MVT (Model, View, Template) yang mudah dipahami.

### Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
-> Sejauh ini, saya tidak memiliki kendala dalam mengerjakan tutorial. Asisten dosen pun selalu stand by untuk membantu dan menjawab pertanyaan. Dokumen instruksi juga sangat jelas dan mudah dipahami.

# Tugas 3
### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
-> Data delivery diperlukan agar aplikasi yang dibuat bersifat dinamis. Server bertugas untuk mengirimkan data ke client agar pengguna dapat melihat informasi yang selalu diperbarui. Selain itu, client juga dapat mengirimkan data input dari user ke server untuk disimpan atau diproses. Jika tidak ada data delivery, maka aplikasi hanya menampilkan konten statis yang tidak dapat diubah sesuai kebutuhan pengguna. 

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
-> Menurut saya, JSON lebih baik dibanding XML karena tampilan JSON lebih sederhana, ringkas, mudah dibaca karena menggunakan key dan value. JSON juga terintegrasi langsung JavaScript sehingga sangat mendukung pengembangan aplikasi web modern. XML sintaksnya cenderung lebih panjang dan sulit dibaca, sehingga penggunaannya semakin jarang, hal itu yang menyebabkan JSON lebih populer dibanding XML

### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
-> Method is_valid() berguna untuk memvalidasi data yang dikirimkan melalui form. Django secara otomatis akan memeriksa apakah data tersebut sudah sesuai dengan aturan yang telah ditetapkan. Contohnya seperti terdapat beberapa field yang sifatnya wajib diisi, ada batasan karakter untuk beberapa atau semua field, dan sebagainya. Jika ada data yang tidak sesuai dengan aturan, form akan menampilkan pesan error. Method ini tentunya sangat penting untuk digunakan karena bisa mencegah input data yang tidak sesuai ke dalam database.


### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
-> csrf_token merupakan salah satu fitur keamanan Django untuk mencegah serangan CSRF (Cross-Site Request Forgery). Token tersebut memastikan bahwa data form benar-benar dikirim dari website kita sendiri, bukan dari website lain. Apabila tidak menggunakan csrf_token, orang lain dapat membuat form palsu diluar website yang kita buat dan mengirimkan request berbahaya bagi user yang mengaksesnya.

###  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Langkah pertama yang saya lakukan adalah membuat file base.html sebagai template dasar yang berisi struktur utama halaman web. base.html tersebut saya tambahkan ke dalam list templates agar Django dapat mengenali semua file html yang ada di dalamnya, sehingga tampilan menjadi lebih konsisten karena memiliki layout atau tampilan dasar yang sudah ditetapkan.

Selanjutnya, saya membuat file forms.py yang berisi ProductForm sebagai form yang menerima input data produk baru. Form tersebut diimport ke dalam views.py dan digunakan pada fungsi create_product untuk menampilkan form serta menyimpan data produk baru ke database. Selanjutnya, membuat fungsi untuk menampilkan detail produk yang terdaftar.

Untuk menampilkan data dalam format lain, saya menambahkan 4 fungsi, yaitu show_xml dan show_json yang berfungsi untuk menampilkan keseluruhan data produk serta show_xml_by_id dan show_json_by_id yang berfungsi untuk menampilkan data salah satu produk berdasarkan id nya.

Agar fungsi tersebut dapat diakses, saya menambahkan routing baru pada urls.py dan membuat button dalam main.html dengan label "Add Product" dan ketika diklik akan redirect ke form untuk menambahkan produk. Saya juga membuat dua file template baru yaitu create_product.html dan product_detail.html untuk menampilkan detail produk tertentu. Selain itu, saya juga menambahkan URL deployment ke dalam CSRF_TRUSTED_ORIGINS di settings.py agar form dapat berjalan dengan baik pada saat project sedang dijalankan di PWS. Dengan melakukan konfigurasi tersebut, request yang dikirim melalui form tetap dianggap aman oleh Django.

### Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

### Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
XML
![alt text](<Screenshot 2025-09-17 004140.png>)
JSON
![alt text](<Screenshot 2025-09-17 004200.png>)
XML by id product
![alt text](<Screenshot 2025-09-17 004217.png>) 
JSON by id product
![alt text](<Screenshot 2025-09-17 004236.png>)

# Tugas 4
### Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
-> Django AuthenticationForm adalah form bawaan yang disediakan oleh Django untuk autentikasi pengguna saat proses login. Biasanya form ini akan mengecek username dan password pengguna untuk menentukan apakah user tersebut valid atau tidak. Kelebihan dari AuthenticationForm diantaranya adalah mudah untuk digunakan karena sudah terintegrasi oleh Django, memvalidasi user yang melakukan login secara otomatis, dan juga aman. Namun, juga terdapat kekurangan yaitu field yang divalidasi oleh sistem terbatas, hanya username dan password. Apabila ingin melakukan validasi terhadap field lain seperti email, maka harus melakukan override.

### Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
-> Autentikasi adalah proses untuk memverifikasi apakah user yang login valid atau tidak di database. Autentikasi hanya sebatas mengecek identitas dari user itu sendiri. Setelah berhasil login, artinya user memiliki hak akses yang sama terhadap website. Sementara itu, otorisasi adalah proses untuk menentukan hak akses atau izin yang dimiliki oleh user setelah identitasnya dinyatakan valid. Misalnya user A sudah berhasil melewati proses autentikasi, lalu user A akan melewati proses otorisasi dan mendapat role atau hak akses sebagai admin yang dapat menghapus atau menambahkan produk. Ketika user lain mendapat role sebagai buyer, maka hak aksesnya akan berbeda dengan admin. Buyer tidak akan bisa menambahkan atau menghapus produk yang ada. Django mengimplementasikan autentikasi melalui sistem login dan logout dan model User. Sementara itu, otorisasi dijalankan dengan permission, decorator seperti **@login_required** (konten hanya dapat diakses oleh user yang sudah login/melakukan autentikasi), dan atribut seperti **is_staff** (admin yang memiliki akses terbatas) atau **is_superuser** (admin yang memiliki akses penuh)


### Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Dalam menyimpan state aplikasi berbasis web, cookies dan sessions digunakan dengan cara yang berbeda. Cookies akan menyimpan data secara langsung dari client atau browser, cara yang digunakan cukup sederhana dan penggunaannya bisa dalam jangka waktu yang lama. Namun, cookies memiliki keterbatasan ukuran dan rawan untuk dimodifikasi oleh pengguna. Hal ini berbahaya karena cookies harus unik untuk setiap pengguna, jika bisa dimodifikasi tidak menutup kemungkinan adanya pengguna yang mengakses website dengan cookies pengguna lain. Jadi cookies lebih berisiko di sisi keamanan. Sementara itu, sessions dapat dibilang lebih aman karena data sessions yang sebenarnya tersimpan di dalam server, sementara client hanya menyimpan session ID yang ada di dalam cookie. Artinya pengguna tidak dapat mengubah data session jadi keamanannya lebih terjaga. Namun, karena data disimpan pada server, maka server membutuhkan lebih banyak resource untuk menyimpan dan mengelola sessions.

### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Penggunaan cookies tidak sepenuhnya aman karena bisa saja dicuri oleh oknum tidak bertanggungjawab melalui serangan seperti XSS dan lainnya. Django menyediakan banyak opsi mekanisme keamanan untuk mengatasi hal tersebut. Salah satunya adalah cookie sessions disediakan secara kriptografis agar tidak dapat diubah sembarangan oleh pengguna. Selain itu, terdapat pengaturan seperti SESSION_COOKIE_HTTPONLY agar cookie tidak bisa diakses lewat JavaScript dan SESSION_COOKIE_SECURE agar cookie hanya dikirim melalui HTTPS.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Langkah pertama yang saya lakukan adalah menambahkan **fungsi registrasi, login, dan logout**. Untuk mengimplementasikan ketiga fungsi tersebut, saya membuat **forms.py** di dalam direktori main. Form tersebut merupakan form registrasi dengan memanfaatkan form bawaan Django untuk melakukan validasi username dan password (autentikasi). Jika valid, pengguna berhasil login. Saya juga menambahkan cookie untuk last_login agar waktu terakhir pengguna login dapat terlihat dan menambahkan informasi username yang sedang login di halaman utama. Saat pengguna logout, informasi sesi login akan dihapus dengan menggunakan fungsi logout.

Selanjutnya, saya menghubungkan model **Product** dengan **User** menggunakan **ForeignKey** yang nantinya setiap produk yang ditambahkan akan terhubung dengan suatu akun. Saya juga telah menambahkan 2 akun yang masing masing memiliki 3 produk dummy untuk memastikan fungsi berjalan dengan benar. Ketika user membuat sebuah produk, username nya akan ditampilkan sebagai seller di informasi detail produk.

di **main.html** saya menambahkan tampilan untuk sesi terakhir login dan juga username pengguna yang sedang login. Setelah semua fitur selesai diimplementasikan, saya melakukan pengecekan ulang untuk menghindari adanya error saat proses registrasi, login, logout, set cookie. Saya juga mengecek data melalui Django admin dengan mendaftarkan akun sebagai superuser. Terakhir, saya melakukan git add, git commit, dan git push ke GitHub dan PWS.

# Tugas 5
### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
-> Dalam CSS, ketika terdapat beberapa selector yang mengatur elemen yang sama, browser akan memilih aturan dengan prioritas tertinggi. Urutannya dimulai dari inline style yang langsung ditulis pada elemen HTML, lalu diikuti oleh ID selector, class selector (termasuk pseudo-class dan attribute selector), kemudian element selector (seperti div, p, dan pseudo-element). Jika ada dua aturan dengan tingkat prioritas yang sama, maka aturan yang ditulis paling terakhir di file CSS yang akan diterapkan. Hal ini disebut dengan specificity dan sangat penting dipahami agar style yang dibuat tidak saling bertabrakan.

### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
-> Responsive design menjadi konsep yang sangat penting dalam pengembangan aplikasi web karena memastikan tampilan aplikasi dapat menyesuaikan diri dengan berbagai ukuran layar, mulai dari desktop, tablet, hingga smartphone. Tanpa responsive design, website hanya akan terlihat bagus di satu jenis perangkat dan menyulitkan pengguna pada perangkat lain. Contohnya, Tokopedia sudah menerapkan desain yang responsive dengan menampilkan grid produk yang otomatis berubah menjadi 2 kolom di layar kecil, sementara website lama atau forum jadul seringkali belum mendukung responsive design sehingga pengguna harus melakukan zoom in dan out untuk membaca konten.

### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
-> Dalam CSS terdapat tiga komponen utama pada box model yaitu margin, border, dan padding. Margin adalah jarak di luar elemen yang berfungsi memberi spasi antar elemen. Border adalah garis tepi yang mengelilingi elemen, dapat diberi warna maupun ketebalan sesuai kebutuhan. Sementara itu, padding adalah jarak di dalam border yang memisahkan konten dengan tepi elemen. Ketiganya sering dipakai bersamaan untuk mengatur tata letak halaman web agar lebih rapi dan enak dilihat.

### Jelaskan konsep flex box dan grid layout beserta kegunaannya!
-> Pengaturan layout pada web modern seringkali menggunakan flexbox dan grid layout. Flexbox digunakan untuk menyusun elemen dalam satu dimensi, misalnya membuat navbar dengan item sejajar atau menyusun tombol dalam satu baris. Sementara itu, grid layout digunakan untuk menyusun elemen dalam dua dimensi, seperti membuat galeri atau daftar produk dalam baris dan kolom. Flexbox lebih cocok untuk layout linear, sedangkan grid lebih kuat untuk desain yang kompleks dan terstruktur.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
-> Dalam mengimplementasikan checklist pada tugas ini, saya memulai dengan menambahkan fungsi edit dan delete product di views.py. Template baru seperti edit_product.html saya buat untuk menampilkan form edit, sementara di main.html saya menambahkan tombol Edit dan Delete pada setiap card produk. Routing kedua fungsi tersebut saya definisikan pada urls.py agar bisa diakses dari halaman utama. Setelah itu, saya melakukan kustomisasi desain menggunakan Tailwind CSS yang saya hubungkan melalui base.html. Kustomisasi dilakukan pada halaman login, register, create product, edit product, dan detail product agar tampak lebih menarik dan konsisten. Pada halaman daftar produk, saya menambahkan kondisi: jika belum ada produk maka ditampilkan ilustrasi dan pesan kosong, sedangkan jika sudah ada maka produk ditampilkan dalam bentuk card lengkap dengan tombol aksi. Selanjutnya, saya menambahkan navbar yang responsive menggunakan Tailwind. Pada layar desktop navbar menampilkan menu penuh, sementara di mobile navbar berubah menjadi hamburger button. Untuk melengkapi tampilan, saya juga menambahkan styling tambahan di global.css yang mengatur input form, tombol, dan card produk agar lebih rapi. Setelah seluruh fitur selesai, saya melakukan pengujian baik di local server maupun di PWS untuk memastikan tampilan berjalan dengan baik di berbagai perangkat. Terakhir, saya melakukan git add, git commit, dan git push ke GitHub serta PWS untuk mendokumentasikan hasil pekerjaan dengan rapi.

# Tugas 5
### Apa perbedaan antara synchronous request dan asynchronous request?
-> Pada synchronous request (metode tradisional) berarti browser perlu menunggu respons sebelum bisa melakukan hal lain. Biasanya halaman akan reload penuh atau berpindah halaman saat user melakukan submit form. Sementara itu, asynchronous request (AJAX/fetch) akan mengirim permintaan di belakang layar tanpa me-reload halaman. Hasilnya bisa langsung dipakai untuk mengubah sebagian DOM (misal hanya daftar produk atau pesan error form) sehingga tampilan terasa lebih cepat dan interaktif.

### Bagaimana AJAX bekerja di Django (alur request–response)?
-> Secara garis besar alur kerja AJAX adalah sebagai berikut:
Ketika user melakukan aksi pada browser, seperti menekan tombol, submit form, scrolling, dsb yang biasa disebut event pada browser. Setelah terjadi event, front-end akan mengirimkan request async. JavaScript (misalnya fetch()) akan mengirimkan HTTP request biasanya POST/GET ke endpoint Django. Ketika user melakukan request yang perlu mengubah data, CSRF token harus disertakan. Path request akan dicocokan ke view yang sesuai pada urls.py. Apabila path valid, maka view akan memproses data (validasi form, query ke models.py, dan logika fungsi lainnya), lalu views.py akan mengembalikan JSON menggunakan JsonResponse atau HTML fragment. Response akan dikirimkan ke browser dan JavaScript akan membaca response lalu mengubah DOM (misal menambahkan card product baru) tanpa reload page. Saat melakukan proses bisa juga menampilkan loading state, notifikasi sukses/error, reset form, dsb. Hubungan MVT nya dari mulai urls.py -> views.py -> models.py -> JsonResponse dan kembali ke JavaScript -> update template/DOM di client/browser.

### Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
-> Keuntungan yang langsung terasa adalah tanpa reload penuh, jadi waktu tanggap lebih cepat dan perceived performance meningkat. Validasi dan pesan error bisa tampil inline di dekat field, sehingga alur pengisian form jadi lebih nyaman. Dari sisi efisiensi, yang dikirim cukup data penting (misalnya JSON) sehingga hemat bandwidth dibanding memuat ulang seluruh HTML/CSS/JS. Di atas itu, AJAX memudahkan fitur interaktif seperti live search, filter dinamis, infinite scroll, dan update sebagian konten. Sementara bagian server tetap rapi di Django, presentasi dan interaksi dipegang JavaScript, sehingga pemisahan concern lebih jelas.

### Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
-> Untuk endpoint autentikasi, saya memastikan beberapa hal penting berjalan bersamaan. Pertama, selalu memakai HTTPS agar kredensial terenkripsi saat transit. Kedua, proteksi CSRF wajib aktif untuk semua POST (sertakan token di header X-CSRFToken, jangan gunakan @csrf_exempt pada login/register, dan pastikan CSRF_TRUSTED_ORIGINS benar saat deploy). Ketiga, validasi tetap dikerjakan server-side dengan form bawaan Django seperti AuthenticationForm/UserCreationForm (otomatis pakai password hashing dan aturan validasi), sehingga keamanan tidak bergantung pada validasi client. Keempat, saya membatasi metode (kredensial dikirim via POST, bukan GET) dan menyesuaikan Content-Type yang diharapkan. Kelima, saya mengamankan cookie sesi dengan SESSION_COOKIE_SECURE = True, SESSION_COOKIE_HTTPONLY = True, serta CSRF_COOKIE_SECURE = True, dan mendorong session rotation saat login untuk mencegah session fixation. Jika dibutuhkan, saya menambahkan rate limiting/lockout untuk meredam brute force. Terakhir, pesan error dibuat cukup informatif namun tidak membocorkan detail (misal “Username atau password salah”) dan CORS tidak dibuka ke domain yang tidak perlu agar same-origin policy tetap melindungi endpoint autentikasi.

### Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
-> Dari sisi UX, AJAX membuat interaksi terasa lebih responsif karena pengguna tidak lagi menunggu reload halaman penuh pada setiap aksi kecil. Konteks halaman tetap terjaga (posisi scroll, fokus elemen, dan state UI tidak hilang), sehingga alur tugas pengguna tidak terputus. Feedback instan seperti spinner/loading kecil, notifikasi sukses, dan error validasi langsung di tempat membantu pengguna memahami apa yang sedang terjadi. Fitur modern seperti autocomplete, live filter, dan load more juga jadi mudah diterapkan. Dengan pengelolaan error dan aksesibilitas yang baik (misalnya penggunaan aria-live untuk pembaca layar), AJAX berujung pada pengalaman yang lebih mulus, cepat, dan ramah bagi pengguna.