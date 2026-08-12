---
geometry: margin=1in
documentclass: report
classoption: 12pt, a4paper
header-includes:
  - \usepackage{geometry}
  - \usepackage{fontspec}
  - \setmainfont{Inter}
  - \usepackage{xcolor}
  - \definecolor{primary}{RGB}{25, 113, 194}
  - \definecolor{secondary}{RGB}{240, 245, 250}
  - \definecolor{accent}{RGB}{0, 150, 136}
  - \usepackage{titlesec}
  - \titleformat{\chapter}[display]{\normalfont\huge\bfseries\color{primary}}{\chaptertitlename\ \thechapter}{20pt}{\Huge\bfseries\color{primary}}
  - \titleformat{\section}{\normalfont\Large\bfseries\color{primary}}{\thesection}{1em}{}
  - \titleformat{\subsection}{\normalfont\large\bfseries\color{accent}}{\thesubsection}{1em}{}
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhf{}
  - \fancyhead[LE,RO]{\thepage}
  - \fancyhead[LO,RE]{\nouppercase{\leftmark}}
  - \renewcommand{\headrulewidth}{0.5pt}
  - \renewcommand{\footrulewidth}{0pt}
  - \definecolor{headerbg}{RGB}{25, 113, 194}
  - \renewcommand{\headrule}{{\color{headerbg}\hrule width=\headwidth height=2pt depth=0pt}}
  - \usepackage{graphicx}
  - \usepackage{booktabs}
  - \usepackage{array}
  - \usepackage{longtable}
  - \usepackage{enumitem}
  - \setlist[itemize]{leftmargin=*}
  - \setlist[enumerate]{leftmargin=*}
  - \usepackage{lipsum}
  - \usepackage{multicol}
  - \usepackage{parskip}
  - \setlength{\parskip}{1em}
  - \usepackage{ragged2e}
  - \usepackage{microtype}
---

\newpage

\begin{center}
{\Huge\bfseries\color{primary} ANALISIS KURIKULUM \\ SISTEKIN}\vspace{0.5cm}

{\Large\bfseries Berdasar Standar APTIKOM OBE & ACM/ACEEE}\vspace{1cm}

{\large\color{accent} Oleh: Profesor Ahli dengan 25+ Tahun Pengalaman}\vspace{0.5cm}

{\small\color{gray} Tanggal: 4 Agustus 2026}\vspace{2cm}

\includegraphics[width=0.3\textwidth]{/home/user/cover_image.png}
\end{center}

\newpage

---

\tableofcontents

\newpage

# Pendahuluan

Program Studi Sistem dan Teknologi Informasi (SISTEKIN) saat ini menghadapi tantangan dalam memenuhi standar nasional dan internasional. Analisis ini disusun untuk mengidentifikasi kesenjangan antara kurikulum yang berjalan dengan standar APTIKOM OBE (Outcome-Based Education) dan ACM/ACEEE Computing Curricula.

\begin{itemize}
\item \textbf{Panduan APTIKOM 2023-2024} mendefinisikan STI sebagai program \textit{hybrid} antara Information Systems (IS) dan Information Technology (IT)
\item \textbf{ACM/ACEEE Computing Curricula 2020} menekankan pentingnya integrasi sistem dan teknologi di tingkat enterprise
\item Analisis ini berfokus pada \textbf{fakta, evidence, dan standar} tanpa overclaim
\end{itemize}

\newpage

# Temuan Utama

## 1. Domain & Profil Lulusan

\begin{table}[h!]
\centering
\begin{tabular}{p{5cm} p{5cm} p{4cm}}
\toprule
\textbf{Aspek} & \textbf{Standar APTIKOM} & \textbf{Kesenjangan} \\
\midrule
Domain Program Studi & STI = Hybrid (IS + IT) & Kurikulum mirip TI dengan tambahan SI \\
Profil Lulusan & Enterprise Architect, Solution Architect, Digital Transformation Lead & Tidak terdefinisi jelas \\
\bottomrule
\end{tabular}
\caption{Pembanding Domain dan Profil Lulusan}
\label{tab:domain}
\end{table}

\textbf{Evidence:} APTIKOM (2023-2024) secara eksplisit mendefinisikan STI sebagai program hybrid [001, 002, 006]. Kurikulum saat ini belum mencerminkan karakteristik ini.

\newpage

## 2. Capaian Pembelajaran Lulusan (CPL)

APTIKOM mendefinisikan \textbf{7 CPL Keterampilan Khusus untuk STI (CPL 11-17)}. Hasil pemetaan:

