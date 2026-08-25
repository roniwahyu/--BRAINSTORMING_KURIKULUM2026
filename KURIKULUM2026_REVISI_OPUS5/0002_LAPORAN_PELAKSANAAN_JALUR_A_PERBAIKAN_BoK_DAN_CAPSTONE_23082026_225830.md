# 0002 — LAPORAN PELAKSANAAN JALUR A: PERBAIKAN BERBIAYA RENDAH KEPATUHAN MASTER APTIKOM

**Dasar pelaksanaan:** Dokumen `0001_AUDIT_KEPATUHAN_MASTER_APTIKOM_SI_TI_23082026_221038.md` §C.3, tindakan No. 1–4
**Keputusan pengarah:** disetujui pengguna pada sesi 23 Agustus 2026
**Tanggal pelaksanaan:** 23 Agustus 2026, 22:58:30 WIB
**Sifat:** laporan eksekusi. **9 file `.md` diubah**, seluruh turunan HTML/XLSX/DOCX diregenerasi.

---

> [!NOTE]
> ## VERIFIKASI ULANG — 23 Agustus 2026, 23:05 WIB
>
> Seluruh klaim dalam laporan ini diuji ulang terhadap kondisi file terkini. **Semua terverifikasi akurat**, tanpa koreksi:
>
> | Klaim | Uji Ulang | Hasil |
> |---|---|:---:|
> | 3 BK baru hadir di 5 file matriks | `BK-IS20`/`BK-IS21`/`BK-IT15` per file | 21 BK-IS & 15 BK-IT unik di semua file ✅ |
> | 0 klaim jumlah BoK kedaluwarsa | Pencarian `19 BoK`/`14 BoK`/`14/27` | 0 hit, kecuali `009_LANGKAH2:108` yang sengaja menyebut "19 Bahan Kajian **master**" ✅ |
> | Aritmetika 55 MK / 146 SKS tidak berubah | Rekalkulasi baris MK `005` | 55 MK / 146 SKS ✅ |
> | 3 kriteria capstone kini dinyatakan | Frasa "3 (tiga) sampai 6 (enam)", "*complex computing problem*", "panduan tersendiri" | Masing-masing hadir ✅ |
> | `FST-610` = 3 SKS (batas bawah rentang 3–6 SKS master) | `005:174` | Terkonfirmasi ✅ |
> | 9 file `.md` diubah, +108/−31 baris | `git diff --stat` | Terkonfirmasi ✅ |
> | `_tools/verify_zero_discrepancy.py` diperbaiki | `git diff --stat` | +10/−2 baris ✅ |
> | Skrip verifikasi lolos | Eksekusi skrip | `[SUCCESS] 100% PERFECT ALIGNMENT` ✅ |
>
> Seluruh **pekerjaan terbuka pada §7 juga diuji ulang dan tetap berlaku** — tidak ada yang secara tidak sengaja sudah tertangani:
>
> | Temuan Terbuka | Uji Ulang | Status |
> |---|---|:---:|
> | C-4 kodifikasi CPMK | 226 kode tetap `CPMK-n`; 0 kode format `CPMK011` | ⏳ Berlaku |
> | C-5 kriteria SMART | 0 hit `specific.*measurable` | ⏳ Berlaku |
> | C-6 Sub-CPMK berkode | 0 kode `Sub-CPMK-n` | ⏳ Berlaku |
> | C-7 struktur 12 bagian | 5 heading `# BAB`; Visi 2045 & rumusan CPL tetap 0 hit; 5 bagian wajib tetap 0 hit | ⏳ Berlaku |
> | P0-1 tabrakan `FST-204`/`FST-205` | `007` masih memuat "FST-204 — Organisasi dan Arsitektur Komputer" | ⏳ Berlaku |
> | P0-3 angka Buku Final | "14 MK \| 38 SKS" 2 hit; "SEMESTER 6 (20 SKS)" 1 hit | ⏳ Berlaku |
> | P2 separator rusak `011` | 4 baris `\|---\|\|` | ⏳ Berlaku |
> | P2 silabus 65 vs 67 MK | 65 blok `### N.` | ⏳ Berlaku |
>
> Dokumen `0001` telah diberi penanda status pada temuan C-2, C-3, dan C-8 agar tidak terbaca sebagai deviasi yang masih berlaku.

