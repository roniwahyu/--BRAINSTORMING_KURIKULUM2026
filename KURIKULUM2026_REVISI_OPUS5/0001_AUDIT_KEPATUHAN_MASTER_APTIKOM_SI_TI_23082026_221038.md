# 0001 — AUDIT KEPATUHAN KURIKULUM SISTEKIN 2026 TERHADAP MASTER OBE APTIKOM SI v2.0 + TI 2023

**Objek audit:** 26 file `.md` dalam `KURIKULUM2026_REVISI/`
**Baseline normatif:**
- `BUKU_OBE/OBE_SISTEM_INFORMASI_2.0_APTIKOM_837172072-S1-SI-APTIKOM.md` (2.580 baris) — disebut **[SI]**
- `716903001-PANDUAN-KURIKULUM-OBE-PRODI-S1-TEKNOLOGI-INFORMASI-2023.txt` (6.352 baris) — disebut **[TI]**

**Tanggal:** 23 Agustus 2026, 22:10:38 WIB
**Sifat:** diagnostik. Tidak ada file yang diubah.

---

## KONVENSI PELAPORAN

| Verdикt | Arti |
|---|---|
| **PATUH** | Sesuai aturan normatif master, terverifikasi |
| **DEVIASI** | Bertentangan dengan aturan yang master tulis sebagai normatif/INSTRUKSI |
| **DI LUAR MASTER** | Master tidak mengatur; keputusan prodi, tidak dapat dinilai patuh/tidak |
| **TIDAK DIVERIFIKASI** | Di luar jangkauan bukti yang saya kumpulkan |

Setiap baris temuan menyertakan nomor baris file. Klaim tanpa nomor baris tidak dimasukkan.

---

## RINGKASAN

**7 DEVIASI** terhadap aturan normatif master, **11 PATUH**, **6 DI LUAR MASTER**.

Deviasi terberat bukan pada angka SKS atau jumlah CPL — ketiganya patuh — melainkan pada **tiga hal yang keduanya master tetapkan sebagai normatif dan SISTEKIN tidak terapkan**: kodifikasi CPMK yang harus membawa jejak CPL, kriteria SMART untuk CPMK/Sub-CPMK, dan struktur 12 bagian buku kurikulum.

Satu temuan bersifat substantif terhadap keilmuan: dari 11 Bahan Kajian kompetensi utama yang [SI] wajibkan diadopsi, **2 tidak memiliki padanan** dalam daftar 19 BK-IS SISTEKIN, dan dari 14 BK Penciri Utama [TI], **1 tidak memiliki padanan**. Mata kuliahnya ada; yang tidak ada adalah entri Bahan Kajiannya.

| No | Temuan | Verdикt |
|:---:|---|:---:|
| C-1 | Jumlah CPL, PL, peminatan, SKS, MKWK | **PATUH** (5 aspek) |
| C-2 | 2 dari 11 BK Utama [SI] tanpa padanan | **DEVIASI** |
| C-3 | 1 dari 14 BK Penciri Utama [TI] tanpa padanan | **DEVIASI** |
| C-4 | Kodifikasi CPMK tanpa jejak CPL | **DEVIASI** |
| C-5 | Kriteria SMART tidak diterapkan | **DEVIASI** |
| C-6 | Sub-CPMK tanpa kodifikasi & tanpa tabel pemetaan | **DEVIASI** |
| C-7 | Struktur 12 bagian buku tidak diikuti | **DEVIASI** |
| C-8 | Kriteria capstone [SI] tidak lengkap dipenuhi | **DEVIASI** |
| C-9 | Genealogi CPL-P01..P17 / CPL-K01..K17 | **PATUH** |
| C-10 | Formula ketercapaian CPL | **DI LUAR MASTER** |
| C-11 | Skema 4 titik asesmen & IKU 7 | **DI LUAR MASTER** |
| C-12 | Pemisahan 3 PEO dari 4 PL | **DI LUAR MASTER** |
| C-13 | Penambahan BK penciri khas (AI, Technopreneurship) | **PATUH** |

---

# BAGIAN A — BASELINE NORMATIF MASTER (dasar penilaian)

Bagian ini merekam apa yang master **benar-benar tulis**, agar setiap verdікt di Bagian B dapat dilacak. Pembedaan antara *normatif* dan *contoh* diambil dari kata kunci yang dipakai master sendiri: "INSTRUKSI", "wajib", "harus" = normatif; "disarankan", "contoh", "dapat" = anjuran.

## A.1 Aturan Bahan Kajian

| Master | Aturan verbatim | Baris | Sifat |
|---|---|:---:|:---:|
| **[SI]** | "INSTRUKSI: Program Studi menyusun Daftar Bahan Kajian dengan **mengadopsi 11 BK kompetensi utama** Program Studi Sistem Informasi dan memilih sejumlah BK kompetensi pendukung… Program Studi **dapat menambah BK** sesuai dengan *domain of practice*/value/ciri khas" | 736 | **Normatif** (adopsi 11) + izin menambah |
| **[TI]** | "Prodi menyusun Daftar BK dengan **mengadopsi 14 BK Penciri Utama** PS Teknologi Informasi dan memilih sejumlah BK Penciri Pendukung… **dapat menambah BK** sesuai dengan domain penciri khas" | 1486–1489 | **Normatif** (adopsi 14) + izin menambah |

**Daftar 11 BK kompetensi utama [SI]** (baris 740–760): BK01 *Foundation of Information Systems*, BK02 *Data/Information Management*, BK03 *IT Infrastructure*, BK04 *IS Project Management*, BK05 *Systems Analysis & Design*, BK06 *IS Management and Strategy*, BK07 *Application Development/Programming*, BK08 *Secure Computing*, BK09 *Ethics, use and implications for society*, BK10 *Internship*, BK11 *Mathematics and statistics*.

Komposisi total [SI]: 11 Utama + 1 Umum (BK12 *Research Methodology*) + 7 Pendukung (BK13–BK19) = **19 BK**.

**Daftar 14 BK Penciri Utama [TI]** (baris 1496–1780): BK01 *Virtual Systems and Services*, BK02 *Internet of Things*, BK03 *Jaringan Komputer*, BK04 *Teknologi Sistem Terintegrasi*, BK05 *Teknologi Platform*, BK06 *Pengembangan Aplikasi Berbasis Platform*, BK07 *Prinsip-prinsip Keamanan Siber*, BK08 *Praktek Profesional Global*, BK09 *Manajemen Data dan Informasi*, BK10 *Fundamental Perangkat Lunak*, BK11 *Desain User Experience*, BK12 *Tata kelola dan Kebijakan Keamanan Siber*, BK13 *Manajemen Proyek*, BK14 *Teknologi dan Implementasi Keamanan Siber*.

Komposisi total [TI]: 14 Penciri Utama + 13 Penciri Pendukung (BK15–BK27) = **27 BK**.

## A.2 Aturan CPL dan Profil Lulusan

| Aspek | [SI] | [TI] |
|---|---|---|
| Jumlah CPL | "jumlah yang **disarankan** adalah antara **10 s/d 15 CPL**" (baris 680) | "jumlah yang **disarankan tidak lebih dari 15** CPL Program Studi" (baris 1103–1109) |
| Skema pengkodean CPL | `CPL01..CPLn` **tanpa prefiks kategori**; "kompetensi sikap, pengetahuan dan keterampilan" sebagai cakupan (baris 672, 680) | **4 kategori SN-Dikti eksplisit**: S1–S10, KU1–KU9, P1–P2, KK1–KK3 (baris 942–1086) |
| Jumlah PL | "Jumlah total Profil lulusan yang disusun **disarankan sebanyak 4 (empat) sampai 5 (lima)**" (baris 612) | "**disarankan sebanyak 4 (empat) sampai 5 (lima)**" (baris 842–850) |
| PEO | Istilah PEO **disamakan dengan Profil Lulusan** (baris 332); master **tidak mengatur** jumlah PEO tersendiri | Tidak mengatur PEO tersendiri |
| Referensi CPL | **Lampiran 1**: CPL-K01..K17 (baris 2508–2532) + CPL-P01..P17 (baris 2534–2559), 34 butir, "**dapat mengadopsi**" (baris 678) | Tabel 3 CPL01–CPL05 penciri utama (baris 1110–1158) |

