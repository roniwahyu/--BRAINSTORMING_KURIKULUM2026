import os
import re
import glob
import html
import markdown
from markdown.extensions.toc import TocExtension

# List of all curriculum documents in sequence
DOC_FILES = [
    ("000_CHANGELOG_ALIGNMENT_FINAL.md", "000 — Changelog Alignment Final"),
    ("001_ANALISIS_VMTS_DAN_POSITIONING_STRATEGIS_SISTEKIN.md", "001 — Analisis VMTS & Positioning Strategis"),
    ("002_FORMULASI_3_PEO_DAN_4_PROFIL_LULUSAN_SISTEKIN.md", "002 — Formulasi 3 PEO & 4 Profil Lulusan"),
    ("003_STANDAR_14_CPL_DAN_PEMETAAN_BoK_APTIKOM.md", "003 — Standar 14 CPL & Pemetaan BoK APTIKOM"),
    ("004_MATRIKS_KETERLACAKAN_OBE_VMTS_PEO_PL_CPL_MK.md", "004 — Matriks Keterlacakan OBE VMTS-PEO-PL-CPL-MK"),
    ("005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md", "005 — 🏛️ Struktur Kurikulum 8 Semester & Peminatan"),
    ("006_DISTRIBUSI_DAN_PANDUAN_MK_PEMINATAN_MBKM.md", "006 — Distribusi MK Peminatan & Panduan MBKM"),
    ("007_FORMULASI_CPMK_DAN_SUB_CPMK_PORTFOLIO_LENGKAP.md", "007 — Silabus 3-Tabel & CPMK 67 MK Portofolio"),
    ("008_SISTEM_ASESMEN_OBE_FORMULA_CPL_DAN_RUBRIK_MASTER.md", "008 — Sistem Asesmen OBE & Attainment CPL"),
    ("009_LANGKAH2_CPL_FORMAL.md", "009 — Ringkasan Langkah 2: CPL Formal"),
    ("009A_CPL_SIKAP_SISTEKIN.md", "009A — Detail CPL Sikap (S1)"),
    ("009B_CPL_KETERAMPILAN_UMUM_SISTEKIN.md", "009B — Detail CPL Keterampilan Umum (KU1-3)"),
    ("009C_CPL_PENGETAHUAN_SISTEKIN.md", "009C — Detail CPL Pengetahuan (P1-4)"),
    ("009D_CPL_KETERAMPILAN_KHUSUS_SISTEKIN.md", "009D — Detail CPL Keterampilan Khusus (KK1-6)"),
    ("009E_RINGKASAN_CPL_LENGKAP_PEMETAAN_BoK.md", "009E — Master Matriks Kompilasi 14 CPL & BoK"),
    ("009_PEDOMAN_CAPSTONE_PROJECT_DAN_TUGAS_AKHIR_NON_SKRIPSI.md", "009 — Pedoman Capstone & 4 Opsi TA Non-Skripsi"),
    ("010_INSTRUMEN_TRACER_STUDY_DAN_EVALUASI_PEO_PPEPP.md", "010 — Instrumen Tracer Study & Evaluasi PEO"),
    ("011_IMPLEMENTASI_OBE_SISTEKIN2026_TABLES.md", "011 — 14 Sheet Matriks Implementasi OBE"),
    ("012_ANALISIS_KRITIS_JALUR_PONDASI_DAN_TREE_PRASYARAT.md", "012 — Analisis Kritis Jalur Pondasi & Tree View Prasyarat"),
    ("013_REKOMENDASI_SOLUSI_DAN_MITIGASI_KELEMAHAN_KURIKULUM.md", "013 — Rekomendasi Solusi & Mitigasi Kelemahan Kurikulum"),
    ("014_ANALISIS_KRITIS_PEMANGKASAN_SKS_TEORI_SEM4_SEM5.md", "014 — Analisis Kritis Pemangkasan SKS Teori Sem 4 & 5"),
    ("015_SIMULASI_AKSELERASI_KELULUSAN_7_SEMESTER.md", "015 — Panduan & Simulasi Akselerasi 7 Semester (Fast-Track)"),
    ("016_ANALISIS_BoK_APTIKOM_REDUNDANSI_DAN_PIPELINE_AI.md", "016 — Analisis BoK APTIKOM, Audit Redundansi & Pipeline AI"),
    ("017_AUDIT_FORENSIK_ZERO_REDUNDANCY_DAN_ZERO_GAP.md", "017 — Audit Forensik Zero Redundancy & Zero Gap 5 Domain"),
    ("018_PANDUAN_RUBRIK_KLASTER_DAN_MODEL_ASESMEN_OBE_DOSEN.md", "018 — Panduan Master Rubrik Klaster & Model Asesmen Dosen"),
    ("019_AUDIT_KRITIS_KESELARASAN_FOLDER_REVISI_23082026_212923.md", "019 — Audit Kritis Keselarasan Dokumen Kurikulum"),
    ("020_TEMPLATE_BUKU_KURIKULUM_KPT_OBE_APTIKOM.md", "020 — Template Buku Kurikulum KPT-OBE & Analisis Gap"),
    ("021_PANDUAN_KPT2024_DIKTI_FULLTEXT.md", "021 — Panduan KPT 2024 Belmawa Dikti (Teks Lengkap)"),
    ("022_AUDIT_KELENGKAPAN_KOMPONEN_VS_TEMPLATE_KPT_OBE.md", "022 — Audit Kelengkapan Komponen vs Template KPT-OBE"),
    ("023_BUKU_KPT_SISTEKIN_2026_STRUKTUR_KPT2024.md", "023 — 📘 BUKU KPT SISTEKIN 2026 (Struktur 12 Bab KPT 2024)"),
    ("024_MATRIKS_EKIVALENSI_KURIKULUM2025_KE_KURIKULUM2026.md", "024 — Matriks Ekivalensi MK Kurikulum 2025 → 2026"),
    ("025_REKOMENDASI_PENGEMBANGAN_MK_PEMINATAN_DAN_CROSS_TRACK_2027.md", "025 — Rekomendasi Pool MK Peminatan & Cross-Track 2027"),
    ("026_ANALISIS_KRITIS_MK_DIHAPUS_DAN_REKOMENDASI_PENGGANTI.md", "026 — Analisis Kritis MK Dihapus & Rekomendasi Pengganti"),
    ("027_RENCANA_RESTRUKTURISASI_KODE_MK_CORE_STI_KONTINU.md", "027 — Rencana Aksi Restrukturisasi Kode Core STI Kontinu"),
    ("028_DEV_REPORT_DAN_LOG_RESTRUKTURISASI_KODE_CORE_STI.md", "028 — Dev Report & Dev Log Restrukturisasi Kode Core STI"),
    ("029_TABEL_VERIFIKASI_KODE_MK_BARU.md", "029 — Tabel Verifikasi Kode MK Baru (Core STI Sem 1 & 3)"),
    ("030_JUSTIFIKASI_AKADEMIS_DAN_BoK_STA02_COMPUTATIONAL_METHODS_SEBAGAI_MK_PILIHAN.md", "030 — Justifikasi Akademis & Audit BoK STA-601 Komputasi Numerik sebagai MK Pilihan"),
    ("031_PETA_KESELARASAN_KPT2024_STATUS_DOKUMEN.md", "031 — Peta Keselarasan KPT 2024 & Status Dokumen"),
    ("031_RENCANA_PENYUSUNAN_BUKU_KPT_APTIKOM_A-L.md", "031 — Rencana Penyusunan Buku KPT APTIKOM Bab A-L"),
    ("032_MODALITAS_PEMBELAJARAN_KPT2024.md", "032 — Modalitas Pembelajaran KPT 2024"),
    ("033_RUBRIK_HOLISTIK_DAN_SKALA_PERSEPSI.md", "033 — Rubrik Holistik & Skala Persepsi Asesmen"),
    ("034_SEMBILAN_BENTUK_MBKM_DAN_REKOGNISI.md", "034 — Sembilan Bentuk MBKM & Skema Rekognisi SKS"),
    ("035_RESTRUKTURISASI_KODE_MK_PEMINATAN_STA_STB_STC.md", "035 — Restrukturisasi Kode MK Peminatan (STA, STB, STC) Berbasis Semester"),
    ("036_DEV_REPORT_DAN_LOG_RESTRUKTURISASI_KODE_PEMINATAN.md", "036 — Dev Report & Dev Log Restrukturisasi Kode MK Peminatan"),
    ("037_BOUNDARY_OF_TOPICS_DAN_MATRIKS_ANTI_OVERLAP_KURIKULUM.md", "037 — Boundary of Topics & Matriks Anti-Overlap Kurikulum"),
    ("038_RENCANA_KONTEN_LAMPIRAN_BUKU_KPT.md", "038 — Rencana Konten Lampiran Buku KPT SISTEKIN 2026"),
    ("039_LAMPIRAN_SIAP_BUKU_KPT_SISTEKIN_2026.md", "039 — Lampiran Siap Buku KPT SISTEKIN 2026"),
    ("040_LAMPIRAN_RAKIT_BUKU_KPT.md", "040 — Lampiran Rakit Buku KPT SISTEKIN 2026"),
    ("041_LAMPIRAN_BARU_BUKU_KPT.md", "041 — Lampiran Baru Buku KPT SISTEKIN 2026"),
    ("042_LAPORAN_AUDIT_KESELARASAN_KURIKULUM_DAN_BOUNDARY_OF_TOPICS.md", "042 — Laporan Audit Mutu & Keselarasan Kurikulum vs Dokumen 005"),
    ("043_MATRIKS_CPL_CPMK_BoK_DAN_BOUNDARY_GUARDRAILS.md", "043 — Matriks CPL, CPMK, BoK, dan Boundary Guardrails (Core & Peminatan)"),
    ("044_DEV_REPORT_DAN_LOG_PENYUSUNAN_MATRIKS_CPL_CPMK_BoK_GUARDRAILS.md", "044 — Dev Report & Log Penyusunan Matriks CPL, CPMK, BoK, dan Boundary Guardrails"),
    ("045_DRAFT_BUKU_KPT_SISTEKIN_2026_MENGIKUTI_TEMPLATE_DOCX.md", "045 — 📘 Draft Buku KPT SISTEKIN 2026 Sesuai Template Dikti"),
    ("046_RENCANA_SUBCPMK_DAN_16_PERTEMUAN_SWI_13092026_2300.md", "046 — Rencana Sub-CPMK & 16 Pertemuan"),
    ("047_ANALISIS_KURIKULER_METODE_NUMERIK_VS_RISET_OPERASI_VS_BIG_DATA_STA601.md", "047 — Analisis Kurikuler: Metode Numerik vs. Riset Operasi vs. Big Data (STA-601)"),
    ("048_KEPUTUSAN_PENGGANTIAN_STA601_NUMERIK_MENJADI_BIG_DATA_ENGINEERING.md", "048 — Keputusan Penggantian STA-601 Menjadi Big Data Engineering"),
    ("049_LAPORAN_EVALUASI_DAN_REVISI_KURIKULUM_STA601_BIG_DATA_ENGINEERING.md", "049 — Laporan Resmi Evaluasi & Revisi Kurikulum STA-601 Big Data Engineering"),
    ("050_DEV_REPORT_DAN_LOG_PERTUKARAN_STRUKTUR_SEM6_SEM7_DAN_HARMONISASI_KURIKULUM.md", "050 — Dev Report & Log Pertukaran Struktur Sem 6-7 & Harmonisasi"),
    ("051_DEV_REPORT_DAN_LOG_RESTRUKTURISASI_KODE_MK_PASCA_PERTUKARAN_SEM6_SEM7.md", "051 — Dev Report & Log Restrukturisasi Kode MK Pasca Pertukaran Sem 6-7"),
    ("052_ANALISIS_FORMAT_DAN_LAYOUT_TEMPLATE_RPS_OBE.md", "052 — 📑 Analisis Format, Layout & Kamus Tag Template RPS OBE FSTI"),
    ("BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md", "📖 BUKU KURIKULUM OBE SISTEKIN 2026 (FINAL UTUH)")
]

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKDIR = os.path.dirname(SCRIPT_DIR)

