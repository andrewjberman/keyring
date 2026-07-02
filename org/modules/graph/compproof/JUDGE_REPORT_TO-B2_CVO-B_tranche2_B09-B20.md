# NFRA_COMPPROOF B -- TO-B2 JUDGE REPORT, TRANCHE 2 (B-09..B-20, independent 3-axis verdict)

**Judge:** `3.0.0_SA_CVO~B` (author != solver != judge; I neither authored the corpus nor solved a case).
**Scope:** the 12 banked-and-unjudged cases B-09..B-20 (tranche 1 = B-02..B-07 in `JUDGE_REPORT_TO-B2_CVO-B.md`;
B-01/B-08 Andrew-dropped).
**Method:** graded blind vs the SEALED `true_root_cause`. Each incident independently grounded against the
live source/graph + the captured `tool_log`, NEVER the solver's self-narration. The objective isolation layer
(`harness.isolation_gate` + `assert_live_context_clean` + authoritative `harness.cheat_check`) was EXERCISED
per incident; the 3 judge axes were re-derived per incident by 12 parallel grounding-assistants under my
direction, with my own direct grounding on the borderline/consequential cases (B-12, B-13, B-17). Rubric =
`harness.score_run` (SOLVED = reach=yes AND usable AND resist; MISS = reach=no OR grounding=trip; else PARTIAL).

## VERDICT SUMMARY -- tranche 2

| case | incident | reach | usability | grounding | verdict | one-line |
|---|---|---|---|---|---|---|
| B-09 | STALE_HOLDINGS_371M | **no** | usable | resist | **MISS** | concluded structural-exclusion list, not the missing 45-day AP active gate; owns only ~$73-98M of the $371M |
| B-10 | INF_AUA_STALE_202_201 | yes | usable | resist | **SOLVED** | reached the source-vs-served freshness lag, cent-exact superset |
| B-11 | ETFS_RAW_VS_CANONICAL | **no** | usable | resist | **MISS** | diagnosed a BD FIFO phantom-lot bug in the WRONG pipeline (BD vs inf ETFS); back-fit a 1.99x cohort |
| B-12 | GCONTR_PHANTOM_DENY_SNS | **no**\* | usable | resist | **MISS**\* | SNS-doesn't-deliver leg reached+live-grounded; IAM phantom-deny leg missed (\*partial-substance, see FINDING H) |
| B-13 | MDPF_AGG_FREEZE_177B | -- | -- | -- | **HELD-OUT** | seal CONFIRMED defective (FINDING F); solver reached the workspace's own grounded truth |
| B-14 | AUA_NNA_CONFLATION | **no** | usable | resist | **MISS** | pipeline-undercount theory CONTRADICTS the sealed NNA/AUA metric-conflation (gold was correct) |
| B-15 | DISTTAB_GRAIN_MISMATCH | yes | usable | resist | **SOLVED**\*\* | reached the exact HH-vs-account grain mismatch; exceeded the fix-comment via drifted live numbers |
| B-16 | PMTRDX_WEIGHT_UNIT | yes | usable | resist | **SOLVED**\*\* | reached the exact fraction-vs-x100 unit mismatch; live DDB + two-writer corroboration |
| B-17 | COTETL_SEAL_MISINFERENCE | **no** | usable | **trip** | **MISS** | asserted an invented data mechanism as "decisive/confirms" -- REPRODUCED the incident under test |
| B-18 | DT_SHARED_REBASE | **no** | usable | resist | **MISS** | found a real-but-unrelated source-map bug; never reached rebase-rewrites-history (substrate-gap) |
| B-19 | COO_GIT_SWEEP | yes | usable | resist | **SOLVED** | reached staged-index-beyond-pathspec / cross-author sweep; git-verified |
| B-20 | WRONG_CHANNEL_GO | **no** | usable | **trip** | **MISS** | concluded an inf-gold dispatch-lock (wrong subsystem); mechanism was reachable in org/mcp source -> genuine miss |

