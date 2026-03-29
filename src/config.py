"""
Project configuration — all analysis parameters in one place.
Change these values to reproduce with different thresholds.
"""

# ── Data Download Date (required by PPMI Publication Policy) ──
DATA_DOWNLOAD_DATE = "2026-XX-XX"   # ← update this when you download PPMI data

# ── Paths ──
RAW_DATA_DIR     = "data/raw"
PROCESSED_DATA_DIR = "data/processed"
FIGURES_DIR      = "figures"

# ── PPMI Key Variable Names ──
PATIENT_ID  = "PATNO"
EVENT_ID    = "EVENT_ID"
VISIT_DATE  = "INFODT"

# ── MDS-UPDRS Part III Subscores ──
# Tremor: items 3.15a-e, 3.16a-b, 3.17a-e, 3.18
TREMOR_ITEMS = [
    "NP3PTRMR", "NP3PTRML", "NP3KTRMR", "NP3KTRML",
    "NP3RTARU", "NP3RTALU", "NP3RTARL", "NP3RTALL",
    "NP3RTALJ", "NP3RTCON"
]
# Bradykinesia: items 3.4a-b, 3.5a-b, 3.6a-b, 3.7a-b, 3.8a-b
BRADY_ITEMS = [
    "NP3FTAPR", "NP3FTAPL", "NP3HMOVR", "NP3HMOVL",
    "NP3PRSPR", "NP3PRSPL", "NP3TTAPR", "NP3TTAPL",
    "NP3LGAGR", "NP3LGAGL"
]
# Rigidity: items 3.3a-e
RIGIDITY_ITEMS = ["NP3RIGRU", "NP3RIGLU", "NP3RIGRL", "NP3RIGLL", "NP3RIGNK"]
# Gait / Postural stability: items 3.10, 3.11, 3.12
GAIT_ITEMS = ["NP3GAIT", "NP3FRZGT", "NP3PSTBL"]

# ── Motor Subtype Classification (Stebbins et al., 2013) ──
# TD ratio > 1.15 → Tremor-Dominant
# TD ratio < 0.90 → PIGD
# 0.90 – 1.15    → Indeterminate
PIGD_ITEMS = ["NP2WALK", "NP2FREZ", "NP3GAIT", "NP3FRZGT", "NP3PSTBL"]
TD_ITEMS_FOR_RATIO = [
    "NP2TRMR", "NP3PTRMR", "NP3PTRML", "NP3KTRMR", "NP3KTRML",
    "NP3RTARU", "NP3RTALU", "NP3RTARL", "NP3RTALL", "NP3RTALJ", "NP3RTCON"
]
TD_THRESHOLD   = 1.15
PIGD_THRESHOLD = 0.90

# ── DAT-SPECT Variables ──
DAT_CAUDATE_R = "DATSCAN_CAUDATE_R"
DAT_CAUDATE_L = "DATSCAN_CAUDATE_L"
DAT_PUTAMEN_R = "DATSCAN_PUTAMEN_R"
DAT_PUTAMEN_L = "DATSCAN_PUTAMEN_L"

# ── CSF Biomarkers ──
CSF_ALPHA_SYN = "CSF_ALPHA_SYNUCLEIN"
CSF_PTAU181   = "PTAU181"
CSF_TTAU      = "TTAU"
CSF_ABETA42   = "ABETA42"
CSF_NfL       = "NFL_CSF"
SERUM_NfL     = "NFL_SERUM"

# ── Verily Study Watch Derived Measures ──
# NOTE: Update these names after inspecting the actual downloaded CSV headers
VERILY_SLEEP_DURATION  = "SLEEP_DURATION_HOURS"
VERILY_SLEEP_EFFICIENCY = "SLEEP_EFFICIENCY"
VERILY_TOTAL_ACTIVITY  = "TOTAL_PHYSICAL_ACTIVITY"
VERILY_ACTIVE_MINUTES  = "ACTIVE_MINUTES"
VERILY_STEP_COUNT      = "STEP_COUNT"
VERILY_HRV             = "HEART_RATE_VARIABILITY"

# ── Analysis Parameters ──
CONCORDANCE_THRESHOLD    = 0.4   # Spearman r below this = "diverged"
ALPHA                    = 0.05  # significance threshold
BONFERRONI               = True  # apply Bonferroni correction
MIN_VISITS_LONGITUDINAL  = 2     # minimum visits per patient for longitudinal analysis
WEARABLE_WINDOW_DAYS     = 14    # days around a clinical visit to average wearable data