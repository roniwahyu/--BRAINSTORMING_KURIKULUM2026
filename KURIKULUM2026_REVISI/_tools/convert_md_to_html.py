import os
import re
import glob
import html
import markdown
from markdown.extensions.toc import TocExtension

# List of all curriculum documents in sequence
DOC_FILES = [
    ("001_ANALISIS_VMTS_DAN_POSITIONING_STRATEGIS_SISTEKIN.md", "001 — Analisis VMTS & Positioning Strategis"),
    ("002_FORMULASI_3_PEO_DAN_4_PROFIL_LULUSAN_SISTEKIN.md", "002 — Formulasi 3 PEO & 4 Profil Lulusan"),
    ("003_STANDAR_14_CPL_DAN_PEMETAAN_BoK_APTIKOM.md", "003 — Standar 14 CPL & Pemetaan BoK APTIKOM"),
    ("004_MATRIKS_KETERLACAKAN_OBE_VMTS_PEO_PL_CPL_MK.md", "004 — Matriks Keterlacakan OBE VMTS-PEO-PL-CPL-MK"),
    ("005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md", "005 — Struktur Kurikulum 8 Semester & Peminatan"),
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
    ("020_TEMPLATE_BUKU_KURIKULUM_KPT_OBE_APTIKOM.md", "020 — Template Buku Kurikulum KPT-OBE & Analisis Gap"),
    ("021_PANDUAN_KPT2024_DIKTI_FULLTEXT.md", "021 — Panduan KPT 2024 Belmawa Dikti (Teks Lengkap)"),
    ("022_AUDIT_KELENGKAPAN_KOMPONEN_VS_TEMPLATE_KPT_OBE.md", "022 — Audit Kelengkapan Komponen vs Template KPT-OBE"),
    ("023_BUKU_KPT_SISTEKIN_2026_STRUKTUR_KPT2024.md", "023 — 📘 BUKU KPT SISTEKIN 2026 (Struktur 12 Bab KPT 2024)"),
    ("024_MATRIKS_EKIVALENSI_KURIKULUM2025_KE_KURIKULUM2026.md", "024 — Matriks Ekivalensi MK Kurikulum 2025 → 2026"),
    ("025_REKOMENDASI_PENGEMBANGAN_MK_PEMINATAN_DAN_CROSS_TRACK_2027.md", "025 — Rekomendasi Pool MK Peminatan & Cross-Track 2027"),
    ("026_ANALISIS_KRITIS_MK_DIHAPUS_DAN_REKOMENDASI_PENGGANTI.md", "026 — Analisis Kritis MK Dihapus & Rekomendasi Pengganti"),
    ("027_RENCANA_RESTRUKTURISASI_KODE_MK_CORE_STI_KONTINU.md", "027 — Rencana Aksi Restrukturisasi Kode Core STI Kontinu"),
    ("028_DEV_REPORT_DAN_LOG_RESTRUKTURISASI_KODE_CORE_STI.md", "028 — Dev Report & Dev Log Restrukturisasi Kode Core STI"),
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
            alert_html = f'''<div class="custom-alert {cls}">
    <div class="alert-header"><span class="alert-icon">{icon}</span> {label}</div>
    <div class="alert-content">{alert_body}</div>
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
    
    html_text = re.sub(r'<code>([A-Za-z0-9_\-\.]+?)</code', code_repl, html_text)
    
    # Category badges
    html_text = html_text.replace('<td>MKWU</td>', '<td><span class="cat-badge cat-mkwu">MKWU</span></td>')
    html_text = html_text.replace('<td>FSTI</td>', '<td><span class="cat-badge cat-fsti">FSTI</span></td>')
    html_text = html_text.replace('<td>Core STI</td>', '<td><span class="cat-badge cat-sti">Core STI</span></td>')
    html_text = html_text.replace('<td>Peminatan</td>', '<td><span class="cat-badge cat-elektif">Peminatan</span></td>')
    html_text = html_text.replace('<td>Elektif</td>', '<td><span class="cat-badge cat-elektif">Elektif</span></td>')
    
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
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- KaTeX for LaTeX Math -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>

    <!-- Mermaid JS for Flowcharts -->
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>

    <style>
        :root {{
            --bg-primary: #0b0f19;
            --bg-secondary: #111827;
            --bg-card: rgba(17, 24, 39, 0.75);
            --bg-card-hover: rgba(31, 41, 55, 0.85);
            --border-color: rgba(255, 255, 255, 0.1);
            --border-accent: rgba(99, 102, 241, 0.35);
            
            --text-primary: #f9fafb;
            --text-secondary: #9ca3af;
            --text-muted: #6b7280;
            
            --primary: #6366f1;
            --primary-light: #818cf8;
            --secondary: #06b6d4;
            --accent: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
            
            --mkwu-color: #ec4899;
            --fsti-color: #8b5cf6;
            --sti-color: #3b82f6;
            --elektif-color: #10b981;
            
            --font-sans: 'Plus Jakarta Sans', 'Inter', sans-serif;
            --font-code: 'Fira Code', monospace;
            --shadow-glow: 0 0 30px rgba(99, 102, 241, 0.12);
            --radius-lg: 16px;
            --radius-md: 12px;
            --radius-sm: 8px;
        }}

        [data-theme="light"] {{
            --bg-primary: #f8fafc;
            --bg-secondary: #ffffff;
            --bg-card: rgba(255, 255, 255, 0.9);
            --bg-card-hover: #ffffff;
            --border-color: rgba(0, 0, 0, 0.08);
            --border-accent: rgba(99, 102, 241, 0.25);
            
            --text-primary: #0f172a;
            --text-secondary: #475569;
            --text-muted: #94a3b8;
            
            --shadow-glow: 0 10px 30px rgba(99, 102, 241, 0.08);
        }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; }}

        body {{
            font-family: var(--font-sans);
            background-color: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.7;
            padding-bottom: 80px;
            transition: background-color 0.3s ease, color 0.3s ease;
        }}

        .container {{
            max-width: 1280px;
            margin: 0 auto;
            padding: 0 24px;
        }}

        /* Navbar */
        .navbar {{
            position: sticky;
            top: 0;
            z-index: 100;
            background: rgba(11, 15, 25, 0.85);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--border-color);
            padding: 14px 0;
            margin-bottom: 32px;
        }}
        [data-theme="light"] .navbar {{ background: rgba(248, 250, 252, 0.85); }}

        .navbar-content {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 16px;
            flex-wrap: wrap;
        }}

        .brand {{
            display: flex;
            align-items: center;
            gap: 12px;
            text-decoration: none;
        }}
        .brand-logo {{
            width: 40px; height: 40px;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            border-radius: var(--radius-sm);
            display: flex; align-items: center; justify-content: center;
            font-weight: 800; color: white; font-size: 1.1rem;
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
        }}
        .brand-text h1 {{ font-size: 1.05rem; font-weight: 700; color: var(--text-primary); }}
        .brand-text p {{ font-size: 0.75rem; color: var(--text-secondary); }}

        .doc-select {{
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            color: var(--text-primary);
            padding: 8px 14px;
            border-radius: var(--radius-sm);
            font-size: 0.85rem;
            font-weight: 600;
            outline: none;
            cursor: pointer;
            max-width: 380px;
        }}

        .search-box {{
            position: relative;
            min-width: 240px;
        }}
        .search-input {{
            width: 100%;
            padding: 8px 14px 8px 34px;
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-sm);
            color: var(--text-primary);
            font-size: 0.85rem;
            outline: none;
            transition: border-color 0.2s;
        }}
        .search-input:focus {{ border-color: var(--primary); }}
        .search-icon {{ position: absolute; left: 10px; top: 50%; transform: translateY(-50%); font-size: 0.8rem; opacity: 0.6; }}

        .nav-actions {{ display: flex; align-items: center; gap: 10px; }}
        .btn-action {{
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            color: var(--text-primary);
            padding: 8px 14px;
            border-radius: var(--radius-sm);
            cursor: pointer; font-size: 0.85rem; font-weight: 600;
            display: inline-flex; align-items: center; gap: 6px;
            transition: all 0.2s ease;
            text-decoration: none;
        }}
        .btn-action:hover {{ border-color: var(--primary); color: var(--primary-light); transform: translateY(-1px); }}

        /* Hero Header */
        .hero {{
            background: radial-gradient(circle at top right, rgba(99, 102, 241, 0.15), transparent 50%),
                        radial-gradient(circle at bottom left, rgba(6, 182, 212, 0.1), transparent 50%);
            border: 1px solid var(--border-accent);
            border-radius: var(--radius-lg);
            padding: 36px;
            margin-bottom: 36px;
            box-shadow: var(--shadow-glow);
        }}
        .hero-badge-group {{ display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 14px; }}
        .badge {{
            font-size: 0.72rem; font-weight: 700; padding: 4px 12px; border-radius: 20px;
            letter-spacing: 0.03em; text-transform: uppercase;
        }}
        .badge-primary {{ background: rgba(99, 102, 241, 0.2); color: var(--primary-light); border: 1px solid rgba(99, 102, 241, 0.4); }}
        .badge-accent {{ background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); }}
        .badge-warning {{ background: rgba(245, 158, 11, 0.2); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.4); }}

        .hero-title {{
            font-size: 2rem; font-weight: 800; letter-spacing: -0.03em; margin-bottom: 8px;
            background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }}
        [data-theme="light"] .hero-title {{
            background: linear-gradient(135deg, #0f172a 0%, #334155 100%);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }}

        /* Typography & Content */
        .content {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 40px;
            backdrop-filter: blur(12px);
            box-shadow: 0 4px 24px rgba(0,0,0,0.15);
        }}

        .content h1 {{ font-size: 1.8rem; font-weight: 800; margin: 32px 0 16px 0; color: var(--text-primary); border-bottom: 2px solid var(--border-accent); padding-bottom: 10px; }}
        .content h2 {{ font-size: 1.4rem; font-weight: 700; margin: 30px 0 14px 0; color: var(--primary-light); border-bottom: 1px solid var(--border-color); padding-bottom: 8px; }}
        .content h3 {{ font-size: 1.15rem; font-weight: 700; margin: 24px 0 12px 0; color: var(--text-primary); }}
        .content h4 {{ font-size: 1rem; font-weight: 600; margin: 18px 0 8px 0; color: var(--text-secondary); }}

        .content p {{ margin-bottom: 16px; color: var(--text-secondary); font-size: 0.96rem; }}
        .content ul, .content ol {{ margin: 0 0 20px 24px; color: var(--text-secondary); font-size: 0.95rem; }}
        .content li {{ margin-bottom: 6px; }}
        .content blockquote {{
            border-left: 4px solid var(--primary);
            padding: 12px 20px;
            background: rgba(99, 102, 241, 0.06);
            border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
            margin: 20px 0;
            color: var(--text-secondary);
            font-style: italic;
        }}

        /* Tables */
        .table-wrapper {{ overflow-x: auto; margin: 24px 0; border-radius: var(--radius-md); border: 1px solid var(--border-color); }}
        table {{ width: 100%; border-collapse: collapse; text-align: left; font-size: 0.9rem; }}
        th {{
            background: rgba(31, 41, 55, 0.7); color: var(--text-primary);
            font-weight: 700; padding: 12px 16px; border-bottom: 1px solid var(--border-color);
            font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.04em;
        }}
        [data-theme="light"] th {{ background: #f1f5f9; }}
        td {{ padding: 12px 16px; border-bottom: 1px solid var(--border-color); color: var(--text-secondary); }}
        tr:last-child td {{ border-bottom: none; }}
        tr:hover td {{ background: var(--bg-card-hover); color: var(--text-primary); }}

        /* Code Badges */
        .code-tag {{
            font-family: var(--font-code); font-weight: 600; font-size: 0.82rem;
            padding: 2px 8px; border-radius: 4px; background: rgba(99, 102, 241, 0.12);
            color: var(--primary-light); border: 1px solid rgba(99, 102, 241, 0.25);
        }}
        code {{
            font-family: var(--font-code); font-size: 0.85rem; padding: 2px 6px;
            background: rgba(255, 255, 255, 0.06); border-radius: 4px; color: var(--primary-light);
        }}

        .cat-badge {{ font-size: 0.72rem; font-weight: 700; padding: 3px 8px; border-radius: 4px; display: inline-block; }}
        .cat-mkwu {{ background: rgba(236, 72, 153, 0.15); color: #f472b6; border: 1px solid rgba(236, 72, 153, 0.3); }}
        .cat-fsti {{ background: rgba(139, 92, 246, 0.15); color: #c084fc; border: 1px solid rgba(139, 92, 246, 0.3); }}
        .cat-sti  {{ background: rgba(59, 130, 246, 0.15); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.3); }}
        .cat-elektif {{ background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); }}

        /* Custom Alerts */
        .custom-alert {{
            border-left: 4px solid var(--primary);
            background: rgba(17, 24, 39, 0.6);
            border: 1px solid var(--border-color);
            border-left-width: 4px;
            border-radius: var(--radius-md);
            padding: 16px 20px;
            margin: 24px 0;
        }}
        .alert-important {{ border-left-color: var(--primary); background: rgba(99, 102, 241, 0.08); }}
        .alert-note {{ border-left-color: var(--secondary); background: rgba(6, 182, 212, 0.08); }}
        .alert-tip {{ border-left-color: var(--accent); background: rgba(16, 185, 129, 0.08); }}
        .alert-warning {{ border-left-color: var(--warning); background: rgba(245, 158, 11, 0.08); }}
        .alert-caution {{ border-left-color: var(--danger); background: rgba(239, 68, 68, 0.08); }}
        
        .alert-header {{ font-weight: 700; font-size: 0.9rem; margin-bottom: 6px; display: flex; align-items: center; gap: 8px; }}
        .alert-important .alert-header {{ color: var(--primary-light); }}
        .alert-note .alert-header {{ color: var(--secondary); }}
        .alert-tip .alert-header {{ color: var(--accent); }}
        .alert-warning .alert-header {{ color: var(--warning); }}
        .alert-caution .alert-header {{ color: var(--danger); }}
        .alert-content {{ color: var(--text-secondary); font-size: 0.92rem; }}

        /* Mermaid Box */
        .mermaid-card {{
            background: rgba(17, 24, 39, 0.5);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 24px; margin: 24px 0;
            text-align: center; overflow-x: auto;
        }}

        /* Bottom Nav Links */
        .doc-nav {{
            display: flex; justify-content: space-between; align-items: center;
            margin-top: 40px; padding-top: 24px; border-top: 1px solid var(--border-color);
        }}
        .nav-btn {{
            background: var(--bg-secondary); border: 1px solid var(--border-color);
            color: var(--text-primary); padding: 10px 18px; border-radius: var(--radius-sm);
            text-decoration: none; font-weight: 600; font-size: 0.88rem; transition: all 0.2s;
        }}
        .nav-btn:hover {{ border-color: var(--primary); color: var(--primary-light); }}

        /* Footer */
        .footer {{ margin-top: 60px; text-align: center; color: var(--text-muted); font-size: 0.85rem; }}

        @media print {{
            body {{ background: white; color: black; }}
            .navbar, .nav-actions, .doc-nav, .search-box {{ display: none; }}
            .hero, .content {{ border: 1px solid #ccc; box-shadow: none; background: white; padding: 20px; }}
            th {{ background: #eee !important; color: black !important; }}
            td {{ color: black !important; }}
            .code-tag {{ background: #f0f0f0; color: black; border: 1px solid #ccc; }}
        }}
    </style>
</head>
<body>

    <!-- Navbar -->
    <nav class="navbar">
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
                <button class="btn-action" onclick="window.print()">🖨️ Cetak PDF</button>
                <button class="btn-action" id="themeToggle">🌓 Tema</button>
            </div>
        </div>
    </nav>

    <div class="container">
        <!-- Hero Section -->
        <header class="hero">
            <div class="hero-badge-group">
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

            <div class="doc-nav">
                <div>{prev_link}</div>
                <div><a href="index.html" class="nav-btn">🏠 Index Utama</a></div>
                <div>{next_link}</div>
            </div>
        </main>

        <footer class="footer">
            <p><strong>Dokumen Resmi Kurikulum KPT-OBE SISTEKIN 2026</strong></p>
            <p>Tim Pengembang Kurikulum FSTI — Universitas Widyagama Malang © 2026</p>
        </footer>
    </div>

    <script>
        // Mermaid Init
        mermaid.initialize({{
            startOnLoad: true,
            theme: 'dark',
            flowchart: {{ curve: 'basis', useMaxWidth: true }}
        }});

        // Theme Toggle
        const themeToggle = document.getElementById('themeToggle');
        let currentTheme = localStorage.getItem('theme') || 'dark';
        document.documentElement.setAttribute('data-theme', currentTheme);

        themeToggle.addEventListener('click', () => {{
            currentTheme = currentTheme === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', currentTheme);
            localStorage.setItem('theme', currentTheme);
        }});

        // Live Table Search Filter
        const searchInput = document.getElementById('globalTableSearch');
        if (searchInput) {{
            searchInput.addEventListener('input', (e) => {{
                const query = e.target.value.toLowerCase().trim();
                const rows = document.querySelectorAll('table tbody tr');
                rows.forEach(row => {{
                    const text = row.innerText.toLowerCase();
                    if (query === '' || text.includes(query)) {{
                        row.style.display = '';
                    }} else {{
                        row.style.display = 'none';
                    }}
                }});
            }});
        }}
    </script>
</body>
</html>'''
    return html_template

def build_index_html():
    cards_html = []
    for doc_fn, doc_title in DOC_FILES:
        html_fn = doc_fn.replace('.md', '.html')
        doc_code = doc_fn.split('_')[0]
        cards_html.append(f'''
        <div class="card" onclick="window.location.href='{html_fn}'" style="cursor: pointer;">
            <div class="badge badge-primary" style="margin-bottom: 10px; display: inline-block;">{doc_code}</div>
            <h3 style="font-size: 1.05rem; color: var(--primary-light); margin-bottom: 8px;">{doc_title}</h3>
            <p style="font-size: 0.85rem; color: var(--text-secondary);">Buka dokumen interaktif dengan tabel, visualisasi, dan diagram alur.</p>
            <div style="margin-top: 14px; text-align: right;">
                <span style="color: var(--secondary); font-weight: 700; font-size: 0.85rem;">Buka Dokumen →</span>
            </div>
        </div>''')
    cards_str = '\n'.join(cards_html)
    
    index_html = f'''<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PORTAL BUKU KURIKULUM OBE SISTEKIN 2026 | FSTI UWG</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-primary: #0b0f19;
            --bg-card: rgba(17, 24, 39, 0.75);
            --border-color: rgba(255, 255, 255, 0.1);
            --border-accent: rgba(99, 102, 241, 0.35);
            --text-primary: #f9fafb;
            --text-secondary: #9ca3af;
            --primary: #6366f1;
            --primary-light: #818cf8;
            --secondary: #06b6d4;
            --radius-lg: 16px;
            --radius-md: 12px;
            --shadow-glow: 0 0 30px rgba(99, 102, 241, 0.15);
        }}
        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            padding: 40px 20px 80px 20px;
        }}
        .container {{ max-width: 1280px; margin: 0 auto; }}
        .hero {{
            background: radial-gradient(circle at top right, rgba(99, 102, 241, 0.2), transparent 50%);
            border: 1px solid var(--border-accent);
            border-radius: var(--radius-lg);
            padding: 40px; text-align: center; margin-bottom: 40px;
            box-shadow: var(--shadow-glow);
        }}
        .hero h1 {{ font-size: 2.2rem; font-weight: 800; margin-bottom: 12px; background: linear-gradient(135deg, #fff, #cbd5e1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .hero p {{ color: var(--text-secondary); font-size: 1.05rem; max-width: 800px; margin: 0 auto; }}
        .badge {{ background: rgba(99, 102, 241, 0.2); color: var(--primary-light); padding: 4px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; border: 1px solid rgba(99, 102, 241, 0.4); }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; }}
        .card {{
            background: var(--bg-card); border: 1px solid var(--border-color);
            border-radius: var(--radius-md); padding: 24px; transition: all 0.25s ease;
            backdrop-filter: blur(12px);
        }}
        .card:hover {{ border-color: var(--border-accent); transform: translateY(-4px); box-shadow: 0 10px 25px rgba(99, 102, 241, 0.15); }}
    </style>
</head>
<body>
    <div class="container">
        <div class="hero">
            <span class="badge">SINGLE SOURCE OF TRUTH DEFINITIF</span>
            <h1>Buku Kurikulum KPT-OBE SISTEKIN 2026</h1>
            <p>Program Studi Sistem dan Teknologi Informasi (S1) — Fakultas Sains dan Teknologi Informasi (FSTI) Universitas Widyagama Malang</p>
        </div>
        <div class="grid">
            {cards_str}
        </div>
    </div>
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
            'sane_lists',
            'pymdownx.superfences',
            'pymdownx.arithmatex'
        ]
    )
    
    print("Starting Markdown to HTML Conversion for all documents...")
    
    for idx, (filename, title) in enumerate(DOC_FILES):
        filepath = os.path.join(WORKDIR, filename)
        if not os.path.exists(filepath):
            print(f"Skipping missing file: {filename}")
            continue
            
        print(f"Converting [{idx+1}/{len(DOC_FILES)}]: {filename}")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            md_text = f.read()
            
        # Pre-process math arrows
        md_text = md_text.replace(r'$\leftrightarrow$', '↔').replace(r'\leftrightarrow', '↔')
        md_text = md_text.replace(r'$\rightarrow$', '→').replace(r'\rightarrow', '→')
        md_text = md_text.replace(r'$\leftarrow$', '←').replace(r'\leftarrow', '←')
        
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
        out_filepath = os.path.join(WORKDIR, out_filename)
        
        with open(out_filepath, 'w', encoding='utf-8') as f:
            f.write(full_html)
            
        print(f"  -> Generated: {out_filename} ({os.path.getsize(out_filepath)} bytes)")

    index_html = build_index_html()
    index_path = os.path.join(WORKDIR, "index.html")
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_html)
    print(f"\n[SUKSES] Generated Index Portal: index.html ({os.path.getsize(index_path)} bytes)")
    print("Semua file HTML berhasil di-generate dan diselaraskan!")

if __name__ == '__main__':
    convert_all()