## A.3 Aturan CPMK dan Sub-CPMK

| Aturan | Master | Baris | Sifat |
|---|---|:---:|:---:|
| **Kodifikasi CPMK** | "Penentuan kode CPMK berdasarkan **kode CPL (2 digit) disertakan dengan nomor urut (1 digit)**. Misalnya **CPMK011** artinya CPMK pertama ini diturunkan dari CPL01 dengan nomor urut 1." | [SI] 1124; [TI] 3995–3997 | **Normatif, identik di kedua master** |
| **Kriteria CPMK/Sub-CPMK** | **SMART**: Specific, Measurable, Achievable, Realistic, Time-bound | [SI] 1253–1267; [TI] 3998–4018 | **Normatif, identik di kedua master** |
| Kata kerja | *action verb* / *capability verb* **Robert M. Gagne (1998)** — 5 ranah | [SI] 1124; [TI] 3986–3994 | Normatif |
| Taksonomi Bloom | **Tidak dipakai** sebagai basis perumusan CPMK. [SI] menyebut Bloom hanya di contoh rubrik J.6 (baris 2105 dst); [TI] tidak menyebut Bloom sama sekali | — | — |
| Format ABCD | **Tidak disebut** di kedua master | — | — |
| Jumlah CPMK per MK | **Tidak diatur.** Contoh [SI] Tabel 14 bervariasi 1–5 CPMK/MK (baris 1206–1243) | — | Di luar master |
| Jumlah Sub-CPMK | **Tidak diatur.** Contoh [SI] Tabel 15 menampilkan 2 Sub-CPMK/CPMK (baris 1271–1313) | — | Di luar master |
| Kewajiban pemetaan | "Prodi **juga wajib** memetakan pencapaian CPMK dan CPL pada matakuliah (MK)" | [TI] 4020–4025 | **Normatif** |
| Tabel Sub-CPMK | "Program Studi **membuat Sub-CPMK** dari masing-masing CPMK yang ditetapkan seperti pada Tabel 15" | [SI] 1269 | **Normatif** |

## A.4 Aturan SKS dan Struktur Semester

| Aturan | Master | Baris |
|---|---|:---:|
| Beban minimal | "beban belajar **minimal 144 SKS**… Masa Tempuh Kurikulum 8 semester" (Permendikbudristek 53/2023 Pasal 18) | [SI] 1091 |
| Batas Sem 1–2 | "semester satu dan semester dua **paling banyak 20 SKS**" | [SI] 1091 |
| Batas Sem 3+ | "semester tiga dan seterusnya **paling banyak 24 SKS**" | [SI] 1091 |
| Rentang [TI] | "sekurang-kurangnya **144** dan sebanyak-banyaknya **160 SKS**… 18–20 SKS per semester, maks 24 bagi mahasiswa berprestasi setelah tahun pertama" | [TI] 3782–3789 |
| MKWK wajib | Agama, Pancasila, Kewarganegaraan, Bahasa Indonesia; "**disarankan** dilakukan di semester awal (2 tahun pertama)" | [TI] 3790–3794; [SI] 1089 |
| Bobot SKS per MK | "**umumnya 2 atau 3 SKS** per mata kuliah" | [SI] 958–970 |
| MK kompetensi utama | "**disarankan menyertakan 25** mata kuliah kompetensi utama" | [SI] 1083 |
| Peminatan | "Jumlah peminatan/konsentrasi program studi **disarankan 1 s/d 3 peminatan**" | [SI] 1089; [TI] 3795–3798 |
| SKS per peminatan | **Tidak diatur** oleh kedua master | — |

## A.5 Aturan Asesmen

| Aturan | Master | Baris |
|---|---|:---:|
| Total bobot per MK | "**Akumulasi bobot penilaian setiap mata kuliah adalah 100**" | [SI] 1776, 1910; [TI] 5697–5700 |
| Bobot akumulasi per CPL | "Bobot akumulasi pada setiap CPL memungkinkan **lebih/kurang dari 100**" | [SI] 1776; [TI] 5697–5700 |
| Jumlah titik asesmen | **Tidak diatur.** "Pemilihan metode perhitungan dan bobot… **ditentukan berdasarkan kebijakan Program Studi**" | [SI] 1622; [TI] 5277–5285 |
| Penempatan pekan | **Tidak diatur** selain pekan 8 (UTS) dan 16 (UAS) di template RPS | [SI] 1484; [TI] 5021–5032 |
| IKU 7 / ambang ≥50% | **Tidak disebut** oleh kedua master. Istilah "IKU" hanya di Daftar Istilah | [SI] 257; [TI] 357–358 |
| Jenis rubrik | 3 jenis: **holistik, analitik, skala persepsi** | [SI] 1719–1725; [TI] 5406–5411 |
| Formula ketercapaian CPL | Σ skor CPMK diperoleh ÷ Σ bobot maksimal CPMK × 100% (contoh: `(30+50+30+40)/(40+60+45+55)×100% = 75%`) | [SI] `.txt` 9322–9323 |
| Ambang lulus CPL | **Tidak ditetapkan angkanya** | — |

## A.6 Aturan Capstone Project

**[SI] baris 1047–1065 — kriteria verbatim, 7 butir:**
1. "Menerapkan pengetahuan/ketrampilan yang telah diperolah dari proses pembelajaran sebelumnya."
2. "Dikerjakan secara berkelompok (**3-6 orang**)."
3. "Menyelesaikan masalah riil/nyata di masyarakat"
4. "*Problem* yang diselesaikan termasuk kategori **permasalahan infokom yang kompleks / *complex computing problem***… keterlibatan lebih dari satu pemangku kepentingan dan kebutuhan/permasalahan yang belum terdefinisi dengan baik."
5. "Hasil *project* berupa desain… atau produk…"
6. "Jumlah sks antara **3-6 SKS**."
7. "Mata kuliah *capstone project* **harus memiliki panduan tersendiri**."

Kewajiban penetapan: "Program studi **harus menentukan** MK yang memenuhi kriteria *capstone project*" ([SI] 818–820), "**wajib menyatakan** mata kuliah yang dapat memenuhi kriteria" ([SI] 828; [TI] 2216–2221).

**TA non-skripsi:** [SI] dan [TI] **tidak mengatur**. [TI] tidak memuat frasa "non-skripsi" sama sekali.

## A.7 Struktur Buku Kurikulum

| Master | Aturan | Baris |
|---|---|:---:|
| **[SI]** | "Program Studi (Prodi) **menyusun buku kurikulum prodi dengan mengikuti struktur** yang ada dalam panduan ini. Buku kurikulum prodi berisi **12 Bagian**" (A–L) | 374–388 |
| **[TI]** | "Buku kurikulum prodi berisi **12 Bab**" (I–XII) | 453–461 |

**12 bagian wajib (identik substansinya di kedua master):**

| # | [SI] Bagian | [TI] Bab |
|:---:|---|---|
| 1 | A. Identitas Program Studi | I. Identitas Program Studi |
| 2 | B. Evaluasi Kurikulum dan *Tracer Study* | II. Evaluasi Kurikulum dan Tracer Study |
| 3 | C. Landasan Perancangan dan Pengembangan Kurikulum | III. (idem) |
| 4 | D. Rumusan Visi, Misi, Tujuan, Strategi, *University Value* | IV. (idem) |
| 5 | E. Rumusan Standar Kompetensi Lulusan | V. Rumusan SKL |
| 6 | F. Penetapan Bahan Kajian | VI. (idem) |
| 7 | G. Pembentukan MK dan Penentuan Bobot SKS | VII. (idem) |
| 8 | H. Matriks dan Peta Kurikulum | VIII. (idem) |
| 9 | I. Rencana Pembelajaran Semester | IX. (idem) |
| 10 | J. Asesmen Pembelajaran | X. (idem) |
| 11 | K. Rencana Implementasi Hak Belajar Maks. 3 Semester di Luar Prodi | XI. (idem) |
| 12 | L. Manajemen dan Mekanisme Pelaksanaan Kurikulum | XII. (idem) |

---

# BAGIAN B — TEMUAN KEPATUHAN

