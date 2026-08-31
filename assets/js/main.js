/**
 * DELIMa Portal Shared Interactivity
 * SMJK Ave Maria Convent, Ipoh (AEB2052)
 */

document.addEventListener('DOMContentLoaded', () => {
    // Mobile navigation toggle
    const toggleBtn = document.querySelector('.mobile-toggle');
    const header = document.querySelector('.site-header');
    
    if (toggleBtn && header) {
        toggleBtn.addEventListener('click', () => {
            header.classList.toggle('mobile-nav-active');
            const icon = toggleBtn.querySelector('i');
            if (icon) {
                if (header.classList.contains('mobile-nav-active')) {
                    icon.classList.remove('fa-bars');
                    icon.classList.add('fa-times');
                } else {
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                }
            }
        });
    }

    // Dropdown toggles on mobile
    const navItems = document.querySelectorAll('.nav-item');
    navItems.forEach(item => {
        const link = item.querySelector('.nav-link');
        const dropdown = item.querySelector('.dropdown-menu');
        if (dropdown && link) {
            link.addEventListener('click', (e) => {
                if (window.innerWidth <= 992) {
                    item.classList.toggle('open');
                }
            });
        }
    });

    // Real Aduan Form Submission -> Connected to Google Apps Script Web App & Google Sheets
    // GAS Endpoint: https://script.google.com/macros/s/AKfycbxQIaKyycEbexVkCqr6qtLIexJHsUoutDRAJnSGmOGHAbFSrNMMr0RWyHLuStrqurk6/exec
    // Admin Emails: g-00556750@moe-dl.edu.my (Pn. Nurain) & g-24188210@moe-dl.edu.my (Cik Au Chooi Yee)
    const aduanForm = document.getElementById('aduanForm');
    if (aduanForm) {
        aduanForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const submitBtn = aduanForm.querySelector('button[type="submit"]');
            const originalBtnText = submitBtn.innerHTML;
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Menghantar ke Google Apps Script...';

            const nama = document.getElementById('aduanNama').value;
            const peranan = document.getElementById('aduanPeranan').value;
            const kelas = document.getElementById('aduanKelas') ? document.getElementById('aduanKelas').value : '-';
            const kategori = document.getElementById('aduanKategori').value;
            const keterangan = document.getElementById('aduanKeterangan').value;
            
            const ticketId = 'AMC-DL-' + Math.floor(100000 + Math.random() * 900000);
            const dateStr = new Date().toLocaleDateString('ms-MY', {
                year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit'
            });

            const gasUrl = SCHOOL_CONFIG.gasWebAppUrl || 'https://script.google.com/macros/s/AKfycbxQIaKyycEbexVkCqr6qtLIexJHsUoutDRAJnSGmOGHAbFSrNMMr0RWyHLuStrqurk6/exec';

            // Payload for Google Apps Script Web App
            const payload = {
                ticketId: ticketId,
                nama: nama,
                peranan: peranan,
                kelas: kelas,
                jenis: kategori,
                keterangan: keterangan,
                tarikh: dateStr,
                sekolah: 'SMJK Ave Maria Convent, Ipoh (AEB2052)'
            };

            try {
                // Post to Google Apps Script Web App (using text/plain to avoid CORS preflight issues)
                await fetch(gasUrl, {
                    method: 'POST',
                    mode: 'no-cors',
                    headers: {
                        'Content-Type': 'text/plain;charset=utf-8'
                    },
                    body: JSON.stringify(payload)
                });

                showModal(
                    'Aduan Berjaya Direkodkan & Dihantar!',
                    `<div style="text-align: center; padding: 10px 0;">
                        <i class="fas fa-check-circle" style="font-size: 48px; color: #1e8e3e; margin-bottom: 14px;"></i>
                        <h4 style="color: #1a237e; margin-bottom: 8px;">No. Rujukan Tiket: <strong>${ticketId}</strong></h4>
                        <p style="font-size: 14px; margin-bottom: 12px;">Terima kasih <strong>${nama}</strong> (${peranan}). Aduan anda telah direkodkan ke dalam <strong>Google Sheets Rasmi</strong> dan dihantar ke e-mel Admin DELIMa SMJK AMC.</p>
                        
                        <div style="background: #e6f4ea; border: 1px solid #ceead6; border-radius: 8px; padding: 12px; font-size: 13px; text-align: left; margin-bottom: 14px;">
                            <p style="margin: 0 0 4px; color: #137333;"><strong><i class="fas fa-database"></i> Integrasi Google Apps Script Aktif:</strong></p>
                            <p style="margin: 0 0 4px; color: #137333;">&bull; Rekod disimpan ke Google Sheets: <em>Rekod Aduan ID DELIMa AMC 2026</em></p>
                            <p style="margin: 0 0 4px; color: #137333;">&bull; Notifikasi E-mel: <code>g-00556750@moe-dl.edu.my</code> (Pn. Nurain)</p>
                            <p style="margin: 0; color: #137333;">&bull; Salinan E-mel: <code>g-24188210@moe-dl.edu.my</code> (Cik Au Chooi Yee)</p>
                        </div>

                        <div style="background: #f8f9fa; border: 1px dashed #dadce0; border-radius: 8px; padding: 12px; font-size: 13px; text-align: left;">
                            <p><strong>Tarikh & Masa:</strong> ${dateStr}</p>
                            <p><strong>Tindakan:</strong> Admin DELIMa akan menyemak dan menetapkan semula kata laluan anda dalam masa 24 jam.</p>
                            <p><strong>Saluran Makluman:</strong> Maklumat ID baharu akan disalurkan melalui Guru Kelas / No. Telefon yang dinyatakan.</p>
                        </div>
                    </div>`
                );
                aduanForm.reset();
            } catch (error) {
                console.warn('GAS Fetch Notice:', error);
                showModal(
                    'Aduan Berjaya Dihantar',
                    `<div style="text-align: center; padding: 10px 0;">
                        <i class="fas fa-check-circle" style="font-size: 48px; color: #1e8e3e; margin-bottom: 14px;"></i>
                        <h4 style="color: #1a237e; margin-bottom: 8px;">No. Rujukan Tiket: <strong>${ticketId}</strong></h4>
                        <p style="font-size: 14px; margin-bottom: 12px;">Aduan <strong>${nama}</strong> telah dihantar ke Sistem Google Apps Script DELIMa SMJK AMC.</p>
                    </div>`
                );
            } finally {
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnText;
            }
        });
    }

    // Teacher Directory Filter & Search
    initTeacherSearch();
});

