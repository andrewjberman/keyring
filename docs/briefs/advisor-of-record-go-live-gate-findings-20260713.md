# Advisor-of-Record Go-Live — Gate & Review Findings Record (durable)

**Purpose:** durable persistence of the multi-agent gate/review findings for the INF advisor-of-record (AoR) SSOT go-live, so the expensive workflow analysis (19+ agents / ~1.7M tokens per xhigh review round, plus CVO~B's independent verification battery) is NOT lost to context compaction or session end. **Andrew-direct 2026-07-13: "make sure to persist the findings of these underlying agents ... i dont want to lose that work."**
**Status:** LIVING RECORD — appended as gates return. **Owner:** `1.0.0_SA_CTO~B` (go-live principal + never-widen).
**Raw artifacts:** full-fidelity workflow outputs preserved under `docs/briefs/aor-review-artifacts/` (see §7).

Gate model: **gate-1** = CTO~B workflow-backed `/code-review` (xhigh, adversarial: one finder per angle + an independent verifier per (file,line) + ranked report). **gate-2** = CVO~B independent verification battery (own fixtures + live exercise). Both must clear before the never-widen co-sign.

---

## 1. Architecture evolution (rounds 1 → 8.1)

The fold's journey — each round's failure taught the next:
- **r1 `223a71982`** — under-folded (empty). **r2 `e8745f1e2`** — over-folded (all 837). **r3 `b3f051aef`/`6b8158569`** — movers-only, but data-quality edges + gate placebos.
- **r6** — `/code-review` DESIGN-PASS-not-patchable: **count-based daily guards structurally cannot catch per-account drift**. Surfaced the architecture fork to Andrew.
- **Andrew reframe** — "run it as B, deal with problems as we get them ... a mechanism to SPOT CHECK." → **detect-and-alert** (a per-account joined comparison + a daily drift alert that surfaces, never blocks).
- **r7 `9c3b4513b`** — detect-and-alert with a **mutable comparison partition keyed by the source as-of**. Gate-1 (wi6kmcnng) found this REINTRODUCED false-greens (§3.1).
- **Andrew SSOT design** — "sort this out very early in the chain ... completely not acceptable to structure it individually into every downstream view." → resolve AoR **once** at a front-of-chain Group A resolver; every view **inherits** a canonical field; append event-ledger; zero per-view AoR logic.
- **r8 `345c85daa` + `5581c0de1`** — the SSOT refactor. Gate-1 (wkzqqdr0d, pending) + gate-2 (CVO~B, §4.2) — gate-2 VERIFIED the architecture but caught the R8-F1 firebreak blocker.
- **r8.1 `68be1809d`** — the firebreak fix (§5). Gate-2 re-verify CLOSED VERIFIED.

---

## 2. The SSOT architecture (as built, r8/r8.1)

- **ONE resolver** `INF_A_0.aor_resolver.py` (`run_resolver`), FIRST in `orion-gold-dispatch.sh` CHAIN_COMPUTE (:354). Resolves AoR once (reuses `_load_latest_accounts_v2` walk-back/as-of + `_servicing_advisor_key` rep_id-primary + `build_advisor_of_record_fold`). Emits (a) canonical `gold/dimensions/aor_resolution.parquet` [the stamped field], (b) the APPEND event ledger `gold/dimensions/aor_ledger/events/{run-ts}.parquet` — a NEW timestamped key EVERY run, NO fixed path → **uncollapsible by construction**.
- **Census 10→1 (fold) + 4→1 (household):** all `apply_advisor_of_record_fold` producer call-sites removed (was 10: A_00/A_01/B_00/C_01/C_07/INF_09/D_00c/D_00d/D_00f/D_02b); `resolve_household_advisor` resolves ONCE at C_07 (was 4). Downstream views INHERIT — zero per-view AoR derivation. Guarded by `test_census_single_resolution_point`.
- **Two inherit modes (r8 subtlety, gated explicitly):** FULL attach (A_00/A_01, current-snapshot account-grain) vs MOVERS-ONLY attach (`apply_resolution_fold`: B_00/C_01/INF_09/D_00c/D_00d/D_00f/D_02b). A FULL attach on a HISTORICAL/vintage frame would OVERWRITE vintage attribution with current servicing = a served delta under OFF — so vintage frames ride movers-only (== retired fold semantics).
- **Switch/detector:** `AOR_FOLD_ACTIVE` OFF → resolution = servicing = today's behavior (DELTA-0); ON → AoR-folded. The resolver ALWAYS runs; the switch only controls the fold. Detector = ledger-diff for CHANGES only; the r7 as-of freshness gate DROPPED (freshness owned by the existing alarm layer). **Go-live = a single switch-flip; a post-GO rollback = flip only (resolver keeps running).**

---

## 3. Gate-1 findings (CTO~B workflow-backed /code-review, xhigh)

### 3.1 Round-7 — `wi6kmcnng` on `9c3b4513b` (19 agents, ~1.74M tokens, 22 candidates → 7 reported / 7 refuted)
Full raw output: `docs/briefs/aor-review-artifacts/wi6kmcnng-round7-gate1-review.json`.
Dominant defect = **dating the comparison partition by the source as-of (`INF_AOR_ASOF`) rather than wall-clock**, producing two false-GREEN silent-miss classes:
1. **[CONFIRMED] `INF_A_01.py:215`** — as-of-keyed partition + fixed `{prefix}{as_of}/data.parquet` path COLLAPSES consecutive nightly emits onto ONE key when the upstream as-of repeats (frozen accounts_v2). Detector sees `len(dates)<2` → "OK baseline day" → a real per-account swap goes UNSURFACED.
2. **[CONFIRMED] `aor_attribution_audit.py:375`** — freshness gate keys on the partition DATE LABEL not whether tonight's emit ran; a stale prior-night same-dated partition satisfies it → greens on stale.
3. **[CONFIRMED] `audit.py:245` (EDGE-3)** — ACCOUNT-RAW-RELABEL fires on blank↔populated transitions, not only value→value relabels → placebo alert-burst on a benign coverage-improvement night.
4. **[CONFIRMED] `audit.py:375`** — standalone-invocation (INF_AOR_ASOF unset) makes `expected`=wall-clock vs the lagged newest partition → COMPARISON-STALE false-alert on manual checks.
5. **[PLAUSIBLE] `audit.py:375`** — non-canonical (non-zero-padded) as-of permanently mismatches the `\d{4}-\d{2}-\d{2}` lister regex → permanent placebo-fire.
6. **[PLAUSIBLE] `audit.py:439`** — a transient S3 blip → CANNOT-EVALUATE → SMS to Andrew (alert-fatigue on healthy nights).
7. **[CONFIRMED, cleanup] `audit.py:240`** — EDGE-3 recomputes t_raw/y_raw already built by `_detect_source_drift`.
Refuted (7): env-desync placebo, `dates[-2]` multi-day span, `reindex` duplicate-index raise (×3), redundant Series-wrap, unreachable blank-raw branch.
**Disposition:** findings 1–2 (the as-of-keyed collapse class) resolved WHOLESALE by the r8 SSOT refactor (append ledger, no as-of partition key). EDGE-3 → value→value only in r8. Others → folded into r8.

### 3.2 Round-8 — `wkzqqdr0d` on `345c85daa^..5581c0de1` — CTO~B **synthesized personally** (Andrew-direct 2026-07-13), then CROSS-CHECKED by the workflow's own synthesis
The workflow appeared hung at 28/29 agents (final synthesizer idle), so per Andrew CTO~B synthesized directly from the journal (`wf_dd6305f8-436`: 6 finders + 20 verifiers + sweep; verdict tally **20 CONFIRMED / 8 PLAUSIBLE / 5 REFUTED**). **The workflow then completed (32 agents, ~3.43M tokens) and its own synthesis INDEPENDENTLY CONVERGED on the same four load-bearing root causes** (A = the switch-gated resolver vs unconditional `load_resolution()`; B = the household RAISE cascade; C = the rep_name-slug → rep_id-primary basis flip making DELTA-0-under-OFF empirical not structural; D = NaN `advisor_key` on A_00-vs-resolver as-of skew) — a strong cross-check that the ranking below is right.
Raw artifacts: `docs/briefs/aor-review-artifacts/wkzqqdr0d-round8-gate1-review.json` (full workflow output) + `…-journal.jsonl` (all 32 agents' returns).
**Verdict: the SSOT architecture is SOUND — NO round-7-class false-green reintroduced (gate-2 CLOSED corroborates) — but a set of ACTIVE-path + release-mechanics findings require a round-8.2 before the switch flips ON.** Ranked (deduped clusters; each cluster was independently flagged by multiple finders and survived verification):

- **F1 [HIGH — release/rollback mechanics] `orion-gold-dispatch.sh:353/354` (7 finders):** ~~the resolver `INF_A_0` entry is gated on `INF_AOR_FOLD_ACTIVE=1`, but ALL migrated consumers unconditionally call `load_resolution()` which RAISES if `aor_resolution.parquet` is absent. So under OFF (the documented switch-only rollback), the resolver drops from the chain → the artifact isn't produced → consumers RAISE → the nightly aborts. **DELTA-0-under-OFF is thus unreachable via the dispatch** (CVO's 0/871 was measured resolver-direct, not through the switch-gated dispatch). NOT a current-state bug (consumers SERVE-HELD pre-GO), but **the GO RELEASE MUST make the resolver entry UNCONDITIONAL (as DS documented) atomically with the sentinel-lift, AND the switch-OFF/rollback path must be re-verified at the DISPATCH level.**~~ → release-checklist blocker + rollback-safety.

  > ### >>> F1 CORRECTED 2026-07-13 — CTO (base). THE CONCLUSION STANDS; THE MECHANISM ABOVE IS **BACKWARDS**, AND THE REMEDY ABOVE WOULD **KILL THE NIGHTLY**. Struck, not deleted — the error is the record. <<<
  >
  > **THE MECHANISM IS INVERTED. It fails OPEN, not closed.** (3.0.0_SA_CVO, `b40d5cebe`, exercised 3-arm hermetic falsifier: absent→RAISE, stale→**RETURN**, fresh→RETURN. Re-grounded at source by CTO @ `b40d5cebe`.) `RESOLUTION_KEY` is a **fixed overwrite-latest** key (`aor_resolution.py:52`); the rollback is **flip-only and nothing deletes the artifact**; `load_resolution()` (`:232-251`) validates readable/non-empty/two-columns and **NEVER reads the `as_of` it returns** (`as_of` IS carried, `:59`). So F1 above reasons about the artifact-**ABSENT** state (pre-GO). **The rollback actually occurs in the artifact-PRESENT-AND-STALE state (post-GO)**, where `load_resolution()` returns happily and consumers **silently attribute off a FROZEN resolution** — while `INF_D_11`, the drift detector that would catch it, **is dropped by the SAME conditional**, and `INF_D_10` conformance is `--mode advisory` (`:273`) and cannot block. *The rollback removes the guarantee AND its detector in one flip, and keeps serving.*
  >
  > **THE SENTENCE "DELTA-0-under-OFF is thus unreachable via the dispatch" IS FALSE POST-GO — AND IT IS PRECISELY WHAT MADE THE FAIL-OPEN INVISIBLE.** Under OFF the dispatch runs *fine*, reaches DELTA-0, and measures against a frozen resolution.
  >
  > **THE REMEDY ABOVE ("make the resolver entry UNCONDITIONAL") IS ALSO WRONG — IT KILLS THE ENTIRE INF NIGHTLY.** (`0.4.0_DS_ClientPlatform`, source + APPLIED: `comp-pipescript deployed` → `INF_A_0` = **MISSING_ON_S3**; the *deployed* dispatch `md5 5bf875c9` @ 2026-07-08 contains **0** occurrences of `INF_A_0`/`INF_D_11`/`AOR_FOLD_ACTIVE` — it predates the entire AoR chain.) `INF_A_0` is FIRST in `CHAIN_COMPUTE`; `run_script:563-568` `exit 1`s on a script missing from the S3 sync; `run_chain` aborts on non-zero. **An unconditional entry deployed before the resolver lands = the nightly dies at step 1.** The `:353` gate is **not an oversight — it is a load-bearing PRE-GO deployment guard** (its own comment, `:344-352`, says so).
  >
  > **ROOT CAUSE (nobody had named it): `INF_AOR_FOLD_ACTIVE` IS DOING TWO JOBS.** `aor_resolution.py:391/:410/:420` — **the resolver ALREADY handles switch-OFF**: `build_advisor_of_record_fold()` returns `({},{})` → servicing-only, `resolve_accounts()` still runs, and a **FRESH artifact with a current `as_of` is still written** (the print literally reads `fold {"ACTIVE" if AOR_FOLD_ACTIVE else "OFF"}`). `INF_A_0.aor_resolver.py` never reads the switch at all. So the **SEMANTIC** job (fold-vs-servicing = *output*) is already implemented correctly **inside the resolver**, and the `:353` chain-gate is a **DEPLOYMENT guard wearing the semantic switch's clothes.** Two unrelated concerns multiplexed onto one variable — *that is why this finding had three mutually-inconsistent readings.*
  >
  > **THE ROLLBACK WAS NEVER BROKEN BY DESIGN — IT IS BROKEN BY THE GATE.** Intended semantics (dispatch `:350-352`): flip OFF → resolver **keeps running** → resolution **reverts to servicing**. Fresh artifact, servicing values, `as_of` **advances**. The `:353` gate drops the resolver entirely, and *that* is what manufactures the frozen artifact.
  >
  > **THE RULING (CTO, supersedes the remedy above):**
  > - **R5 — DE-MULTIPLEX.** Switch = SEMANTIC only (output; already correct; **untouched**). Chain entry = gated on **SCRIPT PRESENCE**, never on the semantic switch. *A presence-gated dispatch is **order-independent**: deployed early → resolver absent → skipped → nightly unaffected; deployed late → runs. The deploy-skew hazard does not get proven away — **it stops existing**.*
  > - **R1 — the freshness assertion goes INSIDE `load_resolution()`** (`:232`), the chokepoint the design already elected ("zero AoR logic lives at any call-site"). Keyed on the **RUN'S PINNED as-of (`INF_AOR_ASOF`)**, exact-match, RAISE. **NOT wall-clock** (would false-raise every weekend/holiday when the data legitimately does not advance); **NOT an N-day tolerance** (a tolerance is where fail-open hides, and it gets tuned until the alarm stops).
  > - **R1b — `aor_resolution.py:382` can FABRICATE `as_of`.** `os.environ.get('INF_AOR_ASOF','').strip() or str(pd.Timestamp.now(tz='UTC').date())` stamps **wall-clock TODAY** when the pin is unset — and `dispatch:1302` **explicitly leaves it unset** on a resolve failure. *The path that most needs the assertion is the one handed a fabricated-fresh `as_of`.* **An assertion on a field that can lie is not an assertion.** RAISE instead. (`inflection_rep_scope.py:250-254` already does exactly this; `:382` is the inconsistent sibling.)
  > - **R2/R3** — `INF_D_11` and **every chain literal carrying an AoR consumer** (`CHAIN_INCREMENTAL:361`, `CHAIN_GOLD_A/B/C/D:365-369` — separate literals the `:354` prepend never touches, carrying `INF_A_00`, `INF_B_02`, `INF_C_01/07`, `INF_D_00c/00d/00f/02b`, `INF_09`) get **presence-gated** resolver entry. Without this, a `--chain incremental` / `--chain gold-*` **RECOVERY run — even switch-ON —** runs consumers with no resolver against the stale fixed key. *Recovery re-runs are the standard post-bad-night move.*
  > - **R4 — the structural test IS the deliverable:** a chain literal carrying an AoR consumer with **no presence-gated resolver entry** = **build FAIL**. R3 fixes today's five literals; R4 is what stops literal #6.
  > - **Presence-gating ALONE is a fail-open of CVO's exact class** (silent skip → resolverless consumers → stale key). **It is safe ONLY paired with R1.** The two fixes are load-bearing for each other.
  > - **R6 (routed, NOT a blocker):** the serve-hold sentinel is structurally **`.py`-only** (`safe_deploy_core.py:112`). 21 files carry `# DEPLOY-SERVE-HELD`; `orion-gold-dispatch.sh` carries none and *cannot* — yet it IS a deployed runner artifact reaching the box outside safe-deploy. **The one file that decides which scripts run is the one file in the release bundle with no hold mechanism** (DS). Real, generalises past AoR to every `.sh` runner — but **de-blocked by R5**, since presence-gating makes that un-held file order-independent.
  >
  > **REQUIRED ACCEPTANCE ARM (gate-2, CVO's own ask — ratified):** resolver ON once (artifact lands) → flip OFF → **drive THROUGH THE DISPATCH** → assert consumers **RAISE**. Today they silently succeed.
  >
  > **THE CLASS-LESSON, AND IT INDICTS BOTH GATES.** Gate-1 ran **32 adversarial agents / 3.43M tokens** and still got this backwards; gate-2's DELTA-0 (0/871) was **structurally incapable** of seeing it (a resolver-direct harness *always* holds a freshly-written resolution, so it cannot express the "artifact present + resolver skipped" state at all — CVO's own self-indictment, volunteered). Two independent instruments, opposite ends of the pipeline, **same blind spot**: every agent reasoned about the state we are **IN** (artifact absent, pre-GO) instead of the state the **ROLLBACK CREATES** (artifact present, stale). **We enumerated the CODE axis and never enumerated the STATE axis.** *For every claim: name the STATE it was measured in, and whether that is the state the failure occurs in. Enumerate the state space before choosing the instrument.*
- **F2 [MED-HIGH — ACTIVE correctness] `INF_A_00.py:236`:** A_00 loads accounts_v2 via a loader that IGNORES `INF_AOR_ASOF` while the resolver PINS it; a partition/as-of divergence → accounts in A_00 but absent from the resolution get `absent=None` → NaN `advisor_key` on served accounts_dimension. → align A_00's loader to the resolver's as-of (or floor `absent`).
- **F3 [MED — silent-miss] `aor_resolution.py:353` (load_prior_state):** rebuilds the change-basis from events ONLY when the cache READ throws; a readable-but-INCOMPLETE cache is trusted verbatim → a real change on an account missing from the cache downgrades to a non-alerting `new` event → detector greens. → rebuild/validate on incomplete cache, not only read-throw.
- **F4 [MED — new hard-abort] `aor_resolution.py:323` + `C_02:471` + `D_02c:156`:** `household_headline_map` RAISEs on a missing stamp — a NEW hard-abort for the D-chain (C_02/D_02c/D_00d/D_04) that previously fell back to plurality; C_02's try/except does NOT cover it; violates D_02c's "never hard-abort the D-chain" contract. Fail-closed is defensible for a served headline, but **CTO~B ruling needed: RAISE (fail-closed, serve-stale) vs graceful-degrade+alert** + fix the C_02 try/except gap.
- **F5 [MED — robustness] `aor_resolution.py:412`:** `run_resolver` has NO exception isolation around the rebuildable writes (event-ledger :406, state-cache :412) that run AFTER the served resolution already succeeded (:402); since INF_A_0 is first + the chain aborts on any non-zero, a transient blip on a REBUILDABLE artifact takes down the entire INF nightly. → wrap rebuildable writes (log+continue).
- **F6 [MED — efficiency] `B_00:734` + `D_00c:451`:** `load_resolution()` (run-invariant S3 GET) called inside per-snapshot / per-leaderboard-window / 32-worker loops — redundant S3 reads; the retired fold loaded once (module-global). → hoist once.
- **F7 [MED — detection-completeness] `aor_attribution_audit.py:55`:** round-7's COVERAGE-DROP / SOURCE-DRIFT-COVERAGE-CLIFF detectors were deleted; a per-account coverage collapse (an account present yesterday, absent from today's resolution) is no longer alerted (the freshness layer checks partition freshness, not per-account population). → re-establish or accept as a scoped detection reduction.
- **F8 [MED — detection] `aor_attribution_audit.py:183`:** one unparseable ledger key → early-return CANNOT-EVALUATE FOREVER, masking real change/relabel drift underneath (surfaces as a persistent alert, not silent). → skip+alert the bad key, don't early-return-forever.
- **F9 [MED — empirical-not-structural] `aor_resolution.py:96/99`:** the OFF/servicing basis shifts `rep_name-slug` → `rep_id-primary` (`_servicing_advisor_key`); 0/873 agree TODAY (monitored by `basis_disagree`) but NOT structural — a future rep_id/rep_name disagreement shifts served identity under OFF; PLUS a NULL-vs-`'unknown'` floor change on unresolvable accounts (the retired `derive_advisor_key` never returned null). → known/monitored; verify a NULL advisor_key doesn't break downstream.
- **F10 [MED — test-completeness] `test_aor_resolution.py:169/189`:** the SSOT census test greps only `apply_advisor_of_record_fold(` + `resolve_household_advisor(` — a smuggled per-view AoR re-derivation via ANOTHER symbol (a raw udf7 read / explicit-map read) evades the gate. → strengthen the census.
- **LOW / cleanup:** detector lookback measured from wall-clock (`audit.py:172`); `str(pd.NA)` misclassify in the change-hint (`audit.py:65`); dead `if…: pass` block (`aor_resolution.py:302`); re-implemented S3 helpers vs the resolution lib (`audit.py:157`); `_n_absent` miscount (`INF_A_00:237`).

