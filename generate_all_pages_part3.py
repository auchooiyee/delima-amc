# -*- coding: utf-8 -*-
"""
Part 3 of DELIMa Page Generator
SMJK Ave Maria Convent, Ipoh (AEB2052)
"""

import os
import json

DRIVE_URL = "https://drive.google.com/drive/folders/10HBSO2m-RKMAEJPsKmPmHZ1HU6zw4-y8?usp=sharing"

from generate_pages import wrap_html
from generate_all_pages import get_breadcrumbs

# Load teacher data
with open('assets/data/teachers_certifications.json', 'r', encoding='utf-8') as f:
    teachers_info = json.load(f)

teachers = teachers_info.get('teachers', [])

# ------------------------------------------------------------------------------
# 9. PEMBUDAYAAN DELIMA (pages/pembudayaan.html)
# ------------------------------------------------------------------------------
pembudayaan_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Pembudayaan DELIMa", "2.0 Pembudayaan", "pembudayaan.html")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fas fa-chart-line"></i> 2.0 Pembudayaan DELIMa Sekolah</h2>
            <p>Analisis Data Penggunaan, KPI Penarafan Kendiri 5 Bintang KPM & Pelan Pembudayaan Digital 2026</p>
        </div>
        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
            <i class="fab fa-google-drive"></i> Folder E-Fail 2.0
        </a>
    </div>

    <!-- KPI Summary Card -->
    <div class="content-box">
        <h3><i class="fas fa-trophy"></i> Skor Penarafan Kendiri DELIMa KPM 2026</h3>
        <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 16px;">
            Berdasarkan data analitik rasmi Kementerian Pendidikan Malaysia (KPM) sesi Ogos 2026, SMJK Ave Maria Convent telah mencapai penarafan <strong>5 BINTANG</strong> dengan purata penggunaan murid 100% dan guru 93.0%.
        </p>

        <table class="delima-table">
            <thead>
                <tr>
                    <th>Indikator Prestasi Utama (KPI)</th>
                    <th>Sasaran KPM</th>
                    <th>Pencapaian SMJK AMC</th>
                    <th>Status Penarafan</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Peratus Keaktifan Murid (Log Masuk)</strong></td>
                    <td>80.0%</td>
                    <td><strong>100.0%</strong> (1,453 / 1,453 murid)</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Cemerlang</span></td>
                </tr>
                <tr>
                    <td><strong>Peratus Keaktifan Guru</strong></td>
                    <td>85.0%</td>
                    <td><strong>93.0%</strong> (100 / 107 guru aktif)</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Cemerlang</span></td>
                </tr>
                <tr>
                    <td><strong>Penggunaan Aplikasi Google Workspace</strong></td>
                    <td>60.0%</td>
                    <td><strong>100.0%</strong> (1,560 pengguna aktif)</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Cemerlang</span></td>
                </tr>
                <tr>
                    <td><strong>Penggunaan Google Classroom (PdP Maya)</strong></td>
                    <td>50.0%</td>
                    <td><strong>90.5%</strong> (96 kelas aktif mingguan)</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Cemerlang</span></td>
                </tr>
                <tr style="background: #e8eaf6; font-weight: 700;">
                    <td>PENARAFAN KESELURUHAN SEKOLAH</td>
                    <td>4 Bintang</td>
                    <td><strong>5 BINTANG (100% KPI MAKSIMUM)</strong></td>
                    <td><span class="badge badge-success" style="font-size: 12px; padding: 4px 10px;"><i class="fas fa-star"></i> 5 BINTANG</span></td>
                </tr>
            </tbody>
        </table>

        <div style="margin-top: 16px;">
            <button class="btn-card btn-card-primary" onclick="previewDoc('Analisis Tahap Penggunaan DELIMa Warga Sekolah (Dashboard KPM) 2026', '2.0 PEMBUDAYAAN DELIMA/2.1 Analisis Penggunaan/Analisis Tahap Penggunaan DELIMa Warga Sekolah (Dashboard KPM).docx')">
                <i class="fas fa-file-alt"></i> Prapapar Laporan Analisis
            </button>
        </div>
    </div>