def process_alerts(md_text):
    """Convert GitHub style alerts like > [!IMPORTANT] to styled HTML blocks."""
    alert_types = {
        'IMPORTANT': ('alert-important', '⚡', 'IMPORTANT'),
        'NOTE': ('alert-note', 'ℹ️', 'NOTE'),
        'TIP': ('alert-tip', '💡', 'TIP'),
        'WARNING': ('alert-warning', '⚠️', 'WARNING'),
        'CAUTION': ('alert-caution', '🚨', 'CAUTION')
    }
    
    lines = md_text.split('\n')
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        match = re.match(r'^>\s*\[\!(IMPORTANT|NOTE|TIP|WARNING|CAUTION)\](.*)', line)
        if match:
            alert_type = match.group(1)
            first_text = match.group(2).strip()
            cls, icon, label = alert_types[alert_type]
            
            content_lines = []
            if first_text:
                content_lines.append(first_text)
                
            i += 1
            while i < len(lines) and (lines[i].startswith('>') or lines[i].strip() == ''):
                if lines[i].startswith('>'):
                    content_lines.append(re.sub(r'^>\s?', '', lines[i]))
                elif lines[i].strip() == '':
                    if i + 1 < len(lines) and lines[i+1].startswith('>'):
                        content_lines.append('')
                    else:
                        break
                i += 1
                
            alert_body = '\n'.join(content_lines)
            alert_body_html = markdown.markdown(alert_body, extensions=['extra', 'tables'])
            alert_html = f'''<div class="custom-alert {cls}">
    <div class="alert-header"><span class="alert-icon">{icon}</span> {label}</div>
    <div class="alert-content">{alert_body_html}</div>
</div>'''
            new_lines.append(alert_html)
        else:
            new_lines.append(line)
            i += 1
            
    return '\n'.join(new_lines)

