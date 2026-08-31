# -*- coding: utf-8 -*-
"""
DELIMa Portal Page Generator
SMJK Ave Maria Convent, Ipoh, Perak (AEB2052)
"""

import os
import json

print("Starting page generator...")

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

def build_nav(depth=0, active='utama'):
    p = '' if depth == 0 else '../'
    pages_p = 'pages/' if depth == 0 else ''
    
    return f"""
    <!-- Top Notification Bar -->
    <div class="top-notice-bar">
        <span><i class="fas fa-bullhorn"></i> <strong>STATUS AUDIT DELIMa 2026:</strong> Penarafan <strong>5 BINTANG</strong> (100% KPI Penggunaan & 100% Guru Bertauliah Digital).</span>
        <a href="{pages_p}pembudayaan.html"><i class="fas fa-chart-pie"></i> Lihat Analisis</a>
    </div>

    <!-- Header & Navigation -->
    <header class="site-header">
        <div class="nav-container">
            <a href="{p}index.html" class="brand-wrapper">
                <img src="{p}assets/images/logo.png" alt="Logo SMJK Ave Maria Convent" class="brand-logo">
                <div class="brand-text">
                    <h1>DELIMa @ SMJK AMC</h1>
                    <span>SMJK AVE MARIA CONVENT, IPOH (AEB2052)</span>
                </div>
            </a>
            
            <nav class="main-nav">
                <ul class="nav-list">
                    <li class="nav-item">
                        <a href="{p}index.html" class="nav-link {'active' if active=='utama' else ''}">
                            <i class="fas fa-home"></i> UTAMA <i class="fas fa-chevron-down"></i>
                        </a>
                        <ul class="dropdown-menu">
                            <li><a href="{pages_p}jawatankuasa.html" class="dropdown-link"><i class="fas fa-users-cog"></i> Jawatankuasa DELIMa</a></li>
                            <li><a href="{pages_p}surat-menyurat.html" class="dropdown-link"><i class="fas fa-envelope-open-text"></i> Surat Menyurat & Pekeliling</a></li>
                            <li><a href="{pages_p}carta-organisasi.html" class="dropdown-link"><i class="fas fa-sitemap"></i> Carta Organisasi</a></li>
                            <li><a href="{pages_p}perancangan-strategik.html" class="dropdown-link"><i class="fas fa-chess"></i> Perancangan Strategik (PSO)</a></li>
                            <li><a href="{pages_p}laporan-aktiviti.html" class="dropdown-link"><i class="fas fa-clipboard-check"></i> Laporan Aktiviti (OPR)</a></li>
                            <li><a href="{pages_p}minit-mesyuarat.html" class="dropdown-link"><i class="fas fa-file-signature"></i> Minit Mesyuarat</a></li>
                            <li><a href="{pages_p}program-delima.html" class="dropdown-link"><i class="fas fa-calendar-alt"></i> Program & Takwim ICT</a></li>
                            <li><a href="{pages_p}jadual-penggunaan.html" class="dropdown-link"><i class="fas fa-desktop"></i> Jadual Makmal & Tempahan</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a href="{pages_p}pembudayaan.html" class="nav-link {'active' if active=='pembudayaan' else ''}">
                            <i class="fas fa-chart-line"></i> PEMBUDAYAAN <i class="fas fa-chevron-down"></i>
                        </a>
                        <ul class="dropdown-menu">
                            <li><a href="{pages_p}pembudayaan.html" class="dropdown-link"><i class="fas fa-chart-pie"></i> Analisis Penggunaan Sekolah</a></li>
                            <li><a href="{pages_p}promosi.html" class="dropdown-link"><i class="fas fa-bullhorn"></i> Promosi & Latihan (LADAP)</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a href="{pages_p}pensijilan.html" class="nav-link {'active' if active=='pensijilan' else ''}">
                            <i class="fas fa-award"></i> PENSIJILAN <i class="fas fa-chevron-down"></i>
                        </a>
                        <ul class="dropdown-menu">
                            <li><a href="{pages_p}pensijilan.html" class="dropdown-link"><i class="fas fa-user-graduate"></i> Direktori Pensijilan Guru</a></li>
                            <li><a href="{pages_p}sijil-gce.html" class="dropdown-link"><i class="fab fa-google"></i> Sijil & Poster GCE (L1 & L2)</a></li>
                            <li><a href="{pages_p}sijil-microsoft.html" class="dropdown-link"><i class="fab fa-microsoft"></i> Sijil Microsoft & Apple Teacher</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a href="{pages_p}pengurusan-sekolah.html" class="nav-link {'active' if active=='pengurusan' else ''}">
                            <i class="fas fa-school"></i> PENGURUSAN SEKOLAH
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="{pages_p}keistimewaan.html" class="nav-link {'active' if active=='keistimewaan' else ''}">
                            <i class="fas fa-star"></i> KEISTIMEWAAN <i class="fas fa-chevron-down"></i>
                        </a>
                        <ul class="dropdown-menu">
                            <li><a href="{pages_p}keistimewaan.html" class="dropdown-link"><i class="fas fa-gem"></i> Hub Keistimewaan Sekolah</a></li>
                            <li><a href="{pages_p}inovasi.html" class="dropdown-link"><i class="fas fa-lightbulb"></i> Inovasi AMC Smart Booking</a></li>
                            <li><a href="{pages_p}kolaboratif.html" class="dropdown-link"><i class="fas fa-handshake"></i> Kolaboratif & Jaringan Pintar</a></li>
                            <li><a href="{pages_p}pencapaian.html" class="dropdown-link"><i class="fas fa-trophy"></i> Pencapaian & Anugerah SSQS</a></li>
                            <li><a href="{pages_p}sumbangan-pdp.html" class="dropdown-link"><i class="fas fa-share-alt"></i> Sumbangan Ruang Ilmu & YouTube</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a href="{pages_p}portal-dashboard.html" class="nav-link {'active' if active=='dashboard' else ''}">
                            <i class="fas fa-th"></i> PORTAL & DASHBOARD
                        </a>
                    </li>
                </ul>
            </nav>

            <div class="nav-actions">
                <a href="{pages_p}aduan-id.html" class="btn-header-aduan">
                    <i class="fas fa-key"></i> Aduan ID DELIMa
                </a>
                <button class="mobile-toggle" aria-label="Buka Menu Navigasi">
                    <i class="fas fa-bars"></i>
                </button>
            </div>
        </div>
    </header>
    """

