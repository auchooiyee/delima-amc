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
                    <td><strong>Google for Education Malaysia</strong></td>
                    <td>Program Pensijilan Google Certified Educator (GCE)</td>
                    <td>Pentauliahan 103 orang guru SMJK AMC dengan sijil profesional Google.</td>
                </tr>
                <tr>
                    <td><strong>Quest International University (QIU)</strong></td>
                    <td>
                        • Bengkel Basic Visual Programming using Visual Studio 2022 (9 Mei 2026)<br>
                        • Bengkel App Development for Beginners (13 Jun 2026)
                    </td>
                    <td>Pendedahan murid kepada asas pengaturcaraan visual dan pembangunan aplikasi serta pengukuhan kemahiran digital melalui perkongsian dan bimbingan daripada pakar bidang teknologi dan pengkomputeran.</td>
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
                    <td><strong>Pentauliahan 100% Guru Digital (GCE / Gemini / Apple)</strong></td>
                    <td>Antarabangsa</td>
                    <td><span class="badge badge-primary"><i class="fas fa-medal"></i> 106 Guru Bertauliah</span></td>
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
                <div class="launchpad-icon" style="background-color: #1a237e;"><i class="fas fa-graduation-cap"></i></div>
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
                <div class="launchpad-icon" style="background-color: #1565c0;"><i class="fas fa-calendar-check"></i></div>
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

DASH_PORTAL_URL = "https://script.google.com/macros/s/AKfycbw3yy7rRiEnUkG-zhOi3nvgzbsjTakH9eD4Uapny0FZfQoidWmBs5zooq25Ub6RqGrfKA/exec?page=student"