## C-1. Jumlah CPL, PL, Peminatan, SKS, MKWK — **PATUH** (5 aspek)

| Aspek | Aturan master | Kondisi SISTEKIN | Bukti | Verdікt |
|---|---|---|---|:---:|
| Jumlah CPL | 10–15 disarankan ([SI] 680); ≤15 ([TI] 1103) | **14 CPL** (S1, KU1–3, P1–4, KK1–6) | `003:56-71` | **PATUH** |
| Skema kategori CPL | 4 kategori SN-Dikti ([TI] 931–937) | 4 kategori S/KU/P/KK | `003`, `009A`–`009D` | **PATUH** |
| Jumlah PL | 4–5 disarankan ([SI] 612; [TI] 842) | **4 PL** | `002` | **PATUH** |
| Jumlah peminatan | 1–3 disarankan ([SI] 1089; [TI] 3795) | **3 peminatan** | `005:216-218` | **PATUH** |
| Beban minimal | ≥144 SKS ([SI] 1091) | **146 SKS** | `005`, hitung ulang 55 baris = 146 | **PATUH** |
| Batas Sem 1–2 | ≤20 SKS ([SI] 1091) | Sem 1 = 19, Sem 2 = 20 | `005:92,107` | **PATUH** |
| Batas Sem 3+ | ≤24 SKS ([SI] 1091) | Maksimum 21 (Sem 4 & 5) | `005:137,152` | **PATUH** |
| MKWK 4 wajib | Agama, Pancasila, Kewarganegaraan, Bhs Indonesia ([TI] 3790) | Keempatnya ada | `005:89,90,91,135` | **PATUH** |
| MKWK di 2 tahun pertama | Disarankan ([TI] 3790–3794) | Sem 1 (3 MK) dan Sem 4 (2 MK) | `005:89-91,135-136` | **PATUH** |
| Bobot SKS per MK | Umumnya 2–3 SKS ([SI] 958) | Seluruh MK 2–3 SKS kecuali `FST-714` 6 SKS | `005` | **PATUH** |

Catatan: `FST-714` Skripsi 6 SKS berada di luar rentang "umumnya 2 atau 3 SKS", tetapi [TI] mencontohkan "MK25 Tugas Akhir | 6" (baris 3743–3752), sehingga 6 SKS untuk TA justru selaras dengan contoh master.

## C-2. Dua dari Sebelas BK Kompetensi Utama [SI] Tanpa Padanan — **DEVIASI**

[SI] baris 736 menetapkan kata **"mengadopsi"** untuk 11 BK kompetensi utama. Pemetaan 19 BK-IS SISTEKIN (`003:114-132`) terhadap 11 BK wajib tersebut:

| # | BK Utama [SI] | Padanan BK-IS SISTEKIN | Status |
|:---:|---|---|:---:|
| BK01 | *Foundation of Information Systems* | `BK-IS01` *Foundations of Information Systems* | ✅ |
| BK02 | *Data/Information Management* | `BK-IS02` *Data and Information Management* | ✅ |
| BK03 | *IT Infrastructure* | `BK-IS03` *IT Infrastructure and Networking* | ✅ |
| BK04 | *IS Project Management* | `BK-IS08` *Project Management* | ✅ |
| BK05 | *Systems Analysis & Design* | `BK-IS07` *Systems Analysis and Design* | ✅ |
| BK06 | *IS Management and Strategy* | `BK-IS05` *IS Management and Governance* | ✅ |
| BK07 | *Application Development/Programming* | `BK-IS11` *Programming Fundamentals & Object-Oriented* | ✅ |
| BK08 | *Secure Computing* | `BK-IS06` *Information Security and Risk Management* | ✅ |
| **BK09** | ***Ethics, use and implications for society*** | **TIDAK ADA** | ❌ |
| **BK10** | ***Internship*** | **TIDAK ADA** | ❌ |
| BK11 | *Mathematics and statistics* | `BK-IS10` *Applied Mathematics and Logic* | ✅ |

**Verifikasi ketiadaan.** Pencarian pada seluruh 26 file `.md`:

```
grep -hn "BK-IS\|BK-IT" *.md | grep -i "ethic\|etika\|society\|sosial"
  → 2 hit, keduanya BUKAN entri BK (baris 26 dan 40 file 016, konteks tabel klaster peminatan)

grep -hn "BK-IS\|BK-IT" *.md | grep -i "intern\|magang\|PKL\|work"
  → 10 hit, SELURUHNYA adalah BK-IS03/BK-IT03 "Networking" (kata "Networking" mengandung "work")
```

Tidak ada satu pun entri BK bertema Etika maupun Internship dalam 19 BK-IS atau 14 BK-IT SISTEKIN.

**Yang perlu dibedakan.** Mata kuliahnya **ada dan terpetakan**: `FST-206` Etika Profesi & Hukum Digital (2 SKS, Sem 2) dan `FST-612` Praktik Kerja Lapangan (3 SKS, Sem 7). Keduanya dipetakan ke BK lain di `004`:

| MK | Dipetakan ke | Baris 004 |
|---|---|:---:|
| `FST-206` | `BK-IS06` *Information Security & Risk Mgmt*, `BK-IS14` *IT Audit and Compliance*, `BK-IT12` *IT Risk Mgmt and Compliance* | 221, 229, 253 |
| `FST-612` | `BK-IS08` *Project Management* | 223 |

Jadi deviasinya bukan kekosongan kurikuler, melainkan **ketiadaan entri Bahan Kajian**. Konsekuensi konkretnya: dalam pemetaan CPL↔BK dan BK↔MK, muatan etika tersubordinasi ke domain keamanan dan audit, sementara PKL tersubordinasi ke manajemen proyek. `BK-IS09` *Ethics* pada master berkategori **Utama** dan bersumber IS2020; `BK-IS10` *Internship* berkategori **Utama** dan bersumber **IABEE** — yang terakhir ini relevan langsung bagi jalur akreditasi internasional.

**Catatan lanjutan.** BK12 *Research Methodology* (kategori **Umum** pada [SI], baris 761) juga tidak memiliki padanan entri BK di SISTEKIN, meski MK `FST-611` Metodologi Penelitian ada. Karena kategorinya "Umum" dan bukan "Utama", ini tidak masuk hitungan deviasi terhadap kata "mengadopsi 11 BK kompetensi utama".

## C-3. Satu dari Empat Belas BK Penciri Utama [TI] Tanpa Padanan — **DEVIASI**

[TI] baris 1486 menetapkan **"mengadopsi 14 BK Penciri Utama"**. Pemetaan 14 BK-IT SISTEKIN (`003:142-155`):

| # | BK Penciri Utama [TI] | Padanan BK-IT SISTEKIN | Status |
|:---:|---|---|:---:|
| BK01 | *Virtual Systems and Services* | `BK-IT05` *Cloud Computing & Virtualization* | ✅ |
| BK02 | *Internet of Things* | `BK-IT14` *IoT and Embedded Smart Systems* | ✅ |
| BK03 | *Jaringan Komputer* | `BK-IT03` *Networking & Communications* | ✅ |
| BK04 | *Teknologi Sistem Terintegrasi* | `BK-IT07` *System Integration and Architecture* | ✅ |
| BK05 | *Teknologi Platform* | `BK-IT04` *Platform Technologies & Web/Mobile* | ✅ |
| BK06 | *Pengembangan Aplikasi Berbasis Platform* | `BK-IT11` *Software Development Practices* | ✅ |
| BK07 | *Prinsip-prinsip Keamanan Siber* | `BK-IT06` *Cybersecurity Principles & Defense* | ✅ |
| **BK08** | ***Praktek Profesional Global*** | **TIDAK ADA** | ❌ |
| BK09 | *Manajemen Data dan Informasi* | `BK-IT09` *Data Analytics & Information Visualization* | ⚠️ parsial |
| BK10 | *Fundamental Perangkat Lunak* | `BK-IT11` *Software Development Practices* | ⚠️ ganda dgn BK06 |
| BK11 | *Desain User Experience* | `BK-IT10` *User Experience & Interaction Design* | ✅ |
| BK12 | *Tata kelola dan Kebijakan Keamanan Siber* | `BK-IT08` *IT Service Management & Governance* | ✅ |
| BK13 | *Manajemen Proyek* | `BK-IT12` *IT Risk Management and Compliance* | ⚠️ tidak setara |
| BK14 | *Teknologi dan Implementasi Keamanan Siber* | `BK-IT06` *Cybersecurity Principles & Defense* | ⚠️ ganda dgn BK07 |

