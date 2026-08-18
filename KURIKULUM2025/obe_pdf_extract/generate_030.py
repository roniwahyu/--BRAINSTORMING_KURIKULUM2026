from pathlib import Path
import json, hashlib

repo = Path('/home/user/--BRAINSTORMING_KURIKULUM2026')
out = repo / 'KURIKULUM2026_ZCODE/030_AUDIT_PER_HALAMAN_IMPLEMENTASI_MODUL_OBE_SISTEKIN2025_18082026.md'
pdf = repo / 'KURIKULUM2025/Implementasi_MODUL_OBE_SISTEKIN2025.pdf'
courses = json.loads(Path('/home/user/obe_pdf_extract/courses.json').read_text())
page5 = Path('/home/user/obe_pdf_extract/page5_matrix.md').read_text().strip()
page9 = Path('/home/user/obe_pdf_extract/page9_irm.md').read_text().strip()
page11 = Path('/home/user/obe_pdf_extract/page11_cpmk.md').read_text().strip()
sha = hashlib.sha256(pdf.read_bytes()).hexdigest()

parts = []
parts.append(f'''# 030 — AUDIT PER HALAMAN `Implementasi_MODUL_OBE_SISTEKIN2025.pdf`
## Inventarisasi Isi, Rekonstruksi Tabel, dan Pemetaan terhadap Materi Kurikulum 2026

**Tanggal audit:** 18 Agustus 2026  
**Sumber:** `KURIKULUM2025/Implementasi_MODUL_OBE_SISTEKIN2025.pdf`  
**Jumlah halaman:** 17  
**Ukuran halaman:** 792 × 612 pt (landscape)  
**Metadata judul:** `Implementasi_Modul_OBE_S1_SISTEKIN_UWG_2025.xlsx`  
**SHA-256:** `{sha}`  
**Basis pembanding:** `KURIKULUM2026_ZCODE/001`–`029` pada commit `f84f452`  

> **Batas audit:** berkas sumber Excel tidak ditemukan di repositori. Karena itu, isi visual dan angka pada PDF dapat diverifikasi, tetapi formula sel, validasi data, dan otomatisasi workbook tidak dapat diuji.

## Legenda status pemanfaatan

| Status | Makna |
|---|---|
| ✅ Tersedia | Substansi sudah tersedia dalam dokumen 2026. |
| ⚠️ Parsial/validasi | Sudah ada sebagian atau sudah berubah, tetapi belum ekuivalen penuh/masih perlu keputusan. |
| ↺ Digantikan | Artefak 2025 berfungsi sebagai baseline historis; versi 2026 memakai struktur/kode berbeda. |
| ❌ Belum operasional | Belum ada data aktual atau instrumen siap-input yang ekuivalen. |
| ⬜ Artefak cetak | Halaman hampir kosong akibat pemisahan area cetak Excel. |

## A. Ringkasan eksekutif

1. PDF bukan sekadar daftar kurikulum. Ia berisi **paket awal implementasi OBE**: self-assessment, 6 PL, 10 CPL, matriks PL–CPL, matriks CPL–MK, struktur semester, peta I/R/M, contoh CPMK/Sub-CPMK, template evaluasi kelas, dan rekap CPL prodi.
2. Sebagian besar **substansi desain** sudah dibuat ulang dan diperluas pada dokumen 2026, khususnya `008`–`012` dan `023`–`029`.
3. Artefak 2025 **tidak boleh disalin langsung** ke 2026 karena berubah dari 10 CPL menjadi 14 CPL, kode/nama MK berubah, dan struktur 56 MK/146 SKS berubah menjadi rancangan 2026.
4. Tiga kekurangan implementasi masih nyata: **RPS lengkap tiap MK**, **lembar nilai operasional tiap MK**, dan **data capaian aktual mahasiswa/kohort beserta bukti CQI**.
5. Ada konflik parameter yang perlu diputuskan: template PDF memakai bobot `15/10/20/20/10/25` dan target 75, sedangkan `029` mengusulkan komposisi `25/35/20/20` serta ambang individual 70 dan target kohort 75%.

## B. Inventaris dan status per halaman

| Hal. | Artefak pada PDF | Isi utama | Status di ZCODE 2026 | Dokumen utama | Tindakan |
|---:|---|---|---|---|---|
| 1 | Self-assessment kesiapan OBE | 17 kriteria; status Ya/Parsial/Belum/Perlu dilengkapi | ⚠️ Parsial | `017`, `022`, `023`, `029` | Perbarui checklist berbasis bukti, bukan pernyataan selesai. |
| 2 | Profil Lulusan 2025 | 6 PL dengan deskripsi dan profesi | ↺ Digantikan | `006`, `008`, `023` | Buat decision log transisi PL lama → PL 2026. |
| 3 | CPL 2025 | 10 CPL lintas domain | ↺ Digantikan | `009`, `009A`–`009E` | Jangan memakai kode CPL01–10 untuk pengukuran 14 CPL baru. |
| 4 | Matriks CPL–PL | 10 CPL × 6 PL; tiap PL ditopang 4–7 CPL | ↺ Digantikan | `009E` §4, `023` Matriks 3 | Validasi matriks 14 CPL × PL 2026. |
| 5 | Matriks CPL–MK | 56 MK/146 SKS × 10 CPL; 121 relasi | ↺ Digantikan | `012`, `023` Matriks 1 | Gunakan hanya sebagai baseline Kurikulum 2025. |
| 6 | Catatan lanjutan halaman 5 | “Seluruh MK telah memiliki minimal satu kontribusi CPL” | ⬜ Artefak cetak | `012` | Gabungkan ke halaman 5 bila PDF dicetak ulang. |
| 7 | Organisasi MK Sem. 1–6 | MK, SKS, CPL dominan per semester | ↺ Digantikan | `003`, `011`, `015` | Baseline 2025; struktur 2026 ada di `011`. |
| 8 | Organisasi MK Sem. 7–8 | Penutup struktur dan total 56 MK/146 SKS | ↺ Digantikan | `003`, `011`, `015` | Gabungkan dengan halaman 7 saat publikasi ulang. |
| 9 | Peta I/R/M bagian 1 | Level Introduced/Reinforced/Mastered untuk MK awal–MFT-002 | ↺ Digantikan | `023` Matriks 1 | Validasi I/R/M 14 CPL melalui RPS. |
| 10 | Peta I/R/M bagian 2 | MK akhir, total I/R/M per CPL | ↺ Digantikan | `023` Matriks 1 | Audit distribusi level M dan benchmark course. |
| 11 | Contoh penurunan CPL→CPMK | 6 MK penciri, 3 CPMK/MK, 6 Sub-CPMK/MK, bobot 100% | ⚠️ Parsial | `024`–`027`, `028` | Substansi meluas, tetapi belum menjadi RPS lengkap semua MK. |
| 12 | Sisa tabel validasi halaman 11 | Hanya baris `STI-743 … 100 OK` | ⬜ Artefak cetak | `024`–`027` | Gabungkan ke halaman 11. |
| 13 | Template evaluasi STI-741 | 20 baris mahasiswa; bobot & target CPMK | ⚠️ Parsial | `026`, `029` | Buat workbook/formula operasional untuk `STI-601`. |
| 14 | Template evaluasi STI-635 | Template UI/UX | ⚠️ Parsial | `025`, `029` | Adaptasi ke `STI-303`; selaraskan rubrik usability. |
| 15 | Template evaluasi STI-526 | Template IoT | ⚠️ Parsial | `026`, `029` | Adaptasi ke `STI-504`; tambahkan rubrik hardware/integrasi. |
| 16 | Template evaluasi STI-743 | Template audit/tata kelola | ⚠️ Parsial | `027`, `029` | Tentukan pengganti 2026 (mis. `STB-04`) dan rubrik kasus. |
| 17 | Rekap CPL prodi | Jumlah MK, pengukur level M, target 75%, capaian kosong | ❌ Belum operasional | `023` Matriks 4, `029` §4–7 | Memerlukan nilai aktual, agregasi, RTM, dan bukti PPEPP. |
''')

