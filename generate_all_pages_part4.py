# -*- coding: utf-8 -*-
"""
Part 4 of DELIMa Page Generator
SMJK Ave Maria Convent, Ipoh (AEB2052)
"""

import os
import json

DRIVE_URL = "https://drive.google.com/drive/folders/10HBSO2m-RKMAEJPsKmPmHZ1HU6zw4-y8?usp=sharing"
SMART_BOOKING_URL = "https://sites.google.com/moe-dl.edu.my/amc-smart-booking-ver1/laman-utama"

from generate_pages import wrap_html
from generate_all_pages import get_breadcrumbs

# ------------------------------------------------------------------------------
# 15. KEISTIMEWAAN SEKOLAH (pages/keistimewaan.html)
# ------------------------------------------------------------------------------
keistimewaan_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Keistimewaan Sekolah", "6.0 Keistimewaan", "keistimewaan.html")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fas fa-gem"></i> 6.0 Keistimewaan Sekolah (Niche Pendigitalan)</h2>
            <p>Amalan Terbaik, Projek Inovasi, Jaringan Kolaboratif & Sumbangan Pendidik SMJK Ave Maria Convent, Ipoh</p>
        </div>
        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
            <i class="fab fa-google-drive"></i> Folder E-Fail 6.0
        </a>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-star"></i> 5 Tonggak Keistimewaan Digital SMJK AMC</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-top: 14px;">
            <div style="background: #ffffff; border: 1px solid var(--border-color); border-radius: 8px; padding: 16px;">
                <h4 style="color: var(--primary); margin-top: 0;"><i class="fas fa-lightbulb"></i> 6.1 Inovasi AMC Smart Booking</h4>
                <p style="font-size: 13px; color: var(--text-muted);">Sistem tempahan bilik khas, makmal komputer dan peranti digital tanpa kertas yang menghubungkan Google Sites dan Google Calendar.</p>
                <a href="inovasi.html" class="btn-card btn-card-primary">Ketahui Lebih Lanjut</a>
            </div>

            <div style="background: #ffffff; border: 1px solid var(--border-color); border-radius: 8px; padding: 16px;">
                <h4 style="color: var(--primary); margin-top: 0;"><i class="fas fa-handshake"></i> 6.2 Jaringan & Jalinan Kolaboratif</h4>
                <p style="font-size: 13px; color: var(--text-muted);">Kerjasama pintar bersama agensi luar seperti MDEC, Digi CyberSAFE, Bengkel Sukarelawan ICT (MIV) & program antarabangsa.</p>
                <a href="kolaboratif.html" class="btn-card btn-card-primary">Ketahui Lebih Lanjut</a>
            </div>

            <div style="background: #ffffff; border: 1px solid var(--border-color); border-radius: 8px; padding: 16px;">
                <h4 style="color: var(--primary); margin-top: 0;"><i class="fas fa-trophy"></i> 6.3 Pencapaian & Anugerah</h4>
                <p style="font-size: 13px; color: var(--text-muted);">Penarafan 5 Bintang SSQS KPM, Pengiktirafan Penarafan Kendiri 5 Bintang DELIMa dan anugerah guru digital cemerlang.</p>
                <a href="pencapaian.html" class="btn-card btn-card-primary">Ketahui Lebih Lanjut</a>
            </div>

            <div style="background: #ffffff; border: 1px solid var(--border-color); border-radius: 8px; padding: 16px;">
                <h4 style="color: var(--primary); margin-top: 0;"><i class="fas fa-share-alt"></i> 6.4 Sumbangan Ruang Ilmu KPM</h4>
                <p style="font-size: 13px; color: var(--text-muted);">Penerbitan modul PdP guru dan saluran video pendidikan YouTube untuk manfaat para pendidik seluruh Malaysia.</p>
                <a href="sumbangan-pdp.html" class="btn-card btn-card-primary">Ketahui Lebih Lanjut</a>
            </div>
        </div>
    </div>
