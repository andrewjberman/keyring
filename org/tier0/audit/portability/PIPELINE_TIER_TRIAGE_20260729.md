# PIPELINE_CODE tier — triage, severity correction, and routing

**Author:** `0.0.0_AB_MSTR~Z` · 2026-07-29
**Register of record:** `org/tier0/audit/portability/` (base confirmed this is canonical, amb-b-0008)
**Status:** triaged, NOT fixed — routed to owners. See §4 for why I did not touch these.

---

## 1. The numbers, with the denominator

From `census-siteZ-20260729.json` (24,778 tracked / 22,964 read / 1,814 unreadable):

| tier | count | meaning |
|---|---|---|
| live-code hardcode, executable | **103** | the raw candidate set |
| of those, **DEPLOYED** (in `lambda-source-map.json`) | 13 | |
| of those, **PIPELINE** `gold/silver/bronze` | 2 | |
| **one-off analysis / probes / misc** | 89 | |

## 2. SEVERITY CORRECTION — the "13 deployed" figure overstates the risk

**I am flagging this against my own numbers, because the raw count invites the wrong conclusion.**

The `smartx` `config.py` family (3 copies: `data/smartx/scripts/`,
`infra/aws/ec2/smartx-exporter/…`, `infra/aws/lambda/smartx_ingestion_pipeline/`) carries:

```python
# Local development paths
if platform.system() == "Windows":
    LOCAL_STAGING_DIR = r"C:\Users\AndrewBerman\OneDrive - Opal Capital\Desktop\ajb_workspace\..."
```

**That branch cannot execute on Lambda — Lambda is Linux.** So the DEPLOYED RUNTIME IS NOT
AFFECTED by these. The exposure is **local execution on a Windows device that is not base**, which
is exactly site Z, and nowhere else.

This is the same over-severity error I made on the six `comp-*` tools, where I labelled a
never-taken fallback as "breaks Z now." **A tier label that overstates spends attention in the
wrong place just as surely as one that understates.** The honest reading:

- **deployed runtime risk: NONE** from this family
- **local-dev-at-Z risk: REAL** — a Z developer running these gets a path that does not exist
- **`/mnt/c/Users/AndrewBerman/.win32s`** (same files, line 15) is a **WSL** secrets path — a
  *fourth* path flavour after `/c/`, `/cygdrive/c/`, and `/mnt/c/…/OneDrive…`

## 3. The genuinely-live one

`data/black_diamond/scripts/silver/merge-capital-gains.py:29`
```python
DOWNLOADS = Path(r'C:\Users\AndrewBerman\Downloads')
```
Not a guarded branch — an unconditional assignment reading base's Downloads folder. It is a
manual-input script (its header names a hand-downloaded `.xlsx`), so it is not on a schedule,
but it *would* fail immediately at Z with no fallback.

## 4. WHY I DID NOT FIX ANY OF THESE — ownership, not caution

**CLAUDE.md Rule 13 is explicit:** DS owns `data/*/scripts/{gold,silver,bronze}/*.py` end to end;
DT/AE own infra. Every file in §2–§3 is on one of those lanes, not mine. My charter is device
portability; it is not a licence to edit other lanes' pipeline code, and a portability fix that
lands in DS's silver tier without DS is exactly the kind of cross-lane edit the ownership rule
exists to prevent.

**Routing instead:**

| files | owner | recommended change |
|---|---|---|
| `smartx` `config.py` ×3 + `compute_account_distribution.py` ×2 + `consolidate_smartx_to_parquet.py` ×2 | **DS** (+ AE for the infra copies) | derive the Windows branch from the script's own location, or read an env var; the `.win32s` WSL path needs the same |
| `black_diamond/scripts/silver/merge-capital-gains.py` | **DS** | `Path.home()/"Downloads"` — portable, no site literal |
| `infra/aws/lambda/smartx_*` copies | **AE/DT** | same fix as the DS copies; note these are **duplicated** source, so a fix in one place does not travel |

**A structural note worth more than the individual fixes:** `config.py`,
`compute_account_distribution.py` and `consolidate_smartx_to_parquet.py` each exist in **three
copies** (`data/`, `infra/aws/ec2/…`, `infra/aws/lambda/…`) carrying the **same** literals. That is
one defect stamped three times, and fixing one copy leaves two. Whoever takes this should treat
the duplication as the primary finding and the path literal as its symptom.

## 5. The 89 one-off scripts

Probes, backfills, ad-hoc analysis (`data/inf/manual_api/probe_*`, `data/analysis/nna_*`, …).
Real hardcodes, but they are historical artifacts that ran once at base. **Recommendation: leave
them.** Rewriting 89 dead scripts spends the night for no live benefit, and each edit is a
cross-lane touch. If one is ever re-run at Z it fails loudly and obviously — the cheap failure
direction. They are enumerated in the census JSON if anyone wants the list.

## 6. What this closes

- `ACTIVE_TOOLING` tier: **CLOSED** (12/12 — 6 `comp-*` @`e95fdd7e42`, 4 harnesses +
  `block-bare-inbox-watch` @`a13254d38`, `settings.local.json` is permission-allowlist strings only).
- `PIPELINE_CODE` tier: **TRIAGED AND ROUTED** — not mine to land.
- Remaining unworked: `ARCHIVE_OR_TEST` (10), `COMMENT_ONLY` (1) — lowest value, and
  comment-only may be correct to keep as incident documentation.
