#!/usr/bin/env python3
"""
Script: update_kode_624_625_726_727.py
Purpose: Update atomik kode MK setelah pertukaran Semester 6-7:
         - STI-626 → STI-624 (Deep Learning, Sem 6)
         - STI-627 → STI-625 (Platform Engineering, Sem 6)
         - STI-624 → STI-726 (AI Integration, Sem 7)
         - STI-625 → STI-727 (Smart City, Sem 7)

Author: Kiro Agent (Curriculum Architect)
Date: 2026-09-22
"""

import re
from pathlib import Path

# Pemetaan kode lama → baru
CODE_MAPPING = {
    'STI-626': 'STI-624',  # Deep Learning ke Sem 6
    'STI-627': 'STI-625',  # Platform Engineering ke Sem 6
    'STI-624': 'STI-726',  # AI Integration ke Sem 7
    'STI-625': 'STI-727',  # Smart City ke Sem 7
}

# Daftar file yang akan diupdate (relatif dari root)
TARGET_FILES = [
    'KURIKULUM2026_REVISI/004_MATRIKS_KETERLACAKAN_OBE_VMTS_PEO_PL_CPL_MK.md',
    'KURIKULUM2026_REVISI/006_DISTRIBUSI_DAN_PANDUAN_MK_PEMINATAN_MBKM.md',
    'KURIKULUM2026_REVISI/009D_CPL_KETERAMPILAN_KHUSUS_SISTEKIN.md',
    'KURIKULUM2026_REVISI/011_IMPLEMENTASI_OBE_SISTEKIN2026_TABLES.md',
    'KURIKULUM2026_REVISI/012_ANALISIS_KRITIS_JALUR_PONDASI_DAN_TREE_PRASYARAT.md',
    'KURIKULUM2026_REVISI/013_REKOMENDASI_SOLUSI_DAN_MITIGASI_KELEMAHAN_KURIKULUM.md',
    'KURIKULUM2026_REVISI/015_SIMULASI_AKSELERASI_KELULUSAN_7_SEMESTER.md',
    'KURIKULUM2026_REVISI/016_ANALISIS_BoK_APTIKOM_REDUNDANSI_DAN_PIPELINE_AI.md',
    'KURIKULUM2026_REVISI/017_AUDIT_FORENSIK_ZERO_REDUNDANCY_DAN_ZERO_GAP.md',
    'KURIKULUM2026_REVISI/018_PANDUAN_RUBRIK_KLASTER_DAN_MODEL_ASESMEN_OBE_DOSEN.md',
    'KURIKULUM2026_REVISI/019_AUDIT_KRITIS_KESELARASAN_FOLDER_REVISI_23082026_212923.md',
    'KURIKULUM2026_REVISI/023_BUKU_KPT_SISTEKIN_2026_STRUKTUR_KPT2024.md',
    'KURIKULUM2026_REVISI/024_MATRIKS_EKIVALENSI_KURIKULUM2025_KE_KURIKULUM2026.md',
    'KURIKULUM2026_REVISI/025_REKOMENDASI_PENGEMBANGAN_MK_PEMINATAN_DAN_CROSS_TRACK_2027.md',
    'KURIKULUM2026_REVISI/026_ANALISIS_KRITIS_MK_DIHAPUS_DAN_REKOMENDASI_PENGGANTI.md',
    'KURIKULUM2026_REVISI/027_RENCANA_RESTRUKTURISASI_KODE_MK_CORE_STI_KONTINU.md',
    'KURIKULUM2026_REVISI/028_DEV_REPORT_DAN_LOG_RESTRUKTURISASI_KODE_CORE_STI.md',
    'KURIKULUM2026_REVISI/032_MODALITAS_PEMBELAJARAN_KPT2024.md',
    'KURIKULUM2026_REVISI/034_SEMBILAN_BENTUK_MBKM_DAN_REKOGNISI.md',
    'KURIKULUM2026_REVISI/035_RESTRUKTURISASI_KODE_MK_PEMINATAN_STA_STB_STC.md',
    'KURIKULUM2026_REVISI/036_DEV_REPORT_DAN_LOG_RESTRUKTURISASI_KODE_PEMINATAN.md',
    'KURIKULUM2026_REVISI/037_BOUNDARY_OF_TOPICS_DAN_MATRIKS_ANTI_OVERLAP_KURIKULUM.md',
    'KURIKULUM2026_REVISI/039_LAMPIRAN_SIAP_BUKU_KPT_SISTEKIN_2026.md',
    'KURIKULUM2026_REVISI/041_LAMPIRAN_BARU_BUKU_KPT.md',
    'KURIKULUM2026_REVISI/042_LAPORAN_AUDIT_KESELARASAN_KURIKULUM_DAN_BOUNDARY_OF_TOPICS.md',
    'KURIKULUM2026_REVISI/043_MATRIKS_CPL_CPMK_BoK_DAN_BOUNDARY_GUARDRAILS.md',
    'KURIKULUM2026_REVISI/043_MATRIKS_CPL_CPMK_BoK_DAN_BOUNDARY_GUARDRAILS_BACKUP.md',
    'KURIKULUM2026_REVISI/043_MATRIKS_CPL_CPMK_BoK_BOUNDARY_GUARDRAILS_PER_SEMESTER.md',
    'KURIKULUM2026_REVISI/043_MATRIKS_CPL_CPMK_BoK_BOUNDARY_GUARDRAILS_PER_SEMESTER-BACKUP.md',
    'KURIKULUM2026_REVISI/044_DEV_REPORT_DAN_LOG_PENYUSUNAN_MATRIKS_CPL_CPMK_BoK_GUARDRAILS.md',
    'KURIKULUM2026_REVISI/045_DRAFT_BUKU_KPT_SISTEKIN_2026_MENGIKUTI_TEMPLATE_DOCX.md',
    'KURIKULUM2026_REVISI/047_ANALISIS_KURIKULER_METODE_NUMERIK_VS_RISET_OPERASI_VS_BIG_DATA_STA601.md',
    'KURIKULUM2026_REVISI/049_LAPORAN_EVALUASI_DAN_REVISI_KURIKULUM_STA601_BIG_DATA_ENGINEERING.md',
    'KURIKULUM2026_REVISI/050_DEV_REPORT_DAN_LOG_PERTUKARAN_STRUKTUR_SEM6_SEM7_DAN_HARMONISASI_KURIKULUM.md',
    'KURIKULUM2026_REVISI/BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md',
    'AGENTS.md',
]