</main>
"""
with open('pages/keistimewaan.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Keistimewaan Sekolah", keistimewaan_body, depth=1, active='keistimewaan'))

# ------------------------------------------------------------------------------
# 16. INOVASI (pages/inovasi.html)
# ------------------------------------------------------------------------------
inovasi_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Inovasi AMC Smart Booking", "6.0 Keistimewaan", "keistimewaan.html")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fas fa-lightbulb"></i> Projek Inovasi Digital: AMC Smart Booking</h2>
            <p>Portal Tempahan Kemudahan Digital & Bilik Khas Bersepadu SMJK Ave Maria Convent, Ipoh</p>
        </div>
        <a href="{SMART_BOOKING_URL}" target="_blank" class="btn-card btn-card-primary">
            <i class="fas fa-external-link-alt"></i> Buka Portal Inovasi
        </a>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-info-circle"></i> Ringkasan Projek Inovasi</h3>
        <table class="delima-table">
            <tbody>
                <tr>
                    <td style="width: 25%; font-weight: 700; background: #f8f9fa;">Tajuk Inovasi</td>
                    <td><strong>AMC SMART BOOKING (Portal Tempahan Kemudahan Digital Sekolah)</strong></td>
                </tr>
                <tr>
                    <td style="font-weight: 700; background: #f8f9fa;">Pautan Portal Rasmi</td>
                    <td><a href="{SMART_BOOKING_URL}" target="_blank"><code>{SMART_BOOKING_URL}</code></a></td>
                </tr>
                <tr>
                    <td style="font-weight: 700; background: #f8f9fa;">Kumpulan Sasaran</td>
                    <td>Semua Guru, Pentadbir & Warga SMJK Ave Maria Convent, Ipoh</td>
                </tr>
                <tr>
                    <td style="font-weight: 700; background: #f8f9fa;">Kategori Inovasi</td>
                    <td>Pengurusan & Pentadbiran Digital Sekolah (Paperless Smart Management)</td>
                </tr>
                <tr>
                    <td style="font-weight: 700; background: #f8f9fa;">Masalah Diselesaikan</td>
                    <td>Mengatasi pertindihan jadual penggunaan makmal komputer & menghapuskan rekod buku log manual secara 100% digital.</td>
                </tr>
                <tr>
                    <td style="font-weight: 700; background: #f8f9fa;">Impak & Keberkesanan</td>
                    <td>Penjimatan masa sehingga 80%, sifar pertindihan tempahan, pengesahan segera melalui Google Calendar & e-mel automatik.</td>
                </tr>
            </tbody>
        </table>

        <div style="margin-top: 16px;">
            <button class="btn-card btn-card-primary" onclick="previewDoc('Kertas Projek Inovasi Digital Sekolah 2026', '6.0 KEISTIMEWAAN SEKOLAH/6.3 Inovasi Sekolah/Kertas Projek Inovasi Digital Sekolah 2026.docx')">
                <i class="fas fa-file-alt"></i> Prapapar Kertas Projek Inovasi
            </button>
            <a href="{SMART_BOOKING_URL}" target="_blank" class="btn-card btn-card-drive">
                <i class="fas fa-external-link-alt"></i> Layari AMC Smart Booking
            </a>
        </div>
    </div>
</main>
"""
with open('pages/inovasi.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Inovasi AMC Smart Booking", inovasi_body, depth=1, active='keistimewaan'))

# ------------------------------------------------------------------------------
# 17. KOLABORATIF (pages/kolaboratif.html)
# ------------------------------------------------------------------------------
kolaboratif_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Kolaboratif & Jaringan Pintar", "6.0 Keistimewaan", "keistimewaan.html")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fas fa-handshake"></i> Program Kolaboratif, Jaringan & Jalinan ICT 2026</h2>
            <p>Perkongsian Pintar Bersama Agensi Kerajaan, Badan Korporat, Komuniti & Institusi Antarabangsa</p>
        </div>
        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
            <i class="fab fa-google-drive"></i> Folder E-Fail 6.1
        </a>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-globe"></i> Rakan Kerjasama Strategik Pendigitalan</h3>
        <table class="delima-table">
            <thead>
                <tr>
                    <th>Agensi / Rakan Kerjasama</th>
                    <th>Nama Program / Inisiatif</th>
                    <th>Impak & Manfaat kepada Warga Sekolah</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>MDEC & BSKK KPM</strong></td>
                    <td>Program Kesedaran Bakat Digital & STEM</td>
                    <td>Pendedahan murid kepada bidang Kecerdasan Buatan (AI) & Pengaturcaraan Python.</td>
                </tr>
                <tr>
                    <td><strong>Suruhanjaya Komunikasi & Multimedia (MCMC)</strong></td>
                    <td>Bengkel Sukarelawan ICT (MIV) & Klik Dengan Bijak</td>
                    <td>Pemerkasaan literasi keselamatan digital dan pencegahan buli siber di kalangan remaja.</td>
                </tr>
                <tr>
                    <td><strong>Digi Telecommunications</strong></td>
                    <td>Modul Digi CyberSAFE in Schools</td>
                    <td>Panduan keselamatan privasi data peribadi dan etika pelayaran internet.</td>
                </tr>
                <tr>
                    <td><strong>Google for Education Malaysia</strong></td>
                    <td>Program Pensijilan Google Certified Educator (GCE)</td>
                    <td>Pentauliahan 103 orang guru SMJK AMC dengan sijil profesional Google.</td>
                </tr>
            </tbody>
        </table>

        <div style="margin-top: 14px;">
            <button class="btn-card btn-card-primary" onclick="previewDoc('Laporan Jaringan dan Jalinan Pintar ICT Bersama Komuniti & Agensi Luar 2026', '6.0 KEISTIMEWAAN SEKOLAH/6.1 Kolaboratif, Jaringan & Jalinan/Laporan Jaringan dan Jalinan Pintar ICT Bersama Komuniti & Agensi Luar 2026.docx')">
                <i class="fas fa-file-alt"></i> Prapapar Laporan Kolaboratif
            </button>
        </div>
    </div>
</main>
"""
with open('pages/kolaboratif.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Kolaboratif & Jaringan", kolaboratif_body, depth=1, active='keistimewaan'))

# ------------------------------------------------------------------------------
# 18. PENCAPAIAN (pages/pencapaian.html)
# ------------------------------------------------------------------------------
pencapaian_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Pencapaian & Anugerah", "6.0 Keistimewaan", "keistimewaan.html")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fas fa-trophy"></i> Rekod Pencapaian & Anugerah Digital Sekolah</h2>
            <p>Pengiktirafan Kejayaan Pembudayaan Teknologi dan Kecemerlangan ICT SMJK Ave Maria Convent, Ipoh</p>
        </div>
        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
            <i class="fab fa-google-drive"></i> Folder E-Fail 6.4
        </a>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-award"></i> Galeri Anugerah & Pengiktirafan</h3>
        <table class="delima-table">
            <thead>
                <tr>
                    <th>Tahun</th>
                    <th>Nama Anugerah / Pencapaian</th>
                    <th>Peringkat</th>
                    <th>Pencapaian / Status</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>2026</strong></td>
                    <td><strong>Penarafan Kendiri DELIMa 5 Bintang KPM</strong></td>
                    <td>Kebangsaan</td>
                    <td><span class="badge badge-success"><i class="fas fa-star"></i> 5 BINTANG (100% KPI)</span></td>
                </tr>
                <tr>
                    <td><strong>2026</strong></td>
                    <td><strong>Pentauliahan 100% Guru Digital (GCE / Gemini / Apple)</strong></td>
                    <td>Antarabangsa</td>
                    <td><span class="badge badge-primary"><i class="fas fa-medal"></i> 106 Guru Bertauliah</span></td>
                </tr>
                <tr>
                    <td><strong>2025/2026</strong></td>
                    <td><strong>Anugerah Pembudayaan Pendigitalan Sekolah Terbaik</strong></td>
                    <td>Negeri / Kebangsaan</td>
                    <td><span class="badge badge-success"><i class="fas fa-trophy"></i> Johan</span></td>
                </tr>
                <tr>
                    <td><strong>2024/2025</strong></td>
                    <td><strong>Penarafan 5 Bintang Smart School Qualification Standards (SSQS)</strong></td>
                    <td>Kementerian Pendidikan Malaysia</td>
                    <td><span class="badge badge-success"><i class="fas fa-star"></i> 5 Bintang Cemerlang</span></td>
                </tr>
                <tr>
                    <td><strong>2024</strong></td>
                    <td><strong>Anugerah Ikon Guru Digital Cemerlang</strong></td>
                    <td>Negeri</td>
                    <td><span class="badge badge-primary"><i class="fas fa-user-check"></i> Ikon Guru</span></td>
                </tr>
            </tbody>
        </table>

        <div style="margin-top: 14px;">
            <button class="btn-card btn-card-primary" onclick="previewDoc('Rekod Pencapaian dan Anugerah Digital Sekolah 2026', '6.0 KEISTIMEWAAN SEKOLAH/6.4 Pencapaian dan Anugerah/Rekod Pencapaian dan Anugerah Digital Sekolah 2026.docx')">
                <i class="fas fa-file-alt"></i> Prapapar Rekod Anugerah
            </button>
        </div>
    </div>
</main>
"""
with open('pages/pencapaian.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Pencapaian & Anugerah", pencapaian_body, depth=1, active='keistimewaan'))

# ------------------------------------------------------------------------------
# 19. SUMBANGAN PDP (pages/sumbangan-pdp.html)
# ------------------------------------------------------------------------------
sumbangan_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Sumbangan Bahan PdP", "6.0 Keistimewaan", "keistimewaan.html")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fas fa-share-alt"></i> Sumbangan Bahan PdP ke Ruang Ilmu KPM & Saluran Guru</h2>
            <p>Inisiatif Perkongsian Terbuka Sumber Pendidikan Digital (OER) Guru-Guru SMJK Ave Maria Convent, Ipoh</p>
        </div>
        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
            <i class="fab fa-google-drive"></i> Folder E-Fail 6.5
        </a>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-book-reader"></i> Modul & Bahan PdP Guru Diterbitkan di Ruang Ilmu KPM</h3>
        <table class="delima-table">
            <thead>
                <tr>
                    <th>Bil</th>
                    <th>Nama Guru Penyumbang</th>
                    <th>Mata Pelajaran & Tingkatan</th>
                    <th>Tajuk Bahan / Modul Pembelajaran</th>
                    <th>Status Penerbitan</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1</td>
                    <td><strong>Cik Au Chooi Yee</strong></td>
                    <td>Sains Komputer Tingkatan 4 & 5</td>
                    <td>Modul Interaktif Struktur Kawalan Pilihan Python & Algoritma</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Diterbitkan di Ruang Ilmu</span></td>
                </tr>
                <tr>
                    <td>2</td>
                    <td><strong>Pn. Nurain Binti Md Nor</strong></td>
                    <td>Matematik Tingkatan 3</td>
                    <td>Video Pembelajaran Animasi Teorem Pythagoras & Garis Lurus</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Diterbitkan di Ruang Ilmu</span></td>
                </tr>
                <tr>
                    <td>3</td>
                    <td><strong>Panitia Bahasa Melayu</strong></td>
                    <td>Bahasa Melayu Tingkatan 5</td>
                    <td>Kompilasi Modul Karangan Berformat SPM Berasaskan Google Docs</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Diterbitkan di Ruang Ilmu</span></td>
                </tr>
                <tr>
                    <td>4</td>
                    <td><strong>Panitia Sains & Matematik</strong></td>
                    <td>Sains Tingkatan 2</td>
                    <td>Bank Soalan Kuiz Interaktif Gamifikasi (Quizizz & Wordwall)</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Perkongsian Komuniti</span></td>
                </tr>
            </tbody>
        </table>

        <div style="margin-top: 14px;">
            <button class="btn-card btn-card-primary" onclick="previewDoc('Rekod Sumbangan Bahan PdP ke Ruang Ilmu KPM 2026', '6.0 KEISTIMEWAAN SEKOLAH/6.5 Sumbangan Bahan PdP Ruang Ilmu/Rekod Sumbangan Bahan PdP ke Ruang Ilmu KPM 2026.docx')">
                <i class="fas fa-file-alt"></i> Prapapar Rekod Sumbangan
            </button>
        </div>
    </div>
</main>
"""
with open('pages/sumbangan-pdp.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Sumbangan Bahan PdP", sumbangan_body, depth=1, active='keistimewaan'))

# ------------------------------------------------------------------------------
# 20. PORTAL DASHBOARD (pages/portal-dashboard.html)
# ------------------------------------------------------------------------------
dashboard_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Portal & Dashboard", "Akses Pantas", "portal-dashboard.html")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fas fa-th"></i> Portal & Dashboard Akses Pantas DELIMa KPM</h2>
            <p>Pusat Sehenti Gerbang Pembelajaran Digital & Aplikasi Pengurusan Pendidikan Warga SMJK AMC</p>
        </div>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-rocket"></i> Gerbang Aplikasi Pembelajaran Utama</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; margin-top: 14px;">
            <a href="https://d3.delima.edu.my/" target="_blank" class="launchpad-card" style="padding: 14px;">
                <div class="launchpad-icon" style="background-color: #b71c1c;"><i class="fas fa-graduation-cap"></i></div>
                <div class="launchpad-info">
                    <h4 style="font-size: 14px;">Portal DELIMa (d3)</h4>
                    <span>Gerbang Rasmi KPM</span>
                </div>
            </a>
            <a href="https://classroom.google.com/" target="_blank" class="launchpad-card" style="padding: 14px;">
                <div class="launchpad-icon" style="background-color: #1e8e3e;"><i class="fab fa-google"></i></div>
                <div class="launchpad-info">
                    <h4 style="font-size: 14px;">Google Classroom</h4>
                    <span>Bilik Darjah Digital</span>
                </div>
            </a>
            <a href="https://drive.google.com/" target="_blank" class="launchpad-card" style="padding: 14px;">
                <div class="launchpad-icon" style="background-color: #1a73e8;"><i class="fab fa-google-drive"></i></div>
                <div class="launchpad-info">
                    <h4 style="font-size: 14px;">Google Drive</h4>
                    <span>Storan Awan & E-Fail</span>
                </div>
            </a>
            <a href="https://www.canva.com/education/" target="_blank" class="launchpad-card" style="padding: 14px;">
                <div class="launchpad-icon" style="background-color: #7b1fa2;"><i class="fas fa-palette"></i></div>
                <div class="launchpad-info">
                    <h4 style="font-size: 14px;">Canva for Education</h4>
                    <span>Bahan Grafik & Banner</span>
                </div>
            </a>
            <a href="{SMART_BOOKING_URL}" target="_blank" class="launchpad-card" style="padding: 14px;">
                <div class="launchpad-icon" style="background-color: #d32f2f;"><i class="fas fa-calendar-check"></i></div>
                <div class="launchpad-info">
                    <h4 style="font-size: 14px;">AMC Smart Booking</h4>
                    <span>Tempahan Makmal AMC</span>
                </div>
            </a>
            <a href="https://quizizz.com/" target="_blank" class="launchpad-card" style="padding: 14px;">
                <div class="launchpad-icon" style="background-color: #8e24aa;"><i class="fas fa-gamepad"></i></div>
                <div class="launchpad-info">
                    <h4 style="font-size: 14px;">Quizizz Education</h4>
                    <span>Kuiz Interaktif Murid</span>
                </div>
            </a>
            <a href="https://apdm.moe.gov.my/" target="_blank" class="launchpad-card" style="padding: 14px;">
                <div class="launchpad-icon" style="background-color: #0288d1;"><i class="fas fa-user-check"></i></div>
                <div class="launchpad-info">
                    <h4 style="font-size: 14px;">APDM KPM</h4>
                    <span>e-Kehadiran Murid</span>
                </div>
            </a>
            <a href="https://splkpm.moe.gov.my/" target="_blank" class="launchpad-card" style="padding: 14px;">
                <div class="launchpad-icon" style="background-color: #f9ab00;"><i class="fas fa-chalkboard-teacher"></i></div>
                <div class="launchpad-info">
                    <h4 style="font-size: 14px;">SPLKPM</h4>
                    <span>Rekod Latihan LADAP Guru</span>
                </div>
            </a>
        </div>
    </div>
</main>
"""
with open('pages/portal-dashboard.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Portal & Dashboard", dashboard_body, depth=1, active='dashboard'))

# ------------------------------------------------------------------------------
# 21. ADUAN ID DELIMA (pages/aduan-id.html)
# ------------------------------------------------------------------------------
aduan_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Aduan ID & Kata Laluan", "Bantuan", "aduan-id.html")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fas fa-key"></i> Borang Aduan Masalah ID DELIMa & Reset Kata Laluan</h2>
            <p>Pusat Meja Bantuan Rasmi Unit ICT SMJK Ave Maria Convent, Ipoh untuk Guru & Murid</p>
        </div>
    </div>

    <!-- Admin Notification Info Box -->
    <div style="background: #e8f0fe; border-left: 4px solid #1a73e8; border-radius: 8px; padding: 16px 20px; margin-bottom: 24px; box-shadow: var(--shadow-sm);">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px;">
            <i class="fas fa-envelope-circle-check" style="font-size: 20px; color: #1a73e8;"></i>
            <h4 style="margin: 0; color: #1a73e8; font-size: 15px;">Penghantaran Automatik ke Admin DELIMa</h4>
        </div>
        <p style="font-size: 13px; color: var(--text-dark); margin: 0;">
            Setiap aduan yang dihantar akan disalurkan secara terus dan serta-merta ke peti masuk e-mel Admin DELIMa Sekolah:
        </p>
        <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px;">
            <span class="badge badge-info" style="font-size: 12px; padding: 4px 10px;"><i class="fas fa-user-shield"></i> Pn. Nurain: <strong>g-00556750@moe-dl.edu.my</strong></span>
            <span class="badge badge-info" style="font-size: 12px; padding: 4px 10px;"><i class="fas fa-user-shield"></i> Cik Au Chooi Yee: <strong>g-24188210@moe-dl.edu.my</strong></span>
        </div>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-edit"></i> Hantar Maklumat Aduan</h3>
        <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 20px;">
            Sila lengkapkan borang di bawah sekiranya anda terlupa kata laluan atau mengalami masalah log masuk akaun <code>@moe-dl.edu.my</code>. Tindakan semakan dan penetapan semula kata laluan akan diambil oleh Admin DELIMa dalam tempoh 24 jam.
        </p>

        <form id="aduanForm">
            <div class="form-grid">
                <div class="form-group">
                    <label for="aduanNama"><i class="fas fa-user"></i> Nama Penuh Pemohon *</label>
                    <input type="text" id="aduanNama" class="form-control" placeholder="Contoh: AU CHOOI YEE" required>
                </div>
                <div class="form-group">
                    <label for="aduanPeranan"><i class="fas fa-user-tag"></i> Peranan Pemohon *</label>
                    <select id="aduanPeranan" class="form-control" required>
                        <option value="">-- Pilih Peranan --</option>
                        <option value="Guru / Staf">Guru / Staf SMJK AMC</option>
                        <option value="Murid Tingkatan 1">Murid Tingkatan 1</option>
                        <option value="Murid Tingkatan 2">Murid Tingkatan 2</option>
                        <option value="Murid Tingkatan 3">Murid Tingkatan 3</option>
                        <option value="Murid Tingkatan 4">Murid Tingkatan 4</option>
                        <option value="Murid Tingkatan 5">Murid Tingkatan 5</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="aduanKelas"><i class="fas fa-chalkboard"></i> Kelas / Panitia (Jika Berkaitan)</label>
                    <input type="text" id="aduanKelas" class="form-control" placeholder="Contoh: 4 Sains 1 / Panitia ICT">
                </div>
                <div class="form-group">
                    <label for="aduanKategori"><i class="fas fa-exclamation-triangle"></i> Jenis Masalah *</label>
                    <select id="aduanKategori" class="form-control" required>
                        <option value="Lupa Kata Laluan (Reset Password)">Lupa Kata Laluan (Reset Password)</option>
                        <option value="Akaun Terkunci / Disabled">Akaun Terkunci / Disabled</option>
                        <option value="Tidak Tahu / Belum Menerima ID DELIMa">Tidak Tahu / Belum Menerima ID DELIMa</option>
                        <option value="Masalah Akses Google Classroom">Masalah Akses Google Classroom</option>
                        <option value="Lain-lain Isu Teknikal">Lain-lain Isu Teknikal</option>
                    </select>
                </div>
            </div>

            <div class="form-group" style="margin-bottom: 18px;">
                <label for="aduanKeterangan"><i class="fas fa-comment-alt"></i> Keterangan Isu & No. Telefon / E-mel untuk Dihubungi *</label>
                <textarea id="aduanKeterangan" class="form-control" placeholder="Sila nyatakan no. KP / maklumat kontak untuk penghantaran kata laluan baharu..." required></textarea>
            </div>

            <button type="submit" class="btn-submit">
                <i class="fas fa-paper-plane"></i> Hantar Aduan ID DELIMa
            </button>
        </form>
    </div>
</main>
"""
with open('pages/aduan-id.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Aduan ID DELIMa", aduan_body, depth=1, active='utama'))

print("All pages part 4 successfully updated!")
