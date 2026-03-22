"""
Project configuration — all analysis parameters in one place.
Updated to reflect PPMI harmonized data structure (Sep 2024 Overview Guide).

IMPORTANT: Variable names below are based on PPMI documentation. After your
first data download, verify actual column names against the annotated data
dictionary and update this file accordingly.
"""

from pathlib import Path

# ── Paths ──
PROJECT_ROOT = Path(__file__).parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"
DICTIONARIES_DIR = PROJECT_ROOT / "data" / "dictionaries"
FIGURES_DIR = PROJECT_ROOT / "figures"

# ── PPMI Metadata ──
DATA_DOWNLOAD_DATE = "2026-03-22"  # UPDATE after download
PPMI_RRID = "SCR_006431"

# ── Core Identifiers ──
PATIENT_ID = "PATNO"
EVENT_ID = "EVENT_ID"  # BL, V01, V02, V04, V06, V08, V10, V12, etc.

# ── Cohort Assignment (CORRECTED per Overview Guide) ──
# Use COHORT from Patient Status dataset, NOT APPRDX from Screening
COHORT_VAR = "COHORT"
COHORT_PD = 1
COHORT_HC = 2
COHORT_SWEDD = 3
COHORT_PRODROMAL = 4

# ── NSD Status (from SAA results) ──
NSD_STATUS_VAR = "NSD_Status"
NSD_POSITIVE = 1
NSD_NEGATIVE = 0

# ── MDS-UPDRS Part III Motor Subscores ──
# Item names from harmonized dataset — VERIFY against annotated data dictionary
TREMOR_ITEMS = [
    "NP3PTRMR", "NP3PTRML",     # Postural tremor R/L hands
    "NP3KTRMR", "NP3KTRML",     # Kinetic tremor R/L hands
    "NP3RTARU", "NP3RTALU",     # Rest tremor amplitude R/L upper
    "NP3RTARL", "NP3RTALL",     # Rest tremor amplitude R/L lower
    "NP3RTALJ",                   # Rest tremor amplitude lip/jaw
    "NP3RTCON",                   # Constancy of rest tremor
]

BRADY_ITEMS = [
    "NP3FTAPR", "NP3FTAPL",     # Finger tapping R/L
    "NP3HMOVR", "NP3HMOVL",     # Hand movements R/L
    "NP3PRSPR", "NP3PRSPL",     # Pronation-supination R/L
    "NP3TTAPR", "NP3TTAPL",     # Toe tapping R/L
    "NP3LGAGR", "NP3LGAGL",     # Leg agility R/L
]

RIGIDITY_ITEMS = [
    "NP3RIGRU", "NP3RIGLU",     # Rigidity R/L upper
    "NP3RIGRL", "NP3RIGLL",     # Rigidity R/L lower
    "NP3RIGNK",                   # Rigidity neck
]

GAIT_ITEMS = [
    "NP3GAIT",                    # Gait
    "NP3FRZGT",                   # Freezing of gait
    "NP3PSTBL",                   # Postural stability
]

# ── Motor Subtype Classification ──
# Stebbins et al., 2013, Movement Disorders
# TD/PIGD ratio: mean(TD items) / mean(PIGD items)
TD_ITEMS_FOR_RATIO = [
    "NP2TRMR",                    # Part II tremor item
    "NP3PTRMR", "NP3PTRML",
    "NP3KTRMR", "NP3KTRML",
    "NP3RTARU", "NP3RTALU",
    "NP3RTARL", "NP3RTALL",
    "NP3RTALJ", "NP3RTCON",
]
PIGD_ITEMS_FOR_RATIO = [
    "NP2WALK", "NP2FREZ",        # Part II gait/freezing items
    "NP3GAIT", "NP3FRZGT", "NP3PSTBL",
]
TD_THRESHOLD = 1.15       # ratio > 1.15 = Tremor-Dominant
PIGD_THRESHOLD = 0.90     # ratio < 0.90 = PIGD
# 0.90–1.15 = Indeterminate

# ── DAT-SPECT Variables ──
# VERIFY exact column names from harmonized Imaging data
DAT_CAUDATE_R = "DATSCAN_CAUDATE_R"
DAT_CAUDATE_L = "DATSCAN_CAUDATE_L"
DAT_PUTAMEN_R = "DATSCAN_PUTAMEN_R"
DAT_PUTAMEN_L = "DATSCAN_PUTAMEN_L"

# ── CSF Biomarkers (from Biomarker Dashboard) ──
# Project 124: Alpha-Synuclein (BioLegend ELISA) — N=517 PD at BL
# Project 155: Alpha-Synuclein SAA (Amprion PMCA) — N=731 PD at BL
# Project 125/159: ABeta 1-42, pTau 181, tTau (Roche Elecsys)
# Project 152: Roche NeuroTool Kit (GFAP, NfL, S100b, YKL40, sTREM2, IL-6)

# ── Verily Study Watch (Digital Sensor section) ──
# Derived measures provided by Verily — weekly averages
# Exact variable names TBD on data download — check Digital Sensor section
VERILY_FEATURES_EXPECTED = [
    "sleep_duration", "sleep_efficiency",
    "total_physical_activity", "active_minutes", "step_count",
    "heart_rate_mean", "heart_rate_variability",
]

# ── Roche PD Mobile App (Digital Sensor section) ──
# Active tests: finger tapping, hand turning, drawing, balance, gait, speech
# Passive monitoring: smartphone + smartwatch
# Separate study NCT03100149, data available in PPMI

# ── Analysis Parameters ──
CONCORDANCE_THRESHOLD = 0.4     # r below this = "diverged"
ALPHA = 0.05
BONFERRONI = True
MIN_VISITS_LONGITUDINAL = 2
WEARABLE_CLINICAL_WINDOW_DAYS = 14  # match wearable weeks to visits within ±14 days

# ── Confounders ──
CONFOUNDERS = ["LEDD", "age_at_visit", "sex", "disease_duration_months"]
# LEDD = Levodopa Equivalent Daily Dose (from Concomitant Medications)
# DBS status: exclude patients with Deep Brain Stimulation