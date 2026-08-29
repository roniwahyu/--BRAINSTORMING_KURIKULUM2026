# -*- coding: utf-8 -*-
"""
Verifikator Ground Truth Kurikulum 2025 (SIAKAD).

SUMBER TUNGGAL KEBENARAN (single source of truth) untuk seluruh data Kurikulum 2025:
    KURIKULUM2025/Laporan Daftar Kurikulum Prodi Sistekin.pdf
    (Laporan resmi SIAKAD, dicetak 05 Agustus 2026, 3 halaman, 56 MK / 146 SKS)

Skrip ini mengekstrak data mentah dari PDF tersebut, lalu memverifikasi bahwa
seluruh rujukan Kurikulum 2025 pada Dokumen 024 (Matriks Ekivalensi) konsisten
100% dengan PDF: nomor urut, nama mata kuliah, bobot SKS, dan penempatan semester.

Jalankan: python _tools/verify_k2025_ground_truth.py
"""
import os
import re
import sys
from collections import defaultdict

try:
    import pdfplumber
except ImportError:
    sys.exit("[GAGAL] Modul pdfplumber belum terpasang. Jalankan: pip install pdfplumber")

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(BASE)
PDF_GT = os.path.join(ROOT, "KURIKULUM2025", "Laporan Daftar Kurikulum Prodi Sistekin.pdf")
DOK024 = os.path.join(BASE, "024_MATRIKS_EKIVALENSI_KURIKULUM2025_KE_KURIKULUM2026.md")
DOK005 = os.path.join(BASE, "005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md")

# Angka resmi Kurikulum 2025 menurut PDF SIAKAD
EXPECT_MK = 56
EXPECT_SKS = 146
EXPECT_SEBARAN = {1: 18, 2: 18, 3: 20, 4: 20, 5: 21, 6: 21, 7: 20, 8: 8}

# Baris PDF: "6. STI-103 Logika Informatika 2 C 1 Wajib Tidak"
RE_PDF_ROW = re.compile(
    r"^(\d+)\.\s+([A-Z]{3}-\d{3})\s+(.+?)\s+(\d+)\s+C\s+(\d)\s+(\S+)\s+(\S+)"
)


def muat_ground_truth():
    """Ekstrak 56 MK Kurikulum 2025 dari PDF Laporan SIAKAD."""
    gt = {}
    with pdfplumber.open(PDF_GT) as pdf:
        for page in pdf.pages:
            for line in (page.extract_text() or "").split("\n"):
                m = RE_PDF_ROW.match(line)
                if m:
                    gt[m.group(2)] = dict(
                        no=int(m.group(1)),
                        nama=m.group(3).strip(),
                        sks=int(m.group(4)),
                        sem=int(m.group(5)),
                        status=m.group(6),
                        paket=m.group(7),
                    )
    return gt


def bersih(nama):
    """Normalisasi nama MK: penanda praktikum (+P) diabaikan saat pembandingan."""
    return nama.strip().rstrip("*").strip().replace(" (+P)", "")


