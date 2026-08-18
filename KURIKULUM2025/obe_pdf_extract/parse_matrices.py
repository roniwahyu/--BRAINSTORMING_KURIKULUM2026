import pymupdf, re, json
from pathlib import Path
pdf='/home/user/--BRAINSTORMING_KURIKULUM2026/KURIKULUM2025/Implementasi_MODUL_OBE_SISTEKIN2025.pdf'
doc=pymupdf.open(pdf)
centers5=[322.0,354.5,387.0,419.5,452.0,484.6,517.1,549.6,582.1,614.6]
centers9=[356.2,394.2,432.2,470.3,508.3,546.4,584.4,622.4,660.5,698.5]

def nearest_col(x,centers):
    return min(range(10),key=lambda i:abs(x-centers[i]))

def code_rows(page):
    words=page.get_text('words')
    rows=[]
    for w in words:
        x0,y0,x1,y1,text,*_=w
        if re.match(r'^(MKU|STI|MFT)-\d',text): rows.append((y0,text))
    return sorted(rows)

# Page 5: mapping V
p5=doc[4]; words5=p5.get_text('words'); courses=[]
for idx,(y,code) in enumerate(code_rows(p5),1):
    line=[w for w in words5 if abs(w[1]-y)<0.9]
    name=' '.join(w[4] for w in sorted(line,key=lambda z:z[0]) if 80<=w[0]<260)
    nums=[w for w in line if 260<=w[0]<312 and re.fullmatch(r'\d+',w[4])]
    smt=next((int(w[4]) for w in nums if w[0]<290),None)
    sks=next((int(w[4]) for w in nums if w[0]>=290),None)
    maps=[]
    for w in line:
        if w[4]=='V' and 310<=w[0]<630:
            maps.append(nearest_col(w[0],centers5)+1)
    count=next((int(w[4]) for w in line if w[0]>640 and re.fullmatch(r'\d+',w[4])),None)
    courses.append({'no':idx,'code':code,'name':name,'smt':smt,'sks':sks,'maps':maps,'count':count})

assert len(courses)==56,len(courses)
calc=[sum(i in c['maps'] for c in courses) for i in range(1,11)]
print('page5 counts',calc)
print('page5 expected',[7,13,12,10,11,8,11,10,17,22])
print('page5 row count mismatches',[(c['no'],c['count'],len(c['maps'])) for c in courses if c['count']!=len(c['maps'])])

# Pages 9-10: I/R/M by code
irm={}
for pno in [8,9]:
    page=doc[pno]; words=page.get_text('words')
    for y,code in code_rows(page):
        line=[w for w in words if abs(w[1]-y)<0.9]
        marks={}
        for w in line:
            if w[4] in {'I','R','M'} and 340<=w[0]<720:
                marks[nearest_col(w[0],centers9)+1]=w[4]
        irm[code]=marks
assert len(irm)==56,len(irm)
for c in courses:c['irm']=irm[c['code']]
counts={letter:[sum(c['irm'].get(i)==letter for c in courses) for i in range(1,11)] for letter in 'IRM'}
print('irm counts',counts)
print('expected',{'I':[1,1,1,1,3,2,2,1,4,3],'R':[5,10,9,7,7,4,8,7,11,17],'M':[1,2,2,2,1,2,1,2,2,2]})

Path('/home/user/obe_pdf_extract/courses.json').write_text(json.dumps(courses,ensure_ascii=False,indent=2))

# compact mapping table
with open('/home/user/obe_pdf_extract/page5_matrix.md','w') as f:
    f.write('| No | Kode MK | Mata Kuliah | Smt | SKS | CPL yang dipetakan | Jumlah |\n|---:|---|---|:---:|:---:|---|:---:|\n')
    for c in courses:
        ms=', '.join(f'CPL{i:02d}' for i in c['maps'])
        f.write(f"| {c['no']} | {c['code']} | {c['name']} | {c['smt']} | {c['sks']} | {ms} | {c['count']} |\n")
    f.write('|  | **Jumlah MK pendukung tiap CPL** |  |  |  | **CPL01=7; CPL02=13; CPL03=12; CPL04=10; CPL05=11; CPL06=8; CPL07=11; CPL08=10; CPL09=17; CPL10=22** | **121 relasi** |\n')

with open('/home/user/obe_pdf_extract/page9_irm.md','w') as f:
    f.write('| No | Kode MK | Mata Kuliah | Smt | SKS | Level CPL (I/R/M) |\n|---:|---|---|:---:|:---:|---|\n')
    for c in courses:
        ms=', '.join(f'CPL{i:02d}={c["irm"][i]}' for i in sorted(c['irm']))
        f.write(f"| {c['no']} | {c['code']} | {c['name']} | {c['smt']} | {c['sks']} | {ms} |\n")
    f.write('|  | **Jumlah I** |  |  |  | **CPL01–CPL10: 1, 1, 1, 1, 3, 2, 2, 1, 4, 3** |\n')
    f.write('|  | **Jumlah R** |  |  |  | **CPL01–CPL10: 5, 10, 9, 7, 7, 4, 8, 7, 11, 17** |\n')
    f.write('|  | **Jumlah M** |  |  |  | **CPL01–CPL10: 1, 2, 2, 2, 1, 2, 1, 2, 2, 2** |\n')
