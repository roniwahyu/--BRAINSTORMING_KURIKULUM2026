import io, re

fn = '004_MATRIKS_KETERLACAKAN_OBE_VMTS_PEO_PL_CPL_MK.md'
lines = io.open(fn, encoding='utf-8').read().split('\n')
from collections import Counter
cnt = Counter()
for i, l in enumerate(lines, 1):
    s = l.strip()
    if not s.startswith('|'):
        continue
    c = [x.strip() for x in s.strip('|').split('|')]
    cnt[len(c)] += 1
print(cnt)
for i, l in enumerate(lines, 1):
    s = l.strip()
    if s.startswith('| 1 |') or s.startswith('| 17 |'):
        c = [x.strip() for x in s.strip('|').split('|')]
        print(i, len(c), c)