def process_ascii_tables(md_text):
    """Convert ASCII box drawing tables into native styled HTML tables."""
    pattern = r'```(?:\n|\r\n)?(┌[^\n]+\n(?:[│├└][^\n]+\n)+)```|(\n┌[^\n]+\n(?:[│├└][^\n]+\n)+)'
    
    def repl(m):
        raw_box = (m.group(1) or m.group(2)).strip()
        lines = [line.strip() for line in raw_box.split('\n') if line.strip()]
        
        if not lines or not lines[0].startswith('┌'):
            return raw_box
            
        row_blocks = []
        current_block = []
        
        for line in lines:
            if line.startswith('┌') or line.startswith('├') or line.startswith('└'):
                if current_block:
                    row_blocks.append(current_block)
                    current_block = []
            else:
                if line.startswith('│') and line.endswith('│'):
                    current_block.append(line)
        if current_block:
            row_blocks.append(current_block)
            
        if not row_blocks:
            return raw_box
            
        parsed_rows = []
        for block in row_blocks:
            cell_lines_per_col = []
            for line in block:
                parts = [p.strip() for p in line.split('│')[1:-1]]
                if not cell_lines_per_col:
                    cell_lines_per_col = [[] for _ in parts]
                for idx, part in enumerate(parts):
                    if idx < len(cell_lines_per_col) and part:
                        cell_lines_per_col[idx].append(part)
            
            row_cells = ['<br>'.join(cell_lines) for cell_lines in cell_lines_per_col]
            if any(row_cells):
                parsed_rows.append(row_cells)
                
        if not parsed_rows:
            return raw_box
            
        title_banner = None
        if len(parsed_rows[0]) == 1:
            title_banner = parsed_rows[0][0]
            parsed_rows = parsed_rows[1:]
            
        if not parsed_rows:
            return f'<div class="table-title-header" style="background: rgba(99, 102, 241, 0.15); padding: 10px 16px; font-weight: 700; color: var(--primary-light); border: 1px solid var(--border-color); border-radius: var(--radius-md); text-align: center; margin: 16px 0;">{html.escape(title_banner)}</div>'
            
        header_row = parsed_rows[0]
        data_rows = parsed_rows[1:]
        
        html_out = ['\n<div class="table-wrapper">']
        if title_banner:
            html_out.append(f'<div class="table-title-header" style="background: rgba(99, 102, 241, 0.15); padding: 10px 16px; font-weight: 700; color: var(--primary-light); border: 1px solid var(--border-color); border-bottom: none; border-radius: var(--radius-md) var(--radius-md) 0 0; text-align: center;">{html.escape(title_banner)}</div>')
            
        html_out.append('<table><thead><tr>')
        for h in header_row:
            html_out.append(f'<th>{html.escape(h)}</th>')
        html_out.append('</tr></thead><tbody>')
        
        for r in data_rows:
            html_out.append('<tr>')
            for c in r:
                formatted_c = html.escape(c).replace('&lt;br&gt;', '<br>').replace('&amp;', '&')
                html_out.append(f'<td>{formatted_c}</td>')
            html_out.append('</tr>')
            
        html_out.append('</tbody></table></div>\n')
        return '\n'.join(html_out)
        
    return re.sub(pattern, repl, md_text, flags=re.DOTALL)

