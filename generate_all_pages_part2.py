# -*- coding: utf-8 -*-
"""
Part 2 of DELIMa Page Generator
SMJK Ave Maria Convent, Ipoh (AEB2052)
"""

import os
import json

# Load teacher data
teachers_info = {}
if os.path.exists('assets/data/teachers_certifications.json'):
    with open('assets/data/teachers_certifications.json', 'r', encoding='utf-8') as f:
        teachers_info = json.load(f)

teachers = teachers_info.get('teachers', [])
stats = teachers_info.get('stats', {'gce_lv1': 103, 'gce_lv2': 21, 'gemini': 24, 'apple_teacher': 8})
total_teachers = teachers_info.get('total_teachers', 106)

DRIVE_URL = "https://drive.google.com/drive/folders/10HBSO2m-RKMAEJPsKmPmHZ1HU6zw4-y8?usp=sharing"
SMART_BOOKING_URL = "https://sites.google.com/moe-dl.edu.my/amc-smart-booking-ver1/laman-utama"

from generate_pages import wrap_html
from generate_all_pages import get_breadcrumbs

# ------------------------------------------------------------------------------
# 5. LAPORAN AKTIVITI (pages/laporan-aktiviti.html)
# ------------------------------------------------------------------------------
laporan_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Laporan Pelaksanaan Aktiviti", "1.0 Pengurusan")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fas fa-clipboard-check"></i> Laporan Aktiviti (OPR) DELIMa 2026</h2>
            <p>Dokumentasi Laporan Ringkas Satu Muka Surat (One-Page Report) Program Pembestarian & Pendigitalan Sekolah</p>
        </div>
        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
            <i class="fab fa-google-drive"></i> Folder E-Fail 1.5
        </a>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-file-invoice"></i> Templat Laporan Pelaksanaan Aktiviti (OPR) Rasmi</h3>
        <table class="delima-table">
            <tbody>
                <tr>
                    <td style="width: 25%; font-weight: 700; background: #f8f9fa;">Nama Program / Aktiviti</td>
                    <td><strong>Bengkel Penggunaan Google Workspace dan AI Generatif (Gemini) dalam PdP Guru</strong></td>
                </tr>
                <tr>
                    <td style="font-weight: 700; background: #f8f9fa;">Tarikh & Masa</td>
                    <td>24 Februari 2026 | 2.00 petang - 4.30 petang</td>
                </tr>
                <tr>
                    <td style="font-weight: 700; background: #f8f9fa;">Tempat</td>
                    <td>Makmal Komputer 1, SMJK Ave Maria Convent, Ipoh</td>
                </tr>
                <tr>
                    <td style="font-weight: 700; background: #f8f9fa;">Penceramah / Fasilitator</td>
                    <td>Cik Au Chooi Yee (Guru ICT / GCE Trainer & Gemini Educator)</td>
                </tr>
                <tr>
                    <td style="font-weight: 700; background: #f8f9fa;">Kumpulan Sasaran</td>
                    <td>Semua Guru SMJK Ave Maria Convent (106 orang peserta)</td>
                </tr>
                <tr>
                    <td style="font-weight: 700; background: #f8f9fa;">Objektif Program</td>
                    <td>
                        1. Meningkatkan kemahiran guru mengintegrasikan alatan Google Workspace.<br>
                        2. Membimbing guru memanfaatkan Gemini AI untuk perancangan PdP & penyediaan bahan e-RPH.<br>
                        3. Memastikan 100% guru aktif menggunakan akaun ID @moe-dl.edu.my.
                    </td>
                </tr>
                <tr>
                    <td style="font-weight: 700; background: #f8f9fa;">Impak & Hasil</td>
                    <td>
                        <span class="badge badge-success"><i class="fas fa-check-circle"></i> 100% Hadir</span>
                        Semua guru berjaya menghasilkan bahan PdP digital dan 100 guru bertauliah GCE Level 1 diperakui.
                    </td>
                </tr>
            </tbody>
        </table>

        <div style="margin-top: 14px;">
            <button class="btn-card btn-card-primary" onclick="previewDoc('Templat Laporan Pelaksanaan Aktiviti (OPR) DELIMa 2026', '1.0 PENGURUSAN/1.5 Laporan Pelaksanaan Aktiviti/Templat Laporan Pelaksanaan Aktiviti (OPR) DELIMa 2026.docx')">
                <i class="fas fa-file-alt"></i> Prapapar Dokumen OPR
            </button>
        </div>
    </div>
