# PANDUAN LENGKAP MEMBINA & MENYIARKAN PORTAL GOOGLE SITES DELIMa
**SMJK AVE MARIA CONVENT, IPOH, PERAK (AEB2052)**

Panduan ini disediakan khas untuk **Cik Au Chooi Yee** (Penolong Penyelaras DELIMa / Guru ICT) dan **Pn. Nurain Binti Md Nor** (Penyelaras DELIMa) bagi membina, mengemas kini dan menerbitkan Portal Rasmi DELIMa SMJK Ave Maria Convent di pelantar Google Sites KPM:
🌐 **Pautan Rasmi Laman:** [https://sites.google.com/moe-dl.edu.my/smjkamcipoh/](https://sites.google.com/moe-dl.edu.my/smjkamcipoh/)

---

## 📋 LANGKAH 1: LOG MASUK KE GOOGLE SITES KPM
1. Buka pelayar web (Google Chrome) dan pastikan anda log masuk menggunakan **ID Akaun DELIMa KPM rasmi** (`...@moe-dl.edu.my`).
2. Layari [https://sites.google.com/new](https://sites.google.com/new) atau akses melalui pautan tapak sedia ada sekolah [https://sites.google.com/moe-dl.edu.my/smjkamcipoh/](https://sites.google.com/moe-dl.edu.my/smjkamcipoh/).
3. Sekiranya membina tapak baharu, klik **Blank Site (+)**.

---

## 🎨 LANGKAH 2: TETAPAN TEMA & IDENTITI VISUAL (THEME)
Untuk memastikan laman anda mempunyai visual profesional yang selaras dengan tema DELIMa Merah/Crimson:

1. Di panel sebelah kanan, klik tab **Themes (Tema)** > Klik **+ Create Theme (Cipta Tema)**:
   - **Theme Name:** `DELIMa AMC Red`
   - **Logo:** Muat naik fail logo sekolah `AMC logo no BG (2).png` *(terdapat di folder `assets/images/logo.png`)*.
   - **Primary Color:** `#b71c1c` (Deep Crimson Red) atau `#d32f2f`.
   - **Secondary Color:** `#f8f9fa` (Light Neutral Gray).
   - **Fonts:**
     - **Titles / Headings:** `Oswald` (Bold / Semi-bold).
     - **Body Text:** `Open Sans` atau `Google Sans`.
2. Klik **Create Theme**.

---

## 📑 LANGKAH 3: STRUKTUR HALAMAN & SUB-HALAMAN (PAGES HIERARCHY)
Di tab **Pages (Halaman)** di panel kanan, bina struktur menu mengikut piawaian E-Fail DELIMa 2026:

```text
├── 🏠 UTAMA (Home)
│   ├── Jawatankuasa DELIMa
│   ├── Surat Menyurat & Pekeliling
│   ├── Carta Organisasi
│   ├── Perancangan Strategik (PSO)
│   ├── Laporan Aktiviti (OPR)
│   ├── Minit Mesyuarat
│   ├── Program & Takwim ICT
│   └── Jadual Makmal & Tempahan
├── 📊 PEMBUDAYAAN DELIMa
│   ├── Analisis Penggunaan Sekolah (Power BI)
│   └── Promosi & Latihan (LADAP)
├── 🎓 PENSIJILAN DELIMa GURU
│   ├── Direktori Pensijilan Guru (106 Guru AMC)
│   ├── Sijil & Poster GCE (Level 1 & 2)
│   └── Sijil Microsoft & Apple Teacher
├── 🏫 PENGURUSAN SEKOLAH
├── ⭐ KEISTIMEWAAN SEKOLAH
│   ├── Hub Keistimewaan Sekolah
│   ├── Inovasi AMC Smart Booking
│   ├── Kolaboratif & Jaringan Pintar
│   ├── Pencapaian & Anugerah SSQS
│   └── Sumbangan Ruang Ilmu & YouTube
├── 🚀 PORTAL & DASHBOARD
└── 🔑 ADUAN ID DELIMa
```

---

## 🧩 LANGKAH 4: CARA MENAMPAL WIDGET INTERAKTIF (COPY-PASTE EMBED)
Pakej ini telah menyediakan kod widget HTML siap pakai di dalam folder `google-sites-guide/embed-widgets/`. Anda hanya perlu salin dan tampal kod ke dalam Google Sites:

### Cara memasukkan Widget ke dalam Google Sites:
1. Di Google Sites, klik tab **Insert (Sisip)** > pilih **`< > Embed` (Sematkan)**.
2. Pilih tab **`Embed code` (Sematkan kod)**.
3. Buka fail widget yang diingini (cth: `widget-aduan-id.html`), salin semua kodnya (`Ctrl + A`, `Ctrl + C`), dan tampal (`Ctrl + V`) ke dalam kotak kod Google Sites.
4. Klik **Next** > **Insert**. Laraskan saiz kotak widget mengikut kesesuaian reka letak halaman.

### Senarai Widget Siap Pakai:
| Nama Fail Widget | Kegunaan di Google Sites | Lokasi Halaman Dicadangkan |
| :--- | :--- | :--- |
| `widget-aduan-id.html` | Borang aduan & reset kata laluan automatik dengan no. tiket | Halaman *Aduan ID DELIMa* / *Utama* |
| `widget-stats-counter.html` | Paparan kad skor KPI 5 Bintang & 100% Guru Bertauliah | Halaman *Utama* / *Pembudayaan* |
| `widget-quick-links.html` | Gerbang ikon pintas ke Classroom, Drive, Canva & Booking | Bahagian atas Halaman *Utama* |
| `widget-gce-badges.html` | Galeri lencana pencapaian GCE Lv1, Lv2, Gemini AI & Apple | Halaman *Pensijilan DELIMa Guru* |
| `widget-amc-smart-booking.html` | Kad seruan tindakan ke sistem tempahan bilik/makmal | Halaman *Jadual Penggunaan* / *Inovasi* |
| `widget-efail-navigator.html` | Grid navigasi pantas 6 Modul E-Fail ke Google Drive | Halaman *Utama* / *Pengurusan* |
| `widget-pencapaian-cards.html` | Galeri kad anugerah SSQS 5 Bintang & Ikon Digital | Halaman *Pencapaian & Anugerah* |

---

## 📂 LANGKAH 5: MENYAMBUNGKAN REPOSITORI GOOGLE DRIVE E-FAIL
Folder Google Drive evidens rasmi sekolah:
🔗 `https://drive.google.com/drive/folders/10HBSO2m-RKMAEJPsKmPmHZ1HU6zw4-y8?usp=sharing`

1. Untuk memaparkan folder Drive secara langsung dalam halaman:
   - Di tab **Insert**, klik **Drive**.
   - Pilih folder `1.0 PENGURUSAN` atau mana-mana subfolder yang ingin dipaparkan.
   - Tetapkan paparan sama ada dalam bentuk **Grid** atau **List (Senarai)**.
2. Pastikan tetapan perkongsian (Sharing Permission) folder di Google Drive diset kepada **"Anyone in Ministry of Education Malaysia with the link can view"** (atau *Public* jika laman boleh diakses ibu bapa).

---

## 🚀 LANGKAH 6: MENYIARKAN LAMAN (PUBLISH)
1. Di bucu atas kanan editor Google Sites, klik butang biru **Publish (Terbitkan)**.
2. **Web address:** Masukkan `smjkamcipoh` (menjadikan URL: `https://sites.google.com/moe-dl.edu.my/smjkamcipoh/`).
3. **Who can view my site:** 
   - Klik **Manage** > Tetapkan kepada **"Ministry of Education Malaysia"** (atau **"Public"** sekiranya ingin membolehkan murid/ibu bapa tanpa ID DELIMa melihat promosi).
4. Klik **Publish**.

🎉 **Tahniah! Portal DELIMa SMJK Ave Maria Convent, Ipoh kini siap sedia untuk semakan audit Penarafan Kendiri 5 Bintang KPM.**