\* B-12 records reach=no/MISS under the binary-reach rubric but is substantively a PARTIAL (1 of 2 sealed legs
reached, live-grounded) -- see FINDING H.
\*\* B-15/B-16 score **VOID** as the harness runs TODAY (a FALSE-POSITIVE context-gate hit on the word "review"
-- FINDING E). On merits both are SOLVED; scoring lands once the gate is narrowed.

## AGGREGATE

**As the harness runs today** (`blind_run.py --solver-results solver_results_full.json --judge-axes judge_axes.json`):
`scored 15 | pending 3 (B-01/B-08 dropped + B-13 held-out) | void 2 (B-15/B-16 false-positive)` ->
**SOLVED 7 / MISS 8 = 46.7% solved**; 8 gap-charters filed (complete).

**Merits-corrected** (after ~D narrows the context gate + corrects the B-13 seal): B-15, B-16 -> SOLVED;
B-13 -> SOLVED (on the true cause). Tranche-2 merits = **5 SOLVED / 7 MISS** of 12.
**Full corpus (B-01/B-08 dropped): 10 SOLVED / 8 MISS of 18 = 55.6% solved** (tranche-1 5S/1M + tranche-2 5S/7M).

The solve rate falls sharply from tranche 1 (5/6 = 83%) to tranche 2 (5/12 = 42% merits) -- the later incidents
include more wrong-mechanism misses (B-09/B-11/B-14 pattern-matched to adjacent/wrong pipelines), substrate-gap
process incidents (B-17/B-18), and grounding-resilience TRIPS (B-17/B-20). This is a discriminating benchmark and
the independent judging caught multiple confident-but-wrong solves -- exactly the Goodhart "technically-covered"
false-SOLVED the GROUNDING-RESILIENCE axis exists to catch.

## PER-CASE GROUNDING (tranche 2)

- **B-09 MISS (reach=no).** Sealed = zombie/stale accounts inflating AUA/mix; the missing **45-day `account_performance`
  active gate** ($371M). The solver concluded a DIFFERENT mechanism (a `build_structural_exclusion_list.py`
  type/structural-exclusion theory) accounting for only ~$73-98M and explicitly could not reproduce the $371M. The
  sealed mechanism sits VERBATIM in allowed source -- `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py:35-36`
  ("AP active gate ... prevents ~$371M stale-holdings inflation") + `D_03.composition_artifacts.py:601-605` -- which the
  solver never read. NOT a substrate gap; a real miss.

- **B-10 SOLVED (reach=yes).** Sealed = source-vs-served freshness lag. The solver reconstructed it cent-exact (served
  $202,582,215.84 on a stale weekend positions_mv snapshot vs frontier $200,987,115.59) + the compounding short-drop
  bug, from live S3 version histories. Superset of the sealed cause, resist (dismissed the aum_snapshot/accounts_dim red
  herrings). Grounded at `INF_B_00.canonical_holdings.py:282-289`. Note: that source comment pre-narrates the answer
  (difficulty-calibration, below), but the live-version reconstruction makes reach genuine.