parts.append('''## C. Rekonstruksi dan analisis per halaman

### Halaman 1 — Self-assessment kesiapan implementasi modul OBE

| No | Aspek | Kriteria/Pertanyaan PDF | Status PDF | Catatan PDF | Status materi 2026 | Bukti/analisis |
|---:|---|---|---|---|---|---|
| 1 | Kurikulum OBE | Profil lulusan tersedia dan menggambarkan peran lulusan | Ya | 6 PL telah dirumuskan | ⚠️ | `008` memuat 6 PL versi baru; nama dan cakupan berubah. |
| 2 | Kurikulum OBE | Jumlah PL >3 dan mencakup bekerja/wirausaha | Ya | 6 PL, termasuk Digital Technopreneur | ⚠️ | Peran praktisi/technopreneur tersedia, tetapi keputusan 5 vs 6 PL perlu jejak pengesahan. |
| 3 | Kurikulum OBE | PL disajikan dengan kode, nama, deskripsi, profesi | Ya | Tersedia pada sheet 1 | ✅ | `008` dan `023` menyediakan PL, peran, jalur, dan target karier. |
| 4 | Kurikulum OBE | CPL tersedia dengan KKO + konten + konteks | Ya | 10 CPL pada sheet 2 | ✅ | `009`–`009E` mengganti menjadi 14 CPL. |
| 5 | Kurikulum OBE | Jumlah CPL 10–15 | Ya | Jumlah CPL = 10 | ✅ | Rancangan 2026 memuat 14 CPL. |
| 6 | Kurikulum OBE | Semua CPL dipetakan ke PL | Ya | Sheet 3 | ✅ | `009E` §4 dan `023` Matriks 3. |
| 7 | Kurikulum OBE | Setiap PL ditopang minimal 3 CPL | Ya | Seluruh PL ditopang 4–7 CPL | ✅ | Matriks 2026 tersedia; tetap perlu pengesahan formal. |
| 8 | Kurikulum OBE | Semua MK dipetakan terhadap CPL | Ya | 56 MK pada sheet 4 | ✅ | `012` memuat pemetaan MK–14 CPL 2026. |
| 9 | Kurikulum OBE | Struktur MK per semester dan total SKS tersedia | Ya | 56 MK, 146 SKS, 8 semester | ⚠️ | `011` tersedia, tetapi istilah beban lulus/portofolio perlu konsisten lintas dokumen. |
| 10 | Kurikulum OBE | Peta pemenuhan CPL oleh MK tersedia | Ya | Level I-R-M pada sheet 6 | ✅ | `023` Matriks 1. |
| 11 | Kurikulum OBE | BK final dan dipetakan CPL–BK–MK | Perlu dilengkapi | Belum tersedia | ✅/⚠️ | `021` dan `023` tersedia; status wajib vs pendukung BoK tetap perlu validasi. |
| 12 | OBLT | Setiap MK memiliki RPS berbasis CPL/CPMK/Sub-CPMK | Perlu dilengkapi | Contoh 6 MK | ⚠️ | `024`–`027` memuat CPMK/Sub-CPMK, tetapi full RPS baru contoh `028`. |
| 13 | OBLT | Metode pembelajaran selaras CPMK dan asesmen | Sebagian | Contoh sheet 7 | ⚠️ | Arahan ada di `024`–`029`; implementasi tiap RPS belum terbukti. |
| 14 | OBLAE | Rencana evaluasi dan bobot tiap MK tersedia | Sebagian | Template sheet 8–11 | ⚠️ | `029` memberi standar umum, belum lembar operasional tiap MK. |
| 15 | OBLAE | Capaian CPMK/CPL dihitung dari nilai aktual | Belum | Memerlukan data asesmen aktual | ❌ | Formula ada di `029`; data aktual belum tersedia. |
| 16 | OBLAE | Analisis ketercapaian dan continuous improvement berkala | Belum | Setelah data semester tersedia | ❌/⚠️ | Prosedur PPEPP ada di `029`; bukti siklus aktual belum ada. |
| 17 | Dokumen | Landasan, tracer study, PEO, referensi terdokumentasi | Perlu verifikasi | Tidak seluruhnya pada lampiran | ⚠️ | PEO tersedia; data tracer/employer survey aktual belum teridentifikasi. |

**Kesimpulan halaman 1:** desain dokumen 2026 mengisi mayoritas gap struktural, tetapi tidak membuktikan implementasi nilai, RPS lengkap, atau CQI aktual.

### Halaman 2 — Profil Lulusan Kurikulum 2025

| Kode | Profil 2025 | Deskripsi ringkas | Profesi PDF | Padanan dominan 2026 `[ANALISIS]` | Status |
|---|---|---|---|---|---|
| PL01 | AI-Driven System Developer | Mengembangkan SI berbasis AI sesuai kebutuhan pengguna/organisasi | AI Application Developer; ML Developer; Software Developer | PL-01 Intelligent IS Developer + sebagian PL-06 Data/ML Engineer | ↺ Dipecah/diperluas |
| PL02 | Human-Centered UX and Gamification Designer | UX dan gamifikasi inklusif dan berorientasi pengguna | UI/UX Designer; UX Researcher; Interaction/Gamification Designer | PL-02 UI/UX & Digital Platform Engineer | ↺ Fokus gamifikasi berkurang; platform bertambah |
| PL03 | IoT and Multimedia System Integrator | Integrasi IoT dan multimedia | IoT Developer; System Integrator; Multimedia/Smart System Developer | PL-03 Smart System & Technology Integrator | ↺ Cloud/infrastruktur diperkuat |
| PL04 | Semantic Knowledge and Data Integration Engineer | Integrasi data/pengetahuan lintas platform | Knowledge Engineer; Data Integration Engineer; Semantic Web Developer | Sebagian PL-06 dan PL-01 | ↺ Tidak ada padanan satu-ke-satu |
| PL05 | Digital Technopreneur | Usaha dan inovasi digital | Technopreneur; Startup Founder; Digital Product Manager | PL-04 Technopreneur | ↺ Renumbering |
| PL06 | Digital Governance and System Analyst | Analisis sistem dan tata kelola transformasi digital | System Analyst; IT Governance Analyst; Digital Transformation Analyst | PL-05 Digital System Governance Analyst | ↺ Renumbering |

> Padanan di atas adalah analisis transisi, bukan keputusan formal. Dokumen 2026 harus memiliki *decision log* agar perubahan PL dapat ditelusuri.

### Halaman 3 — Sepuluh CPL Kurikulum 2025

| Kode | Rumusan ringkas PDF | Fokus/domain | PL terkait | Padanan dominan dalam 14 CPL 2026 `[ANALISIS]` |
|---|---|---|---|---|
| CPL01 | Analisis kebutuhan, proses bisnis, masalah organisasi, dan rancangan solusi | Analisis kebutuhan & solusi | PL01, PL02, PL06 | KU1, P2, KK5 |
| CPL02 | Rancang–bangun–uji–integrasi perangkat lunak, basis data, API, cloud | Perangkat lunak & platform | PL01, PL03, PL04 | P4, KK3, KK5 |
| CPL03 | Metode komputasi, analitik, AI/ML untuk solusi berbasis data | AI & analitika | PL01, PL04, PL06 | P2, P4, KK1, KK2 |
| CPL04 | Antarmuka, UX, gamifikasi, multimedia human-centered | UX/gamifikasi/multimedia | PL02, PL03, PL05 | P4, KK5 |
| CPL05 | Integrasi IoT, jaringan, sensor, multimedia, layanan komputasi | Infrastruktur & integrasi | PL01, PL03 | P3, KK3 |
| CPL06 | Kelola/integrasi/representasi data dan pengetahuan | Data, knowledge, interoperability | PL04, PL06 | P2, P4, KK2 |
| CPL07 | Tata kelola, audit, keamanan, etika, hukum, kebijakan TI | Governance/security | PL05, PL06 | S1, P3, KK3, KK4 |
| CPL08 | Kelola proyek, produk, model bisnis, inovasi digital | Project/technopreneurship | PL01, PL02, PL05 | KU3, KK6 |
| CPL09 | Matematika, statistika, penelitian, computational thinking | Fondasi ilmiah | PL01, PL04, PL06 | P1, KU1, KU3 |
| CPL10 | Profesionalisme, integritas, komunikasi, kolaborasi, leadership, lifelong learning | Etika/profesional | Semua PL | S1, KU2, KU3 |

**Catatan:** halaman menyebut seluruh rumusan sebagai rancangan untuk validasi tim. Pemetaan CPL lama–baru wajib diputuskan jika data asesmen 2025 akan dibawa ke sistem 2026.

### Halaman 4 — Matriks keterkaitan CPL–PL 2025

| CPL | PL01 | PL02 | PL03 | PL04 | PL05 | PL06 | Jumlah PL |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| CPL01 | V | V |  |  |  | V | 3 |
| CPL02 | V |  | V | V |  |  | 3 |
| CPL03 | V |  |  | V |  | V | 3 |
| CPL04 |  | V | V |  | V |  | 3 |
| CPL05 | V |  | V |  |  |  | 2 |
| CPL06 |  |  |  | V |  | V | 2 |
| CPL07 |  |  |  |  | V | V | 2 |
| CPL08 | V | V |  |  | V |  | 3 |
| CPL09 | V |  |  | V |  | V | 3 |
| CPL10 | V | V | V | V | V | V | 6 |
| **Jumlah CPL per PL** | **7** | **4** | **4** | **5** | **4** | **6** | **30 relasi** |

**Analisis:** kriteria internal “minimal 3 CPL per PL” terpenuhi, tetapi matriks ini tidak dapat dipakai untuk 14 CPL baru tanpa matriks transisi.

### Halaman 5 — Matriks pemetaan CPL–Mata Kuliah 2025

Tabel PDF memiliki 56 baris, 10 kolom CPL, dan 121 relasi. Rekonstruksi berikut mengompresi kolom kosong menjadi daftar CPL yang dicentang.
''')
parts.append(page5)
parts.append('''

### Halaman 6 — Catatan lanjutan matriks

| Elemen | Isi |
|---|---|
| Catatan tunggal | “Seluruh MK telah memiliki minimal satu kontribusi CPL.” |
| Analisis | Benar secara aritmetika terhadap halaman 5; setiap baris memiliki 1–4 CPL. |
| Status 2026 | `012` menggantikan matriks ini dengan 14 CPL dan struktur 2026. |
| Masalah tata letak | Hampir seluruh halaman kosong; sebaiknya catatan digabung ke halaman 5. |

### Halaman 7–8 — Organisasi mata kuliah Kurikulum 2025
''')