</main>
"""
with open('pages/pembudayaan.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Pembudayaan DELIMa", pembudayaan_body, depth=1, active='pembudayaan'))

# ------------------------------------------------------------------------------
# 10. PROMOSI & LATIHAN (pages/promosi.html)
# ------------------------------------------------------------------------------
promosi_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Promosi & Latihan", "2.0 Pembudayaan", "promosi.html")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fas fa-bullhorn"></i> 3.0 Promosi & Latihan Pembudayaan DELIMa</h2>
            <p>Aktiviti Pelancaran Bulan DELIMa, Kursus Latihan Dalam Perkhidmatan (LADAP) & Bengkel Literasi Digital Murid</p>
        </div>
        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
            <i class="fab fa-google-drive"></i> Folder E-Fail 3.0
        </a>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-chalkboard-teacher"></i> Takwim Latihan Guru & Murid 2026</h3>
        <table class="delima-table">
            <thead>
                <tr>
                    <th>Tarikh / Bulan</th>
                    <th>Nama Program / Bengkel</th>
                    <th>Kumpulan Sasaran</th>
                    <th>Penceramah / Fasilitator</th>
                    <th>Evidens</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Feb 2026</strong></td>
                    <td><strong>Pensijilan Google Certified Educator (Level 1)</strong></td>
                    <td>Semua Guru SMJK AMC (106 Guru)</td>
                    <td>Cik Au Chooi Yee</td>
                    <td><button class="btn-card btn-card-drive" onclick="previewDoc('Pensijilan Google Certified Educator (Level 1)', '3.0 PROMOSI/3.2 Latihan/Laporan LADAP Aplikasi DELIMa 2026.docx')">Lihat OPR</button></td>
                </tr>
                <tr>
                    <td><strong>Mac 2026</strong></td>
                    <td><strong>Pelancaran Bulan Pembudayaan DELIMa & Galakan ID Digital</strong></td>
                    <td>Semua Warga Sekolah (1,560 orang)</td>
                    <td>Unit ICT & Penyelaras DELIMa</td>
                    <td><button class="btn-card btn-card-drive" onclick="previewDoc('Laporan Pelancaran Bulan DELIMa', '3.0 PROMOSI/3.1 Promosi/Laporan Bergambar Promosi DELIMa 2026.docx')">Lihat OPR</button></td>
                </tr>
                <tr>
                    <td><strong>Jun 2026</strong></td>
                    <td><strong>Bengkel Celik Digital & Keselamatan Siber Murid Tingkatan 1-5</strong></td>
                    <td>Semua Murid AMC</td>
                    <td>Guru ICT</td>
                    <td><button class="btn-card btn-card-drive" onclick="previewDoc('Laporan Bengkel Literasi Digital Murid', '3.0 PROMOSI/3.2 Latihan/Laporan Bengkel Literasi Digital Murid 2026.docx')">Lihat OPR</button></td>
                </tr>
                <tr>
                    <td><strong>Ogos 2026</strong></td>
                    <td><strong>Program Latihan Peningkatan Kaedah Pengajaran dan Pembelajaran Berasaskan Kecergasan Buatan (AI)</strong></td>
                    <td>Semua Guru SMJK AMC (106 Guru)</td>
                    <td>Cik Au Chooi Yee</td>
                    <td><button class="btn-card btn-card-drive" onclick="previewDoc('Program Latihan Peningkatan Kaedah Pengajaran dan Pembelajaran Berasaskan Kecergasan Buatan (AI)', '3.0 PROMOSI/3.2 Latihan/Laporan LADAP Aplikasi DELIMa 2026.docx')">Lihat OPR</button></td>
                </tr>
            </tbody>
        </table>
    </div>
</main>
"""
with open('pages/promosi.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Promosi & Latihan", promosi_body, depth=1, active='pembudayaan'))

# ------------------------------------------------------------------------------
# 11. PENGURUSAN SEKOLAH (pages/pengurusan-sekolah.html)
# ------------------------------------------------------------------------------
pengurusan_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Pengurusan Sekolah", "4.0 Pengurusan", "pengurusan-sekolah.html")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fas fa-school"></i> 4.0 Penggunaan DELIMa dalam Pengurusan Sekolah</h2>
            <p>Integrasi Pentadbiran Digital, Kurikulum e-RPH, Pengurusan Hal Ehwal Murid (HEM) & Kokurikulum</p>
        </div>
        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
            <i class="fab fa-google-drive"></i> Folder E-Fail 4.0
        </a>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-cogs"></i> Sistem & Inisiatif Pengurusan Digital</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-top: 14px;">
            <div style="background: #ffffff; border: 1px solid var(--border-color); border-radius: 8px; padding: 16px;">
                <h4 style="color: var(--primary); margin-top: 0;"><i class="fas fa-file-signature"></i> 4.1 Modul e-RPH Digital</h4>
                <p style="font-size: 13px; color: var(--text-dark);">Penyediaan dan penghantaran Rekod Pengajaran Harian secara 100% digital tanpa kertas (Paperless) menggunakan Google Docs / Google Drive.</p>
                <button class="btn-card btn-card-primary" onclick="previewDoc('Garis Panduan e-RPH Sekolah 2026', '4.0 PENGGUNAAN DELIMa PENGURUSAN SEKOLAH/4.1 e-RPH/Garis Panduan Penyediaan e-RPH DELIMa 2026.docx')">Prapapar Dokumen</button>
            </div>

            <div style="background: #ffffff; border: 1px solid var(--border-color); border-radius: 8px; padding: 16px;">
                <h4 style="color: var(--primary); margin-top: 0;"><i class="fas fa-user-check"></i> 4.2 Pengurusan Hal Ehwal Murid (HEM)</h4>
                <p style="font-size: 13px; color: var(--text-dark);">Pemantauan e-Kehadiran harian murid APDM, pengurusan bantuan kebajikan murid, dan pemantauan disiplin berasaskan storan awan selamat.</p>
                <button class="btn-card btn-card-primary" onclick="previewDoc('Laporan Penggunaan DELIMa dalam HEM 2026', '4.0 PENGGUNAAN DELIMa PENGURUSAN SEKOLAH/4.2 DELIMa dalam HEM/Laporan Penggunaan DELIMa dalam Hal Ehwal Murid 2026.docx')">Prapapar Dokumen</button>
            </div>

            <div style="background: #ffffff; border: 1px solid var(--border-color); border-radius: 8px; padding: 16px;">
                <h4 style="color: var(--primary); margin-top: 0;"><i class="fas fa-trophy"></i> 4.3 Pengurusan Kokurikulum Digital</h4>
                <p style="font-size: 13px; color: var(--text-dark);">Sistem pelaporan kehadiran aktiviti mingguan kelab, persatuan, unit beruniform dan sukan permainan serta penjanaan sijil penyertaan digital (e-Certificate).</p>
                <button class="btn-card btn-card-primary" onclick="previewDoc('Sistem Pengurusan dan Pelaporan Kokurikulum Digital 2026', '4.0 PENGGUNAAN DELIMa PENGURUSAN SEKOLAH/4.3 DELIMa dalam Kokurikulum/Sistem Pengurusan dan Pelaporan Kokurikulum Digital 2026.docx')">Prapapar Dokumen</button>
            </div>
        </div>
    </div>
</main>
"""
with open('pages/pengurusan-sekolah.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Pengurusan Sekolah DELIMa", pengurusan_body, depth=1, active='pengurusan'))

# ------------------------------------------------------------------------------
# 12. PENSIJILAN GURU (pages/pensijilan.html - 106 Teachers Table!)
# ------------------------------------------------------------------------------
teacher_rows_html = []
for t in teachers:
    t_name = t.get('name') or t.get('nama') or ''
    g1 = t.get('gce_l1') or t.get('gce_lv1') or False
    g2 = t.get('gce_l2') or t.get('gce_lv2') or False
    gem = t.get('gemini') or False
    app = t.get('apple') or t.get('apple_teacher') or False

    gce1_badge = '<span class="badge badge-success"><i class="fas fa-check"></i> GCE L1</span>' if g1 else '<span style="color: #999;">-</span>'
    gce2_badge = '<span class="badge badge-primary"><i class="fas fa-star"></i> GCE L2</span>' if g2 else '<span style="color: #999;">-</span>'
    gemini_badge = '<span class="badge badge-info"><i class="fas fa-robot"></i> Gemini AI</span>' if gem else '<span style="color: #999;">-</span>'
    apple_badge = '<span class="badge badge-warning"><i class="fab fa-apple"></i> Apple</span>' if app else '<span style="color: #999;">-</span>'
    
    teacher_rows_html.append(f"""
        <tr class="teacher-row" data-name="{t_name}" data-gcelv1="{'true' if g1 else 'false'}" data-gcelv2="{'true' if g2 else 'false'}" data-gemini="{'true' if gem else 'false'}" data-apple="{'true' if app else 'false'}">
            <td>{t.get('bil', '')}</td>
            <td><strong>{t_name}</strong></td>
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
            <p>Pangkalan Data Rasmi Pentauliahan Profesional Google, Microsoft, Apple & Gemini AI (106 Guru SMJK AMC)</p>
        </div>
        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
            <i class="fab fa-google-drive"></i> Folder E-Fail 5.0
        </a>
    </div>

    <!-- Summary Stats Bar -->
    <div class="stats-grid">
        <div class="stat-card">
            <div class="stat-icon" style="color: var(--primary);"><i class="fas fa-certificate"></i></div>
            <div class="stat-number">106 ORANG</div>
            <div class="stat-label">Jumlah Pendidik AMC</div>
            <div class="stat-sub">100% Memiliki Sijil Digital</div>
        </div>
        <div class="stat-card">
            <div class="stat-icon" style="color: #1a73e8;"><i class="fab fa-google"></i></div>
            <div class="stat-number">106 ORANG</div>
            <div class="stat-label">Google Educator L1</div>
            <div class="stat-sub">100.0% Guru Bertauliah</div>
        </div>
        <div class="stat-card">
            <div class="stat-icon" style="color: var(--primary);"><i class="fas fa-star"></i></div>
            <div class="stat-number">21 ORANG</div>
            <div class="stat-label">Google Educator L2</div>
            <div class="stat-sub">19.8% Guru Pakar</div>
        </div>
        <div class="stat-card">
            <div class="stat-icon" style="color: #7b1fa2;"><i class="fas fa-robot"></i></div>
            <div class="stat-number">24 ORANG</div>
            <div class="stat-label">Gemini AI Educator</div>
            <div class="stat-sub">22.6% AI Generatif</div>
        </div>
        <div class="stat-card">
            <div class="stat-icon" style="color: #333333;"><i class="fab fa-apple"></i></div>
            <div class="stat-number">8 ORANG</div>
            <div class="stat-label">Apple Teacher</div>
            <div class="stat-sub">7.5% Mac & iPad</div>
        </div>
    </div>

    <!-- Interactive Search & Table -->
    <div class="content-box">
        <h3><i class="fas fa-search"></i> Carian & Penapis Direktori Pendidik</h3>
        
        <div class="search-filter-box">
            <input type="text" id="teacherSearch" class="search-input" placeholder="Taip nama guru untuk carian pantas...">
            <select id="certFilter" class="filter-select">
                <option value="all">Semua Jenis Pensijilan</option>
                <option value="gce_lv1">Google Certified Educator L1 (106 Guru)</option>
                <option value="gce_lv2">Google Certified Educator L2 (21 Guru)</option>
                <option value="gemini">Gemini AI Educator (24 Guru)</option>
                <option value="apple">Apple Teacher (8 Guru)</option>
            </select>
        </div>

        <table class="delima-table">
            <thead>
                <tr>
                    <th style="width: 5%;">Bil</th>
                    <th style="width: 45%;">Nama Penuh Guru</th>
                    <th style="text-align: center; width: 12%;">GCE Level 1</th>
                    <th style="text-align: center; width: 12%;">GCE Level 2</th>
                    <th style="text-align: center; width: 13%;">Gemini AI</th>
                    <th style="text-align: center; width: 13%;">Apple Teacher</th>
                </tr>
            </thead>
            <tbody id="teacherTableBody">
                {teachers_table_html}
            </tbody>
        </table>
    </div>
</main>
"""
with open('pages/pensijilan.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Direktori Pensijilan Guru", pensijilan_body, depth=1, active='pensijilan'))

# ------------------------------------------------------------------------------
# 13. SIJIL GOOGLE (pages/sijil-gce.html)
# ------------------------------------------------------------------------------
gce_l2_list_html = """
<tr><td>1</td><td><strong>AU CHOOI YEE</strong></td><td>Google Certified Educator Level 1 & 2</td><td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td></tr>
<tr><td>2</td><td><strong>CHONG MENG HONG</strong></td><td>Google Certified Educator Level 1 & 2</td><td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td></tr>
<tr><td>3</td><td><strong>FARAH NOOR AINA SALWA TAJUDDIN</strong></td><td>Google Certified Educator Level 1 & 2</td><td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td></tr>
<tr><td>4</td><td><strong>FONG JEN LIN</strong></td><td>Google Certified Educator Level 1 & 2</td><td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td></tr>
<tr><td>5</td><td><strong>GOH SAW LIN</strong></td><td>Google Certified Educator Level 1 & 2</td><td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td></tr>
<tr><td>6</td><td><strong>KOO SOK FONG</strong></td><td>Google Certified Educator Level 1 & 2</td><td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td></tr>
<tr><td>7</td><td><strong>LOW CHIU YEN</strong></td><td>Google Certified Educator Level 1 & 2</td><td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td></tr>
<tr><td>8</td><td><strong>MUHAMMAD SAIFUL ZAYANNI BIN ABD RAHMAN</strong></td><td>Google Certified Educator Level 1 & 2</td><td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td></tr>
<tr><td>9</td><td><strong>NG CHIAH PING</strong></td><td>Google Certified Educator Level 1 & 2</td><td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td></tr>
<tr><td>10</td><td><strong>NISSA NABILA BINTI KAMARUZAMAN</strong></td><td>Google Certified Educator Level 1 & 2</td><td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td></tr>
<tr><td>11</td><td><strong>NUR ADRIANA BINTI HAJI SHAIDAN</strong></td><td>Google Certified Educator Level 1 & 2</td><td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td></tr>
<tr><td>12</td><td><strong>NUR AYU ANISA BINTI MOHAMED FAKHRURAZI</strong></td><td>Google Certified Educator Level 1 & 2</td><td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td></tr>
<tr><td>13</td><td><strong>NURAIN BINTI MD NOR</strong></td><td>Google Certified Educator Level 1 & 2</td><td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td></tr>
<tr><td>14</td><td><strong>PRIYA A/P PERANCHIS JOSIP</strong></td><td>Google Certified Educator Level 1 & 2</td><td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td></tr>
<tr><td>15</td><td><strong>PUTERI SHAZILA BINTI MIOR BASHAH</strong></td><td>Google Certified Educator Level 1 & 2</td><td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td></tr>
<tr><td>16</td><td><strong>RANJIDA A/P SHATIASILAN</strong></td><td>Google Certified Educator Level 1 & 2</td><td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td></tr>
<tr><td>17</td><td><strong>SIVAGAAMI A/P THILLAIVANAM</strong></td><td>Google Certified Educator Level 1 & 2</td><td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td></tr>
<tr><td>18</td><td><strong>SYAFIQAH BINTI MOHD RAHIM</strong></td><td>Google Certified Educator Level 1 & 2</td><td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td></tr>
<tr><td>19</td><td><strong>WONG JI JUN</strong></td><td>Google Certified Educator Level 1 & 2</td><td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td></tr>
<tr><td>20</td><td><strong>WONG JIA HUEY</strong></td><td>Google Certified Educator Level 1 & 2</td><td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td></tr>
<tr><td>21</td><td><strong>LEONG VEE BIN</strong></td><td>Google Certified Educator Level 1 & 2</td><td><span class="badge badge-success"><i class="fas fa-check"></i> Bertauliah</span></td></tr>
"""

sijil_gce_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Sijil & Poster GCE", "5.0 Pensijilan", "sijil-gce.html")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fab fa-google"></i> 5.2 Google Certified Educator (GCE L1, L2 & Trainer)</h2>
            <p>Pentauliahan Profesional Google for Education Peringkat Antarabangsa Pendidik SMJK AMC</p>
        </div>
        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
            <i class="fab fa-google-drive"></i> Folder E-Fail 5.2
        </a>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-medal"></i> Ringkasan Pencapaian Google Certified Educator</h3>
        <table class="delima-table">
            <thead>
                <tr>
                    <th>Tahap Pensijilan</th>
                    <th>Bilangan Guru</th>
                    <th>Peratusan (%)</th>
                    <th>Status Pengiktirafan</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Google Certified Educator Level 1</strong></td>
                    <td><strong>106 orang guru</strong></td>
                    <td><strong>100.0%</strong></td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> 100% Warga Pendidik</span></td>
                </tr>
                <tr>
                    <td><strong>Google Certified Educator Level 2</strong></td>
                    <td><strong>21 orang guru</strong></td>
                    <td><strong>19.8%</strong></td>
                    <td><span class="badge badge-primary"><i class="fas fa-star"></i> Pendidik Lanjutan</span></td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-star"></i> Senarai Guru Bertauliah GCE Level 2 (21 Orang Guru)</h3>
        <table class="delima-table">
            <thead>
                <tr>
                    <th style="width: 5%;">Bil</th>
                    <th style="width: 45%;">Nama Penuh Guru</th>
                    <th style="width: 35%;">Pentauliahan Google</th>
                    <th style="width: 15%;">Status</th>
                </tr>
            </thead>
            <tbody>
                {gce_l2_list_html}
            </tbody>
        </table>

        <div style="margin-top: 14px;">
            <button class="btn-card btn-card-primary" onclick="previewDoc('Direktori Guru Bertauliah Google (GCE Level 1, 2 dan Trainer) 2026', '5.0 PENSIJILAN DELIMA GURU/5.2 Google Certified Educator (GCE L1, L2 & Trainer)/Direktori Guru Bertauliah Google (GCE Level 1, 2 dan Trainer) 2026.docx')">
                <i class="fas fa-file-alt"></i> Prapapar Direktori Rasmi GCE
            </button>
        </div>
    </div>
</main>
"""
with open('pages/sijil-gce.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Sijil & Poster GCE", sijil_gce_body, depth=1, active='pensijilan'))

# ------------------------------------------------------------------------------
# 14. SIJIL MICROSOFT, APPLE & GEMINI (pages/sijil-microsoft.html)
# ------------------------------------------------------------------------------
sijil_ms_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Pensijilan Microsoft, Apple & Gemini", "5.0 Pensijilan", "sijil-microsoft.html")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fab fa-microsoft"></i> 5.3 & 5.4 Pensijilan Microsoft Educator, Apple Teacher & Gemini AI</h2>
            <p>Pentauliahan Kompetensi Merentas Pelantar Teknologi Pendidikan SMJK Ave Maria Convent, Ipoh</p>
        </div>
        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
            <i class="fab fa-google-drive"></i> Folder E-Fail 5.0
        </a>
    </div>

    <!-- 5.3 MICROSOFT CERTIFIED EDUCATOR -->
    <div class="content-box">
        <h3><i class="fab fa-microsoft" style="color: #00a4ef;"></i> 5.3 Pensijilan Microsoft Certified Educator & MIE</h3>
        <p style="font-size: 13px; color: var(--text-muted);">
            Program latihan Microsoft Educator membina kompetensi guru dalam integrasi perisian produktiviti Microsoft 365, Teams, OneNote Class Notebook, dan Microsoft Learn bagi memperkaya pedagogi bilik darjah abad ke-21.
        </p>
        <table class="delima-table">
            <thead>
                <tr>
                    <th style="width: 5%;">Bil</th>
                    <th style="width: 45%;">Nama Guru</th>
                    <th style="width: 35%;">Pensijilan Microsoft</th>
                    <th style="width: 15%;">Status</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1</td>
                    <td><strong>Tiada</strong></td>
                    <td>-</td>
                    <td><span class="badge" style="background: #f1f3f4; color: #5f6368;">-</span></td>
                </tr>
            </tbody>
        </table>

        <div style="margin-top: 14px;">
            <button class="btn-card btn-card-primary" onclick="previewDoc('Rekod Pensijilan Microsoft Educator 2026', '5.0 PENSIJILAN DELIMA GURU/5.3 Microsoft Certified Educator & Showcase/Rekod Pensijilan Microsoft Educator 2026.docx')">
                <i class="fas fa-file-alt"></i> Prapapar Dokumen Microsoft
            </button>
        </div>
    </div>

    <!-- 5.4 APPLE TEACHER -->
    <div class="content-box">
        <h3><i class="fab fa-apple" style="color: #333333;"></i> 5.4 Pensijilan Apple Teacher & Apple Learning Centre (8 Orang Guru)</h3>
        <p style="font-size: 13px; color: var(--text-muted);">
            Guru-guru SMJK AMC telah menamatkan lencana modul kreativiti Apple Learning Centre (Pages, Keynote, Numbers, iMovie, GarageBand & Swift Playgrounds untuk iPad & Mac):
        </p>
        <table class="delima-table">
            <thead>
                <tr>
                    <th style="width: 5%;">Bil</th>
                    <th style="width: 45%;">Nama Pendidik Apple Teacher</th>
                    <th style="width: 35%;">Pengiktirafan Apple</th>
                    <th style="width: 15%;">Peranti / Bidang</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1</td>
                    <td><strong>AU CHOOI YEE</strong></td>
                    <td>Apple Teacher (Certified)</td>
                    <td><span class="badge badge-success"><i class="fab fa-apple"></i> iPad & Mac</span></td>
                </tr>
                <tr>
                    <td>2</td>
                    <td><strong>FARAH NOOR AINA SALWA TAJUDDIN</strong></td>
                    <td>Apple Teacher (Certified)</td>
                    <td><span class="badge badge-success"><i class="fab fa-apple"></i> iPad & Mac</span></td>
                </tr>
                <tr>
                    <td>3</td>
                    <td><strong>NURAIN BINTI MD NOR</strong></td>
                    <td>Apple Teacher (Certified)</td>
                    <td><span class="badge badge-success"><i class="fab fa-apple"></i> iPad & Mac</span></td>
                </tr>
                <tr>
                    <td>4</td>
                    <td><strong>NURHANA AFIFA BINTI JAMAL</strong></td>
                    <td>Apple Teacher (Certified)</td>
                    <td><span class="badge badge-success"><i class="fab fa-apple"></i> iPad & Mac</span></td>
                </tr>
                <tr>
                    <td>5</td>
                    <td><strong>PRIYA A/P PERANCHIS JOSIP</strong></td>
                    <td>Apple Teacher (Certified)</td>
                    <td><span class="badge badge-success"><i class="fab fa-apple"></i> iPad & Mac</span></td>
                </tr>
                <tr>
                    <td>6</td>
                    <td><strong>WONG JI JUN</strong></td>
                    <td>Apple Teacher (Certified)</td>
                    <td><span class="badge badge-success"><i class="fab fa-apple"></i> iPad & Mac</span></td>
                </tr>
                <tr>
                    <td>7</td>
                    <td><strong>WONG JIA HUEY</strong></td>
                    <td>Apple Teacher (Certified)</td>
                    <td><span class="badge badge-success"><i class="fab fa-apple"></i> iPad & Mac</span></td>
                </tr>
                <tr>
                    <td>8</td>
                    <td><strong>WOO JIN JIE</strong></td>
                    <td>Apple Teacher (Certified)</td>
                    <td><span class="badge badge-success"><i class="fab fa-apple"></i> iPad & Mac</span></td>
                </tr>
            </tbody>
        </table>

        <div style="margin-top: 14px;">
            <button class="btn-card btn-card-primary" onclick="previewDoc('Rekod Pensijilan Apple Teacher 2026', '5.0 PENSIJILAN DELIMA GURU/5.4 Apple Teacher & Learning Centre/Rekod Pensijilan Apple Teacher 2026.docx')">
                <i class="fas fa-file-alt"></i> Prapapar Dokumen Apple Teacher
            </button>
        </div>
    </div>

    <!-- 5.5 GEMINI AI & KURSUS DIGITAL -->
    <div class="content-box">
        <h3><i class="fas fa-robot" style="color: #7b1fa2;"></i> 5.5 Pensijilan Gemini AI Educator (24 Orang Guru)</h3>
        <p style="font-size: 13px; color: var(--text-muted);">
            Penguasaan teknologi Kecerdasan Buatan (Generative AI dalam Pendidikan) bagi penciptaan bahan PdP, kuiz interaktif, dan pemudahcaraan tugasan bilik darjah abad ke-21.
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 8px; margin-top: 12px;">
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>1. TAN PEI NEE (Pengetua)</strong></div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>2. AU CHOOI YEE</strong></div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>3. CHONG MENG HONG</strong></div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>4. FARAH NOOR AINA SALWA</strong></div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>5. FONG JEN LIN</strong></div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>6. GOH SAW LIN</strong></div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>7. HEW TIET MIN</strong></div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>8. KOO SOK FONG</strong></div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>9. MICHELE TING MEI LING</strong></div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>10. MUHAMMAD SAIFUL ZAYANNI</strong></div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>11. NAGEINTHINI A/P TEWARAJAN</strong></div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>12. NIK NADHIRAH BINTI NIK KAMARUZAMAN</strong></div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>13. NOOR IZZATI BINTI MAJID</strong></div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>14. NOR AZIMA BINTI SHAARI</strong></div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>15. NUR AYU ANISA BINTI MOHAMED</strong></div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>16. NUR AZLIN BINTI IBRAHIM</strong></div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>17. NURAIN BINTI MD NOR</strong></div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>18. PRIYA A/P PERANCHIS JOSIP</strong></div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>19. RANJIDA A/P SHATIASILAN</strong></div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>20. ROSFARADILA BINTI AB.RAHIM</strong></div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>21. SYAFIQAH BINTI MOHD RAHIM</strong></div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>22. WAN ZURAIDA BINTI MIOR SALLEH</strong></div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>23. WONG JIA HUEY</strong></div>
            <div style="background: #f8f9fa; border: 1px solid var(--border-color); border-radius: 6px; padding: 10px 14px; font-size: 12px;"><strong>24. LEONG VEE BIN</strong></div>
        </div>

        <div style="margin-top: 16px;">
            <button class="btn-card btn-card-primary" onclick="previewDoc('Analisis Keseluruhan Pensijilan Digital Guru SMJK Ave Maria Convent 2026', '5.0 PENSIJILAN DELIMA GURU/5.5 Lain-lain Pensijilan & Kursus Digital/Analisis Keseluruhan Pensijilan Digital Guru SMJK Ave Maria Convent 2026.docx')">
                <i class="fas fa-file-alt"></i> Prapapar Analisis Keseluruhan Pensijilan
            </button>
        </div>
    </div>
</main>
"""
with open('pages/sijil-microsoft.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Pensijilan Microsoft, Apple & Gemini", sijil_ms_body, depth=1, active='pensijilan'))

print("Part 3 generation completed successfully!")
