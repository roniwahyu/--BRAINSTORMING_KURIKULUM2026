import pymupdf,re,json
from pathlib import Path
pdf='/home/user/--BRAINSTORMING_KURIKULUM2026/KURIKULUM2025/Implementasi_MODUL_OBE_SISTEKIN2025.pdf'
doc=pymupdf.open(pdf); page=doc[10]; words=page.get_text('words')
starts=sorted([(w[1],w[4]) for w in words if w[0]<30 and w[1]<500 and re.match(r'^STI-\d',w[4])])
assert len(starts)==36,len(starts)
rows=[]
for j,(ys,code) in enumerate(starts):
    ye=starts[j+1][0] if j+1<len(starts) else 510
    band=[w for w in words if ys-0.5<=w[1]<ye-0.5]
    def txt(lo,hi):
        arr=[w for w in band if lo<=w[0]<hi]
        arr=sorted(arr,key=lambda z:(round(z[1],1),z[0]))
        return ' '.join(w[4] for w in arr)
    row={
      'code':code,
      'name':txt(50,190),
      'pl':txt(190,220),
      'cpmk':txt(220,255),
      'rumusan_cpmk':txt(255,402),
      'sub':txt(402,442),
      'rumusan_sub':txt(442,607),
      'cpl':txt(607,638),
      'metode':txt(638,730),
      'bobot':txt(730,770),
    }
    rows.append(row)
from collections import Counter,defaultdict
print('courses',Counter(r['code'] for r in rows))
for code in sorted(set(r['code'] for r in rows)):
 print(code,'weights',sum(int(r['bobot']) for r in rows if r['code']==code))
print('blank fields',[(i+1,[k for k,v in r.items() if not v]) for i,r in enumerate(rows) if any(not v for v in r.items())])
Path('/home/user/obe_pdf_extract/page11_rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
with open('/home/user/obe_pdf_extract/page11_cpmk.md','w') as f:
 f.write('| Kode MK | Mata Kuliah | PL | CPMK | Rumusan CPMK | Sub-CPMK | Rumusan Sub-CPMK | CPL | Evaluasi | Bobot |\n|---|---|---|---|---|---|---|---|---|---:|\n')
 for r in rows:
  vals=[r[k].replace('|','/') for k in ['code','name','pl','cpmk','rumusan_cpmk','sub','rumusan_sub','cpl','metode','bobot']]
  f.write('| '+' | '.join(vals)+' |\n')
