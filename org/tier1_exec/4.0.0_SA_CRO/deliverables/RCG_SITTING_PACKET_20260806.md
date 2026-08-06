# RCG Sitting Packet — 2026-08-06 (Andrew-direct GO, CRO terminal ~1440Z)

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Basis:** scan vintage `20260804T174531Z_f919615b`, model v6 `465f15ce` (single-version verified),
ledger @HEAD this hour (26,488 rows / 17,512 paths; 1 pathless schema row disclosed). All 172 band
files verified still present on the current tree. Prior art folded: CTO~B's
`RCG_V6_BAND_ANALYSIS_20260805.md` (cohort structure adopted; denominators RE-DERIVED at today's
ledger — theirs was an earlier cut, numbers differ, structure holds).

**Decision surface: 4 items, ~30 words of rulings.** Band 172 decomposes: 66 ledger-KEEP + 79
ledger-non-KEEP (labeled; model-doubt rows — my post-sitting per-file review queue under R-0020,
not sitting questions) + **27 genuinely undecided** (no ledger row) — grouped below into 4 cohorts.

---

## ITEM 1 — packet controls: re-cut from ratified truth (program QA, surfaced first)

Running `packet.py` on this vintage **QUARANTINED — 3/4 planted controls misgraded, nothing
ships.** Grounded diagnosis: the controls draw their "truth" from **heuristic seeds**
(`seed:declared-dead`, `seed:root-or-cited`), and every failure sits exactly where **ratified law
has departed from the heuristic**:
- `org/projects/SXIN_DAY1ZG.json` seed=archive (dead-marker) vs model KEEP 0.012 — governance JSONs
  are law-KEEP class (closure discipline); **the model learned your law, the seed didn't.**
- `infra/aws/lambda/infrastructure_monitor/openai/types/...` seed=KEEP (reachability) vs model
  archive 0.999 — vendored dep trees are cohort-A archive class; **reachability structurally marks
  every vendored file KEEP.**
- `infra/aws/lambda/TERRAFORM_DEPLOYMENT_MANDATORY.md` seed=archive vs model 0.146 — genuinely
  adjudicable; the seed is still a heuristic, not a truth.

**The model outgrew its control layer.** A control whose oracle is weaker than its subject fires on
the subject surpassing it, indistinguishably from a regression — these three pattern-match
surpassing. I did NOT bypass the quarantine and did NOT re-cut controls on my own word (re-cutting
to make a packet ship is re-authoring the denominator).

**CALL: re-derive packet controls from RATIFIED/adjudicated ledger rows (heuristic seeds stay as
model features, never as control truths)? REC: GO** — one small packet.py change, mine to land,
mutant-exercised before use.

## ITEM 2 — the seeking-alpha trio (your files) + the locus cascade

All Andrew-authored, Jan-23→Feb-02 vintage, untouched 6 months, cited only by their own cluster;
MSTR's 07-15 cold census already reads `tools/seeking-alpha-ui/` as "dead UI experiment"
(163-174d cold, 30 files). The locus (`data/seeking-alpha` + `tools/market_update` +
`seeking-alpha-ui`) is v6's top archive-candidate signal, **unchanged v5→v6** (survived the ledger
repair — the signal is real, not label bookkeeping).

| Unit | Evidence | REC |
|---|---|---|
| `tools/seeking-alpha-ui/` tree (README.md + THREE_BUTTON_WORKFLOW.md + WEB_UI_UPDATED.md + backend/) | React UI for Lambda scraper backfills, "Production Ready" Jan-23; no external citers | **ARCHIVE** |
| `data/seeking-alpha/backfill_ui.py` (+ launch-ui.sh + UI_README.md cluster) | terminal UI, same system, same vintage; only self-cites | **ARCHIVE** |
| cascade member (in-band, no ledger row): `data/seeking-alpha/scripts/parallel_scraper_coordinator.py` | same locus | your word patterns it |

All sweeps reversible (B-0008 revert drill exercised byte-identical). Note kept distinct: the
finbert-batch-processor (2 ENABLED schedules) was ruled KEEP 08-05 — archiving the UI tooling does
not touch the scheduled sentiment pipeline.

## ITEM 3 — the 27 genuinely undecided, as 4 cohort rulings

**3a. `org/modules/perceive/` + `org/modules/act/` (8 files, p_archive uniformly 0.465 — one
feature-vector object). REC: KEEP.** Measured this hour: imported by
`org/ka_testing/runtime/pipelines/{classification_pipeline,corpus_ingestion}.py` and cited by 2
architecture docs — archiving breaks live imports.

**3b. infra/ (12 files). REC: ARCHIVE the 3 `bd-gold-*` Step Function definitions** — measured
this hour: the account/region holds exactly ONE state machine (`YangDataPipeline`, denominator
printed); all three definitions back nothing live. Remaining 9 (rollback README+script, scripts
pair, `security/policies/README.md` 0.640 — highest in band, `testing/smoke/critical-paths.sh`,
`orchestration/config/.bashrc.agents`, + 2): archive-lean per model; a single cohort word covers
them or leave to my R-0020 per-file queue.

**3c. `tools/market_update/components/news_recap/` (6 files). YOUR WORD** — top candidate locus
both vintages, but it neighbors the KEPT finbert pipeline; your estate knowledge outranks the
model here. Model says archive-lean (0.54-0.61).

**3d. Singletons (2), one carrying a loud flag:**
- `timeseries/vix.json` (0.396) — survived the ratified B-0007 timeseries batch; presumably kept
  deliberately then. REC: KEEP (consistency with B-0007).
- ⚠ `data/smartx/staging/account_distribution.json` (UNDERSCORE) — **a DIFFERENT file from the
  hyphenated `account-distribution.json` that is the LIVE SERVED PORTAL BELL** (standing memory:
  never treat the hyphenated one as abandoned). This underscore/staging one is the plausibly-dead
  sibling. REC: your word, with the hyphen distinction held loudly so no verdict bleeds across.

## ITEM 4 — E-0005 blind-eval readout

CVO~B pinged at 1456Z (sitting-GO relay + the control-provenance caveat for their blind protocol).
Slot open; folds into this record on arrival. SENT, not yet ACKed — stated per SENT-is-not-READ.

---

*Everything above that is a measurement carries its denominator in-line; everything that is a
proposal says REC. Ratified outcomes land in the ledger (RULINGS/LABELS), never in this packet.*