\begin{longtable}{p{1.5cm} p{6cm} p{3cm} p{3cm}}
\toprule
\textbf{CPL} & \textbf{Deskripsi} & \textbf{Status} & \textbf{Mata Kuliah Pendukung} \\
\midrule
11 & Analisis kebutuhan sistem secara enterprise & ⚠️ Sebagian & Analisis dan Perancangan SI \\
12 & Merancang arsitektur sistem dan teknologi terintegrasi & ❌ Tidak ada & - \\
13 & Mengembangkan dan mengintegrasikan solusi sistem & teknologi & ⚠️ Sebagian & API, Cloud \\
14 & Pengujian dan evaluasi sistem enterprise & ❌ Tidak ada & - \\
15 & Merancang dan mengelola arsitektur enterprise & ❌ Tidak ada & - \\
16 & Keamanan enterprise & ⚠️ Sebagian & Keamanan Jaringan \\
17 & Transformasi digital melalui integrasi sistem & ❌ Tidak ada & - \\
\bottomrule
\caption{Pemetaan CPL Keterampilan Khusus STI}
\label{tab:cpl}
\end{longtable}

\textbf{Kesimpulan:} \textbf{5 dari 7 CPL inti STI tidak terpenuhi}

\newpage

## 3. Konsentrasi/Peminatan

\begin{table}[h!]
\centering
\begin{tabular}{p{5cm} p{5cm} p{4cm}}
\toprule
\textbf{Aspek} & \textbf{Standar APTIKOM} & \textbf{Kesenjangan} \\
\midrule
Konsentrasi & 3 konsentrasi wajib & Tidak ada (100% wajib) \\
Pilihan Mata Kuliah & 24 SKS (20-25% total) & 0 SKS \\
Diferensiasi Lulusan & Enterprise Architecture & DT & Tidak ada \\
\bottomrule
\end{tabular}
\caption{Rekomendasi Konsentrasi APTIKOM}
\label{tab:konsentrasi}
\end{table}

\textbf{3 Konsentrasi yang Direkomendasikan APTIKOM:}

\begin{enumerate}
\item \textbf{Enterprise Systems & Business Analytics} (Domain: IS)
\item \textbf{IT Infrastructure & Cybersecurity} (Domain: IT)
\item \textbf{Enterprise Architecture & Digital Transformation} (Domain: Hybrid - UNGGULAN)
\end{enumerate}

\newpage

## 4. Struktur SKS

\begin{table}[h!]
\centering
\begin{tabular}{p{4cm} p{3cm} p{3cm} p{3cm}}
\toprule
\textbf{Komponen} & \textbf{Saat Ini} & \textbf{Standar APTIKOM} & \textbf{Aksi} \\
\midrule
Wajib Umum & 14 SKS & 14 SKS & ✅ Tidak berubah \\
Wajib Prodi & 120+ SKS & 86 SKS & ⚠️ Kurangi 34 SKS \\
Pilihan Konsentrasi & 0 SKS & 24 SKS & ➕ Tambah 24 SKS \\
MBKM & 0 SKS & 14 SKS & ➕ Tambah 14 SKS \\
Skripsi & 6 SKS & 6 SKS & ✅ Tidak berubah \\
\bottomrule
\end{tabular}
\caption{Perbandingan Struktur SKS}
\label{tab:sks}
\end{table}

\textbf{Evidence:} ACM/ACEEE merekomendasikan \textbf{20-25% SKS untuk peminatan}. Saat ini: 0%.

\newpage

# Rekomendasi Perbaikan

## 1. Tambahkan Mata Kuliah Inti STI

\begin{table}[h!]
\centering
\begin{tabular}{p{2cm} p{5cm} p{2cm} p{2cm}}
\toprule
\textbf{CPL} & \textbf{Mata Kuliah} & \textbf{Semester} & \textbf{SKS} \\
\midrule
12, 15 & Enterprise Architecture (TOGAF) & 5 & 3 \\
13 & System Integration & Middleware & 5 & 3 \\
14 & IT Governance (COBIT/ITIL) & 5 & 3 \\
17 & Digital Transformation Strategy & 6 & 3 \\
\bottomrule
\end{tabular}
\caption{Mata Kuliah Inti yang Perlu Ditambahkan}
\label{tab:new_courses}
\end{table}

\textbf{Justifikasi:}
\begin{itemize}
\item TOGAF = Standar \textit{de facto} untuk arsitektur enterprise (ACM/ACEEE, ISO 42010)
\item COBIT/ITIL = Framework governance TI yang diakui industri
\item Digital Transformation = Keterampilan inti STI menurut APTIKOM [003]
\end{itemize}

\newpage

## 2. Implementasi 3 Konsentrasi