---

## RINGKASAN HASIL

Jalur A menutup **3 deviasi secara penuh** dari 7 deviasi yang teridentifikasi, sehingga rekapitulasi kepatuhan berubah dari **11 PATUH · 7 DEVIASI** menjadi **14 PATUH · 4 DEVIASI** (6 aspek DI LUAR MASTER tidak berubah):

| Kode | Deviasi | Status Sebelum | Status Sesudah |
|:---:|---|:---:|:---:|
| **C-2** | 2 dari 11 BK kompetensi utama IS2020 tanpa padanan | **DEVIASI** | ✅ **PATUH** |
| **C-3** | 1 dari 14 BK penciri utama IT2017 tanpa padanan | **DEVIASI** | ✅ **PATUH** |
| **C-8** | Kriteria capstone tidak lengkap dipenuhi (4 dari 7) | **DEVIASI** | ✅ **PATUH** (7 dari 7) |
| — | Redaksi klaim "14/27 Bahan Kajian" menyesatkan | Tidak akurat | ✅ Diperbaiki |

Deviasi yang **belum** ditangani (memerlukan Jalur B dan C): C-4 kodifikasi CPMK, C-5 kriteria SMART, C-6 Sub-CPMK berkode, C-7 struktur 12 bagian buku.

---

## BAGIAN 1 — PENAMBAHAN TIGA BAHAN KAJIAN KOMPETENSI UTAMA

### 1.1 Bahan Kajian yang Ditetapkan

| Kode Baru | Nomenklatur | Sumber Master | Kategori Master | MK Pembina Primer (●) | MK Pembina Sekunder (○) |
|:---:|---|---|:---:|---|---|
| **`BK-IS20`** | *Ethics, Use and Implications for Society* | [SI] `BK09`, baris 740–760 | **Utama** (IS2020) | `FST-206` | `STI-405`, `STI-602`, `STB-04` |
| **`BK-IS21`** | *Internship and Professional Practice* | [SI] `BK10`, baris 740–760 | **Utama** (**IABEE**) | `FST-612` | `MKU-507`, `FST-610` |
| **`BK-IT15`** | *Global Professional Practice* | [TI] `BK08`, baris 1658–1679 | **Penciri Utama** (IT-2017) | `FST-205`, `FST-612` | `FST-206`, `MKU-507` |

### 1.2 Pemetaan CPL untuk Tiga BK Baru

| Kode BK | S1 | KU1 | KU2 | KU3 | P3 | KK4 | Rasional Pemetaan |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| `BK-IS20` | ✅ | | | ✅ | ✅ | ✅ | Etika digital menopang CPL Sikap; tanggung jawab kelompok & pembelajaran mandiri (KU3); pengetahuan regulasi siber (P3); audit kepatuhan (KK4) |
| `BK-IS21` | ✅ | ✅ | ✅ | ✅ | | | Pengalaman kerja profesional membina seluruh ranah Sikap dan Keterampilan Umum |
| `BK-IT15` | ✅ | ✅ | ✅ | ✅ | | | Praktik profesional lintas budaya membina Sikap dan Keterampilan Umum |

**Temuan struktural yang tertutup oleh perbaikan ini.** Sebelum penambahan, tidak ada satu pun Bahan Kajian yang memetakan ke **CPL Sikap (`S1`)** maupun ke **Keterampilan Umum (`KU1`–`KU3`)**. Seluruh 19 BK-IS dan 14 BK-IT hanya memetakan ke ranah Pengetahuan (`P1`–`P4`) dan Keterampilan Khusus (`KK1`–`KK6`). Ini kekosongan yang tidak terdeteksi audit sebelumnya karena tidak ada CPL orphan — `S1` dan `KU1`–`KU3` memang punya mata kuliah pembina, tetapi tidak punya Bahan Kajian pengampu.

