# MORNING BATCH — COO coordination carrier — 2026-07-23 (~04:50Z night close)

**Purpose:** the single durable COO-owned index of what is DONE and what is PARKED behind explicit
gates, so nothing is lost across a session boundary (the "every clock needs a named carrier that
survives a session end" lesson). Written for a reader with ZERO prior context. Detailed band TO
bindings live in the annex `DECOMP_PREP_interpolated_backfill_morning_batch.md` (keep until decomposed).

Owner: `2.0.0_SA_COO`. CTO's full-arc session log: `@ee3264e3f` (the morning package builds from it).

---

## DONE tonight (verified, no morning action)
- **Cottonwood MDPF page LIVE + PROD-verified + go-live SEALED.** DE 5-render check on the DEPLOYED
  opalinvest.dev bundle (portal-v2.1.142 @5ef8bc63): donut $458,114,003.10, model split real, **Long Term
  canonical blue** (zero "Conservative Growth"), bell curve 291 funded / $207,443.23 median, both views
  firm-scoped, zero internal leakage. Inflection ($202M/713) + 49F ($1.64B/7,041) render fully populated
  live = verified no-op for existing firms. CTO sealed Ask-1 on the evidence chain (`@ee3ed6db85`, ETags
  md5-match). Identity set: model_aum 124,376,009.73 / non_model 333,737,993.37 / total 458,114,003.10 /
  account_count 294 distinct (per-model [104,223,7,12,96] sum=442 is NOT the served count).
- **July Inflection anomaly RESOLVED** (Andrew's original concern): 07-06 jump = axis mis-stamp
  (`mdpf_aggregate_aua.py:1176-1179`, min-vintage stamp), NOT methodology; 07-10 = real (+$11.77M, 65
  IWM->Opal migrations, zero residual); 07-11..15 = repaired producer death, propagated. Repull NO-GO;
  cutover carries the fix. Methodology-change refuted 4 ways.
- **qt5/qt4 recovery: both tables 10/10 real value-dates** landed 07-09..07-21 (~1,500 / ~67,000 rows),
  re-mint hardened, zero 401s. Provenance: value = real late-materialized; assignment = current-stamped
  (NOT PIT). ONE vendor mechanism (qt4 late-materializes like qt5), not two.
- **Provenance-read guard CLOSED end-to-end** (test/hook/CI): mutant exit-1 at file:line; real push
  refused; CI run 29980042961 red on exactly the guard step, probe ref deleted unmerged. `@ee3d6db85` /
  portal DEV `7394a58f`.
- **COT_ADVI silver coerce fix** landed clean `@2ed963ef6` (A_03 abs()-of-str halt).

## KEY STANDING FACT for every morning item touching the band
**The model/assignment cohort is PERMANENTLY interpolated.** CRO ruled qt5 CURRENT-STAMPED (`@042742Z`
via CRO msg; recorded CRO-via-COO, not CVO-verified): 0 real historical Opal assignment changes across
778+ accounts, model createdAt stable 22/22. There is no real "which-model-when" history to ever
supersede the interpolated ASSIGNMENT points. Only the VALUE/custody leg upgrades (point_class, deferred).
The served band is yellow-dashed end-to-end BY DESIGN, forever — not transitional.

---

## OPEN — parked behind explicit gates

### A. Interpolated backfill band — serves on NEXT promote
- **Status:** BUILT + STAGED (DS producer `build_cottonwood_interpolated_backfill.py @65a8fa92f`; DE
  accessor + band portal DEV `7394a58f`). CVO ruled DS's candidate-set date-restriction a **DELTA**
  (not within-intent — it SUBSTITUTES+EMITS on the early band), blessed as a GOOD delta, ruling durably
  committed `@ec5ec79f3`.
- **Pin item 1 (M4 substitution mutant): DONE** — DS wrote both legs, set 13/13 green (`@88d165366` area).
- **Pin item 2 (confidence regime): CAP IMPLEMENTED, washout-keyed `@7abc02182` (16/16 green).** Progression
  for the record: DS measured the early band already emitting ~0.50 but flagged the honesty as EMERGENT
  (close-margin fallback), not guaranteed, and proposed a flat `min(current, 0.50)` cap. **CRO's method
  ruling `@044637Z` superseded flat-0.50 BEFORE CVO blessed:** substitution-as-method CONFIRMED intended,
  cap REQUIRED, keyed to `washout(U_terminal, R_terminal)` = sum-min over the B2 terminal decompositions —
  honest BOTH directions (overlapping terminals wash out and may honestly exceed 0.50; distant terminals
  cap BELOW 0.50, which flat would over-claim; flat 0.50 remains only the named conservative fallback).
  Implemented + pushed: `substitution_washout()` reuses the dim's own decompose, fires exactly when the
  restriction changed the answer; M5 mutants encode CVO's invariant machine-checked (a substituted
  assignment can never emit confidence above its pair washout). Set now 16/16 green.
- **Remaining gates (all morning):** (1) **CVO blesses the WASHOUT-KEYED cap** (not flat 0.50) + signs the
  delta into the pin `@ec5ec79f3` — now against LANDED CODE + green mutants, not a proposal; (2) co-sign
  pair AT THE ARTIFACT (DS BF1 + DE BF2 acceptance render on real provenance — DE armed); (3) **>> ANDREW'S
  SERVE-CALCULUS WORD <<** on serving a PERMANENTLY yellow-dashed estimate band on his live page (surfaced
  to him this session; his call, no clock); (4) serve on the next promote. [CRO method-intent + cap:
  CONFIRMED `@044637Z`, no longer pending.]
- **Pins (bind EXACT commits per R-5):** CRO schema `@708661904` (canonical build schema, delta-wins),
  CTO agg spec `@be91775dd` (§4 is ruling-record-not-build-surface), CVO R-5 `@ec5ec79f3`.

### B. 07-22 partial disposition — DE-RISKED; deadline next box window ~02:00Z 07-24
- **Leg 1 (re-land, 0.6.2):** attempted `@~04:45Z` (SSM 91c6c89e) — 07-22 STILL PARTIAL (158/412 vs gates
  760/33,603), NOTHING landed (self-gating script refuses a partial). Staged for next window:
  `code/bronze/qt_0722_reland.py` (gate travels with it — a different owner cannot land a partial).
- **Leg 2 (belt, DS): LANDED+deployed `@88d165366`** — FORWARDFILL_QUARANTINE for ALLOCATIONS +
  UNREALIZED_DAILY 2026-07-22; also closed a single-date `--date`/`--force` bypass (now refuses loudly).
- **Remaining:** next-window re-land (0.6.2 if live; else CTO's never-retry fix structurally covers) ->
  verify full vs neighbors -> **lift DS's two quarantine entries on verified-full re-land** (0.6.2+DS
  coordinate the lift). Worst case: 07-22 honestly absent one extra day. Deletion REJECTED (human-confirm
  law + worthless partial + same-key re-land supersedes).

### C. Cottonwood MEASURED trend — RESOLVED tonight (grounded, no counter-sign owed)
- Served `aggregate_aua_timeseries.json` GROUNDED by COO direct-read @~04:50Z: **0/427 non-null**, axis
  `as_of_last = 2026-07-20` (did NOT advance to 07-21), ETag `3e555439135e` byte-identical to the
  co-signed all-null artifact (head-object LastModified 03:58:35 GMT/UTC). All-null is CORRECT: measured
  data starts 07-21, axis ends 07-20, zero overlap (meta.covered_dates = []).
- The ~04:00Z re-run produced NO non-null points (axis still stale at 07-20). **NO COO counter-sign owed**
  (it was conditioned on non-null count > 0; there are none). Conservative empty line CONFIRMED.
  `PENDING_0400Z_..._trend_rerun_cosign.md` trigger resolved + deleted per its own close-condition.
- FORWARD FILL PATH: the measured trend fills when the axis advances to include 07-21+ — via a nightly
  that advances the axis OR the self-sustaining **6d dispatcher daylight leg (G3w, CTO-gated)**. DISTINCT
  from item A: the interpolated BAND gives the page its 05-28->07-21 history; this measured series is the
  going-forward line. Partial grounding of the 0.7.0_AE nightly-outcome: the cottonwood trend axis had NOT
  advanced past 07-20 as of 04:50Z (0.7.0_AE closure leg — cot gold chain complete / platinum advanced —
  still the authority on the full nightly outcome, due after 02:05Z).

### D. S5 createdAt passthrough fold (CTO/DS, non-blocking)
- bronze `rebalancer_model_detail` carries real per-model createdAt (stable 22/22 = genuine birth date);
  silver slimmed it (Rule-17 legacy violator). Fold createdAt (+updatedAt) passthrough into 3F-S5's
  provenance-sidecar touch = ONE converter pass. **TRAP for the TO text: roster `last_update` is the
  REVALUATION stamp, NEVER a creation proxy** (a 05-28-born model shows last_update 06-15/07-22). CRO's
  CURRENT-STAMPED verdict leaned on exactly this distinction. Non-blocking (BF1 reads bronze for the floor).

### E. Portal PR-flow design item (BACKLOG, named-not-rushed — CTO ruled)
- Guard is closed, BUT with no `pull_request` trigger the CI backstop detects-after-landing, not
  blocks-before-merge. CTO ruled ACCEPTABLE as-is for the portal's direct-push workflow (local hook is
  the proven block layer; red build is loud). Converting to PR-flow + branch protection = deliberate
  later design item: **DE proposes, CTO gates, Andrew's word if it changes how he works with the portal.**
  Do NOT rush into the batch.

### F. Demo credential click-through (COMPLETENESS row, not a gate)
- demo@demo.test Cognito allowlist custody (CTO~B's desk or Andrew's word) -> DE's final credentialed
  click-through evidence row. Go-live stands sealed without it; chase whichever is faster.

### G. WS-1 BD cookie durable-mint fix (morning)
- BD auth alive only on durable 07-06 cookies; nightly capture fires-without-writing on expiry. Morning:
  durable-mint fix + interim capture de-risk. Exposure is bounded (tonight's freshness fix makes expiry
  loud within a day), not silent-for-weeks.

### H. qt4 count-regime shift (DS's eyes, before anyone reads it as book movement)
- qt4 161K -> 77.8K -> 67K around 07-14/15 — OBSERVED, not adjudicated. The silver drift-boundary
  adjudicates schema; the count regime wants DS's read first.

---
**Delete/prune each item as it closes. This file is the carrier, not the work.**  -- `2.0.0_SA_COO`, ~04:50Z
