# 034 — ANALISIS AWAL PEO DAN ARAH PENAJAMAN AGENTIC
## Baseline/Handoff untuk Perumusan Program Educational Objectives SISTEKIN

**Tanggal:** 20 Agustus 2026  
**Status:** **DRAFT BASELINE — BELUM FINAL, BELUM TERKUNCI, BELUM DISAHKAN**  
**Konteks:** Program Studi SISTEKIN baru berjalan dua semester dan belum memiliki alumni  
**Tujuan:** menyimpan hasil analisis awal agar agent berikutnya dapat melakukan verifikasi, penajaman, dan pendalaman PEO tanpa mengulang atau mengunci asumsi yang belum diputuskan.

---

## 1. Kesimpulan awal yang harus dipertahankan

1. **PEO perlu ditetapkan sejak awal penyelenggaraan prodi.** PEO tidak menunggu tracer study karena menjadi dasar perancangan PL, CPL, kurikulum, dan sistem evaluasi.
2. **PEO saat ini bersifat provisional/baseline.** Validitasnya perlu diperoleh melalui VMTS, FGD stakeholder, employer needs survey, benchmark prodi sejenis, standar APTIKOM/ACM/IEEE/SKKNI, dan keputusan formal prodi/UPPS.
3. **Tracer study berfungsi untuk mengukur dan memperbaiki PEO**, bukan untuk pertama kali membentuk PEO. Pengukuran PEO utama baru relevan 3–5 tahun setelah angkatan pertama lulus.
4. **Leadership bukan jalur karier keempat yang berdiri sendiri.** Leadership adalah kemampuan lintas-jalur yang dapat muncul pada akademisi, profesional, dan technopreneur.
5. **Enam Profil Lulusan dapat dikonsolidasikan menjadi tiga PEO.** Tidak diperlukan satu PEO untuk setiap PL.
6. **PEO tidak boleh hanya diturunkan secara mekanis dari PL.** Rumusan akhir harus merupakan sintesis:

```text
VMTS + Profil Lulusan + kebutuhan stakeholder + standar keilmuan
                              ↓
                         Rumusan PEO
```

---

## 2. Posisi konsep dalam arsitektur OBE

| Komponen | Pertanyaan yang dijawab | Waktu pengukuran |
|---|---|---|
| **VMTS** | Arah dan kekhasan institusi/prodi menuju apa? | Jangka panjang |
| **PEO** | Apa yang diharapkan dicapai alumni 3–5 tahun setelah lulus? | 3–5 tahun pascalulus |
| **Profil Lulusan (PL)** | Lulusan dipersiapkan untuk memainkan peran apa? | Saat lulus/awal karier |
| **CPL** | Kompetensi apa yang harus dimiliki saat lulus? | Saat kelulusan |
| **CPMK/Sub-CPMK** | Kemampuan apa yang dicapai melalui mata kuliah? | Selama pembelajaran |

Arsitektur yang akan dipakai oleh agent berikutnya:

```text
VMTS → PEO → PL → CPL → BoK → Klaster/Mata Kuliah → CPMK → Asesmen
  ↑                                                               ↓
  └────────────── Evaluasi stakeholder, tracer, dan PPEPP ─────────┘
```

---

## 3. Kondisi PEO yang ditemukan dalam dokumen saat ini

### 3.1 Materi yang sudah tersedia

- `008_LANGKAH1_PROFIL_LULUSAN_PEO.md` menyediakan capaian 3–5 tahun dan indikator per PL untuk tiga jalur: akademisi, praktisi, dan technopreneur.
- `023_FORMULASI_MATRIKS_OBE_LENGKAP_DAN_TAKSONOMI_CPL_MK.md` memperkenalkan:
  - `PEO-1`: Praktisi / AI Specialist;
  - `PEO-2`: Technopreneur / Founder;
  - `PEO-3`: Akademisi / Researcher.
- `023` juga memuat hubungan VMTS → PEO → PL → CPL → MK.
- `033_ANALISIS_KESELARASAN_VMTS_PL_CPL_BoK_CPMK_DAN_MATRIKS.md` memperluas keterlacakan dari VMTS sampai CPMK, tetapi PEO masih digabung dengan PL dan jalur karier.

