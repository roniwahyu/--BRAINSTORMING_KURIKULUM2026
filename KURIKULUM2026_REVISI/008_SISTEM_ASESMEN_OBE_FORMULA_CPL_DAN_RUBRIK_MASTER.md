# 008 — SISTEM ASESMEN OBE, FORMULA KETERCAPAIAN CPL, DAN RUBRIK MASTER
## Program Studi Sistem dan Teknologi Informasi (S1) — Fakultas Sains dan Teknologi Informasi (FSTI) Universitas Widyagama Malang

**Dokumen Revisi Definitif Kurikulum 2026**  
**Standar Rujukan:** Standar LAM INFOKOM Kriteria 6 (Pendidikan) & Kriteria 9 (Luaran CPL), Panduan Kurikulum OBE APTIKOM v2.0, IABEE Criteria for Assessment & CQI.

---

## 1. KERANGKA ASESMEN OBE SISTEKIN 2026

Sistem penilaian pada Kurikulum OBE SISTEKIN berorientasi penuh pada pembuktian ketercapaian **14 CPL** secara langsung (*Direct Assessment*) melalui Capaian Pembelajaran Mata Kuliah (CPMK):

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                         SIKLUS ASESMEN BERBASIS LUARAN (OBE)                             │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Mata Kuliah merumuskan CPMK & Sub-CPMK (Bloom C2–C6).                                 │
│ 2. Instrumen Asesmen dirancang: Tugas Kasus, Proyek PjBL, Kuis, UTS, UAS.                 │
│ 3. Nilai Mahasiswa dihitung per Sub-CPMK menggunakan Rubrik Analitik Terstandar.         │
│ 4. Skor Ketercapaian CPL dihitung menggunakan Formula Bobot Matriks MK ↔ CPL.            │
│ 5. Analisis Gap & Tindak Lanjut Perbaikan Berkelanjutan (PPEPP / CQI).                   │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

> [!IMPORTANT]
> **Kepatuhan IKU 7 (Indikator Kinerja Utama Kemendikbudristek):**  
> Setiap mata kuliah keahlian dan praktikum wajib mengalokasikan **minimal 50% bobot evaluasi** menggunakan metode pembelajaran partisipatif dan kolaboratif: **Case Method (Studi Kasus)** atau **Team-Based Project (PjBL)**.

---

## 2. FORMULA MATEMATIS KETERCAPAIAN CPL (CPL ATTAINMENT FORMULATION)

### 2.1 Perhitungan Ketercapaian CPMK pada Mata Kuliah ($Score_{CPMK_j}$)
Skor ketercapaian untuk suatu $CPMK_j$ pada mata kuliah $k$ oleh mahasiswa $i$ dihitung sebagai rata-rata berbobot dari instrumen asesmen terkait:

$$Score_{CPMK_j, k}(i) = \sum_{m=1}^{M} \left( W_{jm} \times Score_{m}(i) \right)$$

*Dimana:*
* $Score_m(i)$ = Nilai instrumen asesmen ke-$m$ (skala 0–100).
* $W_{jm}$ = Bobot instrumen ke-$m$ terhadap $CPMK_j$ ($\sum W_{jm} = 1.0$).

---

### 2.2 Perhitungan Nilai Akhir Mata Kuliah ($NA_k$)
Nilai akhir mata kuliah merupakan agregasi dari seluruh ketercapaian CPMK:

$$NA_k(i) = \sum_{j=1}^{J} \left( W_{CPMK_j, k} \times Score_{CPMK_j, k}(i) \right)$$

---

### 2.3 Perhitungan Ketercapaian CPL Mahasiswa Individu ($Attainment_{CPL_x}(i)$)
Ketercapaian seorang mahasiswa $i$ pada suatu $CPL_x$ dihitung dari seluruh mata kuliah pembina $CPL_x$:

$$Attainment_{CPL_x}(i) = \frac{\sum_{k \in MK(CPL_x)} \left( SKS_k \times Weight_{k, CPL_x} \times NA_k(i) \right)}{\sum_{k \in MK(CPL_x)} \left( SKS_k \times Weight_{k, CPL_x} \right)}$$

