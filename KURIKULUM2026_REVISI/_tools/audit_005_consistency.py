import os
import re

base = r'd:\!!MYDOCUMENTS2026\!!!SISTEKIN2026\!!BRAINSTORMING_KURIKULUM2026\KURIKULUM2026_REVISI'

def read_f(fname):
    with open(os.path.join(base, fname), encoding='utf-8') as f:
        return f.read()

d005 = read_f('005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md')
d007 = read_f('007_FORMULASI_CPMK_DAN_SUB_CPMK_PORTFOLIO_LENGKAP.md')
dbuku = read_f('BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md')
d004 = read_f('004_MATRIKS_KETERLACAKAN_OBE_VMTS_PEO_PL_CPL_MK.md')
d011 = read_f('011_IMPLEMENTASI_OBE_SISTEKIN2026_TABLES.md')
d012 = read_f('012_ANALISIS_KRITIS_JALUR_PONDASI_DAN_TREE_PRASYARAT.md')
d024 = read_f('024_MATRIKS_EKIVALENSI_KURIKULUM2025_KE_KURIKULUM2026.md')

# 1. Parse Section 3 of Dok 005
mk_005 = {}
lines = d005.splitlines()
in_sec3 = False
current_sem = None

for line in lines:
    line_s = line.strip()
    m_sem = re.match(r'^### SEMESTER (\d) \((\d+) SKS\)', line_s)
    if m_sem:
        in_sec3 = True
        current_sem = int(m_sem.group(1))
        continue
    if line_s.startswith('### 3.1'):
        in_sec3 = False
        break
    if in_sec3 and line_s.startswith('|') and '`' in line_s:
        parts = [p.strip() for p in line_s.split('|')[1:-1]]
        if len(parts) >= 7 and re.match(r'^[\d.B]+$', parts[0]):
            kode_m = re.search(r'`([A-Z0-9/_-]+)`', parts[1])
            kode = kode_m.group(1) if kode_m else parts[1]
            if kode != 'STA/B/C':
                mk_005[kode] = {
                    'sem': current_sem,
                    'nama': parts[2],
                    'sks': int(parts[3]),
                    'tipe': parts[4],
                    'kat': parts[5],
                    'pra': parts[6]
                }

# Add the 18 elective courses from Dok 005 Section 4
for line in d005.split('## 4. SKEMA 3 PEMINATAN')[1].splitlines():
    m = re.findall(r'`(ST[ABC]-\d\d)`\s+([^(\n<]+)\s+\(([^,\)]+),\s+Sem\s+(\d)\)', line)
    for c, n, t, s in m:
        mk_005[c] = {
            'sem': int(s),
            'nama': n.strip(),
            'sks': 3,
            'tipe': t.strip(),
            'kat': 'Elektif Peminatan',
            'pra': 'Prasyarat Peminatan'
        }

print(f"Total Portfolio MK in Dok 005: {len(mk_005)} (49 paket + 18 elektif = 67 MK)")

# 2. Check against Dok 007
print("\n--- AUDIT vs DOK 007 ---")
diffs_007 = []
for kode, v in mk_005.items():
    # find block in 007: Kode & Nama Mata Kuliah
    # e.g., **STI-519 — Keamanan Informasi Lanjut**
    pat = rf"\*\*{kode}\s*—\s*([^*]+)\*\*"
    m_name = re.search(pat, d007)
    if not m_name:
        diffs_007.append(f"[{kode}] Tidak ditemukan di Dok 007 dengan pattern {pat}")
    else:
        name_007 = m_name.group(1).split('(')[0].strip()
        # check semester
        block_m = re.search(rf"\*\*{kode}\s*—\s*[^*]+\*\*.*?(?=\*\*Target PEO\*\*|\Z)", d007, re.DOTALL)
        if block_m:
            block = block_m.group(0)
            m_sem = re.search(r"\*\*Semester\s*/\s*Rumpun MK\*\*\s*\|\s*\*\*Semester\s+(\d)\*\*", block)
            if m_sem:
                sem_007 = int(m_sem.group(1))
                if sem_007 != v['sem']:
                    diffs_007.append(f"[{kode}] Semester mismatch: Dok 005=Sem {v['sem']} vs Dok 007=Sem {sem_007}")
            m_sks = re.search(r"\*\*Bobot SKS\s*/\s*Tipe\*\*\s*\|\s*\*\*(\d+)\s*SKS\*\*", block)
            if m_sks:
                sks_007 = int(m_sks.group(1))
                if sks_007 != v['sks']:
                    diffs_007.append(f"[{kode}] SKS mismatch: Dok 005={v['sks']} vs Dok 007={sks_007}")

print(f"Discrepancies with Dok 007: {len(diffs_007)}")
for d in diffs_007:
    print(f"  * {d}")

# 3. Check against BUKU_KURIKULUM
print("\n--- AUDIT vs BUKU_KURIKULUM ---")
diffs_buku = []
for kode, v in mk_005.items():
    pat = rf"\*\*{kode}\s*—\s*([^*]+)\*\*"
    m_name = re.search(pat, dbuku)
    if not m_name:
        diffs_buku.append(f"[{kode}] Tidak ditemukan di BUKU dengan pattern {pat}")
    else:
        block_m = re.search(rf"\*\*{kode}\s*—\s*[^*]+\*\*.*?(?=\*\*Target PEO\*\*|\Z)", dbuku, re.DOTALL)
        if block_m:
            block = block_m.group(0)
            m_sem = re.search(r"\*\*Semester\s*/\s*Rumpun MK\*\*\s*\|\s*\*\*Semester\s+(\d)\*\*", block)
            if m_sem:
                sem_buku = int(m_sem.group(1))
                if sem_buku != v['sem']:
                    diffs_buku.append(f"[{kode}] Semester mismatch: Dok 005=Sem {v['sem']} vs BUKU=Sem {sem_buku}")

print(f"Discrepancies with BUKU (Silabus): {len(diffs_buku)}")
for d in diffs_buku:
    print(f"  * {d}")

# 4. Check Section 2 / Table 3.1 text in Dok 005
print("\n--- AUDIT TEKS / NARASI DOK 005 ---")
text_issues = []
if "Sem 5 (21 SKS): Deep Learning" in d005:
    text_issues.append("Mermaid line 23 masih menyebut 'Sem 5: Deep Learning'")
if "Sem 6 (19 SKS): Smart AI, Smart City" in d005:
    text_issues.append("Mermaid line 24 belum menyebut 'Deep Learning'")
if "| **Sem 5** | Deep Learning & IoT |" in d005:
    text_issues.append("Tabel Sebaran 8 Sem (line 150) masih menyebut 'Sem 5: Deep Learning & IoT'")
if "Tahap Spesialisasi Deep Learning, IoT & Peminatan 1" in d005:
    text_issues.append("Header Sem 5 (line 220) masih menyebut 'Spesialisasi Deep Learning'")
if "Tahap Spesialisasi Deep Learning & IoT |" in d005:
    text_issues.append("Tabel 3.1 Sem 5 (line 279) masih menyebut 'Spesialisasi Deep Learning & IoT'")

print(f"Text issues in Dok 005: {len(text_issues)}")
for t in text_issues:
    print(f"  * {t}")