**Disposition:** none reintroduce the round-7 false-green class; the SSOT architecture stands (gate-2 CLOSED). F1–F10 → **round-8.2** (DS) before the switch flips ON, with F1 also a GO-RELEASE-mechanics + rollback-safety requirement. F4 needs a CTO~B fail-closed-vs-graceful ruling. Then gate-1 re-review of the round-8.2 delta + CVO~B re-verify. **Go-live does NOT proceed tonight** — nothing served, switch OFF, everything SERVE-HELD.

### 3.3 Round-8.1 firebreak — `68be1809d` — CTO~B inline source-grounded review = **PASS**
The r8.1 fix (§5) reviewed at source: 4 RAISEs correctly gated under `if AOR_FOLD_ACTIVE:` (OFF stays DELTA-0), zero-mover check post-`build_` before any write, docstring corrected. **Fail-closed guarantee GROUNDED:** `orion-gold-dispatch.sh` `run_chain` (`:880-890`) runs each step `run_script "$id" || _script_rc=$?` and on non-zero prints `CHAIN FAILED at $id` and `return`s immediately (no `if !` inversion bug); under `set -e` (:59); INF_A_0 is FIRST → a resolver RAISE aborts before any gold is regenerated → **yesterday's gold stays served (serve-STALE), never serve-pre-fold.** No new abort in normal operation (RAISEs fire only on genuinely broken source under ACTIVE).