### 3.2 Kelemahan yang harus diperbaiki

| Temuan | Dampak |
|---|---|
| PEO-1/2/3 masih berupa label jalur, belum rumusan tujuan pendidikan lengkap | Belum cukup untuk dokumen formal/akreditasi |
| `008` membuat skenario 6 PL × 3 jalur | Terlalu rinci dan berpotensi mencampur PL, profesi, dan PEO |
| Diagram dan tabel PEO–PL pada `023` tidak sepenuhnya konsisten | Keterlacakan belum stabil |
| Belum ada matriks PEO × CPL yang eksplisit | Kontribusi kurikulum terhadap PEO belum dapat diaudit langsung |
| Belum ada *PEO Measurement Plan* | Tidak ada definisi indikator, sumber data, periode, target, dan PIC |
| Belum ada alumni/tracer study | Ketercapaian PEO belum dapat dinilai secara empiris |
| Belum ada bukti pengesahan PEO | Status PEO masih rancangan |

### 3.3 Inkonsistensi spesifik pada `023`

Diagram `023` menunjukkan:

- PEO-1 → PL-01, PL-03, PL-05, PL-06;
- PEO-2 → PL-02, PL-04;
- PEO-3 tidak memiliki panah ke PL.

Tabel pada dokumen yang sama menyatakan:

- PL-01, PL-03, PL-05, PL-06 → PEO-1 dan PEO-3;
- PL-02 → PEO-1 dan PEO-2;
- PL-04 → PEO-2.

Agent berikutnya wajib merekonsiliasi diagram dan tabel sebelum menyatakan keselarasan PEO selesai.

---

## 4. Enam Profil Lulusan yang menjadi input awal

| Kode | Profil Lulusan |
|---|---|
| **PL-01** | Intelligent Information System Developer |
| **PL-02** | UI/UX Designer & Digital Platform Engineer |
| **PL-03** | Smart System & Technology Integrator |
| **PL-04** | Technopreneur |
| **PL-05** | Digital System & Technology Governance Analyst |
| **PL-06** | Data Analyst & Machine Learning Engineer |

> **Catatan validasi:** dokumen lama dan notulensi pernah menyebut jumlah/nomenklatur PL yang berbeda. Agent berikutnya harus memastikan keputusan formal enam PL sebelum mengunci PEO.

---

## 5. Usulan rumusan awal tiga PEO

### PEO-1 — Professional Practice and Systems Integration

> Dalam 3–5 tahun setelah lulus, alumni mampu berkarier secara profesional dalam menganalisis, merancang, mengembangkan, mengintegrasikan, mengamankan, atau mengelola sistem dan teknologi informasi cerdas sesuai kebutuhan organisasi, industri, dan masyarakat.

**PL utama:** PL-01, PL-02, PL-03, PL-05, PL-06.  
**PL pendukung:** PL-04 dalam konteks pengembangan produk/organisasi.

### PEO-2 — Digital Innovation and Technopreneurship

> Dalam 3–5 tahun setelah lulus, alumni mampu menghasilkan inovasi, produk, layanan, perbaikan proses, atau usaha digital yang relevan, etis, berkelanjutan, dan memberikan nilai bagi pengguna, organisasi, industri, atau masyarakat.

**PL utama:** PL-04.  
**PL pendukung:** PL-01, PL-02, PL-03, PL-06.

### PEO-3 — Advanced Study, Research, and Lifelong Learning

> Dalam 3–5 tahun setelah lulus, alumni mampu mengembangkan kompetensi melalui studi lanjut, penelitian terapan, sertifikasi profesional, komunitas keilmuan, atau pembelajaran sepanjang hayat serta menunjukkan kepemimpinan sesuai konteks profesinya.

**PL terkait:** seluruh PL.

> Rumusan di atas adalah hipotesis desain. Jangan diberi label final sebelum divalidasi stakeholder dan disahkan.

---

## 6. Matriks awal PEO–PL

**U = kontribusi utama; D = pendukung**

