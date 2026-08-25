#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Konversi Buku Panduan KPT 2024 (Direktorat Belmawa, Edisi V) -> Markdown terstruktur.

Arsitektur:
  - PyMuPDF (`get_text("blocks")`) untuk teks  -> bebas dari duplikasi caption
    yang terjadi bila memakai ekstraksi per-kata (PDF ini punya layer teks ganda
    pada beberapa caption tabel).
  - pdfplumber `find_tables()` untuk tabel bergaris (vector) -> tabel Markdown.
  - Halaman yang tabelnya disisipkan sebagai GAMBAR (Tabel 4-8, seluruh Gambar
    1-24) tidak bisa diekstrak; ditandai placeholder eksplisit + rujukan halaman.

Jalankan:  python _tools/convert_kpt2024_pdf_to_md.py
"""
import re
import sys
from pathlib import Path

import pdfplumber
import pymupdf

BASE = Path(__file__).resolve().parent.parent
PDF = BASE / "Buku-Panduan-KPT-2024-Direktorat-Pembelajaran-dan-Kemahasiswaan.pdf"
OUT = BASE / "021_PANDUAN_KPT2024_DIKTI_FULLTEXT.md"

RUNNING_HEADER = "Panduan Penyusunan Kurikulum Pendidikan Tinggi Mendukung"
START_PAGE, END_PAGE = 5, 162

CAPTION_FIG = re.compile(r"^Gambar\s+\d+\.?\s")
CAPTION_TBL = re.compile(r"^Tabel\s+\d+\.?\s")
HEAD_SECTION = re.compile(r"^([A-G])\.\s{1,3}([A-Z][A-Z\s,\-/()]{4,90})$")
LEADER = re.compile(r"\.{4,}")          # penanda baris Daftar Isi

SECTION_MARKS = {
    5: "# CATATAN PENGGUNAAN & IDENTITAS TERBITAN",
    7: "# SAMBUTAN DIREKTUR JENDERAL PENDIDIKAN TINGGI",
    8: "# KATA PENGANTAR DIREKTUR PEMBELAJARAN DAN KEMAHASISWAAN",
    9: "# TIM PENGARAH DAN TIM PENYUSUN",
    10: "# DAFTAR ISI, DAFTAR GAMBAR, DAFTAR TABEL, DAFTAR SINGKATAN",
    17: "# A. PENDAHULUAN",
    35: "# B. TAHAPAN PENYUSUNAN KURIKULUM PENDIDIKAN TINGGI",
    73: "# C. PEMBELAJARAN BERPUSAT PADA MAHASISWA",
    87: "# D. STRATEGI IMPLEMENTASI KURIKULUM DALAM PROGRAM MERDEKA BELAJAR-KAMPUS MERDEKA",
    99: "# E. PENJAMINAN MUTU",
    103: "# F. EVALUASI PROGRAM KURIKULUM",
    111: "# G. PENUTUP",
    113: "# DAFTAR PUSTAKA",
    117: "# LAMPIRAN A — Contoh RPS Model-1 Mata Kuliah Metode Penelitian",
    137: "# LAMPIRAN B — Contoh RPS Model Lainnya",
    160: "# LAMPIRAN C — Contoh Rencana Kegiatan Pembelajaran MBKM",
}

_SUBHEAD = re.compile(
    r"^(\d{1,2})[\.\)]\s+((?:Dasar Pemikiran|Landasan Penyusunan|Pengertian yang|"
    r"Kaitan Kurikulum|Dokumen Kurikulum|Kurikulum Pendidikan Tinggi dengan|"
    r"Tahapan Perancangan|Bentuk, Strategi|Pelaksanaan Proses|Penilaian dan Evaluasi|"
    r"Pembelajaran Daring|Rekognisi Kredit)[^\n]{0,90})$"
)


def subhead(line: str):
    s = line.strip()
    return None if LEADER.search(s) else _SUBHEAD.match(s)


_HYPH = re.compile(r"(\w+)-\s*\n\s*(\w+)")
_HYPH_INLINE = re.compile(r"(?<=\w)-[ \t]+(?=\w)")


def dehyphenate(txt: str) -> str:
    """Sambung kata yang terpotong tanda hubung di ujung baris.

    Tanda hubung dipertahankan bila memang bagian dari kata: reduplikasi
    Indonesia (butir-butir) atau istilah berkapital (sub-CPMK).
    """
    def fix(m):
        a, b = m.group(1), m.group(2)
        if b[:1].isupper() or a.lower() == b.lower():
            return f"{a}-{b}"
        return f"{a}{b}"

    prev = None
    while prev != txt:
        prev = txt
        txt = _HYPH.sub(fix, txt)
    return txt


def tighten_hyphen(txt: str) -> str:
    """Rapatkan `kata- kata` menjadi `kata-kata` (spasi sisa tata letak PDF)."""
    return _HYPH_INLINE.sub("-", txt)


def clean_cell(v) -> str:
    if v is None:
        return ""
    v = dehyphenate(str(v))
    v = v.replace("\n", " ").replace("|", "\\|")
    return tighten_hyphen(re.sub(r"[ \t\u00a0]+", " ", v).strip())


def table_to_md(tbl) -> str:
    rows = [[clean_cell(c) for c in r] for r in tbl
            if r and any(clean_cell(c) for c in r)]
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    head = rows[0] if any(rows[0]) else [f"Kol{i+1}" for i in range(width)]
    body = rows[1:] if any(rows[0]) else rows
    out = ["| " + " | ".join(head) + " |",
           "|" + "|".join(["---"] * width) + "|"]
    out += ["| " + " | ".join(r) + " |" for r in body]
    return "\n".join(out)


def normalize_block(raw: str) -> list:
    """Bersihkan satu blok teks PyMuPDF menjadi daftar paragraf."""
    txt = raw.replace("\t", " ").replace("\u00a0", " ")
    txt = dehyphenate(txt)
    lines = [re.sub(r"\s+", " ", l).strip() for l in txt.split("\n")]
    lines = [l for l in lines if l and not re.fullmatch(r"[•·\-–—_\s\.]+", l)]
    if not lines:
        return []

    paras, buf = [], ""
    bullet = re.compile(
        r"^(\d+[\.\)]\s|\(\d+\)\s|[a-z][\.\)]\s|[A-G]\.\s|[ivx]+[\.\)]\s|[•▪]\s)")
    for l in lines:
        if subhead(l):
            if buf:
                paras.append(buf)
                buf = ""
            paras.append(l)
            continue
        new = bool(bullet.match(l)) or CAPTION_FIG.match(l) or CAPTION_TBL.match(l)
        if buf and not new and not buf.endswith((".", ":", ";", "!", "?")):
            buf += " " + l
        else:
            if buf:
                paras.append(buf)
            buf = l
    if buf:
        paras.append(buf)
    return paras


def is_noise(p: str, pno: int) -> bool:
    s = p.strip()
    if not s or RUNNING_HEADER[:35] in s:
        return True
    if re.fullmatch(r"\d{1,3}", s):
        return True
    if HEAD_SECTION.match(s):
        return True
    if pno in SECTION_MARKS and pno >= 17 and re.match(r"^[A-G]\.\s+\S", s) and len(s) < 70:
        return True
    return False


def convert():
    if not PDF.exists() or PDF.stat().st_size == 0:
        sys.exit(f"ERROR: PDF hilang/kosong: {PDF}")

    md = [
        "# PANDUAN PENYUSUNAN KURIKULUM PENDIDIKAN TINGGI (KPT) 2024",
        "",
        "**Mendukung Merdeka Belajar–Kampus Merdeka Menuju Indonesia Emas — Edisi V**",
        "",
        "**Penerbit:** Direktorat Pembelajaran dan Kemahasiswaan, Direktorat Jenderal "
        "Pendidikan Tinggi, Riset, dan Teknologi, Kementerian Pendidikan, Kebudayaan, "
        "Riset, dan Teknologi (Kemendikbudristek), Juli 2024. 164 halaman.",
        "",
        "**Hak Cipta:** © 2024 Direktorat Jenderal Pendidikan Tinggi, Riset, dan "
        "Teknologi. Milik Negara — Tidak Diperdagangkan.",
        "",
        "> **Cara dokumen ini dihasilkan.** Ekstraksi teks digital (PDF sumber sudah "
        "berlapis teks, sehingga OCR tidak diperlukan) dari "
        "`Buku-Panduan-KPT-2024-Direktorat-Pembelajaran-dan-Kemahasiswaan.pdf`. "
        "Tabel bergaris direkonstruksi menjadi tabel Markdown. Sebagian tabel "
        "normatif (Tabel 4–8) dan seluruh diagram (Gambar 1–24) disisipkan penerbit "
        "sebagai **gambar raster**, sehingga isinya tidak dapat diekstrak dan "
        "ditandai `[GAMBAR — lihat PDF hlm. N]`. Penanda `[hlm. N]` merujuk nomor "
        "halaman **file PDF** (bukan nomor halaman cetak, yang lebih kecil 4 angka) "
        "agar dapat disitasi balik.",
        "",
        "---",
        "",
    ]

    doc = pymupdf.open(str(PDF))
    plumb = pdfplumber.open(str(PDF))

    for pi in range(len(doc)):
        pno = pi + 1
        if pno < START_PAGE or pno > END_PAGE:
            continue

        page_mu = doc[pi]
        page_pl = plumb.pages[pi]

        if len((page_mu.get_text() or "").strip()) < 200 and pno not in SECTION_MARKS:
            continue

        blocks = []

        # Beberapa caption tabel dicetak sebagai layer terpisah yang menimpa baris
        # header tabel (mis. Tabel 25 di hlm. 104, font Cambria). Layer itu dibuang
        # berdasarkan nama font agar tidak menyusup ke dalam sel Markdown.
        def not_caption_layer(obj):
            return "Cambria" not in (obj.get("fontname") or "")

        # --- tabel bergaris ---
        tbl_boxes = []
        for t in page_pl.filter(not_caption_layer).find_tables():
            mdt = table_to_md(t.extract())
            if mdt:
                blocks.append((t.bbox[1], "table", mdt))
                tbl_boxes.append(t.bbox)

        # --- teks ---
        for x0, y0, x1, y1, raw, _, btype in page_mu.get_text("blocks"):
            if btype != 0:
                continue
            cy = (y0 + y1) / 2
            cx = (x0 + x1) / 2
            if any(b[0] - 2 <= cx <= b[2] + 2 and b[1] - 2 <= cy <= b[3] + 2
                   for b in tbl_boxes):
                continue
            paras = [p for p in normalize_block(raw) if not is_noise(p, pno)]
            if paras:
                blocks.append((y0, "text", paras))

        if not blocks:
            continue

        if pno in SECTION_MARKS:
            md += ["", SECTION_MARKS[pno], ""]

        md.append(f"<!-- [hlm. {pno}] -->")

        seen_cap = set()
        has_vector_table = bool(tbl_boxes)
        for _, kind, payload in sorted(blocks, key=lambda b: b[0]):
            if kind == "table":
                md += ["", payload, ""]
                continue
            for para in payload:
                if CAPTION_TBL.match(para) and not LEADER.search(para):
                    key = para[:45].lower()
                    if key in seen_cap:
                        continue
                    seen_cap.add(key)
                    md += ["", f"**{para}**", ""]
                    if not has_vector_table:
                        md += [f"> *[Isi tabel disisipkan sebagai gambar pada PDF "
                               f"hlm. {pno} — tidak dapat diekstrak sebagai teks; "
                               f"rujuk PDF asli.]*", ""]
                elif CAPTION_FIG.match(para) and not LEADER.search(para) and len(para) < 200:
                    md += ["", f"**[GAMBAR — lihat PDF hlm. {pno}]** {para}", ""]
                elif subhead(para) and pno >= 17:
                    m = subhead(para)
                    md += ["", f"## {m.group(1)}. {m.group(2).strip()}", ""]
                else:
                    md += [para, ""]

    plumb.close()
    doc.close()

    text = re.sub(r"\n{4,}", "\n\n\n", "\n".join(md))
    text = tighten_hyphen(text)
    OUT.write_text(text, encoding="utf-8")
    print(f"OK -> {OUT.name}  ({OUT.stat().st_size/1024:.1f} KB)")


if __name__ == "__main__":
    convert()