def update_file_codes(file_path: Path) -> dict:
    """Update kode MK di file markdown."""
    if not file_path.exists():
        return {'status': 'skip', 'reason': 'file not found'}
    
    content = file_path.read_text(encoding='utf-8')
    original_content = content
    total_replacements = 0
    
    # STRATEGI: Ganti kode dengan prioritas urutan
    # Karena STI-624 dan STI-625 muncul 2x (sebagai kode lama & target),
    # kita harus ganti dalam urutan: 626→624, 627→625, 624→726, 625→727
    
    # Tapi ini akan bentrok! Maka kita gunakan placeholder unik dulu
    
    # Tahap 1: 626→TEMP1, 627→TEMP2, 624→TEMP3, 625→TEMP4
    content = re.sub(r'STI-626', 'STI-TEMP1', content)
    content = re.sub(r'STI-627', 'STI-TEMP2', content)
    content = re.sub(r'STI-624', 'STI-TEMP3', content)
    content = re.sub(r'STI-625', 'STI-TEMP4', content)
    
    # Tahap 2: TEMP→final
    content = re.sub(r'STI-TEMP1', 'STI-624', content)
    content = re.sub(r'STI-TEMP2', 'STI-625', content)
    content = re.sub(r'STI-TEMP3', 'STI-726', content)
    content = re.sub(r'STI-TEMP4', 'STI-727', content)
    
    if content != original_content:
        file_path.write_text(content, encoding='utf-8')
        total_replacements = len(re.findall(r'STI-(624|625|726|727)', content)) - len(re.findall(r'STI-(624|625|726|727)', original_content))
        return {'status': 'updated', 'replacements': total_replacements}
    else:
        return {'status': 'no_change', 'replacements': 0}

def main():
    root_dir = Path(__file__).parent.parent
    results = []
    
    print("=" * 70)
    print("Update Kode MK: STI-626/627 → STI-624/625, STI-624/625 → STI-726/727")
    print("=" * 70)
    
    for file_rel_path in TARGET_FILES:
        file_path = root_dir / file_rel_path
        result = update_file_codes(file_path)
        results.append({
            'file': file_rel_path,
            **result
        })
        
        status_icon = '✅' if result['status'] == 'updated' else '⚠️' if result['status'] == 'skip' else '○'
        print(f"{status_icon} {file_rel_path}: {result['status']}")
        if result.get('replacements'):
            print(f"   ↳ {result['replacements']} net replacements")
    
    print("\n" + "=" * 70)
    print(f"Total files processed: {len(results)}")
    print(f"Updated: {sum(1 for r in results if r['status'] == 'updated')}")
    print(f"Skipped: {sum(1 for r in results if r['status'] == 'skip')}")
    print("=" * 70)

if __name__ == '__main__':
    main()
