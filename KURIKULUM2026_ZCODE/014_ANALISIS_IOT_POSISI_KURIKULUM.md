# 014 — ANALISIS STRATEGIS: POSISI INTERNET OF THINGS (IoT) DALAM KURIKULUM SISTEKIN

**Tanggal:** 18 Agustus 2026  
**Status:** FINAL — Terverifikasi Penuh Sesuai Dokumen [011], [020], [021], dan [022]  
**Pertanyaan Kunci:** Mengapa IoT Wajib Tetap Menjadi Mata Kuliah Inti (Core) Prodi dan Bukan Masuk Peminatan?  
**Posisi Terkunci:** **`STI-504 Internet of Things (IoT)` — 3 SKS (+P), Semester 5 (Core Wajib Prodi)**

---

## 1. POSISI STRUKTURAL IoT DALAM KURIKULUM 2026

| Aspek | Penetapan Final Kurikulum 2026 |
|---|---|
| **Kode & Nama MK** | `STI-504 Internet of Things (IoT)` |
| **Beban SKS & Tipe** | 3 SKS (+P / Hands-on Laboratory) |
| **Lokasi Semester** | Semester 5 (Ganjil) — Inti Rekayasa Sistem Cerdas |
| **CPL yang Dibangun** | **P3 (Pengetahuan Infrastruktur/IoT)** & **KK3 (Keterampilan Rekayasa Cloud/IoT)** |
| **Prasyarat Wajib** | `STI-307 Jaringan Komputer` (Sem 3) & `STI-305 Sistem Operasi` (Sem 3) |
| **Mata Kuliah Lanjutan** | Menjadi prasyarat untuk `STI-602 Smart City & SPBE` (Sem 6) & `FST-610 Capstone Project` |

---

## 2. 4 ALASAN UTAMA IoT WAJIB TETAP CORE (BUKAN PEMINATAN)

### 2.1 Menjaga Identitas & Pilar "Teknologi Informasi" (STI $\ne$ SI Konvensional)
Program studi kita adalah **Sistem dan Teknologi Informasi (SISTEKIN)**. Jika IoT dijadikan MK Pilihan, mahasiswa yang memilih jalur P2 (*Cloud/Cyber*) atau P3 (*Digital Platform*) dapat lulus tanpa pernah belajar perangkat keras/sensor sama sekali. Hal ini akan mendegradasi prodi menjadi prodi Sistem Informasi murni atau Manajemen Bisnis Digital.

### 2.2 Hukum Akreditasi OBE (Keterikatan Wajib CPL P3 & KK3)
* **CPL P3 & KK3** adalah Capaian Pembelajaran Lulusan yang **wajib dicapai oleh 100% lulusan** SISTEKIN.
* Asesor LAM INFOKOM / IABEE akan memberikan catatan kritis apabila suatu CPL wajib dibebankan pada mata kuliah yang berstatus *opsional / elektif*.

### 2.3 Relevansi Lintas 3 Peminatan
IoT merupakan *enabler* data fisik untuk seluruh peminatan:
* **P1 (Integrated Smart Systems):** IoT adalah sumber *real-time sensor data stream* untuk algoritma Machine Learning / Edge AI.
* **P2 (Cloud & Cybersecurity):** IoT adalah perangkat *edge* yang wajib diamankan (*IoT security posture*) dan diintegrasikan ke platform cloud (AWS IoT Core / Azure IoT Hub).
* **P3 (Digital Platform Engineering):** IoT menyediakan *telemetry data* untuk visualisasi *real-time dashboard*, aplikasi mobile, dan otomasi proses bisnis.

### 2.4 Jembatan Prasyarat Menuju Smart City & Capstone Project
* Di Semester 6, mahasiswa memprogram MK Wajib **`STI-602 Smart City dan Pemerintahan Digital` (3 SKS, +P)** dan **`FST-610 Capstone Project` (3 SKS, +P)**.
* Kedua mata kuliah tersebut secara langsung mengasumsikan mahasiswa sudah menguasai mikrokontroler (ESP32), sensor array, dan protokol komunikasi IoT (MQTT / HTTP REST).

---

## 3. POLA PEMBELAJARAN: FONDASI CORE $\rightarrow$ SPESIALISASI ELEKTIF

```
┌─────────────────────────────────────────────────────────────┐
│ SEMESTER 5: STI-504 Internet of Things (IoT) [CORE WAJIB]   │
│ (Mikrokontroler ESP32, Protokol MQTT/CoAP, Sensor, Gateway) │
└──────────────────────────────┬──────────────────────────────┘
                               │
       ┌───────────────────────┼───────────────────────┐
       ▼                       ▼                       ▼
┌──────────────┐        ┌──────────────┐        ┌──────────────┐
│ P1 (STA-06)  │        │ P2 (STB-01)  │        │ P3 (STC-04)  │
│ Smart Surv.  │        │ Network Sec. │        │ Immersive XR │
│ & Edge AI    │        │ & IoT Foren. │        │ & Spatial    │
└──────────────┘        └──────────────┘        └──────────────┘
```

---

## 4. KESIMPULAN & KEPUTUSAN FINAL

1. **IoT tetap berstatus Mata Kuliah Wajib Inti (Core Prodi SISTEKIN)** di Semester 5 (3 SKS, +P).
2. **Posisinya di Semester 5 sangat ideal & aman** setelah penataan ulang beban praktikum (DW-BI digeser ke Sem 4 dan Manpro TI digeser ke Sem 5).
3. Pendalaman tingkat lanjut IoT diwadahi melalui MK Pilihan spesialisasi di Semester 5–7 (*Smart Surveillance, Network Forensics, Immersive Media*).

---

*Dokumen ini merupakan analisis resmi posisi strategis IoT dalam struktur Kurikulum SISTEKIN 2026.*