def process_mermaid_blocks(md_text):
    """Convert ```mermaid blocks to <div class="mermaid">."""
    pattern = r'```mermaid\s*\n(.*?)```'
    def repl(m):
        code = html.escape(m.group(1).strip())
        return f'\n<div class="mermaid-card"><div class="mermaid">\n{code}\n</div></div>\n'
    return re.sub(pattern, repl, md_text, flags=re.DOTALL)

def post_process_html(html_text):
    """Enhance generated HTML with badges, tags, and formatting."""
    def code_repl(m):
        code = m.group(1)
        if re.match(r'^(FST|STI|MKU|STA|STB|STC)-\d{3}$', code) or re.match(r'^(P\d|PL-\d|PEO-\d|CPL-\w+|CPMK-\d+)$', code):
            return f'<span class="code-tag">{code}</span>'
        return f'<code>{code}</code>'
    
    # Fix regex bug (must match full closing code tag)
    html_text = re.sub(r'<code>([A-Za-z0-9_\-\.]+?)</code>', code_repl, html_text)
    
    # Category badges (matches whether centered or styled)
    cat_map = {
        'MKWU': 'cat-mkwu',
        'FSTI': 'cat-fsti',
        'Core STI': 'cat-sti',
        'Peminatan': 'cat-elektif',
        'Elektif': 'cat-elektif'
    }
    def cat_repl(m):
        attr = m.group(1)
        val = m.group(2).strip()
        cls = cat_map.get(val, 'cat-sti')
        return f'<td{attr}><span class="cat-badge {cls}">{val}</span></td>'
    html_text = re.sub(r'<td([^>]*)>\s*(MKWU|FSTI|Core STI|Peminatan|Elektif)\s*</td>', cat_repl, html_text)
    
    # Course type badges (matches whether centered or styled)
    type_map = {
        'Teori': 'badge-type-teori',
        '+P': 'badge-type-praktikum',
        'Praktik': 'badge-type-praktikum',
        'Proyek': 'badge-type-proyek',
        'Magang': 'badge-type-magang',
        'Seminar': 'badge-type-proyek',
        'Mandiri': 'badge-type-mandiri'
    }
    def type_repl(m):
        attr = m.group(1)
        val = m.group(2).strip()
        cls = type_map.get(val, 'badge-type-teori')
        label = '+P (Praktikum)' if val == '+P' else val
        return f'<td{attr}><span class="badge-type {cls}">{label}</span></td>'
    html_text = re.sub(r'<td([^>]*)>\s*(Teori|\+P|Praktik|Proyek|Magang|Seminar|Mandiri)\s*</td>', type_repl, html_text)

    return html_text