| Profil Lulusan | PEO-1 Profesional | PEO-2 Inovasi | PEO-3 Pengembangan |
|---|:---:|:---:|:---:|
| PL-01 Intelligent IS Developer | U | D | U |
| PL-02 UI/UX & Platform Engineer | U | D | U |
| PL-03 Smart System Integrator | U | D | U |
| PL-04 Technopreneur | D | U | U |
| PL-05 Governance Analyst | U | — | U |
| PL-06 Data & ML Engineer | U | D | U |

### Pemeriksaan awal

- Setiap PL memiliki minimal satu PEO utama.
- PEO-1 mencakup seluruh domain praktik profesional SISTEKIN.
- PEO-2 menempatkan PL-04 sebagai penanggung jawab utama tanpa mengisolasi inovasi dari PL teknis.
- PEO-3 menjadi tujuan pengembangan berkelanjutan lintas-profesi.
- Leadership ditempatkan sebagai indikator lintas-PEO, bukan PEO keempat.

---

## 7. Leadership sebagai atribut lintas-PEO

| Jalur | Bentuk leadership yang relevan |
|---|---|
| Akademisi/peneliti | Memimpin riset, kelompok kajian, laboratorium, atau pengembangan keilmuan |
| Profesional | Memimpin tim teknis, proyek, arsitektur solusi, tata kelola, atau transformasi digital |
| Technopreneur | Memimpin startup, pengembangan produk, validasi pasar, dan pertumbuhan bisnis |

Indikator lintas-PEO yang dapat dikaji:

- koordinasi tim/proyek;
- pengambilan keputusan berbasis data dan risiko;
- komunikasi profesional;
- tanggung jawab etika dan sosial;
- inisiatif perbaikan atau inovasi;
- pembelajaran dan pengembangan kompetensi berkelanjutan.

---

## 8. Indikator awal PEO — belum memiliki target numerik

| PEO | Indikator kandidat | Sumber data masa depan |
|---|---|---|
| **PEO-1** | Relevansi pekerjaan; peran/tanggung jawab; proyek yang diimplementasikan; sertifikasi; kepuasan pengguna lulusan | Tracer study, employer survey, portofolio alumni, basis data sertifikasi |
| **PEO-2** | Produk/MVP; inovasi proses; usaha digital; pengguna/klien; keberlanjutan usaha; manfaat sosial/organisasi | Tracer, survei alumni, inkubator bisnis, dokumentasi produk |
| **PEO-3** | Studi lanjut; publikasi/riset; sertifikasi; pelatihan; komunitas profesi; peningkatan tanggung jawab | Tracer, data akademik, repository, organisasi profesi |

**Aturan:** jangan menetapkan persentase target tanpa baseline, benchmark, atau keputusan stakeholder. Target awal harus diberi label provisional.

---

## 9. Rencana pengukuran bertahap untuk prodi baru

| Tahap | Fokus evaluasi | Instrumen |
|---|---|---|
| Setiap semester | CPMK dan CPL mahasiswa aktif | Nilai/rubrik, portofolio, evaluasi RPS |
| Setiap tahun | Relevansi PEO dan kurikulum | FGD industri, advisory board, survei mitra |
| Saat lulus | Kesiapan lulusan | Exit survey, portofolio CPL, sertifikasi |
| 6–12 bulan pascalulus | Transisi kerja awal | Tracer awal: waktu tunggu, relevansi pekerjaan |
| 3–5 tahun pascalulus | Ketercapaian PEO | Tracer PEO, employer survey, data karier/inovasi/studi lanjut |
| Setelah evaluasi | Perbaikan PEO/kurikulum | RTM, RCA, RTL, revisi melalui PPEPP |

Prodi yang baru berjalan dua semester belum dapat mengklaim ketercapaian PEO. Yang dapat dinilai sekarang adalah kualitas desain, validasi stakeholder, dan kesiapan instrumen.

---

## 10. Agenda wajib untuk agentic berikutnya

Agent berikutnya harus bekerja dengan urutan berikut dan berhenti pada titik keputusan manusia:

1. **Audit sumber primer dan terminologi**
   - Pastikan definisi PEO menurut panduan yang dipilih.
   - Bedakan PEO, PL, profesi, dan jalur karier.
   - Periksa keputusan resmi jumlah/nomenklatur PL.

2. **Validasi tiga PEO awal**
   - Uji keterlacakan terhadap VMTS.
   - Uji apakah PEO cukup luas, tidak tumpang tindih, dan dapat diukur 3–5 tahun.
   - Siapkan alternatif redaksi bila diperlukan.