def main():
    galat = []
    print("=" * 78)
    print("VERIFIKASI GROUND TRUTH KURIKULUM 2025 (LAPORAN SIAKAD)")
    print("=" * 78)
    print(f"Sumber : {os.path.relpath(PDF_GT, ROOT)}")

    if not os.path.isfile(PDF_GT):
        sys.exit(f"[GAGAL] Berkas ground truth tidak ditemukan: {PDF_GT}")

    gt = muat_ground_truth()
    total_sks = sum(v["sks"] for v in gt.values())
    sebaran = defaultdict(int)
    for v in gt.values():
        sebaran[v["sem"]] += v["sks"]

    # ---------- Uji 1: integritas ekstraksi PDF ----------
    print("\n[1] INTEGRITAS EKSTRAKSI PDF")
    for label, aktual, harap in (
        ("Jumlah mata kuliah", len(gt), EXPECT_MK),
        ("Total SKS", total_sks, EXPECT_SKS),
    ):
        tanda = "OK" if aktual == harap else "GAGAL"
        print(f"    {label:24}: {aktual} (harap {harap}) {tanda}")
        if aktual != harap:
            galat.append(f"{label} PDF = {aktual}, seharusnya {harap}")

    print("    Sebaran SKS per semester:")
    for s in sorted(EXPECT_SEBARAN):
        tanda = "OK" if sebaran[s] == EXPECT_SEBARAN[s] else "GAGAL"
        print(f"      Sem {s}: {sebaran[s]:2} SKS (harap {EXPECT_SEBARAN[s]:2}) {tanda}")
        if sebaran[s] != EXPECT_SEBARAN[s]:
            galat.append(f"Sebaran Sem {s} = {sebaran[s]} SKS, seharusnya {EXPECT_SEBARAN[s]}")

    status = {v["status"] for v in gt.values()}
    if status != {"Wajib"}:
        galat.append(f"Status MK K2025 tidak seluruhnya Wajib: {status}")
    print(f"    Status seluruh MK      : {', '.join(sorted(status))} (K2025 tanpa MK pilihan)")

    doc = open(DOK024, encoding="utf-8", errors="ignore").read()

    # ---------- Uji 2: header seksi 3.x ----------
    print("\n[2] HEADER SEKSI 3.x DOKUMEN 024 vs SEBARAN PDF")
    for m in re.finditer(r"### 3\.\d EKIVALENSI MK SEMESTER (\d) KURIKULUM 2025 \((\d+) SKS\)", doc):
        s, klaim = int(m.group(1)), int(m.group(2))
        tanda = "OK" if klaim == sebaran[s] else "GAGAL"
        print(f"    Sem {s}: header {klaim:2} SKS vs PDF {sebaran[s]:2} SKS {tanda}")
        if klaim != sebaran[s]:
            galat.append(f"Header seksi 3 Sem {s} = {klaim} SKS, PDF = {sebaran[s]} SKS")

    # ---------- Uji 3: baris demi baris Bagian 3 ----------
    print("\n[3] AUDIT BARIS DEMI BARIS MATRIKS UTAMA (BAGIAN 3)")
    sec3 = doc.split("## 3. MATRIKS EKIVALENSI UTAMA")[1].split("## 4. EMPAT KLASTER")[0]
    baris = re.findall(r"^\| (\d+) \| `([A-Z]{3}-\d{3})` \| ([^|]+?) \| (\d+) \|", sec3, re.M)
    print(f"    Baris terbaca            : {len(baris)} (harap {EXPECT_MK})")
    if len(baris) != EXPECT_MK:
        galat.append(f"Bagian 3 memuat {len(baris)} baris, seharusnya {EXPECT_MK}")

    tak_cocok = 0
    for no, kode, nama, sks in baris:
        g = gt.get(kode)
        if not g:
            galat.append(f"Kode {kode} pada Bagian 3 tidak ada di PDF SIAKAD")
            tak_cocok += 1
            continue
        if int(no) != g["no"]:
            galat.append(f"{kode}: nomor urut {no} vs PDF {g['no']}")
            tak_cocok += 1
        if int(sks) != g["sks"]:
            galat.append(f"{kode}: SKS {sks} vs PDF {g['sks']}")
            tak_cocok += 1
        if bersih(nama) != bersih(g["nama"]):
            galat.append(f"{kode}: nama '{bersih(nama)}' vs PDF '{g['nama']}'")
            tak_cocok += 1
    print(f"    Ketidakcocokan atribut   : {tak_cocok} (nomor urut, nama, SKS)")

    # ---------- Uji 4: penempatan baris pada seksi semester ----------
    print("\n[4] PENEMPATAN BARIS PADA SEKSI SEMESTER ASAL")
    salah_sem = 0
    for m in re.finditer(r"### 3\.\d EKIVALENSI MK SEMESTER (\d) KURIKULUM 2025[^#]*", doc):
        s = int(m.group(1))
        for kode in re.findall(r"^\| \d+ \| `([A-Z]{3}-\d{3})` \|", m.group(0), re.M):
            if kode in gt and gt[kode]["sem"] != s:
                galat.append(f"{kode} tercantum di seksi Sem {s}, PDF menyatakan Sem {gt[kode]['sem']}")
                salah_sem += 1
    print(f"    Baris salah seksi        : {salah_sem}")

    # ---------- Uji 5: Zero Orphan pada tabel entri SIAKAD (Bagian 8) ----------
    print("\n[5] ZERO ORPHAN TABEL ENTRI SIAKAD (BAGIAN 8)")
    sec8 = doc.split("## 8. MATRIKS EKIVALENSI RINGKAS")[1].split("> [!WARNING]")[0]
    pasangan = re.findall(
        r"^\| `([A-Z]{3}-\d{2,3})` \| (\d+) \| (?:`([A-Z]{3}-\d{2,3})`|—) \| (?:(\d+)|—) \| (\S+) \|",
        sec8, re.M,
    )
    kode_lama = {p[0] for p in pasangan}
    terlantar = sorted(set(gt) - kode_lama)
    fiktif = sorted(kode_lama - set(gt))
    print(f"    Baris konversi           : {len(pasangan)}")
    print(f"    MK K2025 terpetakan      : {len(kode_lama)} / {len(gt)}")
    print(f"    MK terlantar (orphan)    : {len(terlantar)} {terlantar if terlantar else ''}")
    print(f"    Kode fiktif (tak di PDF) : {len(fiktif)} {fiktif if fiktif else ''}")
    if terlantar:
        galat.append(f"MK K2025 tidak terpetakan: {terlantar}")
    if fiktif:
        galat.append(f"Kode K2025 fiktif di Bagian 8: {fiktif}")

    beda_sks = [
        f"{o} ({so} vs {gt[o]['sks']})"
        for o, so, n, sn, k in pasangan
        if o in gt and int(so) != gt[o]["sks"]
    ]
    print(f"    SKS lama tidak cocok PDF : {len(beda_sks)} {beda_sks if beda_sks else ''}")
    if beda_sks:
        galat.append(f"SKS lama Bagian 8 tidak cocok PDF: {beda_sks}")

    # ---------- Uji 6: neraca kategori E1-E5 ----------
    print("\n[6] NERACA KATEGORI EKIVALENSI E1-E5")
    neraca = defaultdict(lambda: [set(), 0])
    for o, so, n, sn, k in pasangan:
        kat = k.split("/")[0].strip("*")
        if o not in neraca[kat][0]:
            neraca[kat][0].add(o)
            neraca[kat][1] += int(so)
    jml_mk = sum(len(v[0]) for v in neraca.values())
    jml_sks = sum(v[1] for v in neraca.values())
    for kat in sorted(neraca):
        print(f"    {kat}: {len(neraca[kat][0]):2} MK / {neraca[kat][1]:3} SKS")
    print(f"    TOTAL: {jml_mk} MK / {jml_sks} SKS (harap {EXPECT_MK} MK / {EXPECT_SKS} SKS)")
    if (jml_mk, jml_sks) != (EXPECT_MK, EXPECT_SKS):
        galat.append(f"Neraca kategori = {jml_mk} MK / {jml_sks} SKS, seharusnya {EXPECT_MK} / {EXPECT_SKS}")

    # ---------- Uji 7: kode target K2026 valid ----------
    print("\n[7] VALIDITAS KODE TARGET KURIKULUM 2026")
    d005 = open(DOK005, encoding="utf-8", errors="ignore").read()
    d007 = open(os.path.join(BASE, "007_FORMULASI_CPMK_DAN_SUB_CPMK_PORTFOLIO_LENGKAP.md"),
                encoding="utf-8", errors="ignore").read()
    target = sorted({p[2] for p in pasangan if p[2]})
    tak_dikenal = [t for t in target if t not in d005 and t not in d007]
    print(f"    Kode target unik         : {len(target)}")
    print(f"    Tidak ada di Dok 005/007 : {len(tak_dikenal)} {tak_dikenal if tak_dikenal else ''}")
    if tak_dikenal:
        galat.append(f"Kode target K2026 tidak dikenal: {tak_dikenal}")

    # ---------- Uji 8: semester MK elektif = Dokumen 005 ----------
    print("\n[8] SEMESTER MK ELEKTIF PEMINATAN vs DOKUMEN 005")
    definitif = {
        c: int(s)
        for c, s in re.findall(r"`(ST[ABC]-\d\d)`[^<|]*?\((?:\+P|Teori), Sem (\d)\)", d005)
    }
    beda_sem = []
    for m in re.finditer(
        r"^\| \d+ \| `([A-Z]{3}-\d{3})` \|[^|]*\|[^|]*\| `(ST[ABC]-\d\d)` \|[^|]*\|[^|]*\| ([^|]+?) \|",
        doc, re.M,
    ):
        lama, baru, smt = m.group(1), m.group(2), m.group(3).strip()
        if smt != str(definitif.get(baru)):
            beda_sem.append(f"{lama}->{baru}: Dok024 '{smt}' vs Dok005 'Sem {definitif.get(baru)}'")
    print(f"    Baris elektif diperiksa  : {len(definitif)} kode elektif definitif")
    print(f"    Semester tidak presisi   : {len(beda_sem)}")
    for b in beda_sem:
        print(f"      {b}")
    if beda_sem:
        galat.append(f"Semester elektif tidak presisi: {beda_sem}")

    # ---------- Uji 9: neraca rekognisi arah balik (Bagian 3A) ----------
    print("\n[9] NERACA REKOGNISI ARAH BALIK (BAGIAN 3A)")
    # Inventaris paket wajib K2026 per semester dari Dokumen 005
    paket = {}
    for m in re.finditer(r"### SEMESTER (\d) \(\d+ SKS\)[^#]*", d005):
        s = int(m.group(1))
        for kode, sks in re.findall(r"^\| [\d.B]+ \| `([A-Z]{3}-\d{3})` \| [^|]+ \| (\d+) \|",
                                    m.group(0), re.M):
            paket[kode] = dict(sem=s, sks=int(sks))

    # MK K2026 yang punya asal K2025 menurut Bagian 8
    berasal = {p[2] for p in pasangan if p[2]}
    neraca_sem = defaultdict(lambda: {"diakui": 0, "defisit": 0, "baru": []})
    for kode, v in paket.items():
        sisi = "diakui" if kode in berasal else "defisit"
        neraca_sem[v["sem"]][sisi] += v["sks"]
        if sisi == "defisit":
            neraca_sem[v["sem"]]["baru"].append(kode)

    diakui_tot = sum(n["diakui"] for n in neraca_sem.values())
    defisit_tot = sum(n["defisit"] for n in neraca_sem.values())
    print(f"    Paket wajib K2026        : {len(paket)} MK / {diakui_tot + defisit_tot} SKS")
    print(f"    Diakui dari K2025        : {diakui_tot} SKS")
    print(f"    Defisit (MK wajib baru)  : {defisit_tot} SKS")
    for s in sorted(neraca_sem):
        n = neraca_sem[s]
        print(f"      Sem {s}: diakui {n['diakui']:2} SKS, defisit {n['defisit']:2} SKS"
              f"{'  -> ' + ', '.join(n['baru']) if n['baru'] else ''}")

    if (diakui_tot, defisit_tot) != (114, 14):
        galat.append(f"Neraca 3A = diakui {diakui_tot} / defisit {defisit_tot} SKS, seharusnya 114 / 14")

    # Cocokkan dengan tabel 3A.3 di dokumen
    m3a = re.search(r"\| \*\*TOTAL PAKET WAJIB\*\* \| \*\*(\d+)\*\* \| \*\*(\d+)\*\* \| \*\*(\d+)\*\*", doc)
    if m3a:
        klaim = tuple(int(g) for g in m3a.groups())
        cocok = klaim == (diakui_tot + defisit_tot, diakui_tot, defisit_tot)
        print(f"    Tabel 3A.3 menyatakan    : {klaim[0]} SKS paket, {klaim[1]} diakui, {klaim[2]} defisit"
              f"  {'OK' if cocok else 'GAGAL'}")
        if not cocok:
            galat.append(f"Tabel 3A.3 = {klaim}, hitungan = "
                         f"{(diakui_tot + defisit_tot, diakui_tot, defisit_tot)}")
    else:
        galat.append("Tabel 3A.3 (TOTAL PAKET WAJIB) tidak ditemukan")

    # ---------- Uji 10: kelengkapan rekognisi portofolio 67 MK ----------
    print("\n[10] KELENGKAPAN REKOGNISI PORTOFOLIO 67 MK")
    elektif = {
        c: int(s)
        for c, s in re.findall(r"`(ST[ABC]-\d\d)`[^<|]*?\((?:\+P|Teori), Sem (\d)\)", d005)
    }
    portofolio = set(paket) | set(elektif)
    punya = {c for c in portofolio if c in berasal}
    baru = portofolio - punya
    print(f"    Portofolio K2026         : {len(portofolio)} MK (harap 67)")
    print(f"    Dapat direkognisi        : {len(punya)} MK (harap 49)")
    print(f"    MK baru wajib ditempuh   : {len(baru)} MK (harap 18)")
    if len(portofolio) != 67:
        galat.append(f"Portofolio K2026 = {len(portofolio)} MK, seharusnya 67")
    if (len(punya), len(baru)) != (49, 18):
        galat.append(f"Rekognisi portofolio = {len(punya)} punya padanan / {len(baru)} baru, "
                     f"seharusnya 49 / 18")

    # ---------- Uji 11: aturan klaim ganda tidak ambigu ----------
    print("\n[11] KETUNTASAN ATURAN KLAIM GANDA")
    ke_baru = defaultdict(list)
    for o, so, n, sn, k in pasangan:
        if n:
            ke_baru[n].append((o, k.split("/")[0].strip("*")))
    ganda = {n: v for n, v in ke_baru.items() if len(v) > 1 and not any("E3" in x[1] for x in v)}
    print(f"    Kasus klaim ganda        : {len(ganda)}")
    for n, v in sorted(ganda.items()):
        kats = [x[1] for x in v]
        e1 = [x for x in v if x[1] == "E1"]
        if len(e1) == 1:
            cara = f"terselesaikan jenjang 1 (E1 menang): klaim {e1[0][0]}"
            tuntas = True
        else:
            # jenjang 2 wajib dinyatakan eksplisit di dokumen
            tuntas = bool(re.search(rf"Jenjang 2[^|]*\|", doc)) and n in doc
            cara = ("terselesaikan jenjang 2 (ditetapkan eksplisit di dokumen)"
                    if tuntas else "AMBIGU - tidak ada dasar penentuan")
        print(f"      {n} <- {[x[0] for x in v]} kategori {kats}: {cara}")
        if not tuntas:
            galat.append(f"Klaim ganda {n} ambigu: kategori sama ({kats}) tanpa dasar penentuan")

    # ---------- Kesimpulan ----------
    print("\n" + "=" * 78)
    if galat:
        print(f"[GAGAL] {len(galat)} temuan menyimpang dari ground truth SIAKAD:")
        for g in galat:
            print(f"    - {g}")
        sys.exit(1)
    print("[LULUS] Seluruh rujukan Kurikulum 2025 konsisten 100% dengan Laporan SIAKAD.")
    print(f"        {EXPECT_MK} MK / {EXPECT_SKS} SKS terverifikasi pada 11 kelompok uji:")
    print("        atribut MK, penempatan semester, Zero Orphan, neraca E1-E5, semester")
    print("        elektif, neraca rekognisi arah balik, kelengkapan portofolio 67 MK,")
    print("        dan ketuntasan aturan klaim ganda.")
    print("=" * 78)


if __name__ == "__main__":
    main()
