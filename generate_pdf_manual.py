# -*- coding: utf-8 -*-
"""
Generate DaSH Portal Student Manual (PDF)
SMJK Ave Maria Convent, Ipoh (AEB2052)
"""

import os
import base64
import subprocess

# 1. Read image assets
with open('assets/images/logo.png', 'rb') as f:
    logo_b64 = base64.b64encode(f.read()).decode('utf-8')

with open('assets/images/dash_qr.png', 'rb') as f:
    qr_b64 = base64.b64encode(f.read()).decode('utf-8')

DASH_PORTAL_URL = "https://script.google.com/macros/s/AKfycbw3yy7rRiEnUkG-zhOi3nvgzbsjTakH9eD4Uapny0FZfQoidWmBs5zooq25Ub6RqGrfKA/exec?page=student"

html_content = f"""<!DOCTYPE html>
<html lang="ms">
<head>
    <meta charset="UTF-8">
    <title>Manual Pelajar - DaSH Portal SMJK AMC</title>
    <style>
        @page {{
            size: A4 portrait;
            margin: 12mm 15mm 12mm 15mm;
        }}
        * {{
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            color: #202124;
            background: #ffffff;
            margin: 0;
            padding: 0;
            font-size: 13px;
            line-height: 1.45;
        }}
        
        /* Header */
        .manual-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 3px solid #1a237e;
            padding-bottom: 10px;
            margin-bottom: 14px;
        }}
        .header-left {{
            display: flex;
            align-items: center;
            gap: 14px;
        }}
        .school-logo {{
            width: 58px;
            height: 58px;
            object-fit: contain;
        }}
        .school-info h1 {{
            font-size: 16px;
            color: #1a237e;
            margin: 0 0 2px;
            text-transform: uppercase;
            font-weight: 800;
            letter-spacing: 0.5px;
        }}
        .school-info p {{
            font-size: 11px;
            color: #5f6368;
            margin: 0;
        }}
        .badge-kpm {{
            background: #e8eaf6;
            color: #1a237e;
            border: 1px solid #c5cae9;
            font-size: 10.5px;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 4px;
            text-transform: uppercase;
            text-align: right;
        }}

        /* Document Title Banner */
        .title-banner {{
            background: linear-gradient(135deg, #0d1442 0%, #1a237e 60%, #1565c0 100%);
            color: #ffffff;
            border-radius: 8px;
            padding: 14px 18px;
            margin-bottom: 14px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 14px;
        }}
        .title-text h2 {{
            font-size: 20px;
            margin: 0 0 4px;
            color: #ffffff;
            font-weight: 800;
            letter-spacing: 0.5px;
        }}
        .title-text p {{
            font-size: 12px;
            color: #e8eaf6;
            margin: 0;
        }}
        .qr-box {{
            background: #ffffff;
            border-radius: 6px;
            padding: 6px 8px;
            text-align: center;
            color: #0d1442;
            flex-shrink: 0;
            border: 2px solid #fbc02d;
        }}
        .qr-box img {{
            width: 72px;
            height: 72px;
            display: block;
            margin: 0 auto 2px;
        }}
        .qr-box span {{
            font-size: 8.5px;
            font-weight: 700;
            text-transform: uppercase;
            display: block;
        }}

        /* What is DaSH */
        .intro-box {{
            background: #f8f9fa;
            border-left: 4px solid #fbc02d;
            border-radius: 0 8px 8px 0;
            padding: 10px 14px;
            margin-bottom: 14px;
        }}
        .intro-box h3 {{
            font-size: 13.5px;
            color: #1a237e;
            margin: 0 0 4px;
            font-weight: 700;
        }}
        .intro-box p {{
            font-size: 12px;
            margin: 0 0 8px;
            color: #202124;
        }}
        .intro-reasons {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 8px;
        }}
        .reason-chip {{
            background: #ffffff;
            border: 1px solid #dadce0;
            border-radius: 5px;
            padding: 6px 10px;
            font-size: 11px;
        }}
        .reason-chip strong {{
            color: #1565c0;
            display: block;
            font-size: 11.5px;
        }}

        /* Pre-requisite Box */
        .pre-box {{
            background: #fffdf5;
            border: 1px solid #ffe082;
            border-radius: 8px;
            padding: 10px 14px;
            margin-bottom: 14px;
        }}
        .pre-box h3 {{
            font-size: 13px;
            color: #b78103;
            margin: 0 0 6px;
            font-weight: 700;
        }}
        .pre-items {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 8px;
        }}
        .pre-card {{
            background: #ffffff;
            border: 1px solid #ffe082;
            border-radius: 5px;
            padding: 6px 10px;
            font-size: 11px;
        }}
        .pre-card strong {{
            color: #b78103;
            display: block;
        }}

        /* Step by Step */
        .steps-container {{
            margin-bottom: 14px;
        }}
        .section-title {{
            font-size: 14px;
            color: #1a237e;
            margin: 0 0 8px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            border-bottom: 1px solid #e0e0e0;
            padding-bottom: 4px;
        }}
        .steps-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
        }}
        .step-card {{
            border: 1px solid #dadce0;
            border-radius: 8px;
            padding: 10px 12px;
            background: #ffffff;
            position: relative;
        }}
        .step-badge {{
            display: inline-block;
            background: #1a237e;
            color: white;
            font-size: 10px;
            font-weight: 800;
            padding: 2px 8px;
            border-radius: 4px;
            margin-bottom: 6px;
        }}
        .step-card h4 {{
            font-size: 12.5px;
            color: #1a237e;
            margin: 0 0 4px;
            font-weight: 700;
        }}
        .step-card p {{
            font-size: 11px;
            color: #3c4043;
            margin: 0;
            line-height: 1.4;
        }}
        .step-tip {{
            background: #fff8e1;
            color: #856404;
            padding: 4px 6px;
            border-radius: 4px;
            font-size: 10px;
            margin-top: 6px;
            border-left: 2px solid #fbc02d;
        }}

        /* Page 2 Divider for clean print */
        .page-break {{
            page-break-before: always;
        }}

        /* Troubleshooting */
        .trouble-grid {{
            display: grid;
            grid-template-columns: 1fr;
            gap: 8px;
            margin-bottom: 14px;
        }}
        .trouble-card {{
            border: 1px solid #e0e0e0;
            border-radius: 6px;
            padding: 8px 12px;
            background: #ffffff;
        }}
        .trouble-card strong {{
            color: #d93025;
            font-size: 12px;
            display: block;
            margin-bottom: 2px;
        }}
        .trouble-card p {{
            font-size: 11.5px;
            color: #3c4043;
            margin: 0;
        }}

        /* Support Box */
        .support-box {{
            background: #e8f0fe;
            border-left: 4px solid #1a73e8;
            border-radius: 0 8px 8px 0;
            padding: 10px 14px;
            margin-bottom: 14px;
        }}
        .support-box h4 {{
            margin: 0 0 4px;
            color: #1a73e8;
            font-size: 13px;
        }}
        .support-box p {{
            margin: 0 0 6px;
            font-size: 11.5px;
            color: #3c4043;
        }}
        .admin-chips {{
            display: flex;
            gap: 10px;
        }}
        .admin-chip {{
            background: #ffffff;
            border: 1px solid #c2e7ff;
            border-radius: 4px;
            padding: 4px 8px;
            font-size: 11px;
        }}

        /* Footer */
        .manual-footer {{
            border-top: 1px solid #e0e0e0;
            padding-top: 8px;
            margin-top: 14px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 10px;
            color: #5f6368;
        }}
    </style>
</head>
<body>

    <!-- Header -->
    <div class="manual-header">
        <div class="header-left">
            <img src="data:image/png;base64,{logo_b64}" alt="Logo SMJK AMC" class="school-logo">
            <div class="school-info">
                <h1>SMJK Ave Maria Convent, Ipoh</h1>
                <p>Unit ICT & Jawatankuasa DELIMa Sekolah • Kod Sekolah: AEB2052 • Sesi 2026</p>
            </div>
        </div>
        <div class="badge-kpm">
            Manual Rasmi Pelajar<br>Sesi 2026
        </div>
    </div>

    <!-- Title Banner -->
    <div class="title-banner">
        <div class="title-text">
            <h2>DaSH PORTAL — PANDUAN RESET PASSWORD DELIMa</h2>
            <p>Sistem Pertukaran & Reset Kata Laluan DELIMa Kendiri SMJK AMC • Khas untuk Murid</p>
            <p style="margin-top: 6px; font-size: 11px; color: #fbc02d;">
                Pautan Pantas: <strong style="text-decoration: underline; color: #ffffff;">{DASH_PORTAL_URL}</strong>
            </p>
        </div>
        <div class="qr-box">
            <img src="data:image/png;base64,{qr_b64}" alt="QR Code DaSH Portal">
            <span>Imbas Portal</span>
        </div>
    </div>

    <!-- Apa itu DaSH Portal -->
    <div class="intro-box">
        <h3>💡 Apa itu DaSH Portal?</h3>
        <p>
            <strong>DaSH Portal</strong> ialah laman web sekolah yang membolehkan anda menukar (reset) password akaun DELIMa anda sendiri — <strong>tanpa perlu tunggu Cikgu ICT untuk buat untuk anda!</strong>
        </p>
        <div class="intro-reasons">
            <div class="reason-chip">
                <strong>1. Terlupa Password</strong>
                Akaun DELIMa (contoh: <code>m-xxxxxxxx@moe-dl.edu.my</code>)
            </div>
            <div class="reason-chip">
                <strong>2. Gagal Log Masuk</strong>
                Tidak boleh akses Google Classroom / Gmail sekolah
            </div>
            <div class="reason-chip">
                <strong>3. Kemas Kini Kata Laluan</strong>
                Ingin menukar password lama kepada password baharu
            </div>
        </div>
    </div>

    <!-- Sebelum Mula -->
    <div class="pre-box">
        <h3>📋 Sebelum Mula: Sediakan 3 Maklumat Ini Dahulu</h3>
        <p style="font-size: 11.5px; color: #424242; margin: 0 0 6px;">Pastikan anda telah bersedia dengan maklumat pengesahan identiti berikut:</p>
        <div class="pre-items">
            <div class="pre-card">
                <strong>1. Nama Penuh Anda</strong>
                Tepat seperti di dalam rekod pendaftaran sekolah.
            </div>
            <div class="pre-card">
                <strong>2. No. Kad Pengenalan (IC)</strong>
                Nombor MyKad anda (tanpa tanda sengkang '-').
            </div>
            <div class="pre-card">
                <strong>3. Nama Guru Kelas</strong>
                Ejaan nama guru kelas dalam SEMUA HURUF BESAR.
            </div>
        </div>
    </div>

    <!-- Panduan 3 Langkah -->
    <div class="steps-container">
        <div class="section-title">🚀 Panduan 3 Langkah Mudah Reset Password</div>
        <div class="steps-grid">
            <div class="step-card">
                <span class="step-badge">LANGKAH 1</span>
                <h4>Cari Nama Anda</h4>
                <p>Buka pautan DaSH Portal atau imbas kod QR di atas. Taip nama anda dalam kotak carian, kemudian <strong>pilih nama anda</strong> daripada senarai yang terpapar.</p>
            </div>
            <div class="step-card">
                <span class="step-badge" style="background: #1565c0;">LANGKAH 2</span>
                <h4>Sahkan & Reset</h4>
                <p>Isikan No. Kad Pengenalan (IC) dan nama Guru Kelas anda dengan tepat sebagai langkah keselamatan. Kemudian tekan butang <strong>"Reset Password Saya"</strong>.</p>
                <div class="step-tip">⚠️ Had: 1 kali reset setiap 24 jam.</div>
            </div>
            <div class="step-card">
                <span class="step-badge" style="background: #0f9d58;">LANGKAH 3</span>
                <h4>Simpan Password Baharu</h4>
                <p>Jika maklumat disahkan, password baharu akan terus dipaparkan pada skrin. <strong>TULIS atau INGAT password ini segera</strong> kerana ia tidak dipaparkan lagi.</p>
                <div class="step-tip" style="background: #e6f4ea; color: #137333; border-color: #0f9d58;">✅ Tekan "Log Masuk Google"</div>
            </div>
        </div>
    </div>

    <!-- Troubleshooting -->
    <div style="margin-top: 14px;">
        <div class="section-title">❓ Masalah Biasa & Cara Penyelesaian (Troubleshooting)</div>
        <div class="trouble-grid">
            <div class="trouble-card">
                <strong>Paparan Ralat: "Maklumat tidak sepadan"</strong>
                <p>Semak semula ejaan nama, no. IC, dan nama Guru Kelas. Semua maklumat perlu sama persis seperti rekod rasmi sekolah (nama guru kelas wajib huruf besar).</p>
            </div>
            <div class="trouble-card">
                <strong style="color: #f29900;">Paparan Ralat: "Sila cuba lagi selepas X jam"</strong>
                <p>Anda telah membuat pertukaran password dalam tempoh 24 jam yang lalu. Sila tunggu sehingga tempoh bertenang tamat sebelum membuat reset baharu.</p>
            </div>
            <div class="trouble-card">
                <strong style="color: #1565c0;">Nama anda tiada dalam senarai carian</strong>
                <p>Akaun anda mungkin murid baharu atau belum didaftarkan dalam sistem. Sila hubungi Penyelaras DELIMa / Guru Penyelaras Bestari sekolah.</p>
            </div>
        </div>
    </div>

    <!-- Support Admin -->
    <div class="support-box">
        <h4>🛡️ Masih Menghadapi Masalah? Hubungi Admin DELIMa Sekolah</h4>
        <p>Sekiranya akaun anda terkunci (*disabled*) atau menghadapi masalah luar jangka, hubungi guru berikut:</p>
        <div class="admin-chips">
            <div class="admin-chip">
                <strong>Pn. Nurain Binti Md Nor</strong> (Penyelaras DELIMa): <code>g-00556750@moe-dl.edu.my</code>
            </div>
            <div class="admin-chip">
                <strong>Cik Au Chooi Yee</strong> (Penolong Penyelaras DELIMa / Guru ICT): <code>g-24188210@moe-dl.edu.my</code>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <div class="manual-footer">
        <div>Hakcipta Terpelihara &copy; 2026 Unit ICT & Jawatankuasa DELIMa SMJK Ave Maria Convent, Ipoh</div>
        <div>Peringatan: Jangan sesekali berkongsi kata laluan anda dengan sesiapa pun.</div>
    </div>

</body>
</html>
"""

