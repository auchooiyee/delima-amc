# -*- coding: utf-8 -*-
"""
Part 3 of DELIMa Page Generator
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
# 9. PEMBUDAYAAN (pages/pembudayaan.html)
# ------------------------------------------------------------------------------
pembudayaan_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Analisis Pembudayaan DELIMa", "2.0 Pembudayaan", "pembudayaan.html")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fas fa-chart-line"></i> 2.0 Pembudayaan DELIMa & Audit KPI KPM</h2>
            <p>Laporan Analisis Data Keaktifan Penggunaan Berdasarkan Dashboard Microsoft Power BI Rasmi KPM</p>
        </div>
        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
            <i class="fab fa-google-drive"></i> Folder E-Fail 2.0
        </a>
    </div>

    <!-- Power BI Stats Highlight Grid -->
    <div class="stats-grid">
        <div class="stat-card" style="border-top: 4px solid #b71c1c;">
            <div class="stat-icon" style="color: #b71c1c;"><i class="fas fa-trophy"></i></div>
            <div class="stat-number">5 BINTANG</div>
            <div class="stat-label">Penarafan Kendiri Sekolah</div>
            <div class="stat-sub">100.0% Skor Keseluruhan</div>
        </div>
        <div class="stat-card" style="border-top: 4px solid #1a73e8;">
            <div class="stat-icon" style="color: #1a73e8;"><i class="fas fa-chalkboard-teacher"></i></div>
            <div class="stat-number">93.0%</div>
            <div class="stat-label">Keaktifan Guru (Bulanan)</div>
            <div class="stat-sub">100 / 107 Guru Aktif</div>
        </div>
        <div class="stat-card" style="border-top: 4px solid #1e8e3e;">
            <div class="stat-icon" style="color: #1e8e3e;"><i class="fas fa-user-graduate"></i></div>
            <div class="stat-number">100.0%</div>
            <div class="stat-label">Keaktifan Murid (Bulanan)</div>
            <div class="stat-sub">1,453 / 1,453 Murid Aktif</div>
        </div>
        <div class="stat-card" style="border-top: 4px solid #f9ab00;">
            <div class="stat-icon" style="color: #f9ab00;"><i class="fas fa-users"></i></div>
            <div class="stat-number">1,560</div>
            <div class="stat-label">Jumlah Pengguna Aktif</div>
            <div class="stat-sub">Google Workspace for EDU</div>
        </div>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-tachometer-alt"></i> Rumusan Indikator Penggunaan (Data Audit KPM 04/08/2026)</h3>
        <table class="delima-table">
            <thead>
                <tr>
                    <th>Parameter Penilaian</th>
                    <th>Sasaran KPI KPM</th>
                    <th>Pencapaian SMJK AMC</th>
                    <th>Status Gred</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Peratus Keaktifan Guru</strong></td>
                    <td>Minimum 80.0%</td>
                    <td><strong>93.0%</strong> (100 daripada 107 guru aktif log masuk)</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Cemerlang (5 Bintang)</span></td>
                </tr>
                <tr>
                    <td><strong>Peratus Keaktifan Murid</strong></td>
                    <td>Minimum 70.0%</td>
                    <td><strong>100.0%</strong> (1,453 daripada 1,453 murid aktif log masuk)</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Cemerlang (5 Bintang)</span></td>
                </tr>
                <tr>
                    <td><strong>Peratus Penggunaan Keseluruhan</strong></td>
                    <td>Minimum 75.0%</td>
                    <td><strong>100.0%</strong> (1,560 pengguna aktif warga sekolah)</td>
                    <td><span class="badge badge-success"><i class="fas fa-trophy"></i> Penarafan Tertinggi</span></td>
                </tr>
                <tr>
                    <td><strong>Pengguna Google Apps & Drive</strong></td>
                    <td>Penggunaan Aktif</td>
                    <td><strong>1,560 orang</strong> menggunakan dokumen awan</td>
                    <td><span class="badge badge-info"><i class="fas fa-cloud"></i> Menyeluruh</span></td>
                </tr>
                <tr>
                    <td><strong>Pengguna Google Classroom</strong></td>
                    <td>PdP Guru</td>
                    <td><strong>96 orang guru</strong> aktif mengendalikan bilik darjah digital</td>
                    <td><span class="badge badge-success"><i class="fas fa-laptop"></i> 89.7% Guru</span></td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-file-alt"></i> Dokumen Bukti & Laporan Analisis E-Fail 2.0</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; margin-top: 12px;">
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); padding: 14px; border-radius: 6px;">
                <h4 style="margin: 0 0 6px; font-size: 14px;"><i class="fas fa-file-word" style="color: #2b579a;"></i> 2.1 Analisis Penggunaan Guru</h4>
                <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 10px;">Laporan terperinci log masuk guru mengikut panitia mata pelajaran.</p>
                <button class="btn-card btn-card-primary" onclick="previewDoc('Laporan Analisis Penggunaan DELIMa Guru 2026', '2.0 PEMBUDAYAAN DELIMa/2.1 Peratus Penggunaan Guru/Laporan Analisis Penggunaan DELIMa Guru 2026.docx')">Prapapar Laporan</button>
            </div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); padding: 14px; border-radius: 6px;">
                <h4 style="margin: 0 0 6px; font-size: 14px;"><i class="fas fa-file-word" style="color: #2b579a;"></i> 2.2 Analisis Penggunaan Murid</h4>
                <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 10px;">Laporan log masuk 1,453 murid Tingkatan 1 hingga Tingkatan 5.</p>
                <button class="btn-card btn-card-primary" onclick="previewDoc('Laporan Analisis Penggunaan DELIMa Murid 2026', '2.0 PEMBUDAYAAN DELIMa/2.2 Peratus Penggunaan Murid/Laporan Analisis Penggunaan DELIMa Murid 2026.docx')">Prapapar Laporan</button>
            </div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); padding: 14px; border-radius: 6px;">
                <h4 style="margin: 0 0 6px; font-size: 14px;"><i class="fas fa-file-word" style="color: #2b579a;"></i> 2.3 Rumusan KPI Keseluruhan</h4>
                <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 10px;">Laporan Penarafan 5 Bintang Kendiri Sekolah Sesi 2026.</p>
                <button class="btn-card btn-card-primary" onclick="previewDoc('Laporan Pencapaian KPI Penggunaan DELIMa Keseluruhan Sekolah 2026', '2.0 PEMBUDAYAAN DELIMa/2.3 Peratus Keseluruhan Sekolah/Laporan Pencapaian KPI Penggunaan DELIMa Keseluruhan Sekolah 2026.docx')">Prapapar Laporan</button>
            </div>
        </div>
    </div>
</main>
"""
with open('pages/pembudayaan.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Pembudayaan DELIMa", pembudayaan_body, depth=1, active='pembudayaan'))
print("Saved pages/pembudayaan.html")

# ------------------------------------------------------------------------------
# 10. PROMOSI & LATIHAN (pages/promosi.html)
# ------------------------------------------------------------------------------
promosi_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Promosi & Latihan (LADAP)", "3.0 Promosi", "promosi.html")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fas fa-bullhorn"></i> 3.0 Promosi & Latihan Pembudayaan DELIMa</h2>
            <p>Aktiviti Kesedaran Digital, Latihan Dalam Perkhidmatan (LADAP), Sudut DELIMa & Pertandingan Murid</p>
        </div>
        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
            <i class="fab fa-google-drive"></i> Folder E-Fail 3.0
        </a>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-chalkboard-teacher"></i> Inisiatif Promosi & Latihan Sesi 2026</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-top: 14px;">
            <div style="background: #ffffff; border: 1px solid var(--border-color); border-radius: 8px; padding: 16px;">
                <h4 style="color: var(--primary); margin-top: 0;"><i class="fas fa-flag"></i> 3.1 Pelancaran Bulan DELIMa</h4>
                <p style="font-size: 13px; color: var(--text-muted);">Pelancaran rasmi oleh Pengetua Pn. Tan Pei Nee dalam perhimpunan rasmi sekolah & edaran infografik log masuk ke saluran Telegram rasmi murid dan ibu bapa.</p>
                <button class="btn-card btn-card-primary" onclick="previewDoc('Laporan Promosi dan Pelancaran Bulan DELIMa 2026', '3.0 PROMOSI/3.1 Promosi & Pelancaran DELIMa/Laporan Promosi dan Pelancaran Bulan DELIMa 2026.docx')">Lihat Laporan</button>
            </div>
            
            <div style="background: #ffffff; border: 1px solid var(--border-color); border-radius: 8px; padding: 16px;">
                <h4 style="color: var(--primary); margin-top: 0;"><i class="fas fa-user-graduate"></i> 3.2 Kursus LADAP Guru</h4>
                <p style="font-size: 13px; color: var(--text-muted);">Bengkel AI Generatif (Google Gemini), Google Classroom & Canva for Education yang dikendalikan oleh Cik Au Chooi Yee untuk 106 orang guru.</p>
                <button class="btn-card btn-card-primary" onclick="previewDoc('Dokumentasi Kursus Dalaman Guru (LADAP DELIMa) 2026', '3.0 PROMOSI/3.2 Kursus Dalaman Guru (LADAP)/Dokumentasi Kursus Dalaman Guru (LADAP DELIMa) 2026.docx')">Lihat Laporan</button>
            </div>

            <div style="background: #ffffff; border: 1px solid var(--border-color); border-radius: 8px; padding: 16px;">
                <h4 style="color: var(--primary); margin-top: 0;"><i class="fas fa-laptop-code"></i> 3.3 Bengkel Celik Digital Murid</h4>
                <p style="font-size: 13px; color: var(--text-muted);">Latihan berstruktur celik digital, keselamatan siber (CyberSAFE) dan penggunaan alatan pembelajaran Google untuk murid Tingkatan 1 - 5.</p>
                <button class="btn-card btn-card-primary" onclick="previewDoc('Modul dan Laporan Bengkel Celik Digital Murid 2026', '3.0 PROMOSI/3.3 Aktiviti & Kursus Murid/Modul dan Laporan Bengkel Celik Digital Murid 2026.docx')">Lihat Laporan</button>
            </div>

            <div style="background: #ffffff; border: 1px solid var(--border-color); border-radius: 8px; padding: 16px;">
                <h4 style="color: var(--primary); margin-top: 0;"><i class="fas fa-tv"></i> 3.4 Sudut & Bilik DELIMa</h4>
                <p style="font-size: 13px; color: var(--text-muted);">Penyediaan papan kenyataan berinfografik, QR Code Meja Bantuan ID dan Bilik Khas Studio Digital SMJK Ave Maria Convent.</p>
                <button class="btn-card btn-card-primary" onclick="previewDoc('Dokumentasi Sudut dan Bilik DELIMa SMJK Ave Maria Convent 2026', '3.0 PROMOSI/3.4 Papan Kenyataan, Sudut & Bilik DELIMa/Dokumentasi Sudut dan Bilik DELIMa SMJK Ave Maria Convent 2026.docx')">Lihat Laporan</button>
            </div>

            <div style="background: #ffffff; border: 1px solid var(--border-color); border-radius: 8px; padding: 16px;">
                <h4 style="color: var(--primary); margin-top: 0;"><i class="fas fa-trophy"></i> 3.5 Pertandingan Digital</h4>
                <p style="font-size: 13px; color: var(--text-muted);">Pertandingan mereka bentuk poster Canva, video kreatif TikTok/YouTube ilmiah dan cabaran kuiz interaktif sempena Bulan ICT.</p>
                <button class="btn-card btn-card-primary" onclick="previewDoc('Kertas Kerja Pertandingan Kreativiti Digital Murid 2026', '3.0 PROMOSI/3.5 Pertandingan Berkaitan DELIMa/Kertas Kerja Pertandingan Kreativiti Digital Murid 2026.docx')">Lihat Kertas Kerja</button>
            </div>
        </div>
    </div>
</main>
"""
with open('pages/promosi.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Promosi & Latihan DELIMa", promosi_body, depth=1, active='pembudayaan'))
print("Saved pages/promosi.html")

# ------------------------------------------------------------------------------
# 11. PENGURUSAN SEKOLAH (pages/pengurusan-sekolah.html)
# ------------------------------------------------------------------------------
pengurusan_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Penggunaan DELIMa Pengurusan", "4.0 Pengurusan Sekolah", "pengurusan-sekolah.html")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fas fa-school"></i> 4.0 Penggunaan DELIMa dalam Pengurusan Sekolah</h2>
            <p>Integrasi Ekosistem Digital dalam Pentadbiran, Kurikulum (e-RPH), Hal Ehwal Murid & Kokurikulum</p>
        </div>
        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
            <i class="fab fa-google-drive"></i> Folder E-Fail 4.0
        </a>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-cogs"></i> 4 Dimensi Utama Integrasi Digital Sekolah</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 18px; margin-top: 14px;">
            <div style="background: #ffffff; border-left: 4px solid var(--primary); padding: 16px; border-radius: 6px; box-shadow: var(--shadow-sm);">
                <h4 style="color: var(--primary); margin-top: 0;"><i class="fas fa-briefcase"></i> 4.1 Pentadbiran Digital (Paperless)</h4>
                <p style="font-size: 13px; color: var(--text-dark);">Pengurusan surat menyurat, minit mesyuarat guru dan takwim sekolah tanpa kertas menggunakan Google Shared Drives Pentadbiran serta pengesahan kehadiran mesyuarat digital.</p>
                <button class="btn-card btn-card-primary" onclick="previewDoc('Integrasi DELIMa dalam Pengurusan Pentadbiran Sekolah 2026', '4.0 PENGGUNAAN DELIMa PENGURUSAN SEKOLAH/4.1 DELIMa dalam Pengurusan/Integrasi DELIMa dalam Pengurusan Pentadbiran Sekolah 2026.docx')">Prapapar Dokumen</button>
            </div>

            <div style="background: #ffffff; border-left: 4px solid #1a73e8; padding: 16px; border-radius: 6px; box-shadow: var(--shadow-sm);">
                <h4 style="color: #1a73e8; margin-top: 0;"><i class="fas fa-book-open"></i> 4.2 Kurikulum: e-RPH & Bank Sumber</h4>
                <p style="font-size: 13px; color: var(--text-dark);">Penyediaan Rancangan Pengajaran Harian secara elektronik (e-RPH) menggunakan Google Classroom dan perkongsian bahan kurikulum melalui Bank Sumber Digital Panitia.</p>
                <button class="btn-card btn-card-primary" onclick="previewDoc('Pengurusan e-RPH dan Bank Sumber Digital Kurikulum 2026', '4.0 PENGGUNAAN DELIMa PENGURUSAN SEKOLAH/4.2 DELIMa dalam Kurikulum (eRPH)/Pengurusan e-RPH dan Bank Sumber Digital Kurikulum 2026.docx')">Prapapar Dokumen</button>
            </div>

            <div style="background: #ffffff; border-left: 4px solid #1e8e3e; padding: 16px; border-radius: 6px; box-shadow: var(--shadow-sm);">
                <h4 style="color: #1e8e3e; margin-top: 0;"><i class="fas fa-user-check"></i> 4.3 Hal Ehwal Murid: e-Kehadiran</h4>
                <p style="font-size: 13px; color: var(--text-dark);">Sistem pemantauan e-Kehadiran harian murid secara masa nyata (real-time) dan pengurusan data sahsiah murid melalui borang Google & Dashboard APDM KPM.</p>
                <button class="btn-card btn-card-primary" onclick="previewDoc('Sistem e-Kehadiran dan Pengurusan HEM Digital 2026', '4.0 PENGGUNAAN DELIMa PENGURUSAN SEKOLAH/4.4 DELIMa dalam Hal Ehwal Murid (HEM)/Sistem e-Kehadiran dan Pengurusan HEM Digital 2026.docx')">Prapapar Dokumen</button>
            </div>

            <div style="background: #ffffff; border-left: 4px solid #f9ab00; padding: 16px; border-radius: 6px; box-shadow: var(--shadow-sm);">
                <h4 style="color: #b06000; margin-top: 0;"><i class="fas fa-running"></i> 4.4 Kokurikulum: Pelaporan Digital</h4>
                <p style="font-size: 13px; color: var(--text-dark);">Sistem pelaporan kehadiran aktiviti mingguan kelab, persatuan, unit beruniform dan sukan permainan serta penjanaan sijil penyertaan digital (e-Certificate).</p>
                <button class="btn-card btn-card-primary" onclick="previewDoc('Sistem Pengurusan dan Pelaporan Kokurikulum Digital 2026', '4.0 PENGGUNAAN DELIMa PENGURUSAN SEKOLAH/4.3 DELIMa dalam Kokurikulum/Sistem Pengurusan dan Pelaporan Kokurikulum Digital 2026.docx')">Prapapar Dokumen</button>
            </div>
        </div>
    </div>
</main>
"""
with open('pages/pengurusan-sekolah.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Pengurusan Sekolah DELIMa", pengurusan_body, depth=1, active='pengurusan'))
print("Saved pages/pengurusan-sekolah.html")

# ------------------------------------------------------------------------------
# 12. PENSIJILAN GURU (pages/pensijilan.html - 106 Teachers Table!)
# ------------------------------------------------------------------------------
teacher_rows_html = []
for t in teachers:
    gce1_badge = '<span class="badge badge-success"><i class="fas fa-check"></i> GCE L1</span>' if t['gce_lv1'] else '<span style="color: #999;">-</span>'
    gce2_badge = '<span class="badge badge-primary"><i class="fas fa-star"></i> GCE L2</span>' if t['gce_lv2'] else '<span style="color: #999;">-</span>'
    gemini_badge = '<span class="badge badge-info"><i class="fas fa-robot"></i> Gemini AI</span>' if t['gemini'] else '<span style="color: #999;">-</span>'
    apple_badge = '<span class="badge badge-warning"><i class="fab fa-apple"></i> Apple</span>' if t['apple_teacher'] else '<span style="color: #999;">-</span>'
    
    teacher_rows_html.append(f"""
        <tr class="teacher-row" data-name="{t['name']}" data-gcelv1="{'true' if t['gce_lv1'] else 'false'}" data-gcelv2="{'true' if t['gce_lv2'] else 'false'}" data-gemini="{'true' if t['gemini'] else 'false'}" data-apple="{'true' if t['apple_teacher'] else 'false'}">
            <td>{t['bil']}</td>
            <td><strong>{t['name']}</strong></td>
            <td style="text-align: center;">{gce1_badge}</td>
            <td style="text-align: center;">{gce2_badge}</td>
            <td style="text-align: center;">{gemini_badge}</td>
            <td style="text-align: center;">{apple_badge}</td>
        </tr>
    """)

teachers_table_html = "\n".join(teacher_rows_html)

pensijilan_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Direktori Pensijilan Guru", "5.0 Pensijilan", "pensijilan.html")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fas fa-user-graduate"></i> 5.0 Direktori Pensijilan Digital Guru 2026</h2>
            <p>Senarai Lengkap {total_teachers} Orang Pendidik Bertauliah Antarabangsa SMJK Ave Maria Convent, Ipoh</p>
        </div>
        <div style="display: flex; gap: 8px;">
            <a href="sijil-gce.html" class="btn-card btn-card-primary">
                <i class="fab fa-google"></i> Galeri GCE
            </a>
            <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
                <i class="fab fa-google-drive"></i> Folder E-Fail 5.0
            </a>
        </div>
    </div>

    <!-- Certification Stats Counters -->
    <div class="stats-grid">
        <div class="stat-card" style="border-top: 4px solid #1a73e8;">
            <div class="stat-icon" style="color: #1a73e8;"><i class="fab fa-google"></i></div>
            <div class="stat-number">{stats['gce_lv1']} / {total_teachers}</div>
            <div class="stat-label">Google Certified Educator L1</div>
            <div class="stat-sub">97.2% Guru Bertauliah</div>
        </div>
        <div class="stat-card" style="border-top: 4px solid #b71c1c;">
            <div class="stat-icon" style="color: #b71c1c;"><i class="fas fa-star"></i></div>
            <div class="stat-number">{stats['gce_lv2']}</div>
            <div class="stat-label">GCE Level 2 (Advanced)</div>
            <div class="stat-sub">19.8% Guru Pakar</div>
        </div>
        <div class="stat-card" style="border-top: 4px solid #7b1fa2;">
            <div class="stat-icon" style="color: #7b1fa2;"><i class="fas fa-robot"></i></div>
            <div class="stat-number">{stats['gemini']}</div>
            <div class="stat-label">Gemini AI Generatif</div>
            <div class="stat-sub">22.6% Guru Bertauliah AI</div>
        </div>
        <div class="stat-card" style="border-top: 4px solid #555555;">
            <div class="stat-icon" style="color: #555555;"><i class="fab fa-apple"></i></div>
            <div class="stat-number">{stats['apple_teacher']}</div>
            <div class="stat-label">Apple Teacher</div>
            <div class="stat-sub">7.5% Guru Diperakui</div>
        </div>
    </div>

    <!-- Interactive Search and Filter Box -->
    <div class="content-box">
        <h3><i class="fas fa-search"></i> Carian Direktori Guru Bertauliah</h3>
        
        <div class="search-filter-box">
            <input type="text" id="teacherSearch" class="search-input" placeholder="Taip nama guru (cth: Au Chooi Yee, Tan Pei Nee, Nurain)...">
            <select id="certFilter" class="filter-select">
                <option value="all">Semua Pensijilan (106 Guru)</option>
                <option value="gce_lv1">Google Certified Educator L1 ({stats['gce_lv1']} Guru)</option>
                <option value="gce_lv2">Google Certified Educator L2 ({stats['gce_lv2']} Guru)</option>
                <option value="gemini">Gemini Generative AI ({stats['gemini']} Guru)</option>
                <option value="apple">Apple Teacher ({stats['apple_teacher']} Guru)</option>
            </select>
        </div>

        <table class="delima-table" id="teachersTable">
            <thead>
                <tr>
                    <th style="width: 5%;">Bil</th>
                    <th>Nama Penuh Guru</th>
                    <th style="width: 15%; text-align: center;">GCE Level 1</th>
                    <th style="width: 15%; text-align: center;">GCE Level 2</th>
                    <th style="width: 15%; text-align: center;">Gemini AI</th>
                    <th style="width: 15%; text-align: center;">Apple Teacher</th>
                </tr>
            </thead>
            <tbody>
                {teachers_table_html}
            </tbody>
        </table>

        <div style="margin-top: 16px;">
            <button class="btn-card btn-card-primary" onclick="previewDoc('Direktori Guru Bertauliah Google (GCE Level 1, 2 dan Trainer) 2026', '5.0 PENSIJILAN DELIMa GURU/5.2 Google Certified Educator (GCE L1, L2 & Trainer)/Direktori Guru Bertauliah Google (GCE Level 1, 2 dan Trainer) 2026.docx')">
                <i class="fas fa-file-alt"></i> Prapapar Direktori E-Fail 5.2
            </button>
        </div>
    </div>
</main>
"""
with open('pages/pensijilan.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Direktori Pensijilan Guru", pensijilan_body, depth=1, active='pensijilan'))
print("Saved pages/pensijilan.html")

# ------------------------------------------------------------------------------
# 13. SIJIL GCE (pages/sijil-gce.html)
# ------------------------------------------------------------------------------
gce_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Sijil & Poster GCE", "5.0 Pensijilan", "pensijilan.html")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fab fa-google"></i> Google Certified Educator (GCE) Showcase</h2>
            <p>Pencapaian Pensijilan Antarabangsa Google for Education Pendidik SMJK Ave Maria Convent, Ipoh</p>
        </div>
        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
            <i class="fab fa-google-drive"></i> Folder E-Fail 5.2
        </a>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-medal"></i> Tahap Pensijilan Google di SMJK Ave Maria Convent</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 16px;">
            <div style="border: 2px solid #1a73e8; border-radius: 8px; padding: 20px; text-align: center; background: #f8fbff;">
                <i class="fab fa-google" style="font-size: 40px; color: #1a73e8; margin-bottom: 10px;"></i>
                <h4 style="color: #1a73e8; margin-top: 0;">GCE LEVEL 1 (EDUCATOR)</h4>
                <p style="font-size: 13px; color: var(--text-dark); margin-bottom: 12px;">Membuktikan kemahiran asas pengintegrasian Google Workspace for Education dalam bilik darjah.</p>
                <div style="font-family: var(--font-heading); font-size: 24px; font-weight: 700; color: #1a73e8;">{stats['gce_lv1']} ORANG GURU</div>
                <span class="badge badge-success" style="margin-top: 6px;"><i class="fas fa-check"></i> 97.2% Guru AMC</span>
            </div>

            <div style="border: 2px solid #b71c1c; border-radius: 8px; padding: 20px; text-align: center; background: #fff8f8;">
                <i class="fas fa-star" style="font-size: 40px; color: #b71c1c; margin-bottom: 10px;"></i>
                <h4 style="color: #b71c1c; margin-top: 0;">GCE LEVEL 2 (ADVANCED)</h4>
                <p style="font-size: 13px; color: var(--text-dark); margin-bottom: 12px;">Membuktikan penguasaan pedagogi aras tinggi dan strategi kolaboratif digital lanjutan.</p>
                <div style="font-family: var(--font-heading); font-size: 24px; font-weight: 700; color: #b71c1c;">{stats['gce_lv2']} ORANG GURU</div>
                <span class="badge badge-primary" style="margin-top: 6px;"><i class="fas fa-award"></i> 19.8% Guru Pakar</span>
            </div>

            <div style="border: 2px solid #7b1fa2; border-radius: 8px; padding: 20px; text-align: center; background: #faf5fc;">
                <i class="fas fa-robot" style="font-size: 40px; color: #7b1fa2; margin-bottom: 10px;"></i>
                <h4 style="color: #7b1fa2; margin-top: 0;">GEMINI AI EDUCATOR</h4>
                <p style="font-size: 13px; color: var(--text-dark); margin-bottom: 12px;">Kemahiran memanfaatkan Kecerdasan Buatan Generatif untuk PdP abad ke-21.</p>
                <div style="font-family: var(--font-heading); font-size: 24px; font-weight: 700; color: #7b1fa2;">{stats['gemini']} ORANG GURU</div>
                <span class="badge badge-info" style="margin-top: 6px;"><i class="fas fa-microchip"></i> 22.6% Guru Inovatif</span>
            </div>
        </div>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-info-circle"></i> Panduan Peperiksaan & Kursus DCTP KPM</h3>
        <p style="font-size: 13px; color: var(--text-dark); line-height: 1.6;">
            Program latihan pensijilan Google Certified Educator ini dilaksanakan secara berfasa melalui <strong>DELIMa Certified Training Programme (DCTP)</strong> dengan bimbingan Guru Jurulatih Utama (Cik Au Chooi Yee). Peperiksaan dijalankan secara dalam talian dengan pemantauan KPM.
        </p>
        <div style="margin-top: 14px;">
            <a href="pensijilan.html" class="btn-card btn-card-primary"><i class="fas fa-list"></i> Lihat Direktori Lengkap</a>
            <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive"><i class="fab fa-google-drive"></i> Arkib Sijil Google Drive</a>
        </div>
    </div>
</main>
"""
with open('pages/sijil-gce.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Sijil & Poster GCE", gce_body, depth=1, active='pensijilan'))
print("Saved pages/sijil-gce.html")

# ------------------------------------------------------------------------------
# 14. SIJIL MICROSOFT & APPLE (pages/sijil-microsoft.html)
# ------------------------------------------------------------------------------
ms_apple_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Sijil Microsoft & Apple", "5.0 Pensijilan", "pensijilan.html")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fab fa-microsoft"></i> Pensijilan Microsoft Educator & Apple Teacher</h2>
            <p>Pengiktirafan Pelbagai Platform Teknologi Pendidikan Warga Guru SMJK Ave Maria Convent, Ipoh</p>
        </div>
        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
            <i class="fab fa-google-drive"></i> Folder E-Fail 5.3 & 5.4
        </a>
    </div>

    <div class="content-box">
        <h3><i class="fab fa-apple"></i> Pensijilan Apple Teacher (8 Orang Guru)</h3>
        <p style="font-size: 13px; color: var(--text-dark);">Guru-guru SMJK AMC telah menamatkan lencana modul kreativiti Apple Learning Centre (Pages, Keynote, Numbers, GarageBand & iMovie):</p>
        <table class="delima-table">
            <thead>
                <tr>
                    <th>Bil</th>
                    <th>Nama Pendidik Apple Teacher</th>
                    <th>Platform Pensijilan</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1</td>
                    <td><strong>AU CHOOI YEE</strong></td>
                    <td>Apple Teacher Learning Centre (Mac & iPad)</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td>
                </tr>
                <tr>
                    <td>2</td>
                    <td><strong>LOH YI WEN</strong></td>
                    <td>Apple Teacher Recognition</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td>
                </tr>
                <tr>
                    <td>3</td>
                    <td><strong>NG KAH KEAT</strong></td>
                    <td>Apple Teacher Recognition</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td>
                </tr>
                <tr>
                    <td>4</td>
                    <td><strong>NG SIN CHEE</strong></td>
                    <td>Apple Teacher Recognition</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td>
                </tr>
                <tr>
                    <td>5</td>
                    <td><strong>NURUL IZZATI BINTI RUSDI</strong></td>
                    <td>Apple Teacher Recognition</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td>
                </tr>
                <tr>
                    <td>6</td>
                    <td><strong>SITI ASMAH BINTI BAHARUDDIN</strong></td>
                    <td>Apple Teacher Recognition</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td>
                </tr>
                <tr>
                    <td>7</td>
                    <td><strong>TAN LIH LIN</strong></td>
                    <td>Apple Teacher Recognition</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td>
                </tr>
                <tr>
                    <td>8</td>
                    <td><strong>YONG JIN CHIAT</strong></td>
                    <td>Apple Teacher Recognition</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="content-box">
        <h3><i class="fab fa-microsoft"></i> Microsoft Innovative Educator (MIE)</h3>
        <p style="font-size: 13px; color: var(--text-dark);">Penyertaan kursus profesional Microsoft Learn dan integrasi alatan kolaborasi Microsoft Teams serta OneNote dalam pembelajaran harian.</p>
        <div style="margin-top: 14px;">
            <button class="btn-card btn-card-primary" onclick="previewDoc('Rekod Pensijilan Microsoft Educator 2026', '5.0 PENSIJILAN DELIMa GURU/5.3 Microsoft Certified Educator & Showcase/Rekod Pensijilan Microsoft Educator 2026.docx')">
                <i class="fas fa-file-alt"></i> Prapapar Rekod Pensijilan Microsoft
            </button>
        </div>
    </div>
</main>
"""
with open('pages/sijil-microsoft.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Sijil Microsoft & Apple", ms_apple_body, depth=1, active='pensijilan'))
print("Saved pages/sijil-microsoft.html")

print("Generator script part 4 completed.")