**Verifikasi BK08.** Pencarian "professional practice" / "praktek profesional" / "praktik profesional" pada 26 file menghasilkan hit di `002`, `003`, `004`, `007`, `010`, dan Buku Final — namun **seluruhnya merujuk nomenklatur PEO-1 "*Professional Practice & Systems Integration*"**, bukan entri Bahan Kajian. Contoh `004:42`: "**PEO-1** | **Professional Practice & Systems Integration:** Menjadi praktisi profesional…". Tidak ada entri BK bertema Praktek Profesional Global.

**Analisis pemetaan parsial.** Karena SISTEKIN memakai 14 BK-IT untuk memetakan 14 BK Penciri Utama [TI], sementara tiga BK-IT dipakai ganda (`BK-IT06` menampung BK07 dan BK14; `BK-IT11` menampung BK06 dan BK10) dan `BK-IT12` *IT Risk Management* tidak setara dengan BK13 *Manajemen Proyek*, maka **cakupan riil lebih sempit dari yang tampak dari kesamaan angka 14**. Angka 14 BK-IT SISTEKIN adalah kebetulan numerik, bukan pemetaan satu-satu terhadap 14 BK Penciri Utama [TI].

**Klaim "14/27" perlu dikoreksi redaksinya.** `003:24` menuliskan `IT2017["APTIKOM IT2017 (14/27 Bahan Kajian)"]`. Angka 27 memang benar sebagai total BK [TI] (BK01–BK27, terverifikasi [TI] baris 1496–2004). Namun frasa "14/27" mengimplikasikan bahwa 14 BK yang diambil adalah subset dari 27 — padahal nama dan cakupan 14 BK-IT SISTEKIN **tidak identik** dengan BK01–BK14 [TI]. Redaksi yang akurat: "14 BK-IT SISTEKIN, dirumuskan ulang dari 27 BK IT2017/CC2020".

## C-4. Kodifikasi CPMK Tidak Membawa Jejak CPL — **DEVIASI**

Ini deviasi terhadap aturan yang **kedua master tulis identik dan normatif**.

| Master | Aturan verbatim | Baris |
|---|---|:---:|
| [SI] | "Penentuan kode CPMK berdasarkan **kode CPL (2 digit) disertakan dengan nomor urut (1 digit)**. Misalnya CPMK011 artinya CPMK pertama ini diturunkan dari CPL01 dengan nomor urut 1." | 1124 |
| [TI] | Kalimat **identik** | 3995–3997 |

**Kondisi SISTEKIN.** Hitung seluruh kode CPMK pada `007`:

```
grep -oh "CPMK-[0-9]\|CPMK[0-9][0-9][0-9]" 007_...md | sort | uniq -c
     65 CPMK-1
     65 CPMK-2
     62 CPMK-3
     34 CPMK-4
```

Tidak ada satu pun kode berformat `CPMK011` (3 digit). Seluruh 226 kode memakai format `CPMK-n` dengan `n` = nomor urut lokal dalam mata kuliah, **tanpa membawa kode CPL asalnya**.

**Konsekuensi keterlacakan.** Format master memungkinkan asesor membaca satu kode dan langsung mengetahui CPL asalnya. Format SISTEKIN tidak: `CPMK-1` pada `STI-401` dan `CPMK-1` pada `MKU-101` tidak dapat dibedakan asal CPL-nya tanpa membuka Tabel A masing-masing MK. Karena `007` juga tidak mencantumkan kode CPMK pada kolom asesmen maupun pada 1.040 baris matriks pertemuan (terverifikasi: 0 dari 264 baris asesmen dan 0 dari 1.040 baris pertemuan memuat kode CPMK), keterlacakan CPL→CPMK→asesmen menjadi berlapis dua tingkat tidak langsung.

**Catatan angka.** Sebaran 65/65/62/34 mengonfirmasi temuan dokumen 019 (P1-1): 31 MK tidak memiliki 4 CPMK. Di sini relevansinya berbeda — bukan soal jumlah, tetapi bahwa penomoran lokal 1..n membuat ketiadaan CPMK-4 tampak sebagai "kurang satu nomor", sedangkan dengan format master ketiadaannya akan langsung terbaca sebagai CPL mana yang tidak diases.

## C-5. Kriteria SMART Tidak Diterapkan — **DEVIASI**

| Master | Aturan | Baris |
|---|---|:---:|
| [SI] | Sub-CPMK harus **SMART**: Specific, Measurable, Achievable, Realistic, Time-bound | 1253–1267 |
| [TI] | "rumusan CPMK yang baik memiliki sifat: 1. Specific… 2. Measurable… 3. Achievable… 4. Realistic… 5. Time-bound" | 3998–4018 |

**Verifikasi ketiadaan.** Pencarian case-sensitive "SMART" pada 26 file menghasilkan 3 hit, dan **ketiganya adalah nama peminatan**, bukan kriteria:

| File | Baris | Konteks |
|---|:---:|---|
| `011` | 153 | `D. MK PILIHAN P1: INTEGRATED SMART SYSTEMS (6 MK / 18 SKS)` |
| `004` | 142 | `### TABEL 4.1: PEMINATAN 1 — INTEGRATED SMART SYSTEMS` |
| Buku Final | — | konteks sama |

Pencarian frasa penyusunnya (`specific.*measurable` / `measurable.*achievable`, case-insensitive) menghasilkan **0 hit**. Pencarian "Gagne" menghasilkan **0 hit** di seluruh 26 file.

**Apa yang dipakai SISTEKIN sebagai gantinya.** Dokumen memakai **ABCD + Taksonomi Bloom**: 132 kemunculan "ABCD" di `007`, 133 di Buku Final, dan "Bloom" muncul di 10 file (`007`: 132 kali). `AGENTS.md` sendiri menyatakan: *"Gunakan action verb (Gagne) + Taksonomi Bloom untuk CPMK. ABCD = praktik baik, bukan tuntutan literal BUKU_OBE."*

**Penilaian.** Pernyataan `AGENTS.md` bahwa ABCD bukan tuntutan master adalah **benar** — terverifikasi, kedua master tidak menyebut ABCD. Namun kalimat itu menyebut "action verb (Gagne)" sebagai yang dipakai, padahal **Gagne tidak disebut sama sekali** dalam 26 file. Yang dipakai adalah Bloom, yang justru bukan basis perumusan CPMK menurut kedua master ([TI] tidak menyebut Bloom; [SI] menyebutnya hanya di contoh rubrik).

Deviasinya bukan pada pemakaian Bloom — master tidak melarangnya — melainkan pada **tidak diterapkannya kriteria SMART yang kedua master tetapkan secara normatif**. Tidak ada dokumen SISTEKIN yang menyatakan bahwa CPMK/Sub-CPMK-nya memenuhi Specific-Measurable-Achievable-Realistic-Time-bound, dan tidak ada instrumen verifikasi untuk itu.

---

## C-6. Sub-CPMK Tanpa Kodifikasi dan Tanpa Tabel Pemetaan — **DEVIASI**

[SI] baris 1269 (INSTRUKSI, normatif): *"Program Studi **membuat Sub-CPMK** dari masing-masing CPMK yang ditetapkan seperti pada **Tabel 15**."* Tabel 15 [SI] (baris 1271–1313) berbentuk pemetaan eksplisit CPMK → Sub-CPMK dengan kode.

**Kondisi SISTEKIN.** Pemeriksaan `007`:

| Pemeriksaan | Hasil |
|---|:---:|
| Kemunculan string "Sub-CPMK" per blok MK | **tepat 2 per blok** (65 blok × 2 = 130) — yaitu di judul Tabel C dan di header kolom |
| Kode Sub-CPMK spesifik (`Sub-CPMK-1.1`, `Sub-CPMK 1`, `SubCPMK`) | **0 kemunculan** |
| Tabel pemetaan CPMK → Sub-CPMK tersendiri | **tidak ada** |

