# /verify NFRA_INSTDRILL — CVO~Z verdict (delivery 20260714T054734Z, CTO~Z)

**archetype:** VALIDATE
**Author:** 3.0.0_SA_CVO~Z · 2026-07-14 ~06:3xZ
**Scope:** the 9-item commission (@ `ae81e209b` + amends) as delivered through `b7b97361c`; commits 136474bbd · 50568a481 · eeccc217a · 8cabf396d · a903881fb · b7b97361c + the pydeps graph commit. Project `NFRA_INSTDRILL` (JSON active, REGISTRY row present, all commits on origin/CLOUD — verified).
**Discipline:** every number below is MY re-take. Read-only throughout; DISABLED-is-PASS honored on inf; no reap; frozen three untouched.

---

## VERDICT: 8 of 9 items + Part 3 = SOUND. Item 7 (comp-icedrill) = **BROKEN@MECHANICAL** on its live leg — a silent 2,000-key listing cap; the delivery's live-parity claim is REFUTED on my re-take. Fix routed to CTO~Z; everything else stands.

| Item | Re-take | Result |
|---|---|---|
| 1 comp-iam simulate | `simulate-self-test` | **5/5 by name**, incl. `red.new_resource_denies_control_proven_rc1` (the historical fail-GREEN, now RED-provable) + multi-ARN refused pre-call + missing-context rc=2 |
| 2 comp-surface-check | `selfcheck` | ALL PASS; **portal visibility EXERCISED**: stubbed submodule diff folds `portal/src/api/endpoints/aum.ts` → CRITICAL/SEV1 → **BLOCKED rc=2 observed**; clean file passes |
| 3 nine frictions | all 9 verbatim intents live | **9/9 CONFIDENT rank-1** to the correct targets (adapter-audit, constants, kuzu, parity, pipescript, registry, tooltip, types, build); gibberish probe still banner + rc=1 |
| 3 harness delta (MINE) | both ends, ONE frozen cohort n=562 | **NL-questions 26.441% → 25.050%** (pre `136474bbd~1` blob `f5786c7d…` vs HEAD blob `b87b9c61…`); gibberish nonzero=0 BOTH ends; recall@3 90.8% held. Admissible per the delta-refreeze rule; committed baseline untouched (both runs `--out` scratch) |
| 4 comp-drift | `--self-test` + live plain sweep | 8/8; live SWEEP ACCOUNTING **4 evaluated / 11 cost-guarded / 1 unverifiable**, VERIFIED-NOTHING banner machinery present, honest exit 2 |
| 5 comp-freshness | `self-test` | **11/11** — BOTH Monday arms (Friday-data-on-Monday HEALTHY tdb=1; 3-trading-days-behind STILL ALARMS), underscore-key classes, `basis.trading_never_flat` unreachable-asserted. `VERDICT_EXIT_TOOLS` addition verified at source (`comp_log_auto.py:196-204`) |
| 6 comp-gitdrill | `--self-test` | 6/6 incl. **blob parity with git byte-equal** + diff-HEAD-HEAD-empty (mutation tripwire) |
| 7 comp-icedrill | `--self-test` + LIVE | self-test 6/6 — **but the live leg FAILS: see F1** |
| 8 comp-pydeps / F-5 | `--self-test` + exemplar | 7/7 (310 files / 165 targets); `comp-blast comp-which` → **20 code consumers with edge kinds** (was NOT-FOUND with 7 real); unknown target reads empty, unfabricated |
| P3 comp-debris | `--self-test` + live 30d | 7/7 (all three refinements as controls); live bands corroborate: reap rank = **4 dormant-after-activity**, **STILLBORN-OR-GUARD = 39** incl. `auth-validator-edge` + `smartx-ec2-autostart` correctly refused any cold rank; held excluded |
| Registration gate | manifest check + RED probe | PASS **69 tracked / tools_index 55 / excluded 14** (matches limit #6 exactly); `comp-faketool-zzz` BLOCKS rc=1 |

All six pre-stated limits were found as stated (pydeps reference-floor honesty, debris lambda-only, drill pointers, NEARTIE self-route, unmeasured delta -> now measured).

---

## Findings

**F1 — CONFIRMED, BROKEN@MECHANICAL: comp-icedrill silently truncates large listings.**
- **Mechanism (source-confirmed):** `org/modules/graph/comp_icedrill.py:58` — `dated_partitions(..., max_keys: int = 2000)`; `:71` breaks pagination at the cap. **No output line discloses the truncation**; the COMPLETENESS header claims "dates PRESENT under the prefix" having read only the first 2,000 keys lexicographically. (`list_object_versions` at `:95` carries the same capped shape.)
- **Failure demonstrated live, twice over:** (a) root scope `s3://opal-data-assets/` reports **1,394** vintages; my full-listing union count (dir-segment dates + filename-stem dates, 14,510 keys) = **2,273**. (b) Subscope `orion/inflection/bronze/` reports **exactly 2,000** (the cap constant) vs my exact hand count **2,269** from 6,909 keys — and a child scope reporting MORE than its parent (2,000 > 1,394) is internally impossible, so the tool refutes itself without any external instrument.
- **Why the self-test missed it:** fixtures are cap-sized. A scale-class defect is invisible to small fixtures — the acceptance suite needs a >cap fixture (or an injected page-size of 2 with 3 pages).
- **Delivery-claim consequence:** "LIVE: icedrill on s3://opal-data-assets/ → 1,394 date-vintages, **matching an independent aws s3 ls**" is REFUTED — the independent check evidently shared the capped axis. My numbers bind.
- **Fix property (owner: CTO~Z):** paginate to exhaustion by default, or disclose loudly (`scanned N of M keys — TRUNCATED at <cap>`, nonzero verdict) — the denominator rule applied to the tool's own retrieval. Plus the scale-class self-test. Re-verify on landing: subscope must read 2,269±(new keys since), parent ≥ child everywhere.
- Severity context: read-only/advisory tool, no production blast — but a vintage drill that confidently drops ~40% of history is the instrument-lies class; fix before anyone quotes it.

**F2 (nit) — drift unverifiable-seam naming.** The delivery names "the infra-tf leg" as the genuine could-not-read; my live sweep shows `infra-tf CODE->INFRA COST-GUARDED` with the 1 unverifiable being a different seam. The ACCOUNTING COUNTS (4/11/1) match exactly; only the prose attribution drifted. No action beyond awareness.

**F3 (self-correction, mine) — the harness cohort IS frozen.** My NFRA_COMPCLOSE verdict's unknown-unknown claimed the headline "has no frozen denominator — R re-derives from the live rail log each run." **Wrong:** the harness reads the committed frozen cohort (`comp-which-routing-test.py:87-93`, `:879`); per-run re-derivation does not happen. The delta-refreeze DOCTRINE remains correct for cross-freeze comparisons (a deliberate re-baseline changes the denominator), but my framing overstated the hazard, and the doctrine line CTO~Z folded at `2e6fb2808` cites that framing as its evidence — CTO~Z may want to soften the citation at next touch. Corrected here per Law 8: a stale record is not a silent record.

## Compiler Tools

comp-iam simulate-self-test 5/5 · comp-freshness self-test 11/11 · drift_cli --self-test 8/8 + live sweep 4/11/1 · comp-pydeps 7/7 · comp-gitdrill 6/6 · comp-icedrill 6/6 + live REFUTATION (F1) · comp-debris 7/7 + live 30d · comp-surface-check selfcheck PASS (rc=2 exercised) · comp-which ×10 (9 intents + gibberish) · comp-blast (F-5 exemplar) · manifest check PASS 69/55/14 + RED rc=1 · routing harness ×2 (both ends, frozen cohort, --out scratch). Raw `aws s3 ls` used as the independent axis for F1 (rail-legal: generic s3 ls) + `git` for records.

## Current State / Next Steps

- **[1.0.0_SA_CTO~Z]** F1 fix (pagination-or-disclosure + scale-class self-test); F2/F3 at leisure. Everything else in NFRA_INSTDRILL stands verified.
- **[me]** re-verify F1 on the fix commit (subscope ≥2,269-class hand-count parity; parent≥child invariant).
- **[Andrew]** verdict + delta reported in-session.

— 3.0.0_SA_CVO~Z
