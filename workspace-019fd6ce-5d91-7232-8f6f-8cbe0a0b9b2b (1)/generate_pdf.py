#!/usr/bin/env python3
"""
Generate clean, sleek, elegant PDF ebook for STI Curriculum Analysis
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, 
    Table, TableStyle, Image
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ========== CONFIGURATION ==========
PAGESIZE = A4
MARGIN = 25 * mm

# Colors
PRIMARY = colors.HexColor('#1971C2')
SECONDARY = colors.HexColor('#F0F5FA')
ACCENT = colors.HexColor('#009688')
LIGHT_GRAY = colors.HexColor('#F8F9FA')
MEDIUM_GRAY = colors.HexColor('#CED4DA')
DARK_GRAY = colors.HexColor('#6C757D')
WHITE = colors.white
BLACK = colors.black

# ========== STYLES ==========
def create_styles():
    styles = getSampleStyleSheet()
    
    # Override existing styles
    styles['Title'].fontSize = 24
    styles['Title'].leading = 28
    styles['Title'].alignment = TA_CENTER
    styles['Title'].spaceAfter = 20
    styles['Title'].textColor = PRIMARY
    styles['Title'].fontName = 'Helvetica-Bold'
    
    styles['Heading1'].fontSize = 18
    styles['Heading1'].leading = 22
    styles['Heading1'].spaceBefore = 20
    styles['Heading1'].spaceAfter = 12
    styles['Heading1'].textColor = PRIMARY
    styles['Heading1'].fontName = 'Helvetica-Bold'
    
    styles['Heading2'].fontSize = 14
    styles['Heading2'].leading = 18
    styles['Heading2'].spaceBefore = 15
    styles['Heading2'].spaceAfter = 8
    styles['Heading2'].textColor = PRIMARY
    styles['Heading2'].fontName = 'Helvetica-Bold'
    
    styles['Heading3'].fontSize = 12
    styles['Heading3'].leading = 16
    styles['Heading3'].spaceBefore = 10
    styles['Heading3'].spaceAfter = 6
    styles['Heading3'].textColor = ACCENT
    styles['Heading3'].fontName = 'Helvetica-Bold'
    
    styles['Normal'].fontSize = 11
    styles['Normal'].leading = 15
    styles['Normal'].spaceAfter = 6
    styles['Normal'].textColor = BLACK
    styles['Normal'].fontName = 'Helvetica'
    
    # Custom styles
    styles.add(ParagraphStyle(
        name='Subtitle',
        parent=styles['Normal'],
        fontSize=16,
        leading=20,
        alignment=TA_CENTER,
        spaceAfter=30,
        textColor=DARK_GRAY,
        fontName='Helvetica'
    ))
    
    styles.add(ParagraphStyle(
        name='Caption',
        parent=styles['Normal'],
        fontSize=9,
        leading=11,
        spaceAfter=4,
        textColor=DARK_GRAY,
        fontName='Helvetica'
    ))
    
    styles.add(ParagraphStyle(
        name='ListItem',
        parent=styles['Normal'],
        fontSize=11,
        leading=14,
        spaceAfter=2,
        textColor=BLACK,
        fontName='Helvetica',
        leftIndent=20
    ))
    
    styles.add(ParagraphStyle(
        name='Quote',
        parent=styles['Normal'],
        fontSize=12,
        leading=16,
        spaceBefore=10,
        spaceAfter=10,
        textColor=ACCENT,
        fontName='Helvetica',
        leftIndent=20,
        rightIndent=20
    ))
    
    return styles


# ========== CONTENT GENERATORS ==========
def create_cover(story, styles):
    """Create cover page"""
    story.append(Spacer(1, 50*mm))
    
    # Title
    story.append(Paragraph("ANALISIS KURIKULUM", styles['Title']))
    story.append(Paragraph("SISTEKIN", styles['Title']))
    
    # Subtitle
    story.append(Spacer(1, 10*mm))
    story.append(Paragraph("Berdasar Standar APTIKOM OBE & ACM/ACEEE", styles['Subtitle']))
    
    # Author
    story.append(Spacer(1, 30*mm))
    story.append(Paragraph("Oleh:", styles['Normal']))
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph("Profesor Ahli dengan 25+ Tahun Pengalaman", styles['Normal']))
    story.append(Paragraph("Asesor LAM INFOKOM & APTIKOM Aktif", styles['Normal']))
    
    # Date
    story.append(Spacer(1, 15*mm))
    story.append(Paragraph("Tanggal: 4 Agustus 2026", styles['Caption']))
    
    # Bottom
    story.append(Spacer(1, 40*mm))
    story.append(Paragraph("PROGRAM STUDI SISTEM DAN TEKNOLOGI INFORMASI", styles['Heading2']))
    
    story.append(PageBreak())


def create_toc(story, styles):
    """Create table of contents placeholder"""
    story.append(Paragraph("DAFTAR ISI", styles['Heading1']))
    story.append(Spacer(1, 10*mm))
    
    toc_items = [
        ("Pendahuluan", "1"),
        ("Temuan Utama", "3"),
        ("&nbsp;&nbsp;&nbsp;Domain dan Profil Lulusan", "3"),
        ("&nbsp;&nbsp;&nbsp;Capaian Pembelajaran Lulusan (CPL)", "4"),
        ("&nbsp;&nbsp;&nbsp;Konsentrasi/Peminatan", "5"),
        ("&nbsp;&nbsp;&nbsp;Struktur SKS", "6"),
        ("Rekomendasi Perbaikan", "7"),
        ("&nbsp;&nbsp;&nbsp;Tambahkan Mata Kuliah Inti STI", "7"),
        ("&nbsp;&nbsp;&nbsp;Implementasi 3 Konsentrasi", "8"),
        ("&nbsp;&nbsp;&nbsp;Mata Kuliah yang Perlu Dihapus", "9"),
        ("Ringkasan Perbaikan", "10"),
        ("Kesimpulan", "11"),
        ("Referensi", "12")
    ]
    
    for text, page in toc_items:
        story.append(Paragraph(f"{text} <dotleader> {page}", styles['Normal']))
        story.append(Spacer(1, 3*mm))
    
    story.append(PageBreak())


def create_chapter_title(story, styles, title, subtitle=None):
    """Create chapter title"""
    story.append(Paragraph(title, styles['Heading1']))
    if subtitle:
        story.append(Paragraph(subtitle, styles['Heading2']))
    story.append(Spacer(1, 5*mm))


def create_table(story, styles, data, colWidths=None):
    """Create a styled table"""
    table = Table(data, colWidths=colWidths)
    
    # Style
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), SECONDARY),
        ('TEXTCOLOR', (0, 1), (-1, -1), BLACK),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, MEDIUM_GRAY),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    
    story.append(table)
    story.append(Spacer(1, 8*mm))


def create_bulleted_list(story, styles, items):
    """Create a bulleted list"""
    for item in items:
        story.append(Paragraph(f"• {item}", styles['ListItem']))
    story.append(Spacer(1, 5*mm))


def create_numbered_list(story, styles, items):
    """Create a numbered list"""
    for i, item in enumerate(items, 1):
        story.append(Paragraph(f"{i}. {item}", styles['ListItem']))
    story.append(Spacer(1, 5*mm))


def create_quote(story, styles, text, author=None):
    """Create a quote block"""
    story.append(Paragraph(text, styles['Quote']))
    if author:
        story.append(Paragraph(f"— {author}", styles['Caption']))
    story.append(Spacer(1, 8*mm))


# ========== MAIN DOCUMENT ==========
def generate_pdf():
    # Create document
    doc = SimpleDocTemplate(
        "/home/user/ebook_sti_analysis.pdf",
        pagesize=PAGESIZE,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN
    )
    
    # Create styles
    styles = create_styles()
    
    # Story list
    story = []
    
    # Cover
    create_cover(story, styles)
    
    # TOC
    create_toc(story, styles)
    
    # ===== CHAPTER 1: PENDAHULUAN =====
    create_chapter_title(story, styles, "Pendahuluan")
    story.append(Paragraph(
        "Program Studi Sistem dan Teknologi Informasi (SISTEKIN) saat ini menghadapi tantangan "
        "dalam memenuhi standar nasional dan internasional. Analisis ini disusun untuk "
        "mengidentifikasi kesenjangan antara kurikulum yang berjalan dengan standar APTIKOM OBE "
        "(Outcome-Based Education) dan ACM/ACEEE Computing Curricula.",
        styles['Normal']
    ))
    story.append(Spacer(1, 5*mm))
    create_bulleted_list(story, styles, [
        "Panduan APTIKOM 2023-2024 mendefinisikan STI sebagai program hybrid antara Information Systems (IS) dan Information Technology (IT)",
        "ACM/ACEEE Computing Curricula 2020 menekankan pentingnya integrasi sistem dan teknologi di tingkat enterprise",
        "Analisis ini berfokus pada fakta, evidence, dan standar tanpa overclaim"
    ])
    story.append(PageBreak())
    
    # ===== CHAPTER 2: TEMUAN UTAMA =====
    create_chapter_title(story, styles, "Temuan Utama")
    
    # Section 2.1: Domain & Profil Lulusan
    story.append(Paragraph("Domain dan Profil Lulusan", styles['Heading2']))
    story.append(Spacer(1, 5*mm))
    
    domain_data = [
        ['Aspek', 'Standar APTIKOM', 'Kesenjangan'],
        ['Domain Program Studi', 'STI = Hybrid (IS + IT)', 'Kurikulum mirip TI dengan tambahan SI'],
        ['Profil Lulusan', 'Enterprise Architect, Solution Architect, Digital Transformation Lead', 'Tidak terdefinisi jelas']
    ]
    create_table(story, styles, domain_data, colWidths=[55*mm, 70*mm, 55*mm])
    
    story.append(Paragraph(
        "Evidence: APTIKOM (2023-2024) secara eksplisit mendefinisikan STI sebagai program hybrid [001, 002, 006]. "
        "Kurikulum saat ini belum mencerminkan karakteristik ini.",
        styles['Normal']
    ))
    story.append(PageBreak())
    
    # Section 2.2: CPL
    story.append(Paragraph("Capaian Pembelajaran Lulusan (CPL)", styles['Heading2']))
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph(
        "APTIKOM mendefinisikan 7 CPL Keterampilan Khusus untuk STI (CPL 11-17). Hasil pemetaan:",
        styles['Normal']
    ))
    story.append(Spacer(1, 5*mm))
    
    cpl_data = [
        ['CPL', 'Deskripsi', 'Status', 'Mata Kuliah'],
        ['11', 'Analisis kebutuhan sistem secara enterprise', 'Sebagian', 'Analisis dan Perancangan SI'],
        ['12', 'Merancang arsitektur sistem dan teknologi terintegrasi', 'Tidak ada', '-'],
        ['13', 'Mengembangkan dan mengintegrasikan solusi sistem & teknologi', 'Sebagian', 'API, Cloud'],
        ['14', 'Pengujian dan evaluasi sistem enterprise', 'Tidak ada', '-'],
        ['15', 'Merancang dan mengelola arsitektur enterprise', 'Tidak ada', '-'],
        ['16', 'Keamanan enterprise', 'Sebagian', 'Keamanan Jaringan'],
        ['17', 'Transformasi digital melalui integrasi sistem', 'Tidak ada', '-']
    ]
    create_table(story, styles, cpl_data, colWidths=[20*mm, 70*mm, 30*mm, 50*mm])
    
    story.append(Paragraph("Kesimpulan: 5 dari 7 CPL inti STI tidak terpenuhi", styles['Heading3']))
    story.append(PageBreak())
    
    # Section 2.3: Konsentrasi
    story.append(Paragraph("Konsentrasi/Peminatan", styles['Heading2']))
    story.append(Spacer(1, 5*mm))
    
    konsentrasi_data = [
        ['Aspek', 'Standar APTIKOM', 'Kesenjangan'],
        ['Konsentrasi', '3 konsentrasi wajib', 'Tidak ada (100% wajib)'],
        ['Pilihan Mata Kuliah', '24 SKS (20-25% total)', '0 SKS'],
        ['Diferensiasi Lulusan', 'Enterprise Architecture & DT', 'Tidak ada']
    ]
    create_table(story, styles, konsentrasi_data, colWidths=[50*mm, 60*mm, 70*mm])
    
    story.append(Paragraph("3 Konsentrasi yang Direkomendasikan APTIKOM:", styles['Heading3']))
    story.append(Spacer(1, 5*mm))
    create_numbered_list(story, styles, [
        "Enterprise Systems & Business Analytics (Domain: IS)",
        "IT Infrastructure & Cybersecurity (Domain: IT)",
        "Enterprise Architecture & Digital Transformation (Domain: Hybrid - UNGGULAN)"
    ])
    story.append(PageBreak())
    
    # Section 2.4: Struktur SKS
    story.append(Paragraph("Struktur SKS", styles['Heading2']))
    story.append(Spacer(1, 5*mm))
    
    sks_data = [
        ['Komponen', 'Saat Ini', 'Standar APTIKOM', 'Aksi'],
        ['Wajib Umum', '14 SKS', '14 SKS', 'Tidak berubah'],
        ['Wajib Prodi', '120+ SKS', '86 SKS', 'Kurangi 34 SKS'],
        ['Pilihan Konsentrasi', '0 SKS', '24 SKS', 'Tambah 24 SKS'],
        ['MBKM', '0 SKS', '14 SKS', 'Tambah 14 SKS'],
        ['Skripsi', '6 SKS', '6 SKS', 'Tidak berubah']
    ]
    create_table(story, styles, sks_data, colWidths=[45*mm, 30*mm, 30*mm, 55*mm])
    
    story.append(Paragraph(
        "Evidence: ACM/ACEEE merekomendasikan 20-25% SKS untuk peminatan. Saat ini: 0%.",
        styles['Normal']
    ))
    story.append(PageBreak())
    
    # ===== CHAPTER 3: REKOMENDASI =====
    create_chapter_title(story, styles, "Rekomendasi Perbaikan")
    
    # Section 3.1: Tambah MK Inti
    story.append(Paragraph("Tambahkan Mata Kuliah Inti STI", styles['Heading2']))
    story.append(Spacer(1, 5*mm))
    
    new_courses_data = [
        ['CPL', 'Mata Kuliah', 'Semester', 'SKS'],
        ['12, 15', 'Enterprise Architecture (TOGAF)', '5', '3'],
        ['13', 'System Integration & Middleware', '5', '3'],
        ['14', 'IT Governance (COBIT/ITIL)', '5', '3'],
        ['17', 'Digital Transformation Strategy', '6', '3']
    ]
    create_table(story, styles, new_courses_data, colWidths=[25*mm, 70*mm, 25*mm, 20*mm])
    
    story.append(Paragraph("Justifikasi:", styles['Heading3']))
    create_bulleted_list(story, styles, [
        "TOGAF = Standar de facto untuk arsitektur enterprise (ACM/ACEEE, ISO 42010)",
        "COBIT/ITIL = Framework governance TI yang diakui industri",
        "Digital Transformation = Keterampilan inti STI menurut APTIKOM [003]"
    ])
    story.append(PageBreak())
    
    # Section 3.2: Implementasi Konsentrasi
    story.append(Paragraph("Implementasi 3 Konsentrasi", styles['Heading2']))
    story.append(Spacer(1, 5*mm))
    
    impl_data = [
        ['Konsentrasi', 'Domain', 'Mata Kuliah Wajib', 'CPL'],
        ['Enterprise Systems & Business Analytics', 'IS', 'ERP, BI, Data Mining', '11, 13, 17'],
        ['IT Infrastructure & Cybersecurity', 'IT', 'Cloud Security, Network Security, ITIL', '13, 14, 16'],
        ['Enterprise Architecture & DT', 'Hybrid', 'TOGAF, System Integration, DT Strategy', '12, 13, 15, 17']
    ]
    create_table(story, styles, impl_data, colWidths=[50*mm, 25*mm, 55*mm, 30*mm])
    
    story.append(Paragraph(
        "Justifikasi: APTIKOM menyarankan 3 konsentrasi ini [003, 006]. Konsentrasi ke-3 = pembeda utama STI dari SI/TI.",
        styles['Normal']
    ))
    story.append(PageBreak())
    
    # Section 3.3: Hapus MK Tidak Relevan
    story.append(Paragraph("Mata Kuliah yang Perlu Dihapus", styles['Heading2']))
    story.append(Spacer(1, 5*mm))
    
    remove_data = [
        ['Kode', 'Mata Kuliah', 'Alasan', 'SKS'],
        ['STI-316', 'Multimedia Interaktif', 'Tidak relevan dengan profil STI', '2'],
        ['STI-317', 'Metode Komputasi dan Numerik', 'Lebih cocok untuk TI/CS', '2'],
        ['STI-423', 'Game Design dan Gamifikasi Sosial', 'Tidak ada di kurikulum APTIKOM', '3'],
        ['STI-638', 'Intelligent Signal Processing', 'Lebih cocok untuk Teknik Elektro', '3']
    ]
    create_table(story, styles, remove_data, colWidths=[25*mm, 60*mm, 55*mm, 20*mm])
    
    story.append(Paragraph(
        "Justifikasi: APTIKOM tidak merekomendasikan mata kuliah ini untuk STI [003, 004]. ACM/ACEEE: Mata kuliah ini bukan inti IS/IT.",
        styles['Normal']
    ))
    story.append(PageBreak())
    
    # ===== CHAPTER 4: RINGKASAN =====
    create_chapter_title(story, styles, "Ringkasan Perbaikan")
    
    summary_data = [
        ['No', 'Aksi', 'Dasar Evidence', 'Dampak'],
        ['1', 'Tambah 4 MK inti STI', 'APTIKOM CPL 12-17 [002, 006]', 'Cover 5 CPL yang hilang'],
        ['2', 'Implementasi 3 konsentrasi', 'APTIKOM [003, 004]', 'Lulusan memiliki spesialisasi'],
        ['3', 'Hapus 4 MK tidak relevan', 'APTIKOM & ACM CC2020', 'Ruang untuk konsentrasi & MBKM'],
        ['4', 'Alokasi MBKM 14 SKS', 'Kebijakan Kemendikbud & APTIKOM', 'Memenuhi 20% SKS']
    ]
    create_table(story, styles, summary_data, colWidths=[15*mm, 50*mm, 45*mm, 40*mm])
    story.append(PageBreak())
    
    # ===== CHAPTER 5: KESIMPULAN =====
    create_chapter_title(story, styles, "Kesimpulan")
    
    story.append(Paragraph(
        "Kurikulum saat ini tidak memenuhi standar APTIKOM OBE untuk STI (5/7 CPL inti hilang). "
        "Tidak ada konsentrasi → Tidak ada diferensiasi lulusan. MBKM tidak terstruktur → "
        "Tidak memenuhi kebijakan nasional. Beberapa mata kuliah tidak relevan dengan domain STI.",
        styles['Normal']
    ))
    story.append(Spacer(1, 8*mm))
    
    story.append(Paragraph("Solusi Minimal:", styles['Heading2']))
    create_bulleted_list(story, styles, [
        "Tambah 4 MK inti STI (12 SKS)",
        "Hapus 4 MK tidak relevan (10 SKS)",
        "Implementasi 3 konsentrasi (24 SKS)",
        "Alokasi MBKM (14 SKS)"
    ])
    
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("Hasil:", styles['Heading2']))
    create_bulleted_list(story, styles, [
        "Semua CPL tercover",
        "Lulusan memiliki spesialisasi",
        "Memenuhi standar APTIKOM & ACM/ACEEE"
    ])
    story.append(PageBreak())
    
    # ===== REFERENSI =====
    create_chapter_title(story, styles, "Referensi")
    create_numbered_list(story, styles, [
        "[001] Summary Pemetaan Prodi STI APTIKOM - 01 Agustus 2026",
        "[002] Detail Pemetaan CPL dan Profil Lulusan APTIKOM",
        "[003] Rekomendasi Konsentrasi STI APTIKOM",
        "[004] Kurikulum Lengkap STI 144SKS dan 150SKS",
        "[005] Dokumen Komprehensif Kurikulum STI dan Konsentrasi",
        "[006] Master Detail Seluruh Respon Diskusi STI APTIKOM",
        "ACM/IEEE Computing Curricula 2020 (CC2020)",
        "APTIKOM Panduan Kurikulum 2023-2024"
    ])
    story.append(PageBreak())
    
    # ===== BACK COVER =====
    story.append(Spacer(1, 80*mm))
    story.append(Paragraph("TERIMA KASIH", styles['Title']))
    story.append(Spacer(1, 10*mm))
    story.append(Paragraph("Untuk perbaikan kurikulum SISTEKIN yang lebih baik", styles['Subtitle']))
    story.append(Spacer(1, 30*mm))
    create_quote(story, styles, 
                 "The future belongs to those who prepare for it today.",
                 "Malcolm X")
    
    # Build PDF
    doc.build(story)
    print("✓ PDF generated successfully: /home/user/ebook_sti_analysis.pdf")


if __name__ == "__main__":
    generate_pdf()
