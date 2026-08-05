# Instruments cleared, cycle-4 ratified, v6 characterized — and a ratification I retracted on my own measurement

**archetype:** MIXED (VALIDATE + DIAGNOSE + COORDINATE)
**Serial:** `1.0.0_SA_CTO~B` **Window:** 2026-08-04 19:10Z – 2026-08-05 01:30Z
**Andrew-direct (~002xZ, verbatim @deliverables/ANDREW_DIRECT_20260805_tools_ready_cycle4_ratification_proceed.md):** *"Comp-cochange and comp-heat are good to go, please make sure they are both ready to rock (officially registered through comp-tool canonical registration). Cycle-4 Ratification should be able to proceed. Then can look into v6"*
**Counterparts:** `4.0.0_SA_CRO` (RCG, ~8 round trips), `3.0.0_SA_CVO` (dial + seam), `0.7.0_AE_CloudOps~E` (Rule-1 closure).

## 1. Instrument readiness — the gate passed and the tool was still unreachable

`comp-manifest-check completeness` PASS; comp-cochange born-registered `status: canonical`.
**And it resolved on no agent's PATH.** The registration invariant scopes to *tracked-and-committed
on disk*, not *runnable in a shell* — so a tool can satisfy every registration gate and be dead to
every consumer. Fixed (`provision-path-shims.sh`, 96 tools × 2 forms), then **exercised, not
resolved**: comp-cochange `--self-test` 7/7 + 4/4 + live `matrix` (pairs, jaccard, both
denominators, HEAD anchor); comp-heat `--json` returns the exact F2 contract (`half_life_days`,
`summary.mean_score`, per-path `score`). Curated directive entry added (@69e800bbd; rule-bank
two-phase override discharged @02d3cb1c3). **Andrew's Phase-0 sequencing gate is discharged.**

## 2. Cycle-4 ratification relayed — and stopped by law before pass-through

His word went to CRO verbatim. Their gating question (ratify `docs/architecture/archive/` for
completed-project PRDs) **contradicts standing law**: `org/XXX.md` — *"PRDs are NOT a close step.
They stay in `docs/architecture/`; do not archive them."* Their cited precedent (@a749324e7b) I
checked at source: 40 **stale infra docs**, a different artifact class. Denied for PRDs; ratified
`docs/briefs/archive/` for the dated-brief subclass (later narrowed — §4). CRO landed 15 PRD KEEP
corrections with exact-path enforcement rows.
**Class named: LABEL-vs-LAW.** The new VERDICTS gate validates label-vs-RULING and structurally
cannot see label-vs-LAW. The only thing between that proposal and execution was a reviewer
remembering a line in XXX.md — *not a control*. Sitting item.

## 3. v6 band — the decision surface is 30, not 172

Re-derived from `predictions.jsonl` (14,947 rows, single model_version, verified). Band 172, but
**142 already carry KEEP seeds** (model unsure, ledger is not → calibration data, not agenda). The
real surface: 22 unseeded + 8 archive-doubts. The 22 collapse to **4 cohorts** — 8 files under
`org/modules/perceive`+`act` at *identical* p_archive 0.465 (identical feature vector = one object
= one verdict), 3 `bd-gold` Step Functions (**deploy-coupled → handoff class regardless of label**),
the `market_update/news_recap` locus, 3 singletons.
Two findings worth keeping: the band **widening** 151→172 is the instrument RECOVERING (v5's 4,103
wrong-side max-weight labels had falsely sharpened the boundary — 151 was the number to distrust);
and the **top locus is unchanged across the repair**, so the archive signal survived its own
contamination. Also: the model independently doubted 3 of the same `docs/architecture` files the
law ruling pinned — *independent-derivation convergence*, the kind that counts.

## 4. The retraction — I ratified before I measured, and the measurement said no

Cleared the 12-file move-list. **2 moved, 10 pinned**, and I retracted my own 004346Z
`docs/briefs/archive/` ratification to do it. Measured citation-liveness across docs AND code:
**all 8 dated briefs are alive**, two cited by **production Lambda source**
(`ws2_factor_tilts_pull.py` → mdsrc-c5; `yang-model-portfolio-benchmarks/lambda_function.py` →
bmkaud-ws3). The second is the instructive one: it was the *only* brief with zero live-doc
citations, so a docs-only census would have cleared it — **the code check is the sole reason it
survived.** Moving that cohort would have edited two production Lambdas for directory tidiness.
**Predicate banked (CRO D-C006): relocation eligibility is CITATION-LIVENESS across docs AND code,
never a filename pattern.** Dated-filename predicted deadness 0 for 8.
Five per-file calls: all KEEP. Three **self-declare as PRDs in their own first lines** →
**the law binds on what a document IS, not its filename suffix**; filename-suffix classification of
a law-pinned artifact is the name-pattern stopgap class. CRO now enforces law-pinning by CONTENT.

## 5. Also closed

AE~E's Rule-1 census closure accepted (7/7 dispositioned; **the decommission dossiers I explicitly
did NOT close** — Andrew-confirm class, carried OPEN-AT-ANDREW so 7/7-dispositioned is never read as
7/7-resolved). **CORRECTED by AE~E 004443Z: the open set is TWO, not three** — I read the original
verdict table and missed the same-file ADDENDUM (@0983e372a) where base CTO ruled D2
`schwab-anonymizer` ADOPT-NOW (already imported zero-diff into security-ops, tag
`security-ops-v0.2.1`); its retire question rides a later 49F owner consult and is NOT in the
deletion queue. Open-at-Andrew = `opal-bd-transaction-consolidator` + `sentiment_query_api`.
*A deliverable I cited by commit was amended in place after I read it — reading a file once and
citing it later is a vintage claim, and mine was stale by minutes.* CVO's missions-STANCE seam absorbed with a precedence rule (ratified value outranks a
migrated seed). Kimi pipeline ran its first scheduled-era day; F2 ruled scores-only.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `comp-manifest-check completeness` | PASS | 88 executables accounted; **passed while comp-cochange was PATH-unreachable — the gap this log's §1 names** |
| `comp-cochange --self-test` + `matrix` | 7/7, 4/4, live | first exercise as an F4 instrument |
| `comp-heat freshness --json` | PASS | F2 contract confirmed on a live tree |
| `comp-grep` x4 | PASS | citation censuses, denominators printed |
| `comp-system --regen` | PASS | discharged the rule-bank two-phase override |
| `manifest_check.py` (RCG) | CLEAN + 314 INFO | ran independently at my seat, not accepted on report |
| raw `grep`/`git`/`python` | used | citation-liveness across docs AND code; ledger re-derivations — no comp-tool models label×law×citation intersection |

## Open at session end

Andrew's sitting: v6 4 cohorts + 2 architecture calls · cohort-B verdict · 314-row precedence
residue · law-pinned-path predicate · 2 decommission dossiers. Kimi: comp-cochange gate half now
cleared → **Phase-0 sitting is unblocked**; v3 runner build (~B quiet window) still open.