*Ambang Batas Kelulusan CPL Minimum:* **65,0 (Kategori B / Memuaskan)**.

---

### 2.4 Perhitungan Ketercapaian CPL Program Studi ($Cohort\_Attainment_{CPL_x}$)
Untuk akreditasi LAM INFOKOM Kriteria 9, persentase ketercapaian kohor lulusan dihitung:

$$\% Cohort\_Attainment_{CPL_x} = \left( \frac{\text{Jumlah Mahasiswa dengan } Attainment_{CPL_x} \ge 65.0}{\text{Total Mahasiswa dalam Angkatan}} \right) \times 100\%$$

*Target Standar Mutu Prodi SISTEKIN:* **Minimal 80% mahasiswa mencapai threshold CPL $\ge 65,0$**.

---

## 3. MASTER RUBRIK PENILAIAN OBE TERSTANDAR

### 3.1 Rubrik 1: Penilaian Proyek Rekayasa Perangkat Lunak & Coding (PjBL)
*Digunakan untuk MK Praktikum, Platform Engineering, AI, dan Capstone Project.*

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   RUBRIK ANALITIK PROYEK REKAYASA PERANGKAT LUNAK & CODING                       │
├──────────────────┬─────────────────┬─────────────────┬─────────────────┬─────────────────────────┤
│ Kriteria         │ Sangat Baik     │ Baik            │ Cukup           │ Kurang                  │
│                  │ (81 – 100)      │ (70 – 80)       │ (56 – 69)       │ (< 56)                  │
├──────────────────┼─────────────────┼─────────────────┼─────────────────┼─────────────────────────┤
│ 1. Arsitektur &  │ Arsitektur modu-│ Arsitektur cuku-│ Arsitektur ku-  │ Kode monolitik tanpa    │
│    Struktur Kode │ lar, SOLID, rapi│ p modular, pola │ rang teratur,   │ pola, sulit dipahami,   │
│    (Bobot: 25%)  │ & dokumentatif. │ desain standar. │ redundansi kode.│ tidak terstruktur.      │
├──────────────────┼─────────────────┼─────────────────┼─────────────────┼─────────────────────────┤
│ 2. Fungsionalitas│ 100% fitur ber- │ 80-99% fitur ber│ 60-79% fitur ber│ Fitur utama gagal       │
│    & Fitur       │ jalan sempurna, │ jalan baik, bug │ jalan, terjadi  │ berfungsi, sering       │
│    (Bobot: 35%)  │ zero fatal bug. │ minor non-fatal.│ error berulang. │ crash saat runtime.     │
├──────────────────┼─────────────────┼─────────────────┼─────────────────┼─────────────────────────┤
│ 3. UI/UX & Res-  │ Antarmuka intui-│ Antarmuka baik, │ Antarmuka standar│ Antarmuka buruk, sulit │
│    ponsivitas    │ tif, estetik &  │ responsif pada  │ tapi kaku / ada │ digunakan, tidak res-   │
│    (Bobot: 20%)  │ adaptif devices.│ layar utama.    │ cacat layout.   │ ponsif.                 │
├──────────────────┼─────────────────┼─────────────────┼─────────────────┼─────────────────────────┤
│ 4. Pengujian &   │ Unit test kom-  │ Unit test ter-  │ Pengujian manual│ Tidak ada bukti pengu-  │
│    Dokumentasi   │ prehensif, lapo-│ sedia, README   │ terbatas, doku- │ jian, tanpa dokumentasi │
│    (Bobot: 20%)  │ ran teknis rapi.│ cukup memadai.  │ mentasi minim.  │ repositori.             │
└──────────────────┴─────────────────┴─────────────────┴─────────────────┴─────────────────────────┘
```

---

### 3.2 Rubrik 2: Penilaian Presentasi Lisan & Komunikasi Ilmiah
*Digunakan untuk Seminar Proposal, Sidang Proyek, dan Capstone Project.*

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   RUBRIK ANALITIK PRESENTASI LISAN & KOMUNIKASI ILMIAH                           │
├──────────────────┬─────────────────┬─────────────────┬─────────────────┬─────────────────────────┤
│ Kriteria         │ Sangat Baik     │ Baik            │ Cukup           │ Kurang                  │
│                  │ (81 – 100)      │ (70 – 80)       │ (56 – 69)       │ (< 56)                  │
├──────────────────┼─────────────────┼─────────────────┼─────────────────┼─────────────────────────┤
│ 1. Penguasaan    │ Menguasai penuh │ Memahami materi │ Pemahaman cukup │ Tidak menguasai materi, │
│    Materi        │ materi & mampu  │ dengan baik,    │ tetapi ragu-ragu│ tidak mampu menjawab    │
│    (Bobot: 40%)  │ menjawab kritis.│ jawaban tepat.  │ menjawab tanya. │ pertanyaan penguji.     │
├──────────────────┼─────────────────┼─────────────────┼─────────────────┼─────────────────────────┤
│ 2. Kualitas Media│ Slide profesional│ Slide rapi dan  │ Slide terlalu   │ Slide buruk, visual     │
│    Visual        │ visual kuat, data│ teks jelas ter- │ padat teks, gam-│ membingungkan, banyak   │
│    (Bobot: 30%)  │ terstruktur.    │ baca.           │ bar pecah.      │ kesalahan tik (*typo*). │
├──────────────────┼─────────────────┼─────────────────┼─────────────────┼─────────────────────────┤
│ 3. Artikulasi &  │ Artikulasi lu-  │ Komunikasi jelas│ Suara monoton,  │ Komunikasi pasif, waktu │
│    Manajemen Wkt │ gas, percaya    │ kontak mata baik│ melebihi alokasi│ tidak terkontrol, tidak │
│    (Bobot: 30%)  │ diri, tepat wkt.│ tepat waktu.    │ waktu presentasi│ profesional.            │
└──────────────────┴─────────────────┴─────────────────┴─────────────────┴─────────────────────────┘
```