Struktur aktual (`007:85-92`): kolom kedua Tabel C berjudul "Sub-CPMK & Kemampuan Akhir", diisi rumusan naratif per pekan tanpa kode. Contoh baris pekan 4:

```
| **4** | **Mampu menyederhanakan fungsi logika dengan Aljabar Boolean (C3)** | ... | **Tugas 1: Kuis & Problem Solving (Bobot: 20%)** |
```

**Penilaian.** Rumusan kemampuan akhir per pekan **ada** dan bermutu (memuat level Bloom eksplisit). Yang tidak ada adalah (a) kodifikasi Sub-CPMK, dan (b) tabel pemetaan CPMK→Sub-CPMK yang [SI] instruksikan. Akibatnya tidak dapat ditelusuri Sub-CPMK pekan ke-4 diturunkan dari CPMK yang mana — hanya dapat disimpulkan dari kedekatan posisi dengan titik asesmen.

Karena master **tidak mengatur jumlah** Sub-CPMK per CPMK, banyaknya rumusan (16 per MK, satu per pekan) bukan deviasi. Deviasinya murni pada kodifikasi dan tabel pemetaan.

## C-7. Struktur 12 Bagian Buku Kurikulum Tidak Diikuti — **DEVIASI**

Kedua master memakai kata **"menyusun… dengan mengikuti struktur"** ([SI] 374) dan menetapkan 12 bagian. Uji keberadaan setiap bagian pada `BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md` (4.044 baris), memakai pencarian judul **dan** pencarian substansi:

| # | Bagian Wajib Master | Hit Judul | Hit Substansi | Status |
|:---:|---|:---:|:---:|:---:|
| 1 | Identitas Program Studi | **0** | 12 (`Akreditasi`/`Gelar`) | ⚠️ substansi tersebar, tanpa bagian |
| 2 | Evaluasi Kurikulum dan *Tracer Study* | **0** ("Evaluasi Kurikulum") | 7 (`Tracer Study`) | ⚠️ hanya tracer study |
| 3 | Landasan Perancangan & Pengembangan | 4 | — | ⚠️ tersebar |
| 4 | Rumusan Visi, Misi, Tujuan, Strategi | 1 | — | ❌ **isi VMTS tidak ada** (lihat bawah) |
| 5 | Rumusan Standar Kompetensi Lulusan (SKL) | **0** | 2 | ❌ Tidak ada bagian |
| 6 | Penetapan Bahan Kajian | 74 | — | ✅ Ada |
| 7 | Pembentukan MK & Bobot SKS | 67 | — | ✅ Ada |
| 8 | Matriks dan Peta Kurikulum | **0** | — | ❌ Tidak ada bagian |
| 9 | Rencana Pembelajaran Semester | 1 | — | ⚠️ Minimal |
| 10 | Asesmen Pembelajaran | **0** | — | ❌ Tidak ada bagian (materinya ada di Bab VII dgn judul lain) |
| 11 | Hak Belajar Maks. 3 Semester di Luar Prodi | **0** | 9 (`MBKM`) | ⚠️ substansi ada, bagian tidak |
| 12 | Manajemen & Mekanisme Pelaksanaan | **0** | 32 (`Tata Kelola`) | ⚠️ substansi ada, bagian tidak |

**Struktur bab aktual** hanya 5 dari 8 yang direncanakan sendiri: Bab II (`:21`), IV (`:161`), VI (`:408`), VII (`:492`), VIII (`:813`). Bab I, III, dan V tidak ada.

**Temuan yang paling berdampak: Bagian 4 dan 5 kosong isinya.** Bab II berjudul "VISI, MISI, TUJUAN, DAN POSITIONING STRATEGIS", tetapi pencarian frasa kanonik Visi 2045 menghasilkan:

| Frasa dicari | Sumber | Hit di Buku Final |
|---|---|:---:|
| "unggul dalam pengembangan sistem dan teknologi informasi cerdas" | Visi 2045, `001:56` | **0** |
| "bermartabat" | Visi 2045 | **0** |
| "Kekuatan (Strengths)" | SWOT, `001` §3 | **0** |

Bab IV berjudul "CPL dan BoK", tetapi:

| Elemen | Hit di Buku Final |
|---|:---:|
| "Menguasai konsep dasar sains, matematika terapan" (rumusan P1, `009C:14`) | **0** |
| "Bertakwa kepada Tuhan" (rumusan S1, `009A:12`) | **0** |
| "CPL-P01" (genealogi IS2020) | **0** |

Jadi dua bagian yang master tempatkan sebagai inti Standar Kompetensi Lulusan — rumusan VMTS dan rumusan tekstual CPL — **tidak termuat dalam naskah buku**, meskipun tersedia lengkap di dokumen pendukung `001`, `003`, dan `009A`–`009E`.

**Catatan proporsionalitas.** Master menyediakan struktur sebagai kerangka; prodi boleh menamai bab berbeda. Yang menjadikan ini deviasi bukan perbedaan nama, melainkan **tiga bagian wajib yang tidak memiliki representasi sama sekali** (Matriks dan Peta Kurikulum, Standar Kompetensi Lulusan, Asesmen Pembelajaran sebagai bagian tersendiri) ditambah **dua bagian yang ada judulnya tetapi kosong isinya** (VMTS, rumusan CPL).

## C-8. Kriteria Capstone [SI] Tidak Lengkap Dipenuhi — **DEVIASI**

[SI] baris 1047–1065 menetapkan 7 kriteria; baris 828 menyatakan prodi **"wajib menyatakan"** MK yang memenuhinya. Uji terhadap `009_PEDOMAN_CAPSTONE_PROJECT_DAN_TUGAS_AKHIR_NON_SKRIPSI.md` (78 baris) dan `FST-610` Capstone Project FSTI (3 SKS, Sem 7):

| # | Kriteria [SI] | Kondisi SISTEKIN | Bukti | Status |
|:---:|---|---|---|:---:|
| 1 | Menerapkan pengetahuan dari pembelajaran sebelumnya | Prasyarat `STI-506` + ≥100 SKS | `005:174` | ✅ |
| 2 | **Berkelompok 3–6 orang** | **Tidak dinyatakan** | pencarian "3-6"/"anggota"/"orang" pada `009` = 0 hit | ❌ |
| 3 | Menyelesaikan masalah riil di masyarakat | "Identifikasi Masalah Mitra", "Uji Kelayakan Mitra" | `009:13,18` | ✅ |
| 4 | **Kategori *complex computing problem*** | **Tidak dinyatakan di `009`** | frasa hanya muncul di `009C` (2×) dan `011` (1×), bukan di pedoman capstone | ❌ |
| 5 | Luaran berupa desain atau produk | "Capstone Expo / Demo Day… Laporan Akhir" | `009:18` | ✅ |
| 6 | **Jumlah SKS 3–6** | `FST-610` = **3 SKS** | `005:174` | ✅ |
| 7 | **Harus memiliki panduan tersendiri** | `009` ada (78 baris) tetapi **62 dari 78 barisnya membahas 4 opsi TA non-skripsi**, bukan capstone | `009:20-60` | ⚠️ |

**Analisis kriteria 7.** Dokumen `009` bernama "Pedoman Capstone Project dan Tugas Akhir Non-Skripsi". Isinya: baris 13–18 memuat timeline capstone 16 minggu (6 baris), sedangkan baris 20–60 memuat 4 opsi jalur TA secara rinci. Jadi capstone mendapat porsi ~8% dari dokumen yang seharusnya menjadi panduannya. [SI] menuntut **"panduan tersendiri"** — dengan porsi sekecil itu dan tanpa rubrik, tanpa ukuran tim, tanpa kriteria kompleksitas, dokumen ini belum memenuhi tuntutan tersebut.

**Yang justru melampaui master.** 4 opsi TA non-skripsi (`009:20-60`: Skripsi Riset Eksperimental, Proyek Inovasi Produk TRL≥6, Tech Startup MVP, Publikasi SINTA 1-2/Scopus) adalah **materi yang tidak diatur kedua master** — [TI] bahkan tidak memuat frasa "non-skripsi". Ini bersandar pada Permendikbudristek 53/2023 Pasal 19, bukan pada master APTIKOM, dan merupakan kekuatan dokumen SISTEKIN. Tidak dinilai sebagai deviasi.