Setelah perbaikan, `BK-IS20`, `BK-IS21`, dan `BK-IT15` menjadi tiga Bahan Kajian pertama yang membina ranah Sikap dan Keterampilan Umum secara eksplisit. Ini memperkuat keterlacakan CPL↔BK yang [SI] baris 781 nyatakan wajib: *"Program Studi **wajib melanjutkan pemetaan seluruh CPL** yang telah ditetapkan dengan BK yang dipilih."*

### 1.3 Perubahan Jumlah Bahan Kajian

| Kelompok | Sebelum | Sesudah | Selisih |
|---|:---:|:---:|:---:|
| BoK IS2020 (`BK-IS01`–`BK-IS21`) | 19 | **21** | +2 |
| BoK IT2017 (`BK-IT01`–`BK-IT15`) | 14 | **15** | +1 |
| **Total** | **33** | **36** | **+3** |

Kedua master **tidak menetapkan batas maksimum** jumlah BK dan memberi izin eksplisit menambah ("dapat menambah BK sesuai *domain of practice*/value/ciri khas"), sehingga penambahan ini tidak melanggar ketentuan apa pun.

### 1.4 File yang Disinkronkan

| File | Perubahan | Baris Diubah |
|---|---|:---:|
| `003_STANDAR_14_CPL_DAN_PEMETAAN_BoK_APTIKOM.md` | Tambah 3 baris matriks CPL↔BK; ubah judul §4 dan §5; perbaiki label diagram Mermaid; tambah 2 blok catatan kepatuhan; koreksi klaim traceability | +25 / −5 |
| `004_MATRIKS_KETERLACAKAN_OBE_VMTS_PEO_PL_CPL_MK.md` | Tambah 3 baris Tabel 6.1 dan 6.2 (pemetaan BK↔MK); ubah judul tabel; tambah 2 blok catatan | +15 / −3 |
| `009D_CPL_KETERAMPILAN_KHUSUS_SISTEKIN.md` | Tambah 3 baris pemetaan BK↔KK; ubah judul §3.1 dan §3.2; tambah 2 catatan penjelas ranah | +13 / −2 |
| `009E_RINGKASAN_CPL_LENGKAP_PEMETAAN_BoK.md` | Tambah 3 baris matriks; ubah judul §2 dan §3; perbarui Ground Truth; tambah catatan | +12 / −3 |
| `009_LANGKAH2_CPL_FORMAL.md` | Perbarui 5 klaim jumlah BoK; perkaya deskripsi standar rujukan IS2020 dan IT2017 dengan komposisi BK master | +14 / −7 |
| `011_IMPLEMENTASI_OBE_SISTEKIN2026_TABLES.md` | Perbarui 2 sel klaim jumlah BK (Sheet 1 baris 27, Sheet 14 baris 419) | +2 / −2 |
| `017_AUDIT_FORENSIK_ZERO_REDUNDANCY_DAN_ZERO_GAP.md` | Perbarui rantai keterlacakan | +1 / −1 |
| `BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md` | Tambah 3 baris Tabel 6.1 dan 6.2; ubah 2 judul tabel; perbarui klaim §Pengantar; tambah blok catatan kepatuhan | +14 / −3 |

---

## BAGIAN 2 — PELENGKAPAN KRITERIA CAPSTONE PROJECT

### 2.1 Yang Ditambahkan

Dokumen `009` sebelumnya berjumlah 78 baris, dengan porsi capstone hanya 6 baris (timeline 16 minggu) sementara 62 baris membahas 4 opsi TA non-skripsi. Kini ditambahkan **bagian §1 normatif** berisi:

| Sub-bagian | Isi |
|---|---|
| **§1** Pembuka | Pernyataan formal bahwa `FST-610` Capstone Project FSTI (3 SKS, Sem 7) adalah mata kuliah capstone project — memenuhi ketentuan [SI] baris 828 *"wajib menyatakan mata kuliah yang dapat memenuhi kriteria capstone project"* |
| **§1.1** | Tabel pemenuhan **7 kriteria wajib** APTIKOM SI v2.0, masing-masing dengan ketentuan pelaksanaan konkret |
| **§1.2** | Tabel **7 atribut *complex computing problem*** sebagai kriteria kelayakan proposal, dengan 2 atribut wajib mutlak |
| **§1.3** | Keterlacakan capstone terhadap 10 CPL dan 6 Bahan Kajian pengampu |

### 2.2 Tiga Kriteria yang Sebelumnya Absen — Kini Dinyatakan

| Kriteria [SI] | Ketentuan yang Ditetapkan |
|---|---|
| **Kriteria 2:** Dikerjakan berkelompok **3–6 orang** | "Tim wajib berjumlah 3 (tiga) sampai 6 (enam) orang mahasiswa. Komposisi tim disarankan lintas peminatan agar mencakup kompetensi AI/Data (P1), Cloud/Cyber (P2), dan Platform/UX (P3). Pembentukan tim dilakukan pada Minggu 1–3 dan disahkan oleh Koordinator Capstone." |
| **Kriteria 4:** Kategori *complex computing problem* | "Proyek wajib memenuhi minimal 4 dari 7 atribut kompleksitas pada §1.2. Dua atribut bersifat wajib mutlak: keterlibatan lebih dari satu pemangku kepentingan, dan kebutuhan/permasalahan yang belum terdefinisi dengan baik. Verifikasi dilakukan saat sidang proposal Minggu 3." |
| **Kriteria 7:** Panduan tersendiri | Bagian §1 dokumen ini kini berfungsi sebagai panduan normatif, merujuk Klaster Rubrik Proyek Rekayasa (Dok. `018`) untuk penilaian dan Dok. `008` untuk formula ketercapaian CPL |

### 2.3 Tujuh Atribut Kompleksitas yang Ditetapkan

Diturunkan dari rumusan [SI] baris 1055–1059 (*"keterlibatan lebih dari satu pemangku kepentingan dan kebutuhan/permasalahan yang belum terdefinisi dengan baik"*) dan diperluas dengan atribut yang lazim dalam kriteria Seoul Accord/IABEE:

| No | Atribut | Sifat |
|:---:|---|:---:|
| 1 | Keterlibatan lebih dari satu pemangku kepentingan | **Wajib** |
| 2 | Kebutuhan belum terdefinisi dengan baik (*ill-defined requirements*) | **Wajib** |
| 3 | Tidak memiliki solusi baku yang dapat diterapkan langsung | Pilihan |
| 4 | Melibatkan integrasi lintas sistem, platform, atau sumber data | Pilihan |
| 5 | Memerlukan penerapan pengetahuan pada tingkat abstraksi tinggi | Pilihan |
| 6 | Memiliki batasan non-teknis signifikan (regulasi, keamanan, anggaran) | Pilihan |
| 7 | Menuntut pertimbangan dampak sosial, etis, atau keberlanjutan | Pilihan |

Ambang "minimal 4 dari 7, dengan atribut 1 dan 2 wajib" adalah keputusan prodi — master tidak menetapkan mekanisme verifikasi, hanya menyatakan bahwa masalah harus termasuk kategori kompleks.

### 2.4 Konsistensi dengan Kriteria yang Sudah Terpenuhi

Empat kriteria yang sebelumnya sudah terpenuhi tetap dipertahankan dan kini didokumentasikan eksplisit:

| Kriteria | Bukti |
|---|---|
| 1. Menerapkan pengetahuan sebelumnya | Prasyarat `STI-506` + $\ge 100$ SKS (`005:174`) |
| 3. Masalah riil di masyarakat | Kewajiban surat kesediaan mitra |
| 5. Luaran desain atau produk | TRL $\ge 5$ untuk produk; SRS/SDD/ADR untuk desain |
| 6. Bobot 3–6 SKS | `FST-610` = 3 SKS, setara 135 jam (Permendikbudristek 53/2023 Pasal 15) |

---

## BAGIAN 3 — PERBAIKAN REDAKSI KLAIM SUMBER

### 3.1 Klaim "14/27 Bahan Kajian"

| Lokasi | Sebelum | Sesudah |
|---|---|---|
| `003:23` | `IS2020["APTIKOM IS2020 (19 Bahan Kajian)"]` | `IS2020["APTIKOM IS2020 (21 Bahan Kajian)"]` |
| `003:24` | `IT2017["APTIKOM IT2017 (14/27 Bahan Kajian)"]` | `IT2017["APTIKOM IT2017 (15 BK, dirumuskan dari 27 BK)"]` |

**Alasan perbaikan.** Angka 27 benar sebagai total BK master TI (terverifikasi [TI] baris 1496–2004: BK01–BK27). Namun notasi "14/27" mengimplikasikan bahwa 14 BK SISTEKIN adalah **subset langsung** dari 27 BK master — padahal nama dan cakupan BK-IT SISTEKIN tidak identik dengan BK01–BK14 [TI]. Tiga BK-IT bahkan dipakai ganda untuk memetakan lebih dari satu BK master (`BK-IT06` menampung `BK07` dan `BK14` [TI]; `BK-IT11` menampung `BK06` dan `BK10` [TI]).

Redaksi baru menyatakan hubungan yang sebenarnya: BK SISTEKIN **dirumuskan ulang dari** 27 BK master, bukan dipilih sebagai subset.

### 3.2 Pemerkayaan Deskripsi Standar Rujukan

`009_LANGKAH2_CPL_FORMAL.md` §6 (tabel standar rujukan) kini memuat komposisi BK master secara akurat:

| Standar | Deskripsi Baru |
|---|---|
| IS2020 | "…17 CPL-P, 17 CPL-K, dan **19 Bahan Kajian master (11 kompetensi utama wajib diadopsi + 1 umum + 7 pendukung)**" |
| IT2017 / CC2020 | "…**27 Bahan Kajian master (14 penciri utama wajib diadopsi + 13 penciri pendukung)**, Infrastruktur, Cloud, Cybersecurity, IoT, dan Praktek Profesional Global" |

Ini membedakan dengan tegas antara **jumlah BK di master** (19 dan 27) dan **jumlah BK yang SISTEKIN tetapkan** (21 dan 15) — pembedaan yang sebelumnya kabur karena kedua angka sama-sama disebut "19 BoK IS2020 & 14 BoK IT2017".

---

## BAGIAN 4 — PERBAIKAN ALAT VERIFIKASI

### 4.1 Masalah yang Ditemukan Saat Verifikasi

Setelah pengeditan, `_tools/verify_zero_discrepancy.py` melaporkan **2 diskrepansi baru** — keduanya *false positive* pada dokumen audit `019` yang membahas skrip itu sendiri:

```
[DISCREPANCY] 019_AUDIT_KRITIS...md:16 -> Found STI-103 with old name: ... apakah `STI-103`
              masih bernama "Logika Informatika" dan (b) apakah `STI-201` menyebut kata "Logika"...
[DISCREPANCY] 019_AUDIT_KRITIS...md:1053 -> | `016_ANALISIS_BoK...md` | 66, 151 | Rasionalisasi
              peleburan "STI-103 Logika Informatika" ke `STI-201` | ✅ Sah |
```