# Build semester organization table
cpl_dom = {
1:'CPL09, CPL10, CPL07',2:'CPL09, CPL10, CPL02',3:'CPL02, CPL10, CPL05',4:'CPL10, CPL08, CPL07',
5:'CPL05, CPL02, CPL07',6:'CPL03, CPL01, CPL09',7:'CPL10, CPL09, CPL02',8:'CPL09, CPL10, CPL01'}
parts.append('| Hal. | Semester | Jumlah MK | Total SKS | Daftar Mata Kuliah | CPL dominan |\n|---:|---:|---:|---:|---|---|')
for s in range(1,9):
    cs=[c for c in courses if c['smt']==s]
    names='<br>'.join(f"`{c['code']}` {c['name']} ({c['sks']} SKS)" for c in cs)
    parts.append(f"| {'7' if s<=6 else '8'} | {s} | {len(cs)} | {sum(c['sks'] for c in cs)} | {names} | {cpl_dom[s]} |")
parts.append('| 8 | **TOTAL** | **56** | **146** | **Data Kurikulum 2025 sesuai laporan prodi** |  |')
parts.append('''

**Analisis halaman 7–8:** tabel cocok dengan laporan SIAKAD 2025. Dalam ZCODE, `003` mempertahankan baseline, `015` membandingkan 2025–2026, dan `011` berisi rancangan baru. Halaman ini tidak boleh disebut struktur 2026.

### Halaman 9–10 — Peta pemenuhan CPL level I/R/M

Legenda PDF: **I** = Introduced, **R** = Reinforced, **M** = Mastered. PDF sendiri menyatakan level ini merupakan rancangan awal yang perlu divalidasi pada RPS.
''')
parts.append(page9)
parts.append('''

**Analisis halaman 9–10:**
- Distribusi level cocok dengan total PDF.
- `CPL10` sangat padat pada level R (17 MK), sedangkan level M tiap CPL hanya 1–2 MK.
- `023` telah membuat I/R/M untuk 14 CPL baru, tetapi validitasnya tetap bergantung pada CPMK, asesmen, dan RPS riil.
- Data capaian lama tidak dapat digabung dengan CPL baru hanya berdasarkan kemiripan nama.

### Halaman 11 — Contoh penurunan CPL → CPMK → Sub-CPMK → evaluasi

PDF memuat 6 mata kuliah penciri, masing-masing 3 CPMK dan 6 Sub-CPMK. Bobot setiap MK berjumlah 100%.
''')
parts.append(page11)
parts.append('''

#### Status enam contoh pada rancangan 2026

| MK pada PDF | Posisi/padanan 2026 | Dokumen CPMK 2026 | Status |
|---|---|---|---|
| STI-741 Integrasi Layanan Cerdas Berbasis AI | `STI-601` | `026` | ✅ Substansi dipertahankan dengan kode baru |
| STI-635 Desain & Evaluasi UI/UX | `STI-303` | `025` | ✅ Dipindahkan lebih awal dan dipertegas prototyping |
| STI-526 Internet of Things | `STI-504` | `026` | ✅ Dipertahankan dengan kode baru |
| STI-420 Semantic Web & Ontologi | Tidak ada padanan wajib langsung | Tersebar/opsional | ⚠️ Tidak bisa dipindahkan otomatis |
| STI-742 Inovasi Teknologi & Startup Digital | `STI-702` | `027` | ✅ Dipertahankan dengan kode baru |
| STI-743 Audit & Tata Kelola SI | Terdistribusi pada KK4/P2, terutama `STB-04` | `027`, `029` | ⚠️ Berubah menjadi jalur/peminatan |

### Halaman 12 — Sisa tabel validasi halaman 11

| Baris | Total bobot | Validasi | Analisis |
|---|---:|---|---|
| STI-743 Audit dan Tata Kelola Sistem Informasi | 100 | OK | Hanya satu baris akibat *page break*; sebaiknya digabung ke halaman 11. |

### Halaman 13–16 — Empat template evaluasi OBE mata kuliah

#### Identitas dan CPL yang dibebankan

| Hal. | Mata kuliah PDF | CPL PDF | Padanan 2026 | Status |
|---:|---|---|---|---|
| 13 | STI-741 Integrasi Layanan Cerdas Berbasis AI | CPL02, CPL03, CPL05, CPL06 | STI-601 | ⚠️ CPL harus dikonversi ke kode 14 CPL baru |
| 14 | STI-635 Desain dan Evaluasi UI/UX | CPL04, CPL09, CPL10 | STI-303 | ⚠️ Perlu rubrik usability/prototyping baru |
| 15 | STI-526 Internet of Things | CPL02, CPL05 | STI-504 | ⚠️ Perlu asesmen integrasi sensor-edge-cloud |
| 16 | STI-743 Audit dan Tata Kelola SI | CPL07, CPL09, CPL10 | STB-04/klaster KK4 | ⚠️ Status wajib/peminatan berubah |

#### Struktur bobot identik pada keempat halaman

| Komponen | Tugas | Kuis | UTS | UAS | Aktivitas | Project | Total | Target CPMK1 | Target CPMK2 | Target CPMK3 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bobot PDF | 15% | 10% | 20% | 20% | 10% | 25% | 100% | 75 | 75 | 75 |

#### Skema tabel input mahasiswa pada setiap halaman

| No | NIM | Nama Mahasiswa | Tugas | Kuis | UTS | UAS | Aktivitas | Project | Nilai Akhir | CPMK1 | CPMK2 | CPMK3 | Status CPL |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1–20 | *(kosong)* | *(kosong)* | *(input 0–100)* | *(input)* | *(input)* | *(input)* | *(input)* | *(input)* | *(formula tidak dapat diaudit dari PDF)* |  |  |  |  |

| Ringkasan kelas | Nilai |
|---|---|
| Rata-rata Nilai Akhir | Kosong |
| Rata-rata CPMK1 | Kosong |
| Rata-rata CPMK2 | Kosong |
| Rata-rata CPMK3 | Kosong |
| Target CPL | 75 |
| Persentase mahasiswa tercapai | Kosong |

**Analisis halaman 13–16:** `029` menyediakan formula dan rubrik umum, tetapi Markdown tidak menggantikan workbook yang dapat menghitung nilai. Diperlukan `.xlsx`/SIAKAD OBE untuk seluruh MK, lengkap dengan formula, proteksi sel, validasi, dan data dictionary.

### Halaman 17 — Template rekapitulasi ketercapaian CPL program studi

| CPL | Fokus | Jumlah MK pendukung | MK pengukur level M | Target | Capaian aktual | Status PDF |
|---|---|---:|---|---:|---|---|
| CPL01 | Analisis kebutuhan & perancangan solusi | 7 | MFT-004 | 75 | Kosong | Belum ada data |
| CPL02 | Pengembangan perangkat lunak & platform | 13 | MFT-003, STI-741 | 75 | Kosong | Belum ada data |
| CPL03 | AI, komputasi & analitika data | 12 | STI-740, STI-741 | 75 | Kosong | Belum ada data |
| CPL04 | UX, gamifikasi & multimedia | 10 | STI-739, STI-740 | 75 | Kosong | Belum ada data |
| CPL05 | IoT, infrastruktur & integrasi sistem | 11 | STI-741 | 75 | Kosong | Belum ada data |
| CPL06 | Data, knowledge & interoperability | 8 | STI-740, STI-741 | 75 | Kosong | Belum ada data |
| CPL07 | Tata kelola, keamanan & kebijakan digital | 11 | STI-743 | 75 | Kosong | Belum ada data |
| CPL08 | Proyek, inovasi & technopreneurship | 10 | STI-739, STI-742 | 75 | Kosong | Belum ada data |
| CPL09 | Fondasi ilmiah & penelitian | 17 | MFT-004, STI-844 | 75 | Kosong | Belum ada data |
| CPL10 | Etika & keterampilan profesional | 22 | MFT-004, STI-844 | 75 | Kosong | Belum ada data |

**Analisis:** halaman 17 adalah template, bukan hasil pengukuran. `023` dan `029` memperbarui rencana benchmark serta formula, tetapi capaian aktual tetap tidak dapat dinyatakan sebelum tersedia data mahasiswa yang valid.

## D. Matriks pemanfaatan materi PDF untuk paket 2026

| Artefak PDF 2025 | Reuse langsung? | Cara memanfaatkan di 2026 | Risiko jika disalin langsung |
|---|:---:|---|---|
| Self-assessment | Tidak | Jadikan checklist audit berbukti dengan tautan dokumen | Status “Ya/100%” tanpa bukti implementasi |
| 6 PL lama | Tidak | Gunakan sebagai histori dan buat matriks transisi | Perubahan makna/penomoran PL |
| 10 CPL lama | Tidak | Buat matriks ekuivalensi menuju 14 CPL | Data capaian tercampur antarversi |
| Matriks CPL–PL | Tidak | Regenerasi dari 14 CPL | Relasi tidak lagi valid |
| Matriks CPL–MK | Tidak | Gunakan `012`/`023` | Kode MK, SKS, dan CPL berbeda |
| Struktur 56 MK/146 SKS | Baseline | Gunakan untuk komparasi `015` | Disebut keliru sebagai struktur 2026 |
| I/R/M lama | Tidak | Gunakan sebagai pola desain | Level lama tidak setara CPL baru |
| Contoh CPMK 6 MK | Sebagian | Adaptasi substansi ke kode MK baru | KKO, CPL, dan asesmen tidak sinkron |
| Template evaluasi | Sebagian | Jadikan prototipe workbook 2026 | Bobot dan threshold konflik dengan `029` |
| Rekap CPL | Sebagian | Gunakan skema setelah benchmark 14 CPL final | Mengisi angka tanpa data asesmen aktual |

## E. Gap implementasi yang belum boleh diklaim selesai

| Gap | Kondisi sekarang | Bukti yang dibutuhkan agar selesai |
|---|---|---|
| Full RPS seluruh MK | CPMK/Sub-CPMK tersedia; hanya satu contoh RPS lengkap (`028`) | RPS lengkap, disahkan, untuk setiap MK yang ditawarkan |
| Lembar asesmen operasional | Formula naratif dan 4 template PDF lama | Workbook/SIAKAD per MK dengan formula tervalidasi |
| Nilai CPMK/CPL aktual | Belum ada di PDF maupun ZCODE | Dataset nilai mahasiswa, mapping asesmen–CPMK, hasil agregasi |
| CQI/PPEPP aktual | Prosedur tersedia di `029` | Berita acara RTM, RCA, RTL, revisi RPS, bukti tindak lanjut |
| Tracer/employer survey | Disebut sebagai instrumen | Data aktual, metodologi, responden, periode, dan analisis |
| Harmonisasi bobot | PDF dan `029` berbeda | SK/keputusan akademik satu skema atau aturan variasi per tipe MK |
| Harmonisasi threshold | PDF target 75; `029` individual 70/kohort 75% | Definisi target dan formula yang disahkan |
| Migrasi 10 → 14 CPL | Belum ada dokumen transisi eksplisit | Matriks ekuivalensi dan aturan perlakuan data historis |

## F. Kesimpulan

PDF 17 halaman ini merupakan **baseline implementasi OBE Kurikulum 2025 yang substantif**, bukan sekadar laporan struktur. Materi desainnya sebagian besar telah diperluas di ZCODE 2026. Namun, kesiapan dokumen tidak sama dengan implementasi: data nilai aktual, RPS lengkap, instrumen hitung, dan bukti CQI belum tersedia. Dokumen 2026 sebaiknya mempertahankan PDF ini sebagai **arsip baseline**, lalu membangun paket operasional 14 CPL secara terpisah dan terversi.
''')

out.write_text('\n'.join(parts), encoding='utf-8')
print(out)
print('lines', len(out.read_text().splitlines()), 'words', len(out.read_text().split()))