---

## 4. INTEGRASI CAPAIAN CPL KE DALAM SKPI (SURAT KETERANGAN PENDAMPING IJAZAH)

Hasil ketercapaian 14 CPL mahasiswa selama 8 semester akan dicetak sebagai **Portofolio Capaian OBE (Radar Chart CPL)** pada lampiran resmi SKPI lulusan:

```
                  S1 (Sikap & Etika)
                        [100]
                     /    |    \
             KK6 [85]     |     [90] KU1 (Berpikir Kritis)
            /             |             \
      KK5 [92]            |              [88] KU2 (Komunikasi)
     /                    |                    \
   KK4 [80]               |                     [85] KU3 (Manajemen Mandiri)
   |                      |                      |
   KK3 [88]           SISTEKIN                   | P1 (Sains & Mat) [82]
   |                   ALUMNI                    |
   KK2 [94]           OBE RADAR                  | P2 (Konsep SI) [90]
     \                    |                    /
      KK1 [95]            |              [88] P3 (Infra & Security)
            \             |             /
             [92] P4 (RPL & Data Platform)
```

---

## 5. SIKLUS CONTINUOUS QUALITY IMPROVEMENT (CQI) — PPEPP

Apabila terdapat $CPL_x$ yang belum memenuhi ambang batas target prodi ($\ge 80\%$), Program Studi menjalankan siklus perbaikan PPEPP:
1. **Penetapan (P):** Meninjau ulang target baseline CPL.
2. **Pelaksanaan (P):** Mengajar sesuai RPS terstandar OBE.
3. **Evaluasi (E):** Mengukur CPL pada akhir semester via Rapat Tinjauan Kurikulum.
4. **Pengendalian (P):** Melakukan *Root Cause Analysis* (RCA) pada MK yang mengalami anomali nilai.
5. **Peningkatan (P):** Memperbaiki modul praktikum, memberikan pelatihan dosen, atau memperbarui studi kasus industri pada semester berikutnya.

---
*Disahkan sebagai Dokumen Resmi 008 — Kurikulum OBE Revisi SISTEKIN 2026.*  
**Tim Pengembang Kurikulum FSTI Universitas Widyagama Malang**