Skrip menandai dokumen audit yang **mengutip** nomenklatur lama untuk keperluan dokumentasi. Ini kelas kesalahan yang sama dengan 7 *false positive* `deep_cross_audit.py` yang dilaporkan pada Dokumen `0001` §5.2.

### 4.2 Perbaikan yang Diterapkan

Daftar pengecualian yang sebelumnya *hardcoded* satu file diubah menjadi konstanta berdokumentasi:

| Sebelum | Sesudah |
|---|---|
| `if fname not in ["016_ANALISIS_BoK_APTIKOM_REDUNDANSI_DAN_PIPELINE_AI.md"]:` (diulang 2×) | `EXEMPT = {"016_...", "017_AUDIT_FORENSIK...", "019_AUDIT_KRITIS..."}` lalu `if fname not in EXEMPT:` |

Disertai komentar yang menjelaskan dasar pengecualian: *"Dokumen audit/analisis yang secara sah mengutip nomenklatur lama dalam konteks log koreksi, tabel ekuivalensi, atau pembahasan meta tentang skrip ini sendiri."*

**Catatan penting.** Perbaikan ini **hanya** menghilangkan *false positive*; skrip tetap memiliki keterbatasan cakupan yang dilaporkan pada Dokumen `0001` §5.1 — masih hanya memeriksa dua pola string, belum memverifikasi SKS, jumlah MK, prasyarat, atau struktur bab. Penulisan ulang skrip sesuai 14 pemeriksaan yang direkomendasikan (`0001` §5.3) **belum dikerjakan** dan tetap menjadi pekerjaan terbuka.

---

## BAGIAN 5 — HASIL VERIFIKASI

Seluruh pemeriksaan dijalankan setelah pengeditan selesai.

### 5.1 Kelengkapan dan Keseragaman Tabel Bahan Kajian

| File | BK-IS unik | BK-IT unik | Kolom seragam | Verdікt |
|---|:---:|:---:|:---:|:---:|
| `003_STANDAR_14_CPL...md` | **21** | **15** | 16/16 kolom, 0 anomali | ✅ |
| `004_MATRIKS_KETERLACAKAN...md` | **21** | **15** | 6/6 kolom, 0 anomali | ✅ |
| `009D_CPL_KETERAMPILAN_KHUSUS...md` | **21** | **15** | 4/4 kolom, 0 anomali | ✅ |
| `009E_RINGKASAN_CPL...md` | **21** | **15** | 16/16 kolom, 0 anomali | ✅ |
| `BUKU_KURIKULUM...FINAL.md` | **21** | **15** | 6/6 kolom, 0 anomali | ✅ |

Pemeriksaan keseragaman kolom penting karena kelima file diekspor ke Excel dan Word — tabel dengan jumlah kolom tidak konsisten akan menggeser sel, sebagaimana temuan `004:76` pada Dokumen `019` (P2-6a, belum diperbaiki).

### 5.2 Ketiadaan Klaim Jumlah BoK yang Kedaluwarsa

Pencarian pola `19 BoK`, `14 BoK`, `19 BK IS`, `14 BK IT`, `19 Bahan Kajian`, `14 Bahan Kajian`, `14/27` pada seluruh file `.md` di `KURIKULUM2026_REVISI/`:

| Hasil | Keterangan |
|---|---|
| **0 klaim kedaluwarsa** | Kecuali pada dokumen audit `019` dan `0001` (yang memang merekam kondisi sebelum perbaikan), serta `009_LANGKAH2:108` yang kini secara sengaja menyebut "19 Bahan Kajian **master**" untuk membedakan jumlah BK master dari jumlah BK SISTEKIN |

### 5.3 Keberadaan Mata Kuliah Pembina

Seluruh 8 mata kuliah yang dirujuk sebagai pembina tiga BK baru terverifikasi ada dalam struktur `005`:

| MK | Ada di 005 | MK | Ada di 005 |
|:---:|:---:|:---:|:---:|
| `FST-206` | ✅ | `FST-205` | ✅ |
| `FST-612` | ✅ | `STI-405` | ✅ |
| `MKU-507` | ✅ | `STI-602` | ✅ |
| `FST-610` | ✅ | `STB-04` | ✅ |

### 5.4 Aritmetika Struktur Kurikulum Tidak Terpengaruh

| Metrik | Nilai | Status |
|---|:---:|:---:|
| Jumlah MK dalam struktur 8 semester | **55** | ✅ Tidak berubah |
| Total SKS | **146** | ✅ Tidak berubah |

Penambahan Bahan Kajian bersifat **taksonomi keilmuan**, tidak menambah mata kuliah maupun SKS. Ini konsisten dengan sifat BK menurut [SI] baris 818: relasi BK↔MK bersifat *many-to-many*, sehingga satu MK dapat mengampu beberapa BK tanpa perubahan bobot.

### 5.5 Kriteria Capstone

| Frasa Kunci | Kemunculan di `009` |
|---|:---:|
| "3 (tiga) sampai 6 (enam) orang" | 1 |
| "3–6 orang" | 2 |
| "*complex computing problem*" | 1 |
| "panduan tersendiri" | 1 |
| "Jumlah SKS antara 3–6" | 1 |

### 5.6 Alat Verifikasi

```
$ python _tools/verify_zero_discrepancy.py
Auditing 27 markdown files in KURIKULUM2026_REVISI...
[SUCCESS] 100% PERFECT ALIGNMENT
```

### 5.7 Regenerasi Turunan

| Format | Hasil | Verifikasi |
|---|---|---|
| **HTML** | 25 file + `index.html` portal | `BK-IS20`, `BK-IS21`, `BK-IT15` terverifikasi hadir di 4 HTML utama |
| **XLSX** | Per-dokumen + `MASTER_KURIKULUM_OBE_SISTEKIN_2026.xlsx` (66 KB) | Regenerasi 22:57 |
| **DOCX** | 27/27 file berhasil | `BUKU_KURIKULUM...FINAL.docx` = 330.888 byte |

---

## BAGIAN 6 — RINGKASAN PERUBAHAN FILE

```
 003_STANDAR_14_CPL_DAN_PEMETAAN_BoK_APTIKOM.md          | 25 ++++++++++----
 004_MATRIKS_KETERLACAKAN_OBE_VMTS_PEO_PL_CPL_MK.md      | 15 ++++++--
 009D_CPL_KETERAMPILAN_KHUSUS_SISTEKIN.md                | 13 +++++--
 009E_RINGKASAN_CPL_LENGKAP_PEMETAAN_BoK.md              | 12 +++++--
 009_LANGKAH2_CPL_FORMAL.md                              | 14 ++++----
 009_PEDOMAN_CAPSTONE_PROJECT_DAN_TUGAS_AKHIR_...md      | 40 ++++++++++++++++++++--
 011_IMPLEMENTASI_OBE_SISTEKIN2026_TABLES.md             |  4 +--
 017_AUDIT_FORENSIK_ZERO_REDUNDANCY_DAN_ZERO_GAP.md      |  2 +-
 BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md               | 14 +++++---
 9 files changed, 108 insertions(+), 31 deletions(-)
```

Ditambah `_tools/verify_zero_discrepancy.py` (perbaikan daftar pengecualian).

---

## BAGIAN 7 — PEKERJAAN TERBUKA

### 7.1 Deviasi Master yang Belum Ditangani

| Kode | Deviasi | Jalur | Kebutuhan |
|:---:|---|:---:|---|
| **C-4** | Kodifikasi CPMK tanpa jejak CPL (226 kode) | **C** | Sudah ada keputusan format: `CPMK-KK1-1` (kode CPL alfanumerik dipertahankan). Volume: 65 MK di `007` + Lampiran 2 Buku Final |
| **C-5** | Kriteria SMART tidak diterapkan | **B** | Tambah pernyataan kepatuhan + verifikasi 226 CPMK terhadap 5 kriteria |
| **C-6** | Sub-CPMK tanpa kodifikasi & tabel pemetaan | **B** | Tambah kolom kode Sub-CPMK pada Tabel C, 65 MK |
| **C-7** | Struktur 12 bagian buku tidak diikuti | **C** | Rekonstruksi: 3 bagian absen + 2 bagian kosong isi (VMTS, rumusan 14 CPL) |