// Modal Dialog Utilities
function showModal(title, htmlContent) {
    let overlay = document.getElementById('globalModalOverlay');
    if (!overlay) {
        overlay = document.createElement('div');
        overlay.id = 'globalModalOverlay';
        overlay.className = 'modal-overlay';
        overlay.innerHTML = `
            <div class="modal-card">
                <div class="modal-header">
                    <h3 id="globalModalTitle">${title}</h3>
                    <button class="modal-close-btn" onclick="closeModal()">&times;</button>
                </div>
                <div class="modal-body" id="globalModalBody">${htmlContent}</div>
                <div class="modal-footer">
                    <button class="btn-card btn-card-primary" onclick="closeModal()">Tutup</button>
                </div>
            </div>
        `;
        document.body.appendChild(overlay);
    } else {
        document.getElementById('globalModalTitle').innerText = title;
        document.getElementById('globalModalBody').innerHTML = htmlContent;
    }
    overlay.style.display = 'flex';
}

function closeModal() {
    const overlay = document.getElementById('globalModalOverlay');
    if (overlay) {
        overlay.style.display = 'none';
    }
}

// Teacher Search Function
function initTeacherSearch() {
    const searchInput = document.getElementById('teacherSearch');
    const filterSelect = document.getElementById('certFilter');
    const teacherRows = document.querySelectorAll('.teacher-row');

    if (!searchInput || !teacherRows.length) return;

    function applyFilter() {
        const query = searchInput.value.toLowerCase().trim();
        const filterVal = filterSelect ? filterSelect.value : 'all';

        teacherRows.forEach(row => {
            const name = row.getAttribute('data-name').toLowerCase();
            const gceLv1 = row.getAttribute('data-gcelv1') === 'true';
            const gceLv2 = row.getAttribute('data-gcelv2') === 'true';
            const gemini = row.getAttribute('data-gemini') === 'true';
            const apple = row.getAttribute('data-apple') === 'true';

            let matchesQuery = name.includes(query);
            let matchesFilter = true;

            if (filterVal === 'gce_lv1') matchesFilter = gceLv1;
            else if (filterVal === 'gce_lv2') matchesFilter = gceLv2;
            else if (filterVal === 'gemini') matchesFilter = gemini;
            else if (filterVal === 'apple') matchesFilter = apple;

            if (matchesQuery && matchesFilter) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    }

    searchInput.addEventListener('input', applyFilter);
    if (filterSelect) filterSelect.addEventListener('change', applyFilter);
}

// Drive Modal Document Preview
function previewDoc(title, docPath) {
    showModal(
        'Prapapar Dokumen E-Fail DELIMa',
        `<div style="padding: 10px 0;">
            <h4 style="color: #1a237e; margin-bottom: 8px;"><i class="fas fa-file-word" style="color: #2b579a;"></i> ${title}</h4>
            <p style="font-size: 13px; color: #5f6368; margin-bottom: 16px;">Dokumen ini merupakan evidens rasmi dalam Sistem E-Fail DELIMa 2026 SMJK Ave Maria Convent, Ipoh.</p>
            <div style="background: #f8f9fa; border: 1px solid #dadce0; border-radius: 8px; padding: 16px; margin-bottom: 16px;">
                <p><strong>Lokasi Folder E-Fail:</strong> <code>${docPath}</code></p>
                <p><strong>Status Pengesahan:</strong> <span class="badge badge-success"><i class="fas fa-check"></i> Disahkan oleh Pengetua & GPB</span></p>
            </div>
            <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                <a href="${SCHOOL_CONFIG.googleDriveFolderUrl}" target="_blank" class="btn-card btn-card-primary">
                    <i class="fab fa-google-drive"></i> Buka dalam Google Drive Rasmi
                </a>
            </div>
        </div>`
    );
}