def build_full_html(filename, title, content_html, prev_doc, next_doc):
    nav_options = []
    for doc_fn, doc_title in DOC_FILES:
        html_fn = doc_fn.replace('.md', '.html')
        selected = 'selected' if doc_fn == filename else ''
        nav_options.append(f'<option value="{html_fn}" {selected}>{doc_title}</option>')
    nav_options_html = '\n'.join(nav_options)
    
    prev_link = f'<a href="{prev_doc.replace(".md", ".html")}" class="nav-btn">← Sebelumnya</a>' if prev_doc else ''
    next_link = f'<a href="{next_doc.replace(".md", ".html")}" class="nav-btn">Selanjutnya →</a>' if next_doc else ''
    
    search_bar_html = '''
    <div class="search-box">
        <span class="search-icon">🔍</span>
        <input type="text" id="globalTableSearch" class="search-input" placeholder="Cari dalam dokumen (kode, MK, istilah, tabel)...">
    </div>
    '''
    
    html_template = f'''<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Kurikulum OBE SISTEKIN 2026</title>
    <meta name="description" content="Dokumen Resmi Kurikulum OBE 2026 Program Studi Sistem dan Teknologi Informasi (S1) FSTI UWG Malang.">
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700;800&family=Merriweather:ital,wght@0,300;0,400;0,700;1,300;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- KaTeX for LaTeX Math (Enhanced with inline single dollar delimiters) -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body, {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '$', right: '$', display: false}}]}});"></script>

    <!-- Mermaid JS for Flowcharts -->
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>

    <!-- Master External Modular Stylesheet (Zero-Token Redundancy) -->
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>

    <!-- Navbar -->
    <nav class="navbar no-print">
        <div class="container navbar-content">
            <a href="index.html" class="brand">
                <div class="brand-logo">STI</div>
                <div class="brand-text">
                    <h1>SISTEKIN — FSTI UWG</h1>
                    <p>Buku Kurikulum OBE 2026</p>
                </div>
            </a>
            
            <select class="doc-select" onchange="window.location.href=this.value">
                {nav_options_html}
            </select>

            {search_bar_html}

            <div class="nav-actions">
                <a href="index.html" class="btn-action">🏠 Portal Dokumen</a>
                <button class="btn-action btn-print" onclick="window.print()">🖨️ Cetak PDF</button>
                <button class="btn-action" id="themeToggle">🌓 Tema</button>
            </div>
        </div>
    </nav>

    <div class="container">
        <!-- Print Official Header (Visible ONLY on print) -->
        <header class="print-header">
            <h2>Universitas Widyagama Malang — Fakultas Sains dan Teknologi Informasi</h2>
            <h3>Program Studi Sistem dan Teknologi Informasi (S1)</h3>
            <p>Dokumen Resmi Kurikulum OBE 2026 • Sesuai Permendikbudristek No. 53/2023 & Standar APTIKOM</p>
        </header>

        <!-- Reader Toolbar (Interactive UI, Layout, Typography, and Export Controls) -->
        <div class="reader-toolbar no-print">
            <div class="reader-toolbar-left">
                <div class="reader-toolbar-group">
                    <span class="reader-tool-label">📑 Bagian:</span>
                    <select id="quickJumpSelect" class="quick-jump-select">
                        <option value="">Lompat ke bagian...</option>
                    </select>
                </div>
                <div class="reader-toolbar-group">
                    <span class="reader-tool-label">↔️ Lebar:</span>
                    <button type="button" id="btnWidthNarrow" class="reader-tool-btn" title="Mode Baca Nyaman (860px)">📖 Baca</button>
                    <button type="button" id="btnWidthNormal" class="reader-tool-btn active" title="Mode Standar (1240px)">📄 Standar</button>
                    <button type="button" id="btnWidthWide" class="reader-tool-btn" title="Mode Lebar Penuh (Tabel & Matriks)">↔️ Lebar Penuh</button>
                </div>
            </div>
            <div class="reader-toolbar-right">
                <div class="reader-toolbar-group">
                    <span class="reader-tool-label">🔠 Font:</span>
                    <button type="button" id="btnFontMinus" class="reader-tool-btn" title="Kecilkan Font">A-</button>
                    <button type="button" id="btnFontReset" class="reader-tool-btn active" title="Ukuran Font Standar">A</button>
                    <button type="button" id="btnFontPlus" class="reader-tool-btn" title="Perbesar Font">A+</button>
                    <button type="button" id="btnFontToggle" class="reader-tool-btn" title="Ganti Tipografi (Modern Sans / Academic Serif)">🔤 Sans</button>
                </div>
                <div class="reader-toolbar-group">
                    <span class="reader-tool-label">🌓 Tema:</span>
                    <button type="button" id="themeBtnLight" class="reader-tool-btn" title="Mode Terang (Eksekutif A4-Ready)">☀️ Terang</button>
                    <button type="button" id="themeBtnSepia" class="reader-tool-btn" title="Mode Sepia (Kenyamanan Mata Buku)">📖 Sepia</button>
                    <button type="button" id="themeBtnDark" class="reader-tool-btn" title="Mode Gelap">🌙 Gelap</button>
                </div>
                <div class="reader-toolbar-group">
                    <span class="reader-tool-label">📤 Ekspor:</span>
                    <button type="button" id="btnCopyDocument" class="reader-tool-btn btn-export-doc" title="Salin seluruh isi dokumen ke Clipboard berformat Word-ready">📋 Salin ke Word</button>
                    <button type="button" class="btn-action btn-print" onclick="window.print()" title="Cetak atau Simpan sebagai PDF A4">🖨️ Cetak / PDF</button>
                </div>
            </div>
        </div>

        <!-- Hero Section -->
        <header class="hero">
            <div class="hero-badge-group no-print">
                <span class="badge badge-primary">Kurikulum OBE 2026</span>
                <span class="badge badge-accent">Permendikbudristek 53/2023</span>
                <span class="badge badge-warning">FSTI UWG Malang</span>
            </div>
            <h1 class="hero-title">{title}</h1>
            <p style="color: var(--text-secondary); font-size: 0.95rem;">Dokumen Kurikulum OBE Definitif Program Studi Sistem dan Teknologi Informasi (S1)</p>
        </header>

        <!-- Main Content -->
        <main class="content">
            {content_html}

            <div class="doc-nav no-print">
                <div>{prev_link}</div>
                <div><a href="index.html" class="nav-btn">🏠 Index Utama</a></div>
                <div>{next_link}</div>
            </div>
        </main>

        <footer class="footer no-print">
            <p><strong>Dokumen Resmi Kurikulum KPT-OBE SISTEKIN 2026</strong></p>
            <p>Tim Pengembang Kurikulum FSTI — Universitas Widyagama Malang © 2026</p>
        </footer>

        <!-- Print Footer Note -->
        <div class="print-footer-note">
            Buku Kurikulum OBE 2026 Program Studi Sistem dan Teknologi Informasi (S1) — FSTI Universitas Widyagama Malang
        </div>
    </div>

    <!-- Master External Modular Script -->
    <script defer src="assets/js/app.js"></script>
</body>
</html>'''
    return html_template