def build_footer(depth=0):
    p = '' if depth == 0 else '../'
    pages_p = 'pages/' if depth == 0 else ''
    return f"""
    <footer class="site-footer">
        <div class="footer-top">
            <div class="footer-col">
                <h4>SMJK Ave Maria Convent</h4>
                <p><i class="fas fa-map-marker-alt"></i> Jalan Chung Thye Phin, 30250 Ipoh, Perak Darul Ridzuan</p>
                <p><i class="fas fa-id-badge"></i> <strong>Kod Sekolah:</strong> AEB2052 | <strong>PPD:</strong> Kinta Utara</p>
                <p><i class="fas fa-envelope"></i> aeb2052@moe.edu.my</p>
            </div>
            <div class="footer-col">
                <h4>Pautan Pantas</h4>
                <ul class="footer-links">
                    <li><a href="https://d3.delima.edu.my/" target="_blank"><i class="fas fa-external-link-alt"></i> Portal DELIMa KPM (d3)</a></li>
                    <li><a href="https://classroom.google.com/" target="_blank"><i class="fab fa-google"></i> Google Classroom</a></li>
                    <li><a href="{SMART_BOOKING_URL}" target="_blank"><i class="fas fa-calendar-check"></i> Inovasi AMC Smart Booking</a></li>
                    <li><a href="{DRIVE_URL}" target="_blank"><i class="fab fa-google-drive"></i> Repositori E-Fail DELIMa (Google Drive)</a></li>
                    <li><a href="{pages_p}aduan-id.html"><i class="fas fa-life-ring"></i> Meja Bantuan ID & Kata Laluan</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Pentadbir DELIMa & ICT</h4>
                <p><strong>Penyelaras DELIMa:</strong><br>Pn. Nurain Binti Md Nor (Admin DELIMa)</p>
                <p><strong>Penolong Penyelaras / Guru ICT:</strong><br>Cik Au Chooi Yee</p>
                <p style="margin-top: 8px;"><span class="badge badge-success"><i class="fas fa-check-circle"></i> Penarafan 5 Bintang KPM</span></p>
            </div>
        </div>
        <div class="footer-bottom">
            <p>Hakcipta Terpelihara &copy; 2026 Jawatankuasa DELIMa & Unit ICT SMJK Ave Maria Convent, Ipoh. Dikuasakan oleh Google Workspace for Education & DELIMa KPM.</p>
        </div>
    </footer>

    <!-- Global Scripts -->
    <script src="{p}assets/js/config.js"></script>
    <script src="{p}assets/js/main.js"></script>
    """