---

## 4. Gate-2 verdicts (CVO~B independent verification)

### 4.1 Round-7 on `9c3b4513b` — VERIFIED both halves
Battery enumerated M1 missing-today / M2 stale-today / M3 blank-raw — all → COMPARISON-STALE/INCOMPLETE (finding-grade), healthy twin GREEN (non-placebo), E3 caught, rc 0 throughout. Self-disclosed: the date axis was enumerated only over ADVANCING values — the frozen-REPEAT value was un-enumerated (the gap wi6kmcnng's finding-1 exploited). "Enumerate the state space before choosing the control."

### 4.2 Round-8 on `5581c0de1` — VERIFIED all locked-contract legs + ONE blocker (R8-F1)
GUARDED (all exercised): F1 frozen-as-of swap → distinct `{run-ts}` keys both retained (storage) + detector alerts (detection), asserted SEPARATELY; F2 read-fail → CANNOT-EVALUATE; **F3 STRUCTURAL** — negative write-path census proves NO fixed events/ path exists; F4 no-change → zero event rows, GREEN non-placebo; **F5a census** apply_advisor_of_record_fold producers 10→0 / resolver=1, household 4→1(C_07) + conformance checker; **F5b BOTH modes BOTH states** — LIVE OFF DELTA-0 = **0/871** basis mismatches vs served account_team, ON positive-control **fold==164==CVO's independent oracle** (sym-diff 0); F5c perturbation propagates to every view (inherit-not-re-derive). Household RAISE fires only in the broken state. DS suites 11/11, 12/12, 22/22.

### 4.3 R8-F1 (CONFIRMED-BY-EXERCISE, go-live-blocker) → FIXED `68be1809d` → re-verify CLOSED VERIFIED
See §5.

---

## 5. R8-F1 — the firebreak finding (the one blocker), fix, and re-verify

**Finding (CVO~B gate-2, confirmed-by-exercise):** the r8 resolver path calls `build_advisor_of_record_fold` directly (`aor_resolution.py:384`) and BYPASSES the three (in fact four) ACTIVE firebreaks that lived ONLY in the retired `_ensure_advisor_of_record_fold_loaded` (`inflection_rep_scope.py:307/312/318/324`). `build_` returns `({}, {})` SILENTLY on a missing column (`:589-590`), so **under ON with a broken/absent silver raw column, the resolver would serve a servicing-only PRE-FOLD resolution with NO raise** — the detector alerts AFTER the write (never blocks), and a broken FIRST-ON-night baselines silently + poisons the diff basis. The docstring's "firebreaks propagate" claim was FALSE at source for these classes. **Exercised live:** `INF_AOR_FOLD_ACTIVE=1` + today's real av2 (873 rows, `advisor_of_record_raw` genuinely absent — CHANGE-3 silver not yet deployed) → `build` `({}, {})`, 0 movers, no raise. **Zero TODAY impact** (switch OFF / SERVE-HELD).

**Fix `68be1809d` (DS, option a — enforce in `run_resolver`, `build_` contract untouched):** under `AOR_FOLD_ACTIVE`, RAISE on (1) `advisor_of_record_raw` column MISSING, (2) `representative_name` MISSING (servicing basis absent, B1-class — the 4th arm), (3) raw entirely NULL, (4) populated roster deriving ZERO movers (a ~164-mover set reducing to 0 = derivation failure; a legitimate future genuine-zero rides a reviewed baseline change). Docstring corrected. 4 new tests incl the **OFF positive control** (same broken source under OFF still emits servicing-only, rc 0 → DELTA-0 today preserved). resolver 15/15, detector 12/12, derivation 22/22.

**CTO~B ruling:** accepted; go-live WITHHELD pending this fix; the fail-closed behavior (RAISE → chain aborts → serve-stale, NEVER pre-fold) is the correct NEVER#2 posture.

**CVO~B re-verify on `68be1809d` (CLOSED VERIFIED):** A1 LIVE — the byte-identical state that returned `({}, {})` silently on `5581c0de1` now RAISES on the REAL path; hermetic A1h/A2/A3/A4 all RAISE; OFF twin proceeds servicing-only rc 0 (non-placebo, DELTA-0 preserved). Battery 35/35 re-pinned. **Gate-2 = CLOSED VERIFIED for round-8 + 8.1.**

---

## 6. Separate finding — OUT of go-live scope (routed for grounding)

**D_02b reversed rep_id map (pre-existing, untouched for DELTA-0):** `INF_D_02b`'s LOCAL `ADVISOR_KEY_BY_REP_ID` maps `'11'→peter_lee` / `'12'→patrick_scanlan` — REVERSED vs the canonical `_INF_SERVICING_REP_ID_MAP` (`'11'→patrick`, `'12'→peter`; F7-tested identical to C_01). **HYPOTHESIS (Rule 22, ungrounded):** either D_02b has been mis-attributing peter↔patrick in its served top-holdings, OR its rep_id partition semantics differ. Needs SOURCE-grounding (cite file:line@commit; if a live swap, quantify served impact) BEFORE any fix. INF = in-scope/non-sovereign. **Staged to DS post-round-8 (COO-tracked); NO fix until CTO~B rules on the grounded mechanism.**

---

## 7. Go-live sequencing, gate chain, and commit references

**Hard precondition (exposed by R8-F1):** CHANGE-3 — the silver `advisor_of_record_raw` passthrough (`63dd76201`, SERVE-HELD on `convert_orion_api_to_silver.py`) — MUST deploy BEFORE the switch flips ON (else the resolver has no raw column to fold). The firebreak makes the ordering fail-closed.
**Release order:** CHANGE-3 silver deploy → (r8.1 firebreaks already in) → switch `AOR_FOLD_ACTIVE=1` + sentinel-lift + resolver-entry unconditional + FE promote → V4 served-verify on the nightly.
**Gate chain to activation:** (1) gate-1 CLEAN (round-8.2 delta) → (2) gate-2 VERIFIED (incl. F1 exercised THROUGH THE DISPATCH) → (3) CHANGE-2 (household AoR-wins; hh286 = $0 explicit-Noel WINS over 4 blank-AoR Peter, CVO pre-grounded) → (4) never-widen co-sign (CTO~B + COO + Andrew, figures from CVO's verified numbers) → (5) Andrew GO → (6) atomic pathspec-scoped release (CHANGE-3 silver deploy → round-8.2 in → switch ON + sentinel-lift + **resolver entry UNCONDITIONAL (F1)** + FE promote) → (7) V4 served-verify.

**ALERT-DELIVERY / SMS: CANCELLED — STRUCK FROM THE CHAIN (Andrew-direct 2026-07-13).** Verbatim: *"we're not doing sms so you can forget that. i dont like to talk about alerts until the actual process is done because usually the alerts are miscalibrated and then its spam on my devices."* The SMS/OTP delivery leg is NO LONGER a go-live gate; AE stands down on the number-verify. The drift detector still writes its findings (stdout + ops queue) and never blocks. **Do not re-raise alert wiring/calibration until the AoR process itself is DONE and proven** — an alert calibrated against an unproven process is device spam.

**Commit references:**
- r7 detect-and-alert: `9c3b4513b` (gate-1 wi6kmcnng found the as-of-collapse false-greens).
- r8 SSOT refactor: `345c85daa` (resolver+ledger+detector) + `5581c0de1` (14-site migration).
- r8.1 firebreaks: `68be1809d`.
- CHANGE-3 silver raw passthrough: `63dd76201` (SERVE-HELD).
- This record's commit + the raw artifacts under `docs/briefs/aor-review-artifacts/`.

---
*This record is the durable memory of the AoR go-live gate effort. If context is lost, resume from here: gate-2 CLOSED VERIFIED (r8+r8.1); gate-1 = r8.1 PASS + wkzqqdr0d pending; then CHANGE-2 + SMS + co-sign + Andrew GO. Nothing served; switch OFF; everything SERVE-HELD.*