3. **Susun matriks formal**
   - VMTS × PEO;
   - PEO × PL;
   - PEO × CPL;
   - PEO × klaster MK/peminatan;
   - PEO × indikator dan sumber bukti.

4. **Susun PEO Measurement Plan**
   - indikator;
   - definisi operasional;
   - sumber data;
   - periode;
   - baseline;
   - target provisional;
   - PIC/validator;
   - mekanisme PPEPP.

5. **Siapkan validasi stakeholder**
   - FGD industri/pemerintah/komunitas;
   - employer needs survey;
   - advisory board;
   - benchmark prodi sejenis;
   - berita acara dan decision log.

6. **Tentukan status akhir**
   - `DRAFT`;
   - `READY FOR STAKEHOLDER REVIEW`;
   - `APPROVED BY PRODI/UPPS`;
   - `VALIDATED BY TRACER`.

---

## 11. Larangan untuk agent berikutnya

- Jangan menyatakan PEO “100% valid/selaras” hanya karena matriks tersedia.
- Jangan menyamakan jalur karier dengan PEO tanpa justifikasi.
- Jangan menjadikan leadership sebagai PEO baru secara otomatis.
- Jangan membuat target tracer numerik tanpa baseline.
- Jangan mengklaim PEO tercapai sebelum tersedia alumni 3–5 tahun pascalulus.
- Jangan mengubah PL, CPL, atau PEO tanpa mencatat dampak ke seluruh matriks turunannya.
- Jangan memperlakukan label `FINAL` pada dokumen turunan sebagai bukti pengesahan institusi.

---

## 12. Dokumen yang wajib dibaca sebelum penajaman

| Prioritas | Dokumen | Fungsi |
|:---:|---|---|
| 1 | `KURIKULUM2025/Notulensi Rapat VMTS & Kurikulum Program Studi SIST 090626.pdf` | Bukti keputusan VMTS/PL rapat |
| 2 | `006_KEPUTUSAN_FINAL_ARAH_KURIKULUM_SISTEKIN.md` | Arah dan PL terkini |
| 3 | `008_LANGKAH1_PROFIL_LULUSAN_PEO.md` | Bahan awal PL/PEO 3–5 tahun |
| 4 | `009E_RINGKASAN_CPL_LENGKAP_PEMETAAN_BoK.md` | CPL dan PL |
| 5 | `023_FORMULASI_MATRIKS_OBE_LENGKAP_DAN_TAKSONOMI_CPL_MK.md` | PEO-1/2/3 dan traceability awal |
| 6 | `033_ANALISIS_KESELARASAN_VMTS_PL_CPL_BoK_CPMK_DAN_MATRIKS.md` | Master matrix terkini |
| 7 | `031_CHECKLIST_KESIAPAN_IMPLEMENTASI_OBE_BERBASIS_BUKTI_18082026.md` | Aturan bukti dan status kesiapan |
| 8 | Panduan APTIKOM SI v2.0 dan TI 2023 | Terminologi dan standar rujukan |

---

## 13. Keputusan yang masih memerlukan manusia

| ID | Keputusan | Status |
|---|---|---|
| **D-PEO-01** | Menetapkan tiga PEO atau jumlah lain | Belum diputuskan formal |
| **D-PEO-02** | Mengesahkan rumusan PEO-1, PEO-2, PEO-3 | Belum |
| **D-PEO-03** | Mengesahkan matriks PEO–PL dan PEO–CPL | Belum |
| **D-PEO-04** | Menetapkan indikator dan target provisional | Belum |
| **D-PEO-05** | Menetapkan mekanisme stakeholder review dan tracer | Belum |
| **D-PEO-06** | Menetapkan periode review PEO dalam PPEPP | Belum |

---

## 14. Status handoff

**Status akhir dokumen ini: `READY FOR AGENTIC DEEPENING`, bukan `APPROVED`.**

Agent berikutnya harus menggunakan dokumen ini sebagai baseline, menguji setiap asumsi terhadap sumber primer, dan menghasilkan rekomendasi yang dapat diputuskan oleh tim prodi/UPPS.