def wrap_html(title, body_content, depth=0, active='utama'):
    p = '' if depth == 0 else '../'
    return f"""<!DOCTYPE html>
<html lang="ms">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | DELIMa SMJK Ave Maria Convent, Ipoh</title>
    <link rel="icon" href="{p}assets/images/logo.png">
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,400;0,600;0,700;1,400&family=Oswald:wght@400;600;700&display=swap" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="{p}assets/css/style.css?v=2.0">
</head>
<body>
    {build_nav(depth, active)}
    {body_content}
    {build_footer(depth)}
</body>
</html>
"""

# ==============================================================================
# 1. INDEX.HTML (HOME)
# ==============================================================================
home_content = f"""
    <!-- Hero Banner -->
    <section class="hero-banner">
        <div class="hero-container">
            <div class="hero-badge-kpi">
                <i class="fas fa-star"></i> PENARAFAN 5 BINTANG DELIMa KPM 2026
            </div>
            <h1 class="hero-title">DELIMa @ SMJK AVE MARIA CONVENT</h1>
            <p class="hero-subtitle">Digital Educational Learning Initiative Malaysia &bull; Sesi 2026</p>
            <p class="hero-slogan">"Mencapai Pembudayaan Digital Menyeluruh Warga SMJK AMC Setaraf Penarafan 5 Bintang DELIMa"</p>
            
            <div class="hero-actions">
                <a href="pages/aduan-id.html" class="btn-hero btn-hero-yellow">
                    <i class="fas fa-key"></i> Aduan ID DELIMa
                </a>
                <a href="https://d3.delima.edu.my/" target="_blank" class="btn-hero btn-hero-primary">
                    <i class="fas fa-sign-in-alt"></i> Log Masuk DELIMa (d3)
                </a>
                <a href="{SMART_BOOKING_URL}" target="_blank" class="btn-hero btn-hero-outline">
                    <i class="fas fa-calendar-check"></i> AMC Smart Booking
                </a>
                <a href="{DRIVE_URL}" target="_blank" class="btn-hero btn-hero-outline">
                    <i class="fab fa-google-drive"></i> E-Fail DELIMa 2026
                </a>
            </div>
        </div>
    </section>

    <!-- Quick Launchpad -->
    <section class="launchpad-section">
        <div class="launchpad-container">
            <a href="https://classroom.google.com/" target="_blank" class="launchpad-card">
                <div class="launchpad-icon" style="background-color: #1e8e3e;"><i class="fab fa-google"></i></div>
                <div class="launchpad-info">
                    <h4>Classroom</h4>
                    <span>Google Bilik Darjah</span>
                </div>
            </a>
            <a href="https://drive.google.com/" target="_blank" class="launchpad-card">
                <div class="launchpad-icon" style="background-color: #1a73e8;"><i class="fab fa-google-drive"></i></div>
                <div class="launchpad-info">
                    <h4>Google Drive</h4>
                    <span>Storan Awan AMC</span>
                </div>
            </a>
            <a href="https://www.canva.com/education/" target="_blank" class="launchpad-card">
                <div class="launchpad-icon" style="background-color: #7b1fa2;"><i class="fas fa-palette"></i></div>
                <div class="launchpad-info">
                    <h4>Canva EDU</h4>
                    <span>Rekaan Digital Guru</span>
                </div>
            </a>
            <a href="{SMART_BOOKING_URL}" target="_blank" class="launchpad-card">
                <div class="launchpad-icon" style="background-color: #1565c0;"><i class="fas fa-laptop-code"></i></div>
                <div class="launchpad-info">
                    <h4>Smart Booking</h4>
                    <span>Tempahan Makmal</span>
                </div>
            </a>
            <a href="pages/pensijilan.html" class="launchpad-card">
                <div class="launchpad-icon" style="background-color: #f9ab00;"><i class="fas fa-certificate"></i></div>
                <div class="launchpad-info">
                    <h4>Pensijilan GCE</h4>
                    <span>106 Guru Bertauliah</span>
                </div>
            </a>
            <a href="{DRIVE_URL}" target="_blank" class="launchpad-card">
                <div class="launchpad-icon" style="background-color: #0288d1;"><i class="fas fa-folder-open"></i></div>
                <div class="launchpad-info">
                    <h4>E-Fail Rasmi</h4>
                    <span>Audit Penarafan 2026</span>
                </div>
            </a>
        </div>
    </section>

    <!-- Main Content Area -->
    <main class="main-wrapper">
        <!-- Stats Counter Grid -->
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-icon"><i class="fas fa-award"></i></div>
                <div class="stat-number">5 BINTANG</div>
                <div class="stat-label">Penarafan Kendiri DELIMa</div>
                <div class="stat-sub"><i class="fas fa-check-circle"></i> Audit Sesi 2026</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon" style="color: #1a73e8;"><i class="fas fa-chalkboard-teacher"></i></div>
                <div class="stat-number">93.0%</div>
                <div class="stat-label">Keaktifan Guru</div>
                <div class="stat-sub">100 / 107 Guru Aktif</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon" style="color: #1e8e3e;"><i class="fas fa-user-graduate"></i></div>
                <div class="stat-number">100.0%</div>
                <div class="stat-label">Keaktifan Murid</div>
                <div class="stat-sub">1,453 / 1,453 Murid Aktif</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon" style="color: #f9ab00;"><i class="fab fa-google"></i></div>
                <div class="stat-number">{stats['gce_lv1']} ORANG</div>
                <div class="stat-label">Google Certified Educator</div>
                <div class="stat-sub"><i class="fas fa-star"></i> 97.2% Guru GCE Level 1</div>
            </div>
        </div>

        <!-- Vision, Mission & Core Philosophy -->
        <div class="content-box">
            <h3><i class="fas fa-compass"></i> Hala Tuju Pendigitalan SMJK Ave Maria Convent</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 14px;">
                <div style="background: #fff8f8; border-left: 4px solid var(--primary); padding: 16px; border-radius: 6px;">
                    <h4 style="color: var(--primary); margin-top: 0;"><i class="fas fa-eye"></i> VISI</h4>
                    <p style="font-size: 14px; color: var(--text-dark); margin: 0;">Mencapai pembudayaan digital secara menyeluruh dalam kalangan warga SMJK Ave Maria Convent, Ipoh setaraf penarafan 5 Bintang DELIMa KPM menjelang 2026.</p>
                </div>
                <div style="background: #f8fbff; border-left: 4px solid #1a73e8; padding: 16px; border-radius: 6px;">
                    <h4 style="color: #1a73e8; margin-top: 0;"><i class="fas fa-bullseye"></i> MISI</h4>
                    <p style="font-size: 14px; color: var(--text-dark); margin: 0;">Memperkasa kompetensi guru dalam integrasi pedagogi digital, mengoptimumkan pengurusan sekolah tanpa kertas (paperless), serta memupuk murid berdaya saing global melalui teknologi pendidikan.</p>
                </div>
            </div>
        </div>

        <!-- 6 Main Modules of E-Fail DELIMa -->
        <div class="section-title-wrap">
            <h3>Struktur E-Fail & Komponen DELIMa 2026</h3>
            <p>Dokumentasi lengkap pemarkahan instrumen penarafan pembudayaan digital sekolah KPM</p>
        </div>

        <div class="modules-grid">
            <!-- 1.0 Pengurusan -->
            <div class="module-card">
                <div class="module-card-header">
                    <span class="module-code">1.0</span>
                    <h4>Pengurusan DELIMa</h4>
                </div>
                <div class="module-card-body">
                    <p>Sistem tadbir urus dan arkib rasmi jawatankuasa DELIMa & ICT sekolah sesi 2026.</p>
                    <ul class="module-subitems">
                        <li><i class="fas fa-circle"></i> Jawatankuasa DELIMa & Surat Lantikan</li>
                        <li><i class="fas fa-circle"></i> Fail & Pekeliling Rasmi KPM/JPN/PPD</li>
                        <li><i class="fas fa-circle"></i> Carta Organisasi AMC & Perancangan Strategik (PSO)</li>
                        <li><i class="fas fa-circle"></i> Laporan Aktiviti (OPR), Minit Mesyuarat & Jadual Makmal</li>
                    </ul>
                    <div class="module-btn-wrap">
                        <a href="pages/jawatankuasa.html" class="btn-card btn-card-primary"><i class="fas fa-eye"></i> Buka Modul</a>
                        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive"><i class="fab fa-google-drive"></i> Drive</a>
                    </div>
                </div>
            </div>

            <!-- 2.0 Pembudayaan -->
            <div class="module-card">
                <div class="module-card-header">
                    <span class="module-code">2.0</span>
                    <h4>Pembudayaan DELIMa</h4>
                </div>
                <div class="module-card-body">
                    <p>Laporan analisis data audit penggunaan Microsoft Power BI KPM (Guru, Murid, Sekolah).</p>
                    <ul class="module-subitems">
                        <li><i class="fas fa-circle"></i> Peratus Penggunaan Guru: 93.0% (100 Guru Aktif)</li>
                        <li><i class="fas fa-circle"></i> Peratus Penggunaan Murid: 100.0% (1,453 Murid)</li>
                        <li><i class="fas fa-circle"></i> Pencapaian KPI Keseluruhan Sekolah: 100.0%</li>
                        <li><i class="fas fa-circle"></i> Status Penilaian: Penarafan 5 Bintang KPM</li>
                    </ul>
                    <div class="module-btn-wrap">
                        <a href="pages/pembudayaan.html" class="btn-card btn-card-primary"><i class="fas fa-chart-line"></i> Dashboard</a>
                        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive"><i class="fab fa-google-drive"></i> Drive</a>
                    </div>
                </div>
            </div>

            <!-- 3.0 Promosi -->
            <div class="module-card">
                <div class="module-card-header">
                    <span class="module-code">3.0</span>
                    <h4>Promosi & Latihan</h4>
                </div>
                <div class="module-card-body">
                    <p>Program kesedaran, kursus dalaman guru (LADAP) & bengkel celik digital murid.</p>
                    <ul class="module-subitems">
                        <li><i class="fas fa-circle"></i> Pelancaran Bulan DELIMa & Hebahan Perhimpunan</li>
                        <li><i class="fas fa-circle"></i> Kursus LADAP AI Generatif (Gemini) & Workspace</li>
                        <li><i class="fas fa-circle"></i> Modul Bengkel Celik Digital Murid 2026</li>
                        <li><i class="fas fa-circle"></i> Sudut / Bilik DELIMa & Pertandingan Kreativiti</li>
                    </ul>
                    <div class="module-btn-wrap">
                        <a href="pages/promosi.html" class="btn-card btn-card-primary"><i class="fas fa-bullhorn"></i> Lihat Aktiviti</a>
                        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive"><i class="fab fa-google-drive"></i> Drive</a>
                    </div>
                </div>
            </div>

            <!-- 4.0 Pengurusan Sekolah -->
            <div class="module-card">
                <div class="module-card-header">
                    <span class="module-code">4.0</span>
                    <h4>Penggunaan Pengurusan</h4>
                </div>
                <div class="module-card-body">
                    <p>Integrasi DELIMa secara menyeluruh dalam pentadbiran, kurikulum, HEM & kokurikulum.</p>
                    <ul class="module-subitems">
                        <li><i class="fas fa-circle"></i> Pengurusan Pentadbiran Tanpa Kertas (Paperless)</li>
                        <li><i class="fas fa-circle"></i> Kurikulum: Pengurusan e-RPH & Bank Sumber Digital</li>
                        <li><i class="fas fa-circle"></i> HEM: e-Kehadiran & Rekod Disiplin Murid</li>
                        <li><i class="fas fa-circle"></i> Kokurikulum: Pelaporan Digital & e-Sijil Aktiviti</li>
                    </ul>
                    <div class="module-btn-wrap">
                        <a href="pages/pengurusan-sekolah.html" class="btn-card btn-card-primary"><i class="fas fa-school"></i> Integrasi</a>
                        <a href="{DRIVE_URL}" target="_blank" class="btn-card btn-card-drive"><i class="fab fa-google-drive"></i> Drive</a>
                    </div>
                </div>
            </div>

            <!-- 5.0 Pensijilan -->
            <div class="module-card">
                <div class="module-card-header">
                    <span class="module-code">5.0</span>
                    <h4>Pensijilan Guru</h4>
                </div>
                <div class="module-card-body">
                    <p>Direktori bertauliah antarabangsa Google, Gemini Generative AI, Microsoft & Apple.</p>
                    <ul class="module-subitems">
                        <li><i class="fas fa-circle"></i> Google Certified Educator Level 1: 103 Guru (97.2%)</li>
                        <li><i class="fas fa-circle"></i> Google Certified Educator Level 2: 21 Guru (19.8%)</li>
                        <li><i class="fas fa-circle"></i> Gemini AI Certified: 24 Guru | Apple Teacher: 8 Guru</li>
                        <li><i class="fas fa-circle"></i> Pencapaian Keseluruhan: 100% Guru Bertauliah</li>
                    </ul>
                    <div class="module-btn-wrap">
                        <a href="pages/pensijilan.html" class="btn-card btn-card-primary"><i class="fas fa-user-graduate"></i> Direktori Guru</a>
                        <a href="pages/sijil-gce.html" class="btn-card btn-card-drive"><i class="fab fa-google"></i> Sijil GCE</a>
                    </div>
                </div>
            </div>

            <!-- 6.0 Keistimewaan -->
            <div class="module-card">
                <div class="module-card-header">
                    <span class="module-code">6.0</span>
                    <h4>Keistimewaan Sekolah</h4>
                </div>
                <div class="module-card-body">
                    <p>Niche pendigitalan, projek inovasi pintar, jaringan komuniti & anugerah cemerlang.</p>
                    <ul class="module-subitems">
                        <li><i class="fas fa-circle"></i> Inovasi Khas: AMC Smart Booking (Portal Tempahan)</li>
                        <li><i class="fas fa-circle"></i> Jaringan Komuniti & Bengkel MIV / MDEC</li>
                        <li><i class="fas fa-circle"></i> Penarafan 5 Bintang SSQS & Anugerah Digital</li>
                        <li><i class="fas fa-circle"></i> Sumbangan Modul PdP Guru ke Ruang Ilmu KPM</li>
                    </ul>
                    <div class="module-btn-wrap">
                        <a href="pages/keistimewaan.html" class="btn-card btn-card-primary"><i class="fas fa-gem"></i> Keistimewaan</a>
                        <a href="pages/inovasi.html" class="btn-card btn-card-drive"><i class="fas fa-lightbulb"></i> Inovasi AMC</a>
                    </div>
                </div>
            </div>
        </div>

        <!-- 6 DELIMa Ecosystem Pillars -->
        <div class="content-box">
            <h3><i class="fas fa-cubes"></i> 6 Tonggak Utama Ekosistem Pembelajaran DELIMa KPM</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; margin-top: 14px;">
                <div style="border: 1px solid #dadce0; border-radius: 8px; padding: 14px;">
                    <h4 style="color: var(--primary); margin: 0 0 6px;"><i class="fab fa-google" style="color: #ea4335;"></i> 1. Google Workspace</h4>
                    <p style="font-size: 13px; color: var(--text-muted); margin: 0;">Penggunaan menyeluruh Google Classroom, Drive, Docs, Sheets, Slides, Forms dan Google Meet dalam PdP harian.</p>
                </div>
                <div style="border: 1px solid #dadce0; border-radius: 8px; padding: 14px;">
                    <h4 style="color: var(--primary); margin: 0 0 6px;"><i class="fab fa-microsoft" style="color: #00a4ef;"></i> 2. Microsoft 365</h4>
                    <p style="font-size: 13px; color: var(--text-muted); margin: 0;">Sokongan Microsoft Teams, OneNote, Word, PowerPoint dan platform pembelajaran Microsoft Learn.</p>
                </div>
                <div style="border: 1px solid #dadce0; border-radius: 8px; padding: 14px;">
                    <h4 style="color: var(--primary); margin: 0 0 6px;"><i class="fab fa-apple" style="color: #555555;"></i> 3. Apple Learning</h4>
                    <p style="font-size: 13px; color: var(--text-muted); margin: 0;">Peluang pensijilan Apple Teacher dan integrasi aplikasi kreativiti pendidikan digital murid.</p>
                </div>
                <div style="border: 1px solid #dadce0; border-radius: 8px; padding: 14px;">
                    <h4 style="color: var(--primary); margin: 0 0 6px;"><i class="fas fa-handshake" style="color: #f9ab00;"></i> 4. Rakan Kandungan</h4>
                    <p style="font-size: 13px; color: var(--text-muted); margin: 0;">Kerjasama bersama MDEC, UNICEF, Digi CyberSAFE, Astro Kasih dan Perpustakaan Negara Malaysia (PNM).</p>
                </div>
                <div style="border: 1px solid #dadce0; border-radius: 8px; padding: 14px;">
                    <h4 style="color: var(--primary); margin: 0 0 6px;"><i class="fas fa-users" style="color: #1e8e3e;"></i> 5. Ruang Kerjasama</h4>
                    <p style="font-size: 13px; color: var(--text-muted); margin: 0;">Membuka ruang kolaboratif bersama agensi luar, institusi pengajian tinggi dan komuniti setempat.</p>
                </div>
                <div style="border: 1px solid #dadce0; border-radius: 8px; padding: 14px;">
                    <h4 style="color: var(--primary); margin: 0 0 6px;"><i class="fas fa-book-reader" style="color: #8e24aa;"></i> 6. Ruang Ilmu</h4>
                    <p style="font-size: 13px; color: var(--text-muted); margin: 0;">Hab perkongsian inovasi dan bahan PdP guru-guru SMJK AMC untuk dimanfaatkan oleh komuniti pendidik Malaysia.</p>
                </div>
            </div>
        </div>

        <!-- Leadership Directory -->
        <div class="content-box">
            <h3><i class="fas fa-user-shield"></i> Jawatankuasa Peneraju DELIMa SMJK AMC 2026</h3>
            <table class="delima-table">
                <thead>
                    <tr>
                        <th>Jawatan Jawatankuasa</th>
                        <th>Nama Pegawai / Guru</th>
                        <th>Peranan Utama</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Pengerusi</strong></td>
                        <td>Pn. Tan Pei Nee (Pengetua)</td>
                        <td>Penaung & Ketua Pengurusan Pendigitalan</td>
                    </tr>
                    <tr>
                        <td><strong>Timbalan Pengerusi</strong></td>
                        <td>Pn. Cheah Lay Shyuan (PK Pentadbiran)</td>
                        <td>Penyelia Pengurusan & Kurikulum Digital</td>
                    </tr>
                    <tr>
                        <td><strong>Naib Pengerusi I</strong></td>
                        <td>Pn. Yap Yit Yin (PK HEM)</td>
                        <td>Penyelia e-Kehadiran & Hal Ehwal Murid</td>
                    </tr>
                    <tr>
                        <td><strong>Naib Pengerusi II</strong></td>
                        <td>Pn. Lai Mei Yeng (PK Kokurikulum)</td>
                        <td>Penyelia Pelaporan Kokurikulum Digital</td>
                    </tr>
                    <tr>
                        <td><strong>Naib Pengerusi III</strong></td>
                        <td>Cik Thean Fui Kean (PK Petang)</td>
                        <td>Penyelia Pembudayaan Digital Sesi Petang</td>
                    </tr>
                    <tr style="background-color: #fff3f3;">
                        <td><strong>Penyelaras DELIMa</strong></td>
                        <td><strong>Pn. Nurain Binti Md Nor</strong> (Admin DELIMa)</td>
                        <td>Pengurusan Data Pengguna, ID @moe-dl & Portal Rasmi</td>
                    </tr>
                    <tr style="background-color: #fff3f3;">
                        <td><strong>Penolong Penyelaras</strong></td>
                        <td><strong>Cik Au Chooi Yee</strong> (Guru ICT)</td>
                        <td>Pembangunan Laman, Kursus LADAP Guru, Pensijilan GCE & Inovasi</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </main>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(wrap_html("Laman Utama", home_content, depth=0, active='utama'))
print("Saved index.html")

print("Generator script part 1 completed.")