# ------------------------------------------------------------------------------
# 21. DASH PORTAL (pages/dash-portal.html & pages/aduan-id.html)
# ------------------------------------------------------------------------------
dash_portal_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("DaSH Portal (Reset Password)", "Bantuan", "dash-portal.html")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fas fa-key"></i> DaSH Portal — Panduan Reset Password Akaun DELIMa</h2>
            <p>Sistem Pertukaran & Penetapan Semula Kata Laluan DELIMa Kendiri SMJK Ave Maria Convent, Ipoh • Khas untuk Murid</p>
        </div>
        <a href="{DASH_PORTAL_URL}" target="_blank" class="btn-hero btn-hero-yellow" style="box-shadow: 0 4px 15px rgba(251, 192, 45, 0.4); text-transform: uppercase;">
            <i class="fas fa-external-link-alt"></i> Buka DaSH Portal (Pelajar)
        </a>
    </div>

    <!-- Core Feature Highlight Banner -->
    <div class="content-box" style="background: linear-gradient(135deg, #0d1442 0%, #1a237e 50%, #1565c0 100%); color: #ffffff; border-radius: 12px; padding: 26px 28px; box-shadow: 0 6px 20px rgba(26, 35, 126, 0.25);">
        <div style="display: flex; align-items: center; gap: 18px; margin-bottom: 16px; flex-wrap: wrap;">
            <div style="width: 56px; height: 56px; border-radius: 50%; background: #fbc02d; color: #0d1442; display: flex; align-items: center; justify-content: center; font-size: 26px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                <i class="fas fa-bolt"></i>
            </div>
            <div>
                <span class="badge" style="background: #fbc02d; color: #0d1442; font-weight: 800; font-size: 11px; text-transform: uppercase; padding: 4px 10px; margin-bottom: 6px; display: inline-block;">Sistem Kendiri Murid</span>
                <h3 style="margin: 0; color: #ffffff; font-family: 'Oswald', sans-serif; font-size: 24px; letter-spacing: 0.5px; border: none; padding: 0;">Apa itu DaSH Portal?</h3>
            </div>
        </div>
        <p style="font-size: 16px; line-height: 1.6; color: #e8eaf6; margin-bottom: 18px;">
            <strong>DaSH Portal</strong> ialah laman web sekolah yang membolehkan anda menukar (reset) password akaun DELIMa anda sendiri — <strong>tanpa perlu tunggu Cikgu ICT untuk buat untuk anda!</strong>
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px; margin-bottom: 20px;">
            <div style="background: rgba(255,255,255,0.1); border-radius: 8px; padding: 12px 16px; border-left: 3px solid #fbc02d;">
                <div style="font-weight: 700; color: #fbc02d; font-size: 13px; margin-bottom: 4px;"><i class="fas fa-question-circle"></i> Terlupa Password</div>
                <div style="font-size: 12px; color: #ffffff; opacity: 0.9;">Akaun DELIMa (contoh: <code>m-xxxxxxxx@moe-dl.edu.my</code>)</div>
            </div>
            <div style="background: rgba(255,255,255,0.1); border-radius: 8px; padding: 12px 16px; border-left: 3px solid #fbc02d;">
                <div style="font-weight: 700; color: #fbc02d; font-size: 13px; margin-bottom: 4px;"><i class="fas fa-ban"></i> Gagal Log Masuk</div>
                <div style="font-size: 12px; color: #ffffff; opacity: 0.9;">Tidak boleh akses Google Classroom atau Gmail sekolah</div>
            </div>
            <div style="background: rgba(255,255,255,0.1); border-radius: 8px; padding: 12px 16px; border-left: 3px solid #fbc02d;">
                <div style="font-weight: 700; color: #fbc02d; font-size: 13px; margin-bottom: 4px;"><i class="fas fa-sync-alt"></i> Kemas Kini Password</div>
                <div style="font-size: 12px; color: #ffffff; opacity: 0.9;">Ingin menukar kata laluan lama kepada yang baharu</div>
            </div>
        </div>
        <div>
            <a href="{DASH_PORTAL_URL}" target="_blank" class="btn-hero btn-hero-yellow" style="font-size: 14px; padding: 10px 22px;">
                <i class="fas fa-external-link-alt"></i> Klik Sini Untuk Buka DaSH Portal
            </a>
        </div>
    </div>

    <!-- Sebelum Mula Box -->
    <div class="content-box" style="border-left: 4px solid #fbc02d; background: #fffdf5;">
        <h3 style="color: #b78103; margin-bottom: 8px; border: none; padding: 0;"><i class="fas fa-clipboard-list"></i> Sebelum Mula: Sediakan 3 Maklumat Ini Dahulu</h3>
        <p style="font-size: 13.5px; color: var(--text-dark); margin-bottom: 12px;">Pastikan anda telah bersedia dengan maklumat pengesahan identiti berikut:</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px;">
            <div style="background: #ffffff; border: 1px solid #ffe082; border-radius: 8px; padding: 12px 16px;">
                <strong style="color: #b78103; font-size: 14px;">1. Nama Penuh Anda</strong>
                <p style="font-size: 12px; color: var(--text-muted); margin: 4px 0 0;">Tepat seperti di dalam rekod pendaftaran sekolah.</p>
            </div>
            <div style="background: #ffffff; border: 1px solid #ffe082; border-radius: 8px; padding: 12px 16px;">
                <strong style="color: #b78103; font-size: 14px;">2. No. Kad Pengenalan (IC)</strong>
                <p style="font-size: 12px; color: var(--text-muted); margin: 4px 0 0;">Nombor MyKad anda (tanpa tanda sengkang '-').</p>
            </div>
            <div style="background: #ffffff; border: 1px solid #ffe082; border-radius: 8px; padding: 12px 16px;">
                <strong style="color: #b78103; font-size: 14px;">3. Nama Penuh Guru Kelas</strong>
                <p style="font-size: 12px; color: var(--text-muted); margin: 4px 0 0;">Ejaan nama guru kelas dalam SEMUA HURUF BESAR.</p>
            </div>
        </div>
    </div>

    <!-- 3 Langkah Mudah -->
    <div class="content-box">
        <h3><i class="fas fa-list-ol"></i> Panduan 3 Langkah Reset Password</h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 18px; margin-top: 16px;">
            <!-- Langkah 1 -->
            <div style="background: #ffffff; border: 1px solid var(--border-color); border-radius: 10px; padding: 20px; position: relative; box-shadow: var(--shadow-sm);">
                <div style="position: absolute; top: -12px; left: 16px; background: #1a237e; color: #ffffff; font-weight: 800; font-size: 12px; padding: 2px 12px; border-radius: 12px;">LANGKAH 1</div>
                <h4 style="color: #1a237e; margin-top: 10px; margin-bottom: 8px;"><i class="fas fa-search"></i> Cari Nama Anda</h4>
                <p style="font-size: 13px; color: var(--text-dark); line-height: 1.5;">
                    Buka pautan DaSH Portal. Taip nama anda dalam kotak carian, kemudian <strong>pilih nama anda</strong> daripada senarai nama yang terpapar.
                </p>
            </div>

            <!-- Langkah 2 -->
            <div style="background: #ffffff; border: 1px solid var(--border-color); border-radius: 10px; padding: 20px; position: relative; box-shadow: var(--shadow-sm);">
                <div style="position: absolute; top: -12px; left: 16px; background: #1565c0; color: #ffffff; font-weight: 800; font-size: 12px; padding: 2px 12px; border-radius: 12px;">LANGKAH 2</div>
                <h4 style="color: #1565c0; margin-top: 10px; margin-bottom: 8px;"><i class="fas fa-shield-alt"></i> Sahkan & Reset</h4>
                <p style="font-size: 13px; color: var(--text-dark); line-height: 1.5;">
                    Selepas memilih nama, isikan No. Kad Pengenalan (IC) dan nama Guru Kelas anda dengan tepat sebagai langkah keselamatan. Kemudian tekan butang <strong>"Reset Password Saya"</strong>.
                </p>
                <div style="background: #fff8e1; border-radius: 6px; padding: 8px 10px; font-size: 11.5px; color: #856404; margin-top: 10px;">
                    <i class="fas fa-info-circle"></i> <strong>Penting:</strong> Had <strong>1 KALI sahaja</strong> dalam tempoh 24 jam.
                </div>
            </div>

            <!-- Langkah 3 -->
            <div style="background: #ffffff; border: 1px solid var(--border-color); border-radius: 10px; padding: 20px; position: relative; box-shadow: var(--shadow-sm);">
                <div style="position: absolute; top: -12px; left: 16px; background: #0f9d58; color: #ffffff; font-weight: 800; font-size: 12px; padding: 2px 12px; border-radius: 12px;">LANGKAH 3</div>
                <h4 style="color: #0f9d58; margin-top: 10px; margin-bottom: 8px;"><i class="fas fa-save"></i> Simpan Password Baharu</h4>
                <p style="font-size: 13px; color: var(--text-dark); line-height: 1.5;">
                    Jika maklumat disahkan, password baharu akan terus dipaparkan pada skrin. <strong>TULIS atau INGAT password ini serta-merta</strong> kerana ia tidak akan dipaparkan lagi selepas halaman ditutup.
                </p>
                <div style="background: #e6f4ea; border-radius: 6px; padding: 8px 10px; font-size: 11.5px; color: #137333; margin-top: 10px;">
                    <i class="fas fa-check-circle"></i> Tekan <strong>"Log Masuk Google"</strong> untuk terus mula!
                </div>
            </div>
        </div>
    </div>

    <!-- Masalah Biasa & Troubleshooting -->
    <div class="content-box">
        <h3><i class="fas fa-question-circle"></i> Masalah Biasa & Penyelesaian (Troubleshooting)</h3>
        
        <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 14px;">
            <div style="background: #ffffff; border: 1px solid var(--border-color); border-radius: 8px; padding: 14px 18px;">
                <div style="font-weight: 700; color: #d93025; font-size: 14px; margin-bottom: 4px;">
                    <i class="fas fa-times-circle"></i> Paparan Ralat: "Maklumat tidak sepadan"
                </div>
                <p style="font-size: 13px; color: var(--text-dark); margin: 0;">
                    Semak semula ejaan nama anda, nombor Kad Pengenalan, dan ejaan nama Guru Kelas. Semua maklumat perlu sama persis seperti yang didaftarkan dalam rekod sekolah (termasuk penggunaan SEMUA huruf besar bagi nama guru kelas).
                </p>
            </div>

            <div style="background: #ffffff; border: 1px solid var(--border-color); border-radius: 8px; padding: 14px 18px;">
                <div style="font-weight: 700; color: #f29900; font-size: 14px; margin-bottom: 4px;">
                    <i class="fas fa-clock"></i> Paparan Ralat: "Sila cuba lagi selepas X jam"
                </div>
                <p style="font-size: 13px; color: var(--text-dark); margin: 0;">
                    Anda telah melakukan pertukaran password dalam tempoh 24 jam yang lalu. Atas faktor keselamatan akaun, sila tunggu sehingga tempoh bertenang 24 jam tersebut tamat sebelum membuat reset baharu.
                </p>
            </div>

            <div style="background: #ffffff; border: 1px solid var(--border-color); border-radius: 8px; padding: 14px 18px;">
                <div style="font-weight: 700; color: #1a73e8; font-size: 14px; margin-bottom: 4px;">
                    <i class="fas fa-search-minus"></i> Nama anda tiada dalam senarai carian portal
                </div>
                <p style="font-size: 13px; color: var(--text-dark); margin: 0;">
                    Akaun anda mungkin murid baharu atau belum didaftarkan sepenuhnya ke dalam pangkalan data sistem. Sila hubungi Penyelaras DELIMa / Guru Penyelaras Bestari sekolah untuk bantuan pengaktifan.
                </p>
            </div>
        </div>
    </div>

    <!-- Peringatan Keselamatan & Sokongan Pentadbir -->
    <div class="content-box" style="background: #f8f9fa; border: 1px solid var(--border-color);">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
            <div>
                <h4 style="margin: 0 0 6px; color: var(--primary);"><i class="fas fa-user-shield"></i> Peringatan Keselamatan:</h4>
                <p style="font-size: 13px; color: var(--text-dark); margin: 0;">
                    Jangan sesekali berkongsi password akaun DELIMa anda dengan sesiapa pun, termasuk rakan sekelas.
                </p>
                <div style="margin-top: 10px; font-size: 12px; color: var(--text-muted);">
                    Dibina khas oleh Unit ICT untuk murid SMJK Ave Maria Convent, Ipoh.
                </div>
            </div>
            <div>
                <a href="{DASH_PORTAL_URL}" target="_blank" class="btn-hero btn-hero-yellow" style="padding: 10px 20px; font-size: 13px;">
                    <i class="fas fa-external-link-alt"></i> Buka DaSH Portal Sekarang
                </a>
            </div>
        </div>
    </div>

    <!-- Bantuan Admin DELIMa Sekolah -->
    <div class="content-box">
        <h3><i class="fas fa-headset"></i> Masih Menghadapi Masalah? Hubungi Admin DELIMa</h3>
        <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 16px;">
            Sekiranya akaun anda disekat (*disabled*), terlupa ID @moe-dl, atau perlukan bantuan khas guru:
        </p>
        <div style="display: flex; flex-wrap: wrap; gap: 12px;">
            <div style="background: #ffffff; border: 1px solid var(--border-color); border-radius: 8px; padding: 12px 16px; flex: 1; min-width: 250px;">
                <strong style="color: var(--primary);">Pn. Nurain Binti Md Nor</strong>
                <div style="font-size: 12px; color: var(--text-muted);">Penyelaras DELIMa / Admin DELIMa Sekolah</div>
                <div style="margin-top: 6px;"><a href="mailto:g-00556750@moe-dl.edu.my" style="color: #1a73e8; font-size: 13px;"><i class="fas fa-envelope"></i> g-00556750@moe-dl.edu.my</a></div>
            </div>
            <div style="background: #ffffff; border: 1px solid var(--border-color); border-radius: 8px; padding: 12px 16px; flex: 1; min-width: 250px;">
                <strong style="color: var(--primary);">Cik Au Chooi Yee</strong>
                <div style="font-size: 12px; color: var(--text-muted);">Penolong Penyelaras DELIMa / Guru ICT</div>
                <div style="margin-top: 6px;"><a href="mailto:g-24188210@moe-dl.edu.my" style="color: #1a73e8; font-size: 13px;"><i class="fas fa-envelope"></i> g-24188210@moe-dl.edu.my</a></div>
            </div>
        </div>
    </div>
</main>
"""

with open('pages/dash-portal.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("DaSH Portal (Reset Password)", dash_portal_body, depth=1, active='utama'))
print("Saved pages/dash-portal.html")

with open('pages/aduan-id.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("DaSH Portal (Reset Password)", dash_portal_body, depth=1, active='utama'))
print("Saved pages/aduan-id.html")

print("All pages part 4 successfully updated!")