## C-9. Genealogi CPL-P01..P17 dan CPL-K01..K17 — **PATUH**

[SI] baris 678 menyatakan prodi "**dapat mengadopsi** beberapa referensi CPL pada **Lampiran 1 Tabel Referensi CPL**". Lampiran 1 [SI] memuat CPL-K01..K17 (baris 2508–2532) dan CPL-P01..P17 (baris 2534–2559), total 34 butir.

`AGENTS.md` menyatakan CPL SISTEKIN "Dilengkapi genealogi sumber IS2020 CPL-P01..P17 & CPL-K01..K17 serta IT2017 KK1..KK3". Terverifikasi ada di `003` (35 kemunculan pola CPL-P/CPL-K, sebagaimana dilaporkan pada audit terdahulu) dan `009C`.

**Verdікt PATUH**, dengan dua catatan faktual:
1. Sifat aturannya **"dapat mengadopsi"**, bukan wajib — jadi mencantumkan genealogi adalah praktik yang melebihi tuntutan minimum, bukan kepatuhan wajib.
2. Lampiran 1 [SI] **tidak menyediakan** blok referensi untuk ranah Sikap dan Keterampilan Umum. Karena itu genealogi `S1` dan `KU1`–`KU3` SISTEKIN tidak dapat bersumber dari Lampiran 1; keduanya bersumber SN-Dikti langsung, yang juga sah dan konsisten dengan [TI] baris 942–1037 (S1–S10, KU1–KU9 dari SN-DIKTI).

## C-10. Formula Ketercapaian CPL — **DI LUAR MASTER** (lebih ketat dari master)

| Aspek | Master | SISTEKIN |
|---|---|---|
| Formula | Σ skor CPMK ÷ Σ bobot maks × 100%. Contoh [SI] `.txt` 9322: `(30+50+30+40)/(40+60+45+55)×100% = 75%` | `008:66`: $Attainment_{CPL_x}(i) = \frac{\sum_k (SKS_k \times Weight_{k,CPL_x} \times NA_k(i))}{\sum_k (SKS_k \times Weight_{k,CPL_x})}$ |
| Pembobot | Bobot CPMK saja | **SKS × Weight** — menambahkan SKS sebagai pembobot |
| Ambang lulus CPL | **Tidak ditetapkan** | `008:75-77`: threshold individu ≥65,0; target kohort **≥80% mahasiswa** |
| Aturan yang mengikat | "Pemilihan metode perhitungan… **ditentukan berdasarkan kebijakan Program Studi**" ([SI] 1622) | — |

**Penilaian.** Master secara eksplisit menyerahkan metode perhitungan ke prodi, sehingga formula SISTEKIN **tidak dapat dinilai patuh/menyimpang**. Secara substansi formula SISTEKIN lebih informatif karena membobot kontribusi MK dengan SKS-nya — MK 3 SKS berkontribusi lebih besar pada ketercapaian CPL daripada MK 2 SKS, yang secara pedagogis dapat dipertahankan. Penetapan ambang ≥65,0 dan target kohort ≥80% juga mengisi kekosongan yang master tinggalkan.

Satu hal yang perlu dicatat: karena master tidak menetapkan ambang, angka 65,0 dan 80% adalah keputusan prodi yang **harus dapat dipertanggungjawabkan sendiri** di hadapan asesor — tidak dapat dirujuk ke APTIKOM.

## C-11. Skema 4 Titik Asesmen dan IKU 7 — **DI LUAR MASTER**

| Aspek | Master | SISTEKIN |
|---|---|---|
| Jumlah titik asesmen | **Tidak diatur.** Kedua master menyerahkan ke prodi ([SI] 1622; [TI] 5277–5285) | 4 titik baku: Tugas 1 (20%), UTS (25–30%), Tugas 2 (20–25%), UAS (30%) — `008:33-37` |
| Penempatan pekan | Hanya pekan 8 (UTS) & 16 (UAS) di template RPS ([SI] 1484) | Pekan 4/5, 8, 12/13, 16 — `008:33-36` |
| Total bobot per MK | **=100** (normatif, [SI] 1776) | 100% pada **65/65 MK** (terverifikasi) — **PATUH** |
| IKU 7 ≥50% | **Tidak disebut** kedua master; "IKU" hanya di Daftar Istilah ([SI] 257; [TI] 357) | `008:23` mewajibkan ≥50% Case Method/PjBL |
| Jenis rubrik | 3 jenis: holistik, analitik, skala persepsi ([SI] 1719) | `008:88-113` memakai **rubrik analitik** (4 rubrik master) |

**Penilaian.** Skema 4 titik dan IKU 7 adalah kebijakan prodi yang sah dan lebih terstruktur dari master. Aturan master yang benar-benar normatif di area ini — total bobot per MK = 100 — **dipatuhi sempurna pada 65 dari 65 MK**.

Rubrik analitik yang dipilih SISTEKIN adalah satu dari tiga jenis yang master sediakan, jadi **PATUH**. Namun perlu dicatat bahwa master menyediakan tiga jenis untuk konteks berbeda; `018_PANDUAN_RUBRIK_KLASTER` hanya mengembangkan jenis analitik. Untuk asesmen ranah Sikap (CPL `S1`), master mencontohkan rubrik skala persepsi dan portofolio ([SI] 1755–1764) — apakah rubrik analitik memadai untuk ranah afektif adalah pertanyaan yang layak diantisipasi.

## C-12. Pemisahan 3 PEO dari 4 PL — **DI LUAR MASTER**

| Master | Perlakuan PEO |
|---|---|
| [SI] | Istilah PEO muncul **sekali**, disamakan dengan PL: "apakah **profil lulusan (PEO)** dan capaian pembelajaran program (PLO) telah tercapai" (baris 332). Bagian E hanya mengatur Profil Lulusan. |
| [TI] | Tidak mengatur PEO sebagai entitas tersendiri |

**Kondisi SISTEKIN:** memisahkan **3 PEO** (`002`) dari **4 PL** (`002`), dengan matriks PEO↔CPL tersendiri di `003` §7 dan `004` §2.

**Penilaian.** Master **tidak mengatur** pemisahan ini, sehingga tidak dapat dinilai patuh/menyimpang. Pemisahan PEO dari PL adalah praktik standar IABEE/ABET (PEO = tujuan 3–5 tahun pascalulus; PL/PLO = capaian saat lulus), sehingga secara konseptual dapat dipertahankan dan justru memperkuat kesiapan akreditasi internasional.

Konsekuensi praktisnya: karena master menyamakan keduanya, **asesor LAM INFOKOM yang berpedoman pada master APTIKOM dapat mempertanyakan mengapa ada dua entitas**. Dokumen `002` perlu memuat penjelasan eksplisit tentang dasar pemisahan ini (rujukan IABEE/ABET), agar tidak terbaca sebagai penyimpangan dari template.

Perlu dicatat pula bahwa jumlah 4 PL SISTEKIN **PATUH** terhadap anjuran 4–5 PL kedua master, sedangkan jumlah 3 PEO tidak memiliki pembanding di master.

## C-13. Penambahan BK Penciri Khas — **PATUH**

Kedua master memberi izin eksplisit: "Program Studi **dapat menambah BK** sesuai dengan *domain of practice*/value/ciri khas dari Perguruan Tinggi atau Program Studi" ([SI] 736; [TI] 1486–1489).

BK-IS SISTEKIN yang tidak berpadanan langsung dengan 19 BK [SI], yakni tambahan penciri khas:

| BK-IS SISTEKIN | Baris 003 | Justifikasi VMTS |
|---|:---:|---|
| `BK-IS16` *Artificial Intelligence & Intelligent Systems* | 129 | Penciri AI/Smart Systems |
| `BK-IS18` *Machine Learning and Data Science* | 131 | Penciri AI |
| `BK-IS19` *Cloud Architecture & DevOps* | 132 | Penciri Cloud (peminatan P2) |
| `BK-IS14` *IT Audit and Compliance* | 128 | Penciri tata kelola |
| `BK-IS12` *Web and Mobile Application Development* | 125 | Penciri platform (peminatan P3) |
| `BK-IT02` *Applied AI & Intelligent Technologies* | 143 | Penciri AI |
| `BK-IT13` *Technology Entrepreneurship* | 154 | Penciri Technopreneurship |
| `BK-IT14` *IoT and Embedded Smart Systems* | 155 | Penciri Smart Systems |

