# -*- coding: utf-8 -*-
"""
Full Page Generator for DELIMa Portal SMJK Ave Maria Convent, Ipoh
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

# Helper for standard breadcrumbs
def get_breadcrumbs(current_title, parent_title="UTAMA", parent_link="../index.html"):
    return f"""
    <div class="breadcrumb-nav">
        <a href="../index.html"><i class="fas fa-home"></i> Laman Utama</a> &gt; 
        <a href="{parent_link}">{parent_title}</a> &gt; 
        <span>{current_title}</span>
    </div>
    """

# ------------------------------------------------------------------------------
# 1. JAWATANKUASA DELIMA (pages/jawatankuasa.html)
# ------------------------------------------------------------------------------
jawatankuasa_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Jawatankuasa DELIMa", "1.0 Pengurusan")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fas fa-users-cog"></i> Jawatankuasa DELIMa 2026</h2>
            <p>Struktur Tadbir Urus dan Pembahagian Tugas Jawatankuasa Digital Educational Learning Initiative Malaysia</p>
        </div>
        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
            <i class="fab fa-google-drive"></i> Folder E-Fail 1.1
        </a>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-id-card"></i> Carta Pentadbiran Jawatankuasa DELIMa Sesi 2026</h3>
        <table class="delima-table">
            <thead>
                <tr>
                    <th>Jawatan DELIMa</th>
                    <th>Nama Pegawai / Guru</th>
                    <th>Jawatan Hakiki Sekolah</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Pengerusi</strong></td>
                    <td>Pn. Tan Pei Nee</td>
                    <td>Pengetua</td>
                </tr>
                <tr>
                    <td><strong>Timbalan Pengerusi</strong></td>
                    <td>Pn. Cheah Lay Shyuan</td>
                    <td>Penolong Kanan Pentadbiran</td>
                </tr>
                <tr>
                    <td><strong>Naib Pengerusi I</strong></td>
                    <td>Pn. Yap Yit Yin</td>
                    <td>Penolong Kanan Hal Ehwal Murid</td>
                </tr>
                <tr>
                    <td><strong>Naib Pengerusi II</strong></td>
                    <td>Pn. Lai Mei Yeng</td>
                    <td>Penolong Kanan Kokurikulum</td>
                </tr>
                <tr>
                    <td><strong>Naib Pengerusi III</strong></td>
                    <td>Cik Thean Fui Kean</td>
                    <td>Penolong Kanan Petang</td>
                </tr>
                <tr style="background-color: #fff0f0;">
                    <td><strong>Penyelaras DELIMa</strong></td>
                    <td><strong>Pn. Nurain Binti Md Nor</strong></td>
                    <td>Admin DELIMa & Pengurusan ID @moe-dl</td>
                </tr>
                <tr style="background-color: #fff0f0;">
                    <td><strong>Penolong Penyelaras DELIMa</strong></td>
                    <td><strong>Cik Au Chooi Yee</strong></td>
                    <td>Guru ICT, Latihan Guru & Inovasi</td>
                </tr>
                <tr>
                    <td><strong>AJK Dashboard Kurikulum</strong></td>
                    <td>Setiausaha Kurikulum</td>
                    <td>SU Kurikulum</td>
                </tr>
                <tr>
                    <td><strong>AJK Dashboard Kokurikulum</strong></td>
                    <td>Setiausaha Kokurikulum</td>
                    <td>SU Kokurikulum</td>
                </tr>
                <tr>
                    <td><strong>AJK Dashboard HEM</strong></td>
                    <td>Setiausaha HEM</td>
                    <td>SU Hal Ehwal Murid</td>
                </tr>
                <tr>
                    <td><strong>AJK Promosi & Hebahan</strong></td>
                    <td>Cik Au Chooi Yee</td>
                    <td>Guru ICT</td>
                </tr>
                <tr>
                    <td><strong>AJK Latihan Guru (LADAP)</strong></td>
                    <td>Cik Au Chooi Yee</td>
                    <td>Guru Penyelaras Latihan Digital</td>
                </tr>
                <tr>
                    <td><strong>AJK Pertandingan Digital Murid</strong></td>
                    <td>Pn. Nurain Binti Md Nor</td>
                    <td>Admin DELIMa</td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-tasks"></i> Peranan & Tanggungjawab AJK DELIMa 2026</h3>
        <table class="delima-table">
            <thead>
                <tr>
                    <th style="width: 25%;">Ahli Jawatankuasa</th>
                    <th>Peranan & Tanggungjawab Utama</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Penyelaras & Penolong Penyelaras DELIMa</strong></td>
                    <td>
                        <ul style="padding-left: 20px; font-size: 13px; line-height: 1.6;">
                            <li>Menetapkan semula (reset) kata laluan guru dan murid secara individu dan pukal.</li>
                            <li>Mengurus ruang portal DELIMa sekolah dan menyiarkan pengumuman rasmi.</li>
                            <li>Mengakses senarai pengguna dan memantau dashboard keaktifan DELIMa sekolah.</li>
                            <li>Melapor ke meja bantuan (helpdesk) KPM/JPN bagi sebarang isu teknikal ID.</li>
                            <li>Menyediakan folder Google Drive dan menguruskan ekosistem E-Fail DELIMa 2026.</li>
                            <li>Merancang dan mengendalikan kursus LADAP DELIMa / AI Generatif untuk guru.</li>
                            <li>Menguruskan pertandingan kreativiti digital murid dan modul celik teknologi.</li>
                        </ul>
                    </td>
                </tr>
                <tr>
                    <td><strong>AJK Dashboard Kurikulum / HEM / Koko</strong></td>
                    <td>
                        <ul style="padding-left: 20px; font-size: 13px; line-height: 1.6;">
                            <li>Menyelaras tapak e-RPH guru di Google Classroom & repositori kurikulum digital.</li>
                            <li>Menguruskan sistem e-Kehadiran harian murid dan rekod sahsiah digital.</li>
                            <li>Menguruskan rekod kehadiran aktiviti kokurikulum serta pelaporan digital kelab/persatuan.</li>
                        </ul>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-file-signature"></i> Surat Lantikan Jawatankuasa DELIMa 2026</h3>
        <p>Surat pelantikan rasmi bernombor rujukan <code>SMJKAMC/DELIMA/2026/(01)</code> bertarikh 2 Januari 2026 telah diedarkan kepada semua AJK.</p>
        <div style="margin-top: 14px;">
            <button class="btn-card btn-card-primary" onclick="previewDoc('Surat Pelantikan AJK DELIMa 2026', '1.0 PENGURUSAN/1.1 Jawatankuasa DELIMa/Surat Lantikan Jawatankuasa DELIMa 2026.docx')">
                <i class="fas fa-file-alt"></i> Prapapar Surat Pelantikan
            </button>
            <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
                <i class="fab fa-google-drive"></i> Lihat Dokumen Asal
            </a>
        </div>
    </div>
</main>
"""
with open('pages/jawatankuasa.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Jawatankuasa DELIMa 2026", jawatankuasa_body, depth=1, active='utama'))
print("Saved pages/jawatankuasa.html")

# ------------------------------------------------------------------------------
# 2. SURAT MENYURAT (pages/surat-menyurat.html)
# ------------------------------------------------------------------------------
surat_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Surat Menyurat & Pekeliling", "1.0 Pengurusan")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fas fa-envelope-open-text"></i> Surat Menyurat & Pekeliling DELIMa 2026</h2>
            <p>Rekod Daftar Surat Pekeliling Ikhtisas, Surat Siaran KPM, JPN Perak dan PPD Kinta Utara</p>
        </div>
        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
            <i class="fab fa-google-drive"></i> Folder E-Fail 1.2
        </a>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-list-ol"></i> Senarai Daftar Surat Rasmi & Pekeliling 2026</h3>
        <table class="delima-table">
            <thead>
                <tr>
                    <th style="width: 5%;">Bil</th>
                    <th style="width: 12%;">Tarikh</th>
                    <th style="width: 25%;">No. Rujukan Surat</th>
                    <th>Perkara / Tajuk Pekeliling</th>
                    <th style="width: 15%;">Tindakan</th>
                    <th style="width: 12%;">Status</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1</td>
                    <td>02/01/2026</td>
                    <td>KPM.600-14/1/56 Jld.3 (12)</td>
                    <td>Surat Siaran Pemerkasaan Pelantar DELIMa dan Pengisian Penilaian Kendiri Sekolah 2026</td>
                    <td>Penyelaras DELIMa</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Selesai</span></td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>15/01/2026</td>
                    <td>SMJKAMC/DELIMA/2026/(01)</td>
                    <td>Surat Pelantikan Jawatankuasa DELIMa SMJK Ave Maria Convent Sesi 2026</td>
                    <td>Semua AJK</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Diedarkan</span></td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>08/02/2026</td>
                    <td>KPM.100-1/3/1 Jld.5 (28)</td>
                    <td>Surat Pekeliling Ikhtisas Pelaksanaan Dasar Pendidikan Digital (DPD) Kementerian Pendidikan Malaysia</td>
                    <td>Semua Guru</td>
                    <td><span class="badge badge-info"><i class="fas fa-info-circle"></i> Dipatuhi</span></td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>20/03/2026</td>
                    <td>JPNPK.SPb.ICT.600-3/2/1 (45)</td>
                    <td>Garis Panduan Keselamatan Siber dan Pengurusan Akaun ID @moe-dl Guru dan Murid</td>
                    <td>Guru ICT & HEM</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Dihebahkan</span></td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>10/05/2026</td>
                    <td>KPM.600-14/1/56 Jld.3 (30)</td>
                    <td>Pencalonan Peperiksaan Pensijilan Google Certified Educator (GCE) dan Apple Teacher KPM</td>
                    <td>Au Chooi Yee</td>
                    <td><span class="badge badge-success"><i class="fas fa-star"></i> 100% Lulus</span></td>
                </tr>
            </tbody>
        </table>
        
        <div style="margin-top: 16px;">
            <button class="btn-card btn-card-primary" onclick="previewDoc('Senarai Surat Menyurat dan Pekeliling DELIMa 2026', '1.0 PENGURUSAN/1.2 Fail DELIMa & Surat Menyurat/Senarai Surat Menyurat dan Pekeliling DELIMa 2026.docx')">
                <i class="fas fa-file-alt"></i> Prapapar Rekod Daftar E-Fail
            </button>
        </div>
    </div>
</main>
"""
with open('pages/surat-menyurat.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Surat Menyurat DELIMa", surat_body, depth=1, active='utama'))
print("Saved pages/surat-menyurat.html")

# ------------------------------------------------------------------------------
# 3. CARTA ORGANISASI (pages/carta-organisasi.html)
# ------------------------------------------------------------------------------
carta_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Carta Organisasi", "1.0 Pengurusan")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fas fa-sitemap"></i> Carta Organisasi Jawatankuasa DELIMa 2026</h2>
            <p>Hierarki Pengurusan Pendigitalan & Pembudayaan ICT SMJK Ave Maria Convent, Ipoh</p>
        </div>
        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
            <i class="fab fa-google-drive"></i> Folder E-Fail 1.3
        </a>
    </div>

    <!-- Visual Tree Structure -->
    <div class="content-box">
        <h3><i class="fas fa-network-wired"></i> Struktur Visual Carta AMC</h3>
        
        <div style="display: flex; flex-direction: column; align-items: center; gap: 16px; margin: 20px 0;">
            <!-- Pengerusi -->
            <div style="background: linear-gradient(135deg, #b71c1c, #d32f2f); color: white; padding: 14px 28px; border-radius: 8px; text-align: center; box-shadow: var(--shadow-md); min-width: 260px;">
                <div style="font-size: 11px; text-transform: uppercase; font-weight: 700; opacity: 0.85;">Pengerusi</div>
                <div style="font-family: var(--font-heading); font-size: 18px; font-weight: 700;">Pn. Tan Pei Nee</div>
                <div style="font-size: 12px;">Pengetua SMJK Ave Maria Convent</div>
            </div>

            <div style="width: 2px; height: 20px; background: var(--border-color);"></div>

            <!-- Timbalan Pengerusi -->
            <div style="background: #ffffff; border: 2px solid var(--primary); padding: 12px 24px; border-radius: 8px; text-align: center; min-width: 240px;">
                <div style="font-size: 11px; text-transform: uppercase; font-weight: 700; color: var(--primary);">Timbalan Pengerusi</div>
                <div style="font-family: var(--font-heading); font-size: 16px; font-weight: 700;">Pn. Cheah Lay Shyuan</div>
                <div style="font-size: 12px; color: var(--text-muted);">Penolong Kanan Pentadbiran</div>
            </div>

            <div style="width: 2px; height: 20px; background: var(--border-color);"></div>

            <!-- Naib Pengerusi Grid -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; width: 100%;">
                <div style="background: #f8f9fa; border: 1px solid var(--border-color); padding: 10px; border-radius: 6px; text-align: center;">
                    <div style="font-size: 10px; font-weight: 700; color: var(--text-muted);">Naib Pengerusi I</div>
                    <div style="font-weight: 700; font-size: 13px;">Pn. Yap Yit Yin</div>
                    <div style="font-size: 11px; color: var(--text-muted);">PK HEM</div>
                </div>
                <div style="background: #f8f9fa; border: 1px solid var(--border-color); padding: 10px; border-radius: 6px; text-align: center;">
                    <div style="font-size: 10px; font-weight: 700; color: var(--text-muted);">Naib Pengerusi II</div>
                    <div style="font-weight: 700; font-size: 13px;">Pn. Lai Mei Yeng</div>
                    <div style="font-size: 11px; color: var(--text-muted);">PK Kokurikulum</div>
                </div>
                <div style="background: #f8f9fa; border: 1px solid var(--border-color); padding: 10px; border-radius: 6px; text-align: center;">
                    <div style="font-size: 10px; font-weight: 700; color: var(--text-muted);">Naib Pengerusi III</div>
                    <div style="font-weight: 700; font-size: 13px;">Cik Thean Fui Kean</div>
                    <div style="font-size: 11px; color: var(--text-muted);">PK Petang</div>
                </div>
            </div>

            <div style="width: 2px; height: 20px; background: var(--border-color);"></div>

            <!-- Penyelaras & Penolong Penyelaras -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; width: 100%;">
                <div style="background: #ffebee; border: 1px solid #ffcdd2; padding: 14px; border-radius: 8px; text-align: center;">
                    <div style="font-size: 11px; font-weight: 700; color: var(--primary);">Penyelaras DELIMa (Admin DELIMa)</div>
                    <div style="font-family: var(--font-heading); font-size: 16px; font-weight: 700; color: var(--primary-dark);">Pn. Nurain Binti Md Nor</div>
                    <div style="font-size: 12px; color: var(--text-dark);">Data ID @moe-dl, Pengurusan Laman & Pertandingan</div>
                </div>
                <div style="background: #ffebee; border: 1px solid #ffcdd2; padding: 14px; border-radius: 8px; text-align: center;">
                    <div style="font-size: 11px; font-weight: 700; color: var(--primary);">Penolong Penyelaras (Guru ICT)</div>
                    <div style="font-family: var(--font-heading); font-size: 16px; font-weight: 700; color: var(--primary-dark);">Cik Au Chooi Yee</div>
                    <div style="font-size: 12px; color: var(--text-dark);">Latihan LADAP, Pensijilan GCE, Inovasi & Promosi</div>
                </div>
            </div>
        </div>

        <div style="margin-top: 18px; text-align: center;">
            <button class="btn-card btn-card-primary" onclick="previewDoc('Carta Organisasi Jawatankuasa DELIMa 2026', '1.0 PENGURUSAN/1.3 Carta Organisasi/Carta Organisasi Jawatankuasa DELIMa 2026.docx')">
                <i class="fas fa-file-alt"></i> Prapapar Dokumen Carta AMC
            </button>
        </div>
    </div>
</main>
"""
with open('pages/carta-organisasi.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Carta Organisasi DELIMa", carta_body, depth=1, active='utama'))
print("Saved pages/carta-organisasi.html")

# ------------------------------------------------------------------------------
# 4. PERANCANGAN STRATEGIK (pages/perancangan-strategik.html)
# ------------------------------------------------------------------------------
pso_body = f"""
<main class="main-wrapper">
    {get_breadcrumbs("Perancangan Strategik (PSO)", "1.0 Pengurusan")}
    
    <div class="page-header-box">
        <div>
            <h2><i class="fas fa-chess"></i> Pelan Strategik, Taktikal & Operasi DELIMa 2026</h2>
            <p>Perancangan Bersepadu Pengurusan Pendigitalan & Pembudayaan Teknologi Pendidikan SMJK AMC</p>
        </div>
        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive">
            <i class="fab fa-google-drive"></i> Folder E-Fail 1.4
        </a>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-bullseye"></i> Sasaran Strategik & KPI Utama 2026</h3>
        <table class="delima-table">
            <thead>
                <tr>
                    <th>Bidang Fokus</th>
                    <th>Objektif / Sasaran KPI 2026</th>
                    <th>Pencapaian Sebenar (Audit Ogos 2026)</th>
                    <th>Status Penarafan</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Penggunaan Guru</strong></td>
                    <td>Sekurang-kurangnya 90% log masuk aktif setiap bulan</td>
                    <td><strong>93.0%</strong> (100 / 107 Guru Aktif)</td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Melepasi Sasaran</span></td>
                </tr>
                <tr>
                    <td><strong>Penggunaan Murid</strong></td>
                    <td>Sekurang-kurangnya 85% murid mengakses Google Classroom & DELIMa</td>
                    <td><strong>100.0%</strong> (1,453 / 1,453 Murid Aktif)</td>
                    <td><span class="badge badge-success"><i class="fas fa-star"></i> 5 Bintang KPM</span></td>
                </tr>
                <tr>
                    <td><strong>Pensijilan Digital Guru</strong></td>
                    <td>Sekurang-kurangnya 40% guru lulus Google Certified Educator (GCE)</td>
                    <td><strong>100.0%</strong> (103 GCE Lv1, 21 GCE Lv2, 24 Gemini)</td>
                    <td><span class="badge badge-success"><i class="fas fa-trophy"></i> 5 Bintang Khas</span></td>
                </tr>
                <tr>
                    <td><strong>Inovasi Pengurusan</strong></td>
                    <td>Mewujudkan 1 inovasi pengurusan tempahan pintar tanpa kertas</td>
                    <td>Portal Inovasi <strong>AMC Smart Booking</strong></td>
                    <td><span class="badge badge-success"><i class="fas fa-check"></i> Berjaya Dilaksana</span></td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="content-box">
        <h3><i class="fas fa-calendar-check"></i> Pelan Taktikal & Pelan Operasi DELIMa 2026</h3>
        <table class="delima-table">
            <thead>
                <tr>
                    <th>Program / Aktiviti</th>
                    <th>Tarikh / Tempoh</th>
                    <th>Kumpulan Sasaran</th>
                    <th>Pegawai Bertanggungjawab</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Bulan Pelancaran DELIMa 2026</strong></td>
                    <td>Januari - Februari 2026</td>
                    <td>Semua Guru & Murid AMC</td>
                    <td>Pn. Tan Pei Nee & Pn. Nurain</td>
                </tr>
                <tr>
                    <td><strong>LADAP 1: AI Generatif (Gemini) & Workspace</strong></td>
                    <td>24 Februari 2026</td>
                    <td>Semua Guru (106 orang)</td>
                    <td>Cik Au Chooi Yee</td>
                </tr>
                <tr>
                    <td><strong>Bengkel Celik Digital & Keselamatan Siber Murid</strong></td>
                    <td>Mac - April 2026</td>
                    <td>Murid Tingkatan 1 - 5</td>
                    <td>Cik Au Chooi Yee & Guru ICT</td>
                </tr>
                <tr>
                    <td><strong>Klinik DCTP & Ujian Pensijilan GCE Guru</strong></td>
                    <td>Mei - Julai 2026</td>
                    <td>Semua Guru</td>
                    <td>Cik Au Chooi Yee</td>
                </tr>
                <tr>
                    <td><strong>Pelaksanaan Portal AMC Smart Booking</strong></td>
                    <td>Sepanjang Tahun 2026</td>
                    <td>Warga Sekolah</td>
                    <td>Cik Au Chooi Yee & Admin</td>
                </tr>
            </tbody>
        </table>
        
        <div style="margin-top: 16px;">
            <button class="btn-card btn-card-primary" onclick="previewDoc('Pelan Strategik, Taktikal dan Operasi DELIMa 2026', '1.0 PENGURUSAN/1.4 Perancangan Strategik/Pelan Strategik, Taktikal dan Operasi DELIMa 2026.docx')">
                <i class="fas fa-file-alt"></i> Prapapar Dokumen PSO Lengkap
            </button>
        </div>
    </div>
</main>
"""
with open('pages/perancangan-strategik.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Perancangan Strategik DELIMa", pso_body, depth=1, active='utama'))
print("Saved pages/perancangan-strategik.html")

print("Generator script part 2 completed.")