</main>
"""
with open('pages/laporan-aktiviti.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Laporan Aktiviti DELIMa", laporan_body, depth=1, active='utama'))
print("Saved pages/laporan-aktiviti.html")

# ------------------------------------------------------------------------------
# 6. MINIT MESYUARAT (pages/minit-mesyuarat.html)
# ------------------------------------------------------------------------------
minit_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Minit Mesyuarat", "1.0 Pengurusan")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fas fa-file-signature"></i> Minit Mesyuarat Jawatankuasa DELIMa 2026</h2>
            <p>Arkib Rekod Minit Mesyuarat dan Keputusan Jawatankuasa ICT & DELIMa SMJK AMC</p>
        </div>
        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
            <i class="fab fa-google-drive"></i> Folder E-Fail 1.6
        </a>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-archive"></i> Rekod Minit Mesyuarat Sesi 2026</h3>
        <table class="delima-table">
            <thead>
                <tr>
                    <th>Bil</th>
                    <th>Mesyuarat / Sidang</th>
                    <th>Tarikh & Masa</th>
                    <th>Pengerusi Sidang</th>
                    <th>Status Minit</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1</td>
                    <td><strong>Mesyuarat Jawatankuasa DELIMa & ICT Bil. 1/2026</strong></td>
                    <td>12 Januari 2026 (2.30 petang)</td>
                    <td>Pn. Tan Pei Nee (Pengetua)</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Disahkan & Diedarkan</span></td>
                </tr>
                <tr>
                    <td>2</td>
                    <td><strong>Mesyuarat Jawatankuasa DELIMa & ICT Bil. 2/2026</strong></td>
                    <td>08 Julai 2026 (2.30 petang)</td>
                    <td>Pn. Cheah Lay Shyuan (PK Pentadbiran)</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Disahkan</span></td>
                </tr>
            </tbody>
        </table>

        <div style="margin-top: 14px;">
            <button class="btn-card btn-card-primary" onclick="previewDoc('Minit Mesyuarat Jawatankuasa DELIMa Bil 1 2026', '1.0 PENGURUSAN/1.6 Mesyuarat & Minit Mesyuarat/Minit Mesyuarat Jawatankuasa DELIMa Bil 1 2026.docx')">
                <i class="fas fa-file-alt"></i> Prapapar Minit Mesyuarat Bil 1/2026
            </button>
        </div>
    </div>
</main>
"""
with open('pages/minit-mesyuarat.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Minit Mesyuarat DELIMa", minit_body, depth=1, active='utama'))
print("Saved pages/minit-mesyuarat.html")

# ------------------------------------------------------------------------------
# 7. PROGRAM DELIMA (pages/program-delima.html)
# ------------------------------------------------------------------------------
program_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Program & Takwim ICT", "1.0 Pengurusan")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fas fa-calendar-alt"></i> Takwim Program & Aktiviti DELIMa 2026</h2>
            <p>Jadual Perancangan Tahunan Program Pembudayaan Digital & Kursus ICT SMJK AMC</p>
        </div>
        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
            <i class="fab fa-google-drive"></i> Folder E-Fail 1.7
        </a>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-calendar-check"></i> Takwim Rasmi Unit ICT & DELIMa 2026</h3>
        <table class="delima-table">
            <thead>
                <tr>
                    <th style="width: 12%;">Bulan</th>
                    <th>Nama Program / Aktiviti</th>
                    <th>Sasaran</th>
                    <th>Pegawai Bertanggungjawab</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Januari</strong></td>
                    <td>Pengagihan & Pengaktifan Semula ID @moe-dl Tingkatan 1 dan Murid Baharu</td>
                    <td>Murid Tingkatan 1</td>
                    <td>Pn. Nurain (Admin DELIMa)</td>
                </tr>
                <tr>
                    <td><strong>Februari</strong></td>
                    <td>Pelancaran Bulan Pembudayaan DELIMa & LADAP 1 (Gemini AI & Workspace)</td>
                    <td>Semua Guru & Murid</td>
                    <td>Pn. Tan Pei Nee & Au Chooi Yee</td>
                </tr>
                <tr>
                    <td><strong>Mac</strong></td>
                    <td>Bengkel Celik Digital Murid & Keselamatan Siber Kebangsaan</td>
                    <td>Murid Menengah Rendah</td>
                    <td>Au Chooi Yee & Guru ICT</td>
                </tr>
                <tr>
                    <td><strong>April</strong></td>
                    <td>Pelaksanaan & Integrasi Sistem Inovasi AMC Smart Booking</td>
                    <td>Semua Guru</td>
                    <td>Au Chooi Yee & Pentadbir</td>
                </tr>
                <tr>
                    <td><strong>Mei - Jun</strong></td>
                    <td>Klinik Latihan Ujian Pensijilan Google Certified Educator (GCE Level 1 & 2)</td>
                    <td>Semua Guru AMC</td>
                    <td>Au Chooi Yee (GCE Trainer)</td>
                </tr>
                <tr>
                    <td><strong>Julai</strong></td>
                    <td>Penilaian Kendiri DELIMa Fasa 1 (Pengisian Skor Penarafan 5 Bintang KPM)</td>
                    <td>Jawatankuasa DELIMa</td>
                    <td>Pn. Cheah Lay Shyuan & Pn. Nurain</td>
                </tr>
                <tr>
                    <td><strong>Ogos</strong></td>
                    <td>Audit Dalaman Prestasi Penggunaan Power BI KPM (Pencapaian 100% KPI)</td>
                    <td>Warga Sekolah</td>
                    <td>Penyelaras DELIMa</td>
                </tr>
                <tr>
                    <td><strong>Oktober</strong></td>
                    <td>Pertandingan Rekaan Grafik Digital & Video Kreatif Bulan ICT AMC</td>
                    <td>Semua Murid</td>
                    <td>Pn. Nurain & Panitia ICT</td>
                </tr>
                <tr>
                    <td><strong>November</strong></td>
                    <td>Penilaian Kendiri DELIMa Fasa 2 & Rumusan Pensijilan Guru 2026</td>
                    <td>Pengurusan Sekolah</td>
                    <td>Pn. Tan Pei Nee & AJK</td>
                </tr>
            </tbody>
        </table>

        <div style="margin-top: 14px;">
            <button class="btn-card btn-card-primary" onclick="previewDoc('Takwim Program dan Aktiviti DELIMa 2026', '1.0 PENGURUSAN/1.7 Program dalam Takwim/Takwim Program dan Aktiviti DELIMa 2026.docx')">
                <i class="fas fa-file-alt"></i> Prapapar Dokumen Takwim
            </button>
        </div>
    </div>
</main>
"""
with open('pages/program-delima.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Program & Takwim DELIMa", program_body, depth=1, active='utama'))
print("Saved pages/program-delima.html")

# ------------------------------------------------------------------------------
# 8. JADUAL PENGGUNAAN (pages/jadual-penggunaan.html)
# ------------------------------------------------------------------------------
jadual_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Jadual & Tempahan Makmal", "1.0 Pengurusan")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fas fa-desktop"></i> Jadual & Log Penggunaan Makmal Komputer 2026</h2>
            <p>Pengurusan Jadual Waktu Penggunaan Makmal Komputer, Troli Chromebook dan Sistem Tempahan Digital</p>
        </div>
        <div style="display: flex; gap: 8px;">
            <a href="{SMART_BOOKING_URL}" target="_blank" class="btn-card btn-card-primary">
                <i class="fas fa-external-link-alt"></i> Buka AMC Smart Booking
            </a>
            <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
                <i class="fab fa-google-drive"></i> Folder E-Fail 1.8
            </a>
        </div>
    </div>

    <!-- Smart Booking Innovation Highlight -->
    <div class="content-box" style="border-left: 5px solid #0f9d58; background: #f6fcf8;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
            <div>
                <h3 style="color: #0f9d58; margin-bottom: 4px; border: none; padding: 0;"><i class="fas fa-lightbulb"></i> Inovasi Tempahan: AMC Smart Booking</h3>
                <p style="font-size: 13px; color: var(--text-dark); margin: 0;">SMJK Ave Maria Convent kini menggunakan sistem tempahan kemudahan digital paperless berasaskan Google Sites & Calendar.</p>
            </div>
            <a href="{SMART_BOOKING_URL}" target="_blank" class="btn-hero btn-hero-yellow" style="padding: 8px 16px; font-size: 12px;">
                <i class="fas fa-calendar-plus"></i> Tempah Makmal Secara Online
            </a>
        </div>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-clock"></i> Kemudahan ICT & Makmal Komputer Sekolah</h3>
        <table class="delima-table">
            <thead>
                <tr>
                    <th>Kemudahan / Bilik Khas</th>
                    <th>Kapasiti Peranti</th>
                    <th>Perkakasan / Perisian</th>
                    <th>Guru Pengurus</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Bilik Komputer</strong></td>
                    <td>48 buah Komputer PC & Projector &Visualiser</td>
                    <td>Windows 11, Edge, Microsoft Office</td>
                    <td>Cik Au Chooi Yee</td>
                </tr>
                <tr>
                    <td><strong>Bilik Akses</strong></td>
                    <td>21 buah Laptop, 20 buah Komputer PC, Projektor & Visualiser</td>
                    <td>Google Workspace for Education, Pelayar DELIMa</td>
                    <td>Pn. Nor Areen Binti Alil</td>
                </tr>
                <tr>
                    <td><strong>Setiap Kelas</strong></td>
                    <td>Touchscreen Komputer & Projektor</td>
                    <td>Windows 11, Edge, Microsoft Office</td>
                    <td>Penyelaras ICT</td>
                </tr>
                <tr>
                    <td><strong>Bilik Tayangan</strong></td>
                    <td>Peranti Rakaman & Skrin Interaktif</td>
                    <td>Webcam HD, Mikrofon Lavalier, Green Screen</td>
                    <td>AJK Media</td>
                </tr>
            </tbody>
        </table>

        <div style="margin-top: 14px;">
            <button class="btn-card btn-card-primary" onclick="previewDoc('Jadual dan Log Penggunaan Makmal Komputer dan DELIMa 2026', '1.0 PENGURUSAN/1.8 Jadual Penggunaan DELIMa/Jadual dan Log Penggunaan Makmal Komputer dan DELIMa 2026.docx')">
                <i class="fas fa-file-alt"></i> Prapapar Dokumen Log Makmal
            </button>
        </div>
    </div>
</main>
"""
with open('pages/jadual-penggunaan.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Jadual & Tempahan Makmal", jadual_body, depth=1, active='utama'))
print("Saved pages/jadual-penggunaan.html")

print("Generator script part 3 completed.")