**Verdікt PATUH.** Penambahan ini persis penggunaan izin yang master berikan, dan selaras langsung dengan konsensus VMTS 2045 (AI/Smart Systems + Technopreneurship). Master tidak menetapkan batas maksimum jumlah BK, sehingga 19 BK-IS + 14 BK-IT tidak melanggar apa pun.

Ini juga menjelaskan mengapa temuan C-2 dan C-3 penting: kekuatan SISTEKIN dalam **menambah** BK penciri khas tidak diimbangi dengan kelengkapan dalam **mengadopsi** BK utama yang master wajibkan. Tiga BK utama (Ethics, Internship, Praktek Profesional Global) hilang justru sementara delapan BK penciri khas ditambahkan.

---

# BAGIAN C — REKAPITULASI DAN TINDAK LANJUT

## C.1 Matriks Kepatuhan Penuh

| Kode | Aspek | Aturan Master | Sifat Aturan | Kondisi SISTEKIN | Verdікt |
|:---:|---|---|:---:|---|:---:|
| C-1a | Jumlah CPL | 10–15 / ≤15 | Anjuran | 14 | **PATUH** |
| C-1b | Skema kategori CPL | 4 kategori SN-Dikti | Normatif [TI] | S/KU/P/KK | **PATUH** |
| C-1c | Jumlah PL | 4–5 | Anjuran | 4 | **PATUH** |
| C-1d | Jumlah peminatan | 1–3 | Anjuran | 3 | **PATUH** |
| C-1e | Beban minimal | ≥144 SKS | Normatif | 146 SKS | **PATUH** |
| C-1f | Batas Sem 1–2 | ≤20 SKS | Normatif | 19 / 20 | **PATUH** |
| C-1g | Batas Sem 3+ | ≤24 SKS | Normatif | maks 21 | **PATUH** |
| C-1h | MKWK 4 wajib | Wajib UU 12/2012 | Normatif | Lengkap, 2 tahun pertama | **PATUH** |
| C-1i | Bobot SKS per MK | Umumnya 2–3 | Anjuran | 2–3 (TA 6) | **PATUH** |
| C-2 | Adopsi 11 BK Utama [SI] | "mengadopsi 11" | **Normatif** | 9 dari 11 | **DEVIASI** |
| C-3 | Adopsi 14 BK Penciri Utama [TI] | "mengadopsi 14" | **Normatif** | 13 dari 14, 3 ganda | **DEVIASI** |
| C-4 | Kodifikasi CPMK | `CPMK011` (kode CPL + urut) | **Normatif, 2 master** | `CPMK-n` lokal | **DEVIASI** |
| C-5 | Kriteria SMART | 5 kriteria | **Normatif, 2 master** | Tidak diterapkan (0 hit) | **DEVIASI** |
| C-6 | Sub-CPMK berkode + Tabel 15 | INSTRUKSI [SI] 1269 | **Normatif** | Naratif, tanpa kode/tabel | **DEVIASI** |
| C-7 | Struktur 12 bagian buku | "mengikuti struktur" | **Normatif** | 3 bagian absen, 2 kosong isi | **DEVIASI** |
| C-8 | 7 kriteria capstone | "wajib menyatakan" | **Normatif** | 4 dari 7 terpenuhi | **DEVIASI** |
| C-9 | Genealogi CPL-P/CPL-K | "dapat mengadopsi" | Izin | Diterapkan | **PATUH** |
| C-10 | Formula ketercapaian CPL | Kebijakan prodi | Diserahkan | SKS-weighted, ambang 65/80% | **DI LUAR MASTER** |
| C-11a | Total bobot per MK = 100 | Normatif | **Normatif** | 100% pada 65/65 MK | **PATUH** |
| C-11b | Jumlah titik asesmen | Kebijakan prodi | Diserahkan | 4 titik baku | **DI LUAR MASTER** |
| C-11c | IKU 7 ≥50% | Tidak disebut | — | Diwajibkan prodi | **DI LUAR MASTER** |
| C-11d | Jenis rubrik | 3 jenis tersedia | Pilihan | Analitik | **PATUH** |
| C-12 | Pemisahan PEO dari PL | Tidak diatur | — | 3 PEO + 4 PL | **DI LUAR MASTER** |
| C-13 | Penambahan BK penciri khas | "dapat menambah" | Izin | 8 BK tambahan | **PATUH** |
| — | Opsi TA non-skripsi | Tidak diatur | — | 4 opsi | **DI LUAR MASTER** |

**Rekapitulasi:** 11 PATUH · 7 DEVIASI · 6 DI LUAR MASTER.

## C.2 Bobot Deviasi Berdasarkan Sifat Aturan yang Dilanggar

Ketujuh deviasi tidak setara. Pengurutan berdasarkan seberapa tegas master menyatakan aturannya:

| Peringkat | Deviasi | Dasar Ketegasan | Kesulitan Perbaikan |
|:---:|---|---|:---:|
| **1** | **C-4** Kodifikasi CPMK | Aturan **identik verbatim di kedua master**, disertai contoh eksplisit `CPMK011` | Tinggi — 226 kode di `007` + Buku Final |
| **2** | **C-2** 2 BK Utama [SI] absen | Kata **"mengadopsi"**, kategori Utama, salah satunya bersumber **IABEE** | Sedang — tambah 2 entri BK + pemetaan ulang |
| **3** | **C-5** Kriteria SMART | Aturan **normatif di kedua master**, 5 kriteria terurai | Sedang — pernyataan kepatuhan + verifikasi 65 MK |
| **4** | **C-7** Struktur 12 bagian | Kata **"mengikuti struktur"**; 2 bagian inti (VMTS, rumusan CPL) kosong isi | Tinggi — rekonstruksi naskah |
| **5** | **C-6** Sub-CPMK | INSTRUKSI [SI] 1269 merujuk Tabel 15 | Sedang — tambah kolom kode |
| **6** | **C-8** Kriteria capstone | Kata **"wajib menyatakan"**; 3 kriteria terukur tidak dinyatakan | Rendah — tambah 3 pernyataan |
| **7** | **C-3** 1 BK Penciri Utama [TI] absen | Kata "mengadopsi"; namun [TI] adalah master sekunder bagi prodi hibrida | Rendah — tambah 1 entri BK |

## C.3 Tindakan Perbaikan Konkret

### Perbaikan berbiaya rendah, berdampak langsung

| No | Tindakan | File | Volume |
|:---:|---|---|:---:|
| 1 | Tambah entri `BK-IS20` *Ethics, Use and Implications for Society* (kategori Utama, ref IS2020) dan `BK-IS21` *Internship and Professional Practice* (kategori Utama, ref IABEE); petakan `FST-206`→BK-IS20 dan `FST-612`→BK-IS21 | `003`, `004`, `009D`, `009E`, `011` | 2 entri + 5 file |
| 2 | Tambah entri `BK-IT15` *Global Professional Practice* (ref IT-2017); petakan `FST-612`, `FST-205` | `003`, `004`, `009D` | 1 entri |
| 3 | Nyatakan 3 kriteria capstone yang absen: ukuran tim 3–6 orang, kategori *complex computing problem*, dan pisahkan pedoman capstone dari pedoman TA | `009` | 3 pernyataan |
| 4 | Perbaiki redaksi `003:24` dari "IT2017 (14/27 Bahan Kajian)" menjadi rumusan yang tidak mengimplikasikan subset langsung | `003` | 1 baris |

### Perbaikan berbiaya sedang

| No | Tindakan | File | Volume |
|:---:|---|---|:---:|
| 5 | Tambahkan kolom kode Sub-CPMK pada Tabel C (format `Sub-CPMK-{n}.{m}` merujuk CPMK-n), atau tambahkan tabel pemetaan CPMK→Sub-CPMK tersendiri per MK | `007`, Buku Final | 65 MK |
| 6 | Tambahkan pernyataan kepatuhan SMART pada panduan perumusan CPMK, dan verifikasi 65 MK terhadap 5 kriteria (khususnya *Measurable* dan *Time-bound*) | `007` §1, `018` | 1 bagian + audit 65 MK |

