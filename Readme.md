Nama    : Nurul Izza Afkharinah
NIM     : 18219011
Tugas   : Autentifikasi FastAPI untuk operasi Create (Add Menu), Read (Read Menu), Update (Update Menu), dan Delete (Delete Menu)

Cara Compile di VSCode: 
1. Masuk menu Terminal > New Terminal
2. Pilih terminal 'wsl', pastikan direktori file yang dituju sudah benar
3. $ service venv/bin/activate
4. $ python main.py 
5. click link http://127.0.0.1:8000/docs

Deskripsi Singkat Tugas
Authentikasi FastAPI
    Diberikan menu autentikasi untuk user ketika ingin melakukan CRUD Menu. 
    User diharuskan melakukan login terlebih dahulu agar mendapat token yang digunakan untuk authorize.
    Di-set username dan password untuk login, yaitu untuk username = 'asdf' dan password == 'asdf'
    Apabila user tidak melakukan login terlebih dahulu, CRUD Menu akan gagal dan sistem akan menampilkan pesan 
        {
        "detail": "Not authenticated"
        }
    Step untuk login sebagai berikut:
        1. User memasukkan username dan password pada menu 'User Login'
        2. Ketika user berhasil melakukan login, sistem akan memberikan access token authorize
        3. Copy access token dan paste di menu 'Authorize' 
        4. User berhasil login apabila token benar, dan bisa mengakses CRUD Menu 

Update Menu Item
    Dilakukan update untuk tiap menu item yang terdapat di menu.json
    User perlu meng-input id item dan juga nama item yang ingin dilakukan pembaruan/update data
    Menu akan ter-update secara otomatis di menu.json ketika user selesai melakukan update

Delete Item from Menu
    Dilakukan delete untuk tiap menu item yang terdapat di menu.json
    User perlu meng-input id item yang ingin dihapus
    Menu (id dan nama) dengan id item tersebut akan terhapus secara otomatis, dan menu.json akan melakukan update data

Add New Menu Item
    Dilakukan penambahan menu item baru pada menu.json
    User hanya perlu meng-input nama item yang ingin ditambahkan, tidak perlu melakukan input id item karena id item bersifat increment
    Menu (id dan nama) akan bertambah secara otomatis di menu.json ketika user selesai menambahkan menu dan id menu akan otomatis terurut menaik (id+1)