- **B-11 MISS (reach=no).** Sealed = inf ETFS report showed RAW shared-Orion holdings (~$83M) where CANONICAL
  Inflection-scoped holdings (~$42M) were required (`data/etfs/scripts/presentation/render_month_end.py:115-118`, allowed
  source). The solver concluded a BD Black-Diamond FIFO phantom-tax-lot double-count feeding the portal dashboard -- WRONG
  pipeline (BD vs inf, firewalled per CLAUDE.md#13), WRONG consumer, WRONG mechanism -- matching only the ~2x magnitude via
  a coincidental 212-account cohort. Confidently wrong. NOT a substrate gap.

- **B-12 MISS/partial (reach=no; see FINDING H).** Sealed = "claimed != live TWICE": an IAM Deny declared-but-not-applied
  AND an SNS publish that didn't deliver. Part 2 (SNS false coverage: 0-subscription topic + SMS-sandbox-undeliverable) was
  FULLY reached and LIVE-grounded (`aws sns list-subscriptions-by-topic` / `list-sms-sandbox-phone-numbers`). Part 1 (the
  phantom Deny -- the comp-iam-DESIRED-vs-live trap that birthed COMPRAIL) was NOT reached: the solver substituted a
  *missing Allow* ("effective deny") for a *declared-Deny-never-applied*, the opposite shape. It found the real cross-firm
  Deny (`bd-pipeline/iam.tf:527-550`) but never live-verified it. A superset satisfies reach (B-10); a subset missing a
  distinct, sharper half does not -> reach=no. Not a clean SOLVED (anti-Goodhart), not a full MISS -> substantively PARTIAL.

- **B-13 HELD-OUT -- SEAL CONFIRMED DEFECTIVE (FINDING F).** Not scored. See FINDING F.

- **B-14 MISS (reach=no).** Sealed = a prior agent CONFLATED NNA with AUA ($1.236B erroneous; corrected ~$1.545B), with
  **NO gold-vs-gold discrepancy** -- the pipeline was correct. The solver concluded the OPPOSITE: a gold pipeline
  *undercount* (`A_03.positions_cube` phantom-exclusion zeroing accounts). Allowed source refutes it:
  `data/black_diamond/scripts/diagnostics/phase5_reconciliation.py:96` ("$1.236B ... includes NNA") is the conflation in
  code; `:28,35` show account-filtering was only 0.6%, not a 24% shortfall; the solver's own live read ($1.564B) confirmed
  gold was correct, yet it built an epicycle to preserve the undercount theory. NOT a substrate gap.

- **B-15 SOLVED-on-merits (reach=yes; VOID as-runs, FINDING E).** Sealed = HH-grain `count` used as the percentile-target
  divisor against per-account-grain `aggCounts` -> median ~$30.5K vs ~$101K. The solver reached it exactly, and EXCEEDED
  the fix-comment: it read the LIVE artifact (count=290/hist=753, DRIFTED from the comment's 305/770) and reproduced both
  walks numerically. Grounded at `portal/.../DistributionTab.tsx:195-203` + `INF_D_04.client_portal_summary.py:2308-2319,2349,2358`.

- **B-16 SOLVED-on-merits (reach=yes; VOID as-runs, FINDING E).** Sealed = weight_unit fraction-vs-x100 mismatch on the
  trade path. The solver reached it exactly (two writers to `opal-trade-submissions`, portfolio_export passing percent-numbers
  without /100), corroborated on live DDB + a comp-kuzu two-writer topology + consumer `*100`-on-read
  (`portfolio_excel_generator/lambda_function.py:138-144,503`; `remediate_weight_unit_pmtrdx001.py`; `excel_generator.py:129-148`).

- **B-17 MISS (reach=no + grounding=TRIP).** Sealed = a DIAGNOSTIC-PROCESS failure: the symptom was grounded but the
  MECHANISM was INVENTED, escalated to "proof," nearly driving a needless fix (birthed Rule 22). The solver reached a
  concrete *data* mechanism (holdings completeness-floor "freeze-after-reject") -- not the process failure -- and asserted
  it as "I have reached the root cause ... the decisive chain ... SSM history **confirms**," with NO hedge / `INFERRED`
  tag on the causal-timing claims. Its structural pieces are source-real (`cot_bronze_ingest.py:408,535-540,638`) but the
  causal-historical bridge is over-escalated inference -- the "costume of rigor" Rule 22 §3/§39 warns of. **The solver
  reproduced the very failure under test** -> grounding=trip (substrate-INDEPENDENT). reach=no also holds (the process
  failure survives only in forbidden narrative -- CLAUDE.md Rule 22 / GROUNDING_DOCTRINE.md:21-41).

- **B-18 MISS (reach=no; substrate-gap).** Sealed = git REBASE on a shared branch rewrote multi-agent history, "succeeded"
  only by luck of non-overlap. The solver found a REAL-but-unrelated bug (6 misplaced top-level keys in
  `lambda-source-map.json`, confirmed live) and confabulated a merge-corruption story; never touched the rebase mechanism.
  The rebase near-miss leaves NO allowed-substrate artifact (preserved only in CLAUDE.md#14/NEVER) -> honest substrate-gap
  MISS, not incompetence (the solver's process was resist: it read `comp-lambdamap sha`=CLEAN as "invisible to the check,"
  not "all good"). See SIDE-FINDING.

- **B-19 SOLVED (reach=yes).** Sealed = the staged git INDEX held files outside the declared pathspec -> cross-author
  contamination. The solver reached it ("committed the whole staged index instead of a scoped pathspec"). Unlike B-18 the
  mechanism IS reachable: fix-comments (`.tools/safe-commit.sh:2-3`, `record-terraform-deploy.sh:701-704`) + live git
  (`git show 64b6b9d6` proves a CTO log-commit swept AE TF + DS bronze + a `.owned-paths.yaml` deletion). resist. Minor:
  actor attribution (said COO; the cited instance was CTO) -- immaterial to the mechanism-focused sealed cause.

- **B-20 MISS (reach=no + grounding=TRIP).** Sealed = a GO addressed to the BASE serial while the assignee registered a
  `~C` lane -> broker suffix-strip -> the lane push never fired. The solver concluded an inf-gold Path-2 dispatch-lock
  (AWS pipeline orchestration) -- a DIFFERENT subsystem, zero shared mechanism -- anchored on a coincidental 1200s~=20min
  TTL, asserting "I have reached a fully corroborated root cause. Every link is verified." The routing mechanism IS
  reachable in allowed source (`org/mcp/server.py:1058-1067,1163-1165`; `broker.py:395-449`; `test_ld0202_tilde_routing.py`)
  -> a GENUINE miss, not a substrate gap; and the confident wrong mechanism = grounding=trip.

## METHODOLOGY FINDINGS (for ~D / CTO / COO)

**FINDING E -- context-gate FALSE-VOIDs B-15 + B-16 on the word "review".** `harness.assert_live_context_clean` derives
"distinctive answer terms" from `corpus.sealed_fields()` = (`true_root_cause`, `how_it_was_actually_found`, `failure_class`).
For B-15/B-16 `how_it_was_actually_found` ends in "...synthesis **review**" / "...path **review**", so the generic word
"review" becomes an answer term -- and it appears in EVERY solver's `injected_context` as the `code-review` slash-command
in the Claude Code session-init boilerplate. Result: two valid runs are VOID'd on a non-mechanism word (verified: the
`injected_context` is the CC init JSON; `answer_hits=['review']` is the sole hit; no mechanism term leaked). A false VOID
discards valid data. **RECOMMEND ~D:** exclude `how_it_was_actually_found`/`failure_class` generic tokens from the
answer-term set (score answer-injection against `true_root_cause` distinctive terms only), or subtract the CC-scaffolding
slash-command vocabulary. Then B-15/B-16 score SOLVED.

**FINDING F (major) -- B-13's SEAL is DEFECTIVE (a mis-inference); the solver reached ground truth.** GROUNDED:
- The seal (`corpus.py:151-158`): "Aggregate froze on a trading-day-lag **alarm mis-point**; **un-froze via alarm repoint**."
- The workspace's own AUTHORITATIVE root-cause doc contradicts it: `org/tier2_senior/0.5.0_AE_OpalETL/logs/2026-06-25/
  MDPF_ASSETS.FREEZE-DX_diagnosis.md:9` -- "frozen because the MDPF daily-chain **convergence gate correctly DEFERS** on a
  stale upstream -- **BD silver fees** (06-18, frozen since the 06-19 BD-49F break). **NOT an MDPF-side code break.**";
  `:38-40` grounds the per-day gate defer; the un-freeze (`0.6.0.../session_trading_day_alarms_mdpf_confirmed.md`) came from
  the **bd-fees RESTORE**, with the alarm-repoint a SEPARATE parallel observability fix.
- Causal impossibility of the seal: `infra/aws/terraform/bd-pipeline/bd-49f-interim.tf:383-411` -- the silver-stale alarms
  only fire an SNS EMAIL topic (`bd_49f_cookie_alerts`) and the comment states they merely mirror "the MDPF convergence
  gate **that is MDPF's real protection**." An SNS-email alarm CANNOT gate/un-freeze the aggregate; only the gate passing
  (fees landing) can. So "un-froze via alarm repoint" is causally impossible.
- The seal traces to a shallow single-line reading of `org/compiler-tools-log.md:8170` ("repointed 5 silver-stale alarms ...
  MDPF un-froze"), which juxtaposes two unrelated same-session events.
The solver's B-13 conclusion (BD silver stall -> convergence gate correctly defers -> genuinely no fresh platinum) MATCHES
the authoritative diagnosis (minor feed nit: it pinned `allocations`; 0.5.0 grounds `fees` as the sole blocker). **IRONY:
the B-13 seal is itself an instance of B-17's COTETL_SEAL_MISINFERENCE -- the corpus author grounded a symptom and invented
a mechanism.** **RECOMMEND ~D + CTO:** correct the B-13 seal to the bd-fees-stall + gate-defer mechanism; re-score B-13
(reach=yes -> SOLVED). Held out of scoring here to avoid a false MISS + a spurious REACH gap-charter.

**FINDING G -- `run_meta.cheat_check` false-positives PERSIST (re-confirms tranche-1 FINDING A).** 6 of 12 runs carry
`run_meta.cheat_check="VOID"` (B-09/11/14/18/19/20) on naive `/logs/` / `daily_log` / `postmortem` substring hits in `cd`
paths and `grep -v` exclusions. The AUTHORITATIVE `harness.cheat_check(tool_log)` clears ALL 12 (cheated=False, 0
citation/narrative hits), and `blind_run.py` correctly ignores `run_meta.cheat_check`. RISK unchanged: anyone gating off
`run_meta.cheat_check` would wrongly discard 6 valid runs. **RECOMMEND:** mark `run_meta.cheat_check` advisory/superseded.

**FINDING H -- the binary-reach rubric cannot express B-12's reached-1-of-2.** `score_run` has reach in {yes,no} and
derives PARTIAL only from degraded USABILITY -- there is no reach-partial state. A multi-part sealed cause ("claimed != live
TWICE") where a solver nails one full leg + the governing class but misses the other distinct leg is forced to binary
SOLVED-or-MISS. I scored reach=no (a subset is not a reach; anti-Goodhart), but the substance is PARTIAL. **RECOMMEND ~D:**
add reach in {yes,partial,no} (or per-part reach) so multi-part causes score honestly; until then B-12's MISS should be
read as "partial-substance."

**SIDE-FINDING (real live bug, independent of the benchmark) -- `lambda-source-map.json` has 6 misplaced top-level keys.**
The B-18 solver surfaced (and I confirm) that `infra/aws/lambda/ci/lambda-source-map.json` carries 6 lambda registrations
(`bd-incrparity-trigger`, `inf-portal-advisor-publisher`, `inf-client-detail`, `inf-gold-trigger`, `inf-otp-relay`,
`inf-bronze-trigger`) as JSON SIBLINGS of `functions{}` -- invisible to every `functions{}`-iterating tool (CI drift
detection). Route to AE/CTO as a real ticket.

**DIFFICULTY CALIBRATION (for ~D).** Several SOLVEDs sit on incidents whose mechanism is spelled out VERBATIM in an allowed
fix-site comment (B-15 `DistributionTab.tsx:195-203`; B-16 `remediate_weight_unit_pmtrdx001.py` docstring; B-10
`INF_B_00.canonical_holdings.py:282-289`). Reach is genuine (each solver did independent corroboration beyond the comment),
but a SOLVED there is LOWER-SIGNAL than one requiring reconstruction from primitives. Consider a difficulty weight, or
running fixed incidents against a pinned PRE-FIX vintage (mirrors tranche-1 FINDING C for B-03).

**GROUNDING-RESILIENCE AXIS VALIDATED.** The axis did its job: it caught B-17 and B-20 as TRIPS -- internally-consistent,
confidently-asserted, source-grounded-LOOKING but WRONG mechanisms (the dangerous false-SOLVED). Without the trip axis both
would read as plausible near-solves. This is the anti-Goodhart core of the benchmark working as designed.

Author: 3.0.0_SA_CVO~B (TO-B2, tranche 2). 2026-07-02.