### Perbaikan berbiaya tinggi — perlu keputusan Tim Pengembang

| No | Tindakan | Keputusan yang Diperlukan |
|:---:|---|---|
| 7 | **Kodifikasi CPMK.** Konversi `CPMK-n` → format master `CPMK{kodeCPL}{urut}`. Contoh: CPMK ke-1 `STI-401` yang diturunkan dari `KK1` menjadi `CPMK-KK1-1` atau setara. | Format mana yang dipakai, mengingat kode CPL SISTEKIN alfanumerik (`S1`, `KU1`, `KK1`) sedangkan master mengasumsikan numerik 2 digit (`CPL01`). Master tidak menyediakan pola untuk kode alfanumerik. |
| 8 | **Rekonstruksi buku ke 12 bagian.** Tambah Bab I, III, V; isikan rumusan VMTS ke Bab II dan rumusan 14 CPL + genealogi ke Bab IV; tambah bagian Matriks & Peta Kurikulum, SKL, Asesmen Pembelajaran, Hak Belajar, Manajemen Pelaksanaan. | Apakah mengikuti penomoran master (A–L / I–XII) atau mempertahankan penomoran sendiri dengan tabel korespondensi ke 12 bagian master. |

**Rekomendasi urutan:** kerjakan No. 1–4 lebih dulu (berbiaya rendah, menutup 2 dari 7 deviasi sepenuhnya dan 1 sebagian), lalu No. 8 (karena rekonstruksi buku akan menyerap hasil perbaikan lain), baru No. 5–7.

Untuk No. 8, tabel korespondensi ke 12 bagian master lebih dianjurkan daripada mengganti penomoran: penomoran Bab I–VIII SISTEKIN sudah dirujuk oleh dokumen `012`–`018`, sehingga penggantian akan menimbulkan kerja ikutan.

---

# BAGIAN D — BATAS AUDIT

## D.1 Yang Diverifikasi

| Aspek | Metode |
|---|---|
| Daftar BK kedua master | Ekstraksi verbatim [SI] baris 740–775 dan [TI] baris 1496–2004 |
| Aturan normatif vs contoh | Klasifikasi berdasarkan kata kunci master sendiri ("INSTRUKSI"/"wajib"/"harus" vs "disarankan"/"contoh"/"dapat") |
| Kodifikasi CPMK SISTEKIN | Hitung penuh 226 kode pada `007` |
| Ketiadaan BK Ethics/Internship/Professional Practice | Pencarian pada 26 file, dengan pemeriksaan manual setiap hit untuk menyingkirkan false positive |
| Ketiadaan SMART & Gagne | Pencarian case-sensitive + case-insensitive, seluruh hit diperiksa konteksnya |
| Sub-CPMK | Hitung per blok MK (65 blok), pemeriksaan struktur Tabel C |
| 12 bagian buku | Uji ganda: pencarian judul dan pencarian substansi |
| Kriteria capstone | Pembacaan penuh `009` (78 baris) |
| Aritmetika SKS | Rekalkulasi 55 baris MK `005` |

## D.2 Yang TIDAK Diverifikasi

| Aspek | Alasan |
|---|---|
| Ketepatan substansi 19 BK-IS dan 14 BK-IT terhadap dokumen asli **IS2020** dan **IT2017/CC2020** | Dokumen asli ACM/IEEE tidak tersedia di workspace; audit hanya membandingkan terhadap master APTIKOM yang mengutipnya |
| Apakah rumusan setiap CPMK memenuhi kriteria SMART secara substantif | Memerlukan penilaian per-CPMK atas 226 CPMK; audit hanya memverifikasi bahwa kriteria SMART tidak disebut sebagai standar yang dipakai |
| Kesesuaian level Bloom yang dipilih per CPMK | Di luar cakupan; audit hanya mencatat bahwa Bloom bukan basis yang master tetapkan |
| Ketepatan pemetaan CPL↔BK dan BK↔MK secara substantif | Audit memeriksa kelengkapan entri BK, bukan ketepatan setiap sel pemetaan |
| Isi file `.xlsx`, `.docx`, `.html` hasil ekspor | Audit terbatas pada file `.md` sesuai permintaan |
| Bagian kodifikasi [TI] baris 430–451 | Kolom "Pengkodean" untuk PL/CPL/BK/MK/CPMK **kosong** di hasil ekstraksi PDF (kemungkinan berupa gambar); aturan kodifikasi PL/CPL/BK/MK karena itu tidak dapat diverifikasi dari [TI] |
| Radar chart CC-2020 [TI] Gambar 4 | Ligatur rusak pada ekstraksi (`ti`→`3`, `ft`→`Y`); 34 label terbaca tetapi tidak dipakai sebagai dasar verdікt |
| Dokumen `013`, `014`, `015`, `018` | Tidak diaudit terhadap master secara mendalam |

## D.3 Catatan Kualitas Sumber

Dua hal pada master sendiri yang perlu diketahui pembaca laporan ini:

1. **[SI] baris 761** — deskripsi BK12 *Research Methodology* berbunyi "…melakukan penelitian di bidang **bimbingan dan konseling**…", tampak salah-tempel dari dokumen domain lain. Dilaporkan verbatim tanpa penilaian; tidak memengaruhi verdікt apa pun dalam audit ini.
2. **[SI] batang tubuh bagian C** menampilkan sub-bab bernomor 1, 3, 5 (baris 506, 514, 526) — nomor 2 dan 4 tidak muncul sebagai heading. Jadi master sendiri memiliki celah penomoran, yang relevan sebagai konteks saat menilai deviasi C-7.
3. Formula ketercapaian CPL pada [SI] versi `.md` tersimpan sebagai gambar (baris 2350, 2362 kosong); formula diambil dari versi `.txt` baris 9322–9323 dan 9333–9334, dengan narasi pengantar yang identik di kedua versi.

## D.4 Hubungan dengan Audit Sebelumnya

Audit ini **berbeda fokus** dari `KURIKULUM2026_REVISI/019_AUDIT_KRITIS_KESELARASAN_FOLDER_REVISI_23082026_212923.md`:

| Audit | Fokus | Pertanyaan yang dijawab |
|---|---|---|
| Dokumen 019 | Konsistensi **internal** antar 26 file | Apakah dokumen SISTEKIN saling selaras? |
| Dokumen 0001 (ini) | Kepatuhan **eksternal** terhadap master APTIKOM | Apakah dokumen SISTEKIN patuh pada standar induknya? |

Keduanya tidak tumpang tindih kecuali pada tiga titik, di mana laporan ini menambahkan dimensi baru:

| Titik | Temuan 019 (internal) | Tambahan 0001 (terhadap master) |
|---|---|---|
| Jumlah CPMK | 31 MK tidak punya 4 CPMK → skema 1-to-1 gugur | Master **tidak mengatur** jumlah CPMK; yang dilanggar justru **kodifikasinya** (C-4) — temuan yang lebih mengikat |
| Struktur bab buku | Bab I, III, V hilang dari 8 bab rencana sendiri | Master menuntut **12 bagian**, sehingga kekurangannya lebih besar dari yang tampak: 3 bagian absen + 2 kosong isi (C-7) |
| Rumusan CPL & VMTS tidak ada di buku | Dicatat sebagai ketidaklengkapan internal | Merupakan **inti Bagian D dan E master** — dua dari 12 bagian wajib (C-7) |

Deviasi C-2, C-3, C-5, C-6, dan C-8 adalah temuan baru yang tidak dapat muncul dari audit konsistensi internal, karena dokumen SISTEKIN konsisten satu sama lain dalam hal-hal tersebut — konsisten, tetapi konsisten menyimpang dari master.

---

**Status:** Laporan diagnostik. Tidak ada file yang diubah.
**Rujukan silang:** `KURIKULUM2026_REVISI/019_AUDIT_KRITIS_KESELARASAN_FOLDER_REVISI_23082026_212923.md` (audit konsistensi internal).