def build_index_html():
    cards_html = []
    for doc_fn, doc_title in DOC_FILES:
        html_fn = doc_fn.replace('.md', '.html')
        doc_code = doc_fn.split('_')[0]
        cards_html.append(f'''
        <div class="portal-card" onclick="window.location.href='{html_fn}'">
            <div class="badge badge-primary" style="margin-bottom: 10px; display: inline-block;">{doc_code}</div>
            <h3>{doc_title}</h3>
            <p>Buka dokumen kurikulum interaktif lengkap dengan tabel, visualisasi, dan diagram alur.</p>
            <div class="portal-card-footer">
                <span class="portal-card-link">Buka Dokumen →</span>
            </div>
        </div>''')
    cards_str = '\n'.join(cards_html)
    
    index_html = f'''<!DOCTYPE html>
<html lang="id" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PORTAL BUKU KURIKULUM OBE SISTEKIN 2026 | FSTI UWG</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <div class="container">
        <header class="navbar">
            <div class="nav-brand" style="display: flex; align-items: center; gap: 10px;">
                <span class="nav-brand-logo" style="font-size: 1.5rem;">🎓</span>
                <span class="nav-brand-text" style="font-weight: 800; font-size: 1.1rem; color: var(--text-primary);">SISTEKIN 2026 PORTAL</span>
            </div>
            <div class="nav-actions">
                <button type="button" class="btn-action btn-print" onclick="window.print()">🖨️ Cetak</button>
                <button type="button" class="theme-toggle-btn btn-action" id="themeToggle" title="Ganti Tema" aria-label="Ganti Tema">
                    🌓 Mode Tema
                </button>
            </div>
        </header>

        <section class="hero" style="text-align: center;">
            <div class="hero-badge-group" style="justify-content: center;">
                <span class="badge badge-primary">SINGLE SOURCE OF TRUTH DEFINITIF</span>
                <span class="badge badge-accent">AKREDITASI & LAM INFOKOM READY</span>
            </div>
            <h1 class="hero-title" style="margin-bottom: 12px;">Buku Kurikulum KPT-OBE SISTEKIN 2026</h1>
            <p class="hero-subtitle" style="margin: 0 auto 24px auto; color: var(--text-secondary);">Program Studi Sistem dan Teknologi Informasi (S1) — Fakultas Sains dan Teknologi Informasi (FSTI) Universitas Widyagama Malang</p>
            
            <div class="search-box" style="max-width: 520px; margin: 0 auto;">
                <span class="search-icon">🔍</span>
                <input type="text" id="portalSearchInput" class="search-input" placeholder="Cari dokumen kurikulum (kode, judul, kata kunci)...">
            </div>
        </section>

        <main class="portal-grid">
            {cards_str}
        </main>

        <footer class="footer">
            <p><strong>Dokumen Resmi Kurikulum KPT-OBE SISTEKIN 2026</strong></p>
            <p>Tim Pengembang Kurikulum FSTI — Universitas Widyagama Malang © 2026</p>
        </footer>
    </div>

    <!-- Master External Modular Script -->
    <script defer src="assets/js/app.js"></script>
</body>
</html>'''
    return index_html