html_file = os.path.abspath("assets/docs/dash-portal-manual.html")
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated HTML manual: {html_file}")

# 2. Export to PDF using headless Edge or Chrome
pdf_target_1 = os.path.abspath("assets/docs/Manual_Pelajar_DaSH_Portal_SMJK_AMC.pdf")
downloads_dir = os.path.expanduser(r"~\Downloads")
pdf_target_2 = os.path.join(downloads_dir, "Manual_Pelajar_DaSH_Portal_SMJK_AMC.pdf")

browser_bin = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(browser_bin):
    browser_bin = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

print(f"Using browser: {browser_bin}")

cmd = [
    browser_bin,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_target_1}",
    html_file
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Edge/Chrome return code:", res.returncode)

if os.path.exists(pdf_target_1):
    sz1 = os.path.getsize(pdf_target_1)
    print(f"Successfully generated PDF: {pdf_target_1} ({sz1:,} bytes)")
    
    # Also copy to user's Downloads folder
    import shutil
    try:
        shutil.copy2(pdf_target_1, pdf_target_2)
        print(f"Copied to Downloads: {pdf_target_2} ({os.path.getsize(pdf_target_2):,} bytes)")
    except Exception as e:
        print("Copy to downloads error:", e)
else:
    print("PDF generation failed!")
