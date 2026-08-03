# W1 premise refuted mid-flight; ETFS July finals delivered to Andrew; four rulings issued

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, DIAGNOSE, SCRIBE

Continues `mdlp_monpub_fix_ordering_and_c3l1_loop_close_1435-1450Z.md` @3183d63b4d. Two threads
interleaved live: the MDLP_MONPUB incident arc (CVO GO -> W1 refutation -> STOPs -> rulings) and
an Andrew-direct ETFS July briefing + deliverables ask, executed simultaneously.

## 1. MDLP_MONPUB arc (chronological)

- **CVO CONDITIONAL GO** (145054Z @f4ab1ae778) folded @2733bfceff: W2 build-before-publish
  amendment (FAILED executions PUBLISH -- upload_json :316/:319 precedes the :324 crash),
  W1 estate probe, residuals R1/R2, W3 Choice widening. CVO re-read -> **UNCONDITIONAL** (150701Z).
- **W1 PREMISE REFUTED** (MSTR~Z 151159Z): the "known-good 07-30" build is GARBAGE on ST
  (content-verified; 1Y -13.64 vs bmk +4.74) and the 13:27Z "clobber" was Andrew's DELIBERATE
  rollback. [STOP]s (ACK-required) to DS+DT same turn; served key ETag-verified NOT fired;
  W1 BLOCKED @626ab523a4 behind a content sanity gate. CVO independently content-confirmed both
  directions + banked its own miss @d077c9a4db. **Class lesson, banked to memory by the fabric:
  "known-good" is a CONTENT claim -- 3 agents + CVO carried it unread into a republish order.**
- **Residual re-armed + resolved:** DS's pre-hold retry had re-staged the 07-30 pkls in uploads/;
  Andrew-direct GO ("yeah we can delete those") relayed via MSTR; deleted with evidence.
- **W4 root cause source-confirmed** (MSTR~Z 153412Z): Yang nb cell-16 month-end double-append
  (0731: 60 lossless price_monthly dups + 168 NON-value-identical return_monthly dups -- naive
  groupby().last() would destroy field data); 0730 wrong-instrument = terminal-side custom-index
  resolution (.ST resolved to a different instrument's 1449-row history). **CONTENT GATE added to
  W4 acceptance @6239fe3ebb** (ST inception 2023-12-29 / ~676 rows / price ~112.5). Yang re-pull
  risk + Bloomberg -4003 review-block flagged to Andrew by MSTR directly.
- **W2/W3 code legs closed by DS** (05dcbe7651 / b48785adad). **Rulings issued (155100Z):**
  (1) W3 keeps Choice handling -- criterion 3 = zero Task-state loss, not byte-identity;
  (2) W2's exercised-PASSING leg DEFERS TO AND IS W4's content-gated recovery publish -- no
  synthetic newer-date publish touches Andrew's chosen 07-27 serve; W2 records as
  DEPLOYED-EXERCISED-PENDING-PASSING-LEG (named third state). NoSuchKey-vs-other-errors split
  approved (fail closed on ambiguity).
- **Division with COO:** COO drives RAVC loops; I hold arch gates + CVO witness points.

## 2. ETFS July finals (Andrew-direct, delivered)

Package committed under `org/tier1_exec/1.0.0_SA_CTO/deliverables/ETFS_JULY_2026_FINAL/`:
workbook (Excel-COM recalc, 0 formula errors; totals cross-checked to @5f27b84c0f exactly),
6-slide briefing deck (validated + visually QA'd via PowerPoint COM export; 3 defects found+fixed
in QA), corrected trading-day CSVs x3, as-delivered Aug-1 CSVs preserved labeled, README.

**The finding the build surfaced (new, quantified):** the Aug-1 DELIVERED CSVs were stale --
inflection carried 7 weekdays (backfill landed 14:10Z, 4h AFTER the 10:00Z fire; ~$622K
understated on TD-mean), cottonwood 2 days (pre-repoint 07-20: 48.39M->50.29M; carried 07-31;
~$79K), 49financial EXACT. The partial-flag defect observed live. Final basis (TD-mean, 22
trading days, AVGCAP aggregation still UNCONFIRMED): 49F $528,375,243.69 · cottonwood
$33,861,836.15 · inflection $47,608,356.91 published / $48,032,419.82 true-settled
(+$424,062.91 / 0.891%) · combined $609,845,436.75.

## 3. Arch-gate + housekeeping

- **PASS (permanent-scoped):** 0.2.0_DS into YANG_PIPELINE_DEPLOY + DATA_REFRESH_DEPLOY,
  grounded on .owned-paths.yaml:343/:369 directly; COO grantor-landed @46d4b1110d (SoD held).
- COO closed the 10 expired findings (@52bcb6c1b5); closeout-hook defect routed to
  0.8.0_AE_CloudComp~B under COO dispatch; NFRA_TOOLSTACK umbrella row: my call =
  Complete-as-superseded, COO executes.
- **Gate candidate banked (COO observation, real):** workspace-side SURFACE_ACK set on a
  hand-run SEV1 verdict is NEVER consumed when the staged file is not a watched carve token --
  conscientious ack and skipped hand-run are audit-identical. Fix shape: safe-commit consumes
  SURFACE_ACK whenever set (voluntary-ack audit line). Unrouted, non-urgent.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `comp-estate etf-reports` | PASS | producer roster for the ETFS vertical (grounded the artifact hunt) |
| `comp-blast` (x2, earlier window) | PASS w/ known cp1252 defect | radii unchanged on re-measure by DS |
| `comp-surface-check check` | PASS (SEV1 named) | discipline carried into W2/W3 TOs; DS exercised it live |
| Excel COM recalc + PowerPoint COM export | PASS | the working substitutes for the skills' LibreOffice tooling on this box (AF_UNIX broken); banked as the local pattern |
| `head-object`/body reads (live, x4) | PASS | W1 fired-check, serve-clean checks, delivered-CSV grounding |
| pptx `validate.py` | PASS under `PYTHONUTF8=1` | bare run false-fails on cp1252 (same class as comp-blast defect) |

## Current State / Next Steps

- [DT] W2/W3 deploys (TF-only, simulate+positive-control, ledger); CVO witnesses W2 failing legs.
- [W4/DS+MSTR~Z] corrected-0731 dedup (field-bearing-row rule) behind sitez trace + content gate;
  its recovery publish closes W2's passing leg.
- [ANDREW] AVGCAP aggregation confirmation (gates final certainty on every July figure);
  normalization build + restatement decisions; C3L.1 still on /open-calls.
- [CTO] W1 unblock adjudication when a content-gated clean target exists.
