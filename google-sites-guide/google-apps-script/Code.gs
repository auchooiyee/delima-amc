/**
 * GOOGLE APPS SCRIPT (GAS) - SISTEM MEJA BANTUAN ADUAN ID DELIMA SMJK AMC
 * Web App URL: https://script.google.com/macros/s/AKfycbxQIaKyycEbexVkCqr6qtLIexJHsUoutDRAJnSGmOGHAbFSrNMMr0RWyHLuStrqurk6/exec
 * 
 * Skrip ini menerima permohonan daripada borang aduan laman web/Google Sites, 
 * merekodkan data ke dalam Google Sheets "Rekod Aduan ID DELIMa AMC 2026",
 * dan menghantar notifikasi e-mel automatik kepada pentadbir.
 */

const ADMIN_EMAILS = "g-00556750@moe-dl.edu.my, g-24188210@moe-dl.edu.my";

function doGet(e) {
  return ContentService.createTextOutput("Meja Bantuan DELIMa SMJK AMC - Web App Aktif.");
}

function doPost(e) {
  try {
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    const sheet = ss.getActiveSheet();
    
    // Auto-create Header Row if empty
    if (sheet.getLastRow() === 0) {
      sheet.appendRow([
        "Tarikh & Masa",
        "No. Rujukan Tiket",
        "Nama Pemohon",
        "Peranan",
        "Kelas / Panitia",
        "Jenis Masalah",
        "Keterangan & Maklumat Kontak",
        "Status Tindakan"
      ]);
      sheet.getRange(1, 1, 1, 8).setFontWeight("bold").setBackground("#b71c1c").setFontColor("#ffffff");
      sheet.setFrozenRows(1);
    }

    let data = {};
    if (e && e.postData && e.postData.contents) {
      try {
        data = JSON.parse(e.postData.contents);
      } catch (jsonErr) {
        data = e.parameter || {};
      }
    } else if (e && e.parameter) {
      data = e.parameter;
    }

    const timestamp = new Date();
    const ticketId = data.ticketId || "AMC-DL-" + Math.floor(100000 + Math.random() * 900000);
    const nama = data.nama || "Tiada Nama";
    const peranan = data.peranan || "Guru / Murid";
    const kelas = data.kelas || "-";
    const jenis = data.jenis || "Isu Log Masuk ID DELIMa";
    const keterangan = data.keterangan || "-";

    // 1. Rekod ke dalam Google Sheets
    sheet.appendRow([
      timestamp,
      ticketId,
      nama,
      peranan,
      kelas,
      jenis,
      keterangan,
      "DALAM TINDAKAN"
    ]);

    // 2. Hantar Notifikasi E-mel kepada Kedua-dua Pentadbir
    const emailSubject = `[DELIMa AMC] Aduan ID Baharu (${ticketId}) - ${nama}`;
    const emailBody = `
==================================================
MEJA BANTUAN DELIMa SMJK AVE MARIA CONVENT, IPOH
NOTIFIKASI ADUAN MASALAH ID & RESET KATA LALUAN
==================================================

No. Rujukan Tiket : ${ticketId}
Tarikh & Masa     : ${timestamp.toLocaleString('ms-MY')}
Nama Pemohon      : ${nama}
Peranan           : ${peranan}
Kelas / Panitia   : ${kelas}
Jenis Masalah     : ${jenis}

Keterangan Isu & Maklumat Kontak:
${keterangan}

--------------------------------------------------
Pegawai Bertanggungjawab:
1. Pn. Nurain Binti Md Nor (g-00556750@moe-dl.edu.my)
2. Cik Au Chooi Yee (g-24188210@moe-dl.edu.my)

Sila log masuk ke Konsol Pentadbir DELIMa KPM untuk semakan dan penetapan semula kata laluan pemohon.
==================================================
`;

    try {
      MailApp.sendEmail({
        to: ADMIN_EMAILS,
        subject: emailSubject,
        body: emailBody
      });
    } catch (mailErr) {
      Logger.log("Mail Error: " + mailErr.toString());
    }

    return ContentService.createTextOutput(JSON.stringify({
      status: "success",
      ticketId: ticketId,
      message: "Aduan berjaya direkodkan dan e-mel telah dihantar."
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    Logger.log("Error: " + err.toString());
    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: err.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}
