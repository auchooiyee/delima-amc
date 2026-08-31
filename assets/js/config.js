/**
 * DELIMa Portal Configuration - SMJK Ave Maria Convent, Ipoh, Perak
 * Kod Sekolah: AEB2052
 * Sesi: 2026
 */

const SCHOOL_CONFIG = {
    schoolName: "SMJK Ave Maria Convent, Ipoh",
    schoolShortName: "SMJK AMC",
    schoolCode: "AEB2052",
    ppd: "PPD Kinta Utara",
    jpn: "JPN Perak",
    address: "Jalan Chung Thye Phin, 30250 Ipoh, Perak Darul Ridzuan",
    portalTitle: "DELIMa @ SMJK AMC",
    slogan: "Mencapai Pembudayaan Digital Menyeluruh Warga SMJK AMC Setaraf Penarafan 5 Bintang DELIMa",
    logoPath: "assets/images/logo.png",
    
    // Official Links
    officialSiteUrl: "https://sites.google.com/moe-dl.edu.my/smjkamcipoh/",
    delimaPortalUrl: "https://d3.delima.edu.my/",
    delimaLoginUrl: "https://portal.moe.edu.my/",
    googleDriveFolderUrl: "https://drive.google.com/drive/folders/10HBSO2m-RKMAEJPsKmPmHZ1HU6zw4-y8?usp=sharing",
    smartBookingUrl: "https://sites.google.com/moe-dl.edu.my/amc-smart-booking-ver1/laman-utama",
    
    // Google Apps Script Web App Endpoint for Live Complaints & Google Sheets
    gasWebAppUrl: "https://script.google.com/macros/s/AKfycbxQIaKyycEbexVkCqr6qtLIexJHsUoutDRAJnSGmOGHAbFSrNMMr0RWyHLuStrqurk6/exec",

    // Admin Emails for Aduan & Reset ID
    adminEmails: {
        penyelaras: "g-00556750@moe-dl.edu.my",   // Pn. Nurain Binti Md Nor
        penolong: "g-24188210@moe-dl.edu.my",     // Cik Au Chooi Yee
        all: ["g-00556750@moe-dl.edu.my", "g-24188210@moe-dl.edu.my"]
    },

    // Leadership & Committee 2026
    leadership: {
        pengetua: {
            title: "Pengerusi (Pengetua)",
            name: "Pn. Tan Pei Nee",
            role: "Penaung & Ketua Pentadbir Pendigitalan Sekolah"
        },
        pkPentadbiran: {
            title: "Timbalan Pengerusi (PK Pentadbiran)",
            name: "Pn. Cheah Lay Shyuan",
            role: "Penyelia Pengurusan & Kurikulum Digital"
        },
        pkHEM: {
            title: "Naib Pengerusi I (PK HEM)",
            name: "Pn. Yap Yit Yin",
            role: "Penyelia e-Kehadiran & Disiplin Murid"
        },
        pkKoko: {
            title: "Naib Pengerusi II (PK Kokurikulum)",
            name: "Pn. Lai Mei Yeng",
            role: "Penyelia Aktiviti & Rekod Kokurikulum Digital"
        },
        pkPetang: {
            title: "Naib Pengerusi III (PK Petang)",
            name: "Cik Thean Fui Kean",
            role: "Penyelia Sesi Petang & Pembudayaan Digital"
        },
        penyelarasDelima: {
            title: "Penyelaras DELIMa (Admin DELIMa)",
            name: "Pn. Nurain Binti Md Nor",
            email: "g-00556750@moe-dl.edu.my",
            role: "Pengurusan Data, ID @moe-dl & Portal Rasmi"
        },
        penolongPenyelaras: {
            title: "Penolong Penyelaras DELIMa (Guru ICT)",
            name: "Cik Au Chooi Yee",
            email: "g-24188210@moe-dl.edu.my",
            role: "Pembangunan Laman, Latihan Guru (LADAP), Pensijilan & Inovasi"
        }
    },

    // Current Performance Statistics (Audit Ogos 2026)
    stats: {
        overallRating: "5 Bintang (Cemerlang)",
        overallUsagePct: "100.0%",
        totalUsers: 1560,
        guruActivePct: "93.0%",
        guruActiveCount: "100 / 107 orang",
        muridActivePct: "100.0%",
        muridActiveCount: "1,453 / 1,453 murid",
        googleAppsUsers: 1560,
        googleClassroomUsers: 96,
        
        // Certification Stats
        totalTeachers: 106,
        gceLv1Count: 103,
        gceLv1Pct: "97.2%",
        gceLv2Count: 21,
        gceLv2Pct: "19.8%",
        geminiCount: 24,
        geminiPct: "22.6%",
        appleCount: 8,
        applePct: "7.5%",
        digitalCertOverallPct: "100.0%"
    }
};