\begin{longtable}{p{4cm} p{2cm} p{5cm} p{3cm}}
\toprule
\textbf{Konsentrasi} & \textbf{Domain} & \textbf{Mata Kuliah Wajib} & \textbf{CPL} \\
\midrule
Enterprise Systems & Business Analytics & IS & ERP, BI, Data Mining & 11, 13, 17 \\
IT Infrastructure & Cybersecurity & IT & Cloud Security, Network Security, ITIL & 13, 14, 16 \\
\textbf{Enterprise Architecture & DT} & \textbf{Hybrid} & \textbf{TOGAF, System Integration, DT Strategy} & \textbf{12, 13, 15, 17} \\
\bottomrule
\caption{Implementasi 3 Konsentrasi}
\label{tab:implementation}
\end{longtable}

\textbf{Justifikasi:} APTIKOM menyarankan 3 konsentrasi ini [003, 006]. Konsentrasi ke-3 = \textbf{pembeda utama STI} dari SI/TI.

\newpage

## 3. Mata Kuliah yang Perlu Dihapus

\begin{table}[h!]
\centering
\begin{tabular}{p{2cm} p{5cm} p{4cm} p{2cm}}
\toprule
\textbf{Kode} & \textbf{Mata Kuliah} & \textbf{Alasan} & \textbf{SKS} \\
\midrule
STI-316 & Multimedia Interaktif & Tidak relevan dengan profil STI & 2 \\
STI-317 & Metode Komputasi dan Numerik & Lebih cocok untuk TI/CS & 2 \\
STI-423 & Game Design dan Gamifikasi Sosial & Tidak ada di kurikulum APTIKOM & 3 \\
STI-638 & Intelligent Signal Processing & Lebih cocok untuk Teknik Elektro & 3 \\
\bottomrule
\end{tabular}
\caption{Mata Kuliah yang Perlu Dihapus}
\label{tab:remove_courses}
\end{table}

\textbf{Justifikasi:} APTIKOM tidak merekomendasikan mata kuliah ini untuk STI [003, 004]. ACM/ACEEE: Mata kuliah ini bukan inti IS/IT.

\newpage

# Ringkasan Perbaikan

\begin{table}[h!]
\centering
\begin{tabular}{p{1cm} p{5cm} p{4cm} p{3cm}}
\toprule
\textbf{No} & \textbf{Aksi} & \textbf{Dasar Evidence} & \textbf{Dampak} \\
\midrule
1 & Tambah 4 MK inti STI & APTIKOM CPL 12-17 [002, 006] & Cover 5 CPL yang hilang \\
2 & Implementasi 3 konsentrasi & APTIKOM [003, 004] & Lulusan memiliki spesialisasi \\
3 & Hapus 4 MK tidak relevan & APTIKOM & ACM CC2020 & Ruang untuk konsentrasi & MBKM \\
4 & Alokasi MBKM 14 SKS & Kebijakan Kemendikbud & APTIKOM & Memenuhi 20% SKS \\
\bottomrule
\end{tabular}
\caption{Ringkasan Aksi Perbaikan}
\label{tab:summary}
\end{table}

\newpage

# Kesimpulan

\begin{itemize}
\item Kurikulum saat ini \textbf{tidak memenuhi standar APTIKOM OBE untuk STI} (5/7 CPL inti hilang)
\item \textbf{Tidak ada konsentrasi} → Tidak ada diferensiasi lulusan
\item \textbf{MBKM tidak terstruktur} → Tidak memenuhi kebijakan nasional
\item Beberapa mata kuliah \textbf{tidak relevan} dengan domain STI
\end{itemize}

\textbf{Solusi minimal:}
\begin{itemize}
\item ✅ Tambah 4 MK inti STI (12 SKS)
\item ✅ Hapus 4 MK tidak relevan (10 SKS)
\item ✅ Implementasi 3 konsentrasi (24 SKS)
\item ✅ Alokasi MBKM (14 SKS)
\end{itemize}

\textbf{Hasil:}
\begin{itemize}
\item Semua CPL tercover
\item Lulusan memiliki spesialisasi
\item Memenuhi standar APTIKOM & ACM/ACEEE
\end{itemize}

\newpage

# Referensi

\begin{itemize}
\item [001] Summary Pemetaan Prodi STI APTIKOM - 01 Agustus 2026
\item [002] Detail Pemetaan CPL dan Profil Lulusan APTIKOM
\item [003] Rekomendasi Konsentrasi STI APTIKOM
\item [004] Kurikulum Lengkap STI 144SKS dan 150SKS
\item [005] Dokumen Komprehensif Kurikulum STI dan Konsentrasi
\item [006] Master Detail Seluruh Respon Diskusi STI APTIKOM
\item ACM/IEEE Computing Curricula 2020 (CC2020)
\item APTIKOM Panduan Kurikulum 2023-2024
\end{itemize}

\newpage

\begin{center}
{\Large\bfseries\color{primary} TERIMA KASIH}\vspace{0.5cm}

{\large\color{accent} Untuk perbaikan kurikulum SISTEKIN yang lebih baik}
\end{center}