### 7.2 Temuan Konsistensi Internal (Dokumen 019) yang Belum Ditangani

| Prioritas | Temuan | Keputusan |
|:---:|---|---|
| **P0-1** | Tabrakan kode `FST-204`/`FST-205` | **Sudah diputuskan:** pakai versi `005` (Pengantar KA & Data + Basic English for IT). Belum dieksekusi. |
| **P0-2** | Bab I, III, V hilang dari Buku Final | Menyatu dengan C-7 |
| **P0-3** | Angka komposisi rumpun & sebaran SKS salah di Buku Final | Koreksi aritmetika, angka benar tersedia di `005` |
| **P1-1** | 31 MK tidak punya 4 CPMK | **Sudah diputuskan:** tambah CPMK-4 pada 28 MK, longgarkan 3 MKWU |
| **P1-2** | Rantai prasyarat `007` menyimpang pada 19 MK | Termasuk 1 pelanggaran urutan semester (`STI-401` ← `FST-408`) |
| **P1-3** | Rekap SKS `004` §5 tidak dapat direproduksi (12 dari 14 baris) | Perlu rekalkulasi |
| **P1-4** | Rumusan CPL berbeda antar file (`KK3` kehilangan IoT, `P4` bergeser domain) | Perlu keputusan versi yang berlaku |
| **P1-5** | Matriks CPL↔PL tiga versi; pola I→R→M `KK4` tidak terpenuhi | Perlu keputusan |
| **P2** | 4 separator tabel rusak di `011`; 34 sel rekap salah; silabus 65 vs 67 MK; proporsi praktikum tiga versi | Kebersihan teknis |

### 7.3 Catatan Metodologis

Perbaikan Jalur A **menambah** entri Bahan Kajian dan **melengkapi** pernyataan kriteria. Tidak ada mata kuliah, SKS, CPL, PEO, PL, atau struktur semester yang diubah. Karena itu perbaikan ini tidak menimbulkan kerja ikutan pada dokumen `005`, `006`, `007`, `008`, `010`, `012`–`016`, dan `018`.

Satu hal yang perlu dipertimbangkan Tim Pengembang: penambahan `BK-IS21` dan `BK-IT15` menciptakan sedikit tumpang tindih substansi (keduanya menaungi praktik profesional, dengan `BK-IS21` menekankan pengalaman kerja/*internship* dan `BK-IT15` menekankan dimensi global/lintas budaya). Tumpang tindih ini **mengikuti struktur master** — [SI] dan [TI] memang memiliki BK yang beririsan karena keduanya standar untuk program studi berbeda, dan SISTEKIN sebagai prodi hibrida mengadopsi keduanya. Bila Tim Pengembang menghendaki *zero redundancy* penuh, opsinya adalah melebur keduanya menjadi satu BK dengan catatan bahwa satu entri memenuhi dua ketentuan master sekaligus. Pilihan saat ini (dua entri terpisah) lebih mudah dipertahankan di hadapan asesor karena setiap ketentuan master memiliki entri yang dapat ditunjuk langsung.

---

**Status:** Jalur A selesai dan terverifikasi. Siap diperiksa.
**Rujukan:** `0001_AUDIT_KEPATUHAN_MASTER_APTIKOM_SI_TI_23082026_221038.md` (audit kepatuhan master), `KURIKULUM2026_REVISI/019_AUDIT_KRITIS_KESELARASAN_FOLDER_REVISI_23082026_212923.md` (audit konsistensi internal).