def convert_all():
    md = markdown.Markdown(
        extensions=[
            'extra',
            'tables',
            'fenced_code',
            'toc',
            'sane_lists'
        ]
    )
    
    HTML_DIR = os.path.join(WORKDIR, "HTML")
    os.makedirs(HTML_DIR, exist_ok=True)

    print(f"Starting Markdown to HTML Conversion for all documents into {HTML_DIR}...")
    
    for idx, (filename, title) in enumerate(DOC_FILES):
        filepath = os.path.join(WORKDIR, filename)
        if not os.path.exists(filepath):
            print(f"Skipping missing file: {filename}")
            continue
            
        print(f"Converting [{idx+1}/{len(DOC_FILES)}]: {filename}")
        
        if filename == "045_DRAFT_BUKU_KPT_SISTEKIN_2026_MENGIKUTI_TEMPLATE_DOCX.md":
            import build_045_template_master_html
            build_045_template_master_html.build_045_html()
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            md_text = f.read()
            
        # Pre-process math arrows & inequalities cleanly
        md_text = md_text.replace(r'$\leftrightarrow$', '↔').replace(r'\leftrightarrow', '↔')
        md_text = md_text.replace(r'$\rightarrow$', '→').replace(r'\rightarrow', '→')
        md_text = md_text.replace(r'$\leftarrow$', '←').replace(r'\leftarrow', '←')
        md_text = re.sub(r'\$\\ge\s*([0-9]+)(?:\\text\{\s*SKS\})?\$', r'≥ \1 SKS', md_text)
        md_text = re.sub(r'\$\\le\s*([0-9]+)(?:\\text\{\s*SKS\})?\$', r'≤ \1 SKS', md_text)
        md_text = md_text.replace(r'$\ge$', '≥').replace(r'$\le$', '≤')
        md_text = md_text.replace(r'\ge', '≥').replace(r'\le', '≤')
        
        md_text = process_alerts(md_text)
        md_text = process_mermaid_blocks(md_text)
        md_text = process_ascii_tables(md_text)
        
        md.reset()
        content_html = md.convert(md_text)
        
        content_html = re.sub(r'<table>', '<div class="table-wrapper"><table>', content_html)
        content_html = re.sub(r'</table>', '</table></div>', content_html)
        content_html = post_process_html(content_html)
        
        prev_doc = DOC_FILES[idx-1][0] if idx > 0 else None
        next_doc = DOC_FILES[idx+1][0] if idx < len(DOC_FILES)-1 else None
        
        full_html = build_full_html(filename, title, content_html, prev_doc, next_doc)
        
        out_filename = filename.replace('.md', '.html')
        out_filepath = os.path.join(HTML_DIR, out_filename)
        
        with open(out_filepath, 'w', encoding='utf-8') as f:
            f.write(full_html)
            
        print(f"  -> Generated: {out_filename} ({os.path.getsize(out_filepath):,} bytes)")

    index_html = build_index_html()
    index_path = os.path.join(HTML_DIR, "index.html")
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_html)
    print(f"\n[SUKSES] Generated Index Portal: HTML/index.html ({os.path.getsize(index_path):,} bytes)")

    # Also create root index.html redirect to HTML/index.html for convenience
    root_index_path = os.path.join(WORKDIR, "index.html")
    root_redirect = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=HTML/index.html">
    <title>Mengarahkan ke Portal Kurikulum OBE SISTEKIN 2026</title>
</head>
<body>
    <p>Mengarahkan ke <a href="HTML/index.html">Portal Kurikulum OBE SISTEKIN 2026</a>...</p>
</body>
</html>"""
    with open(root_index_path, 'w', encoding='utf-8') as f:
        f.write(root_redirect)

    print("Semua file HTML berhasil di-generate dan diselaraskan!")

if __name__ == '__main__':
    convert_all()

