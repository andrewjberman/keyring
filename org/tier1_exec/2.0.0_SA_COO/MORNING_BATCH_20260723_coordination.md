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

## OPEN — behind explicit gates

**TEMPO (Andrew "go" @050247Z, via CTO):** no-hard-clock items accelerate to NOW-when-ready (not "morning")
— same as the night has run. Items with REAL clocks keep them: the **02:00Z 07-24 07-22 re-land** (item B)
and the **14:15Z B3 pass** (Inflection propagation, CTO-owned). CTO gates as before. "go" discharges WAITING,
never CHECKS.

**>> BATCH FIRED @~10:36Z (CTO 103121Z, daylight):** dispatched to owners in the ruled order —
**WS-1 FIRST** (0.6.2, cookie durable-mint fix, the shelf-life item, CTO gates auth) -> 6d dispatcher
wiring (DS+0.7.0, trend grows itself tonight) -> never-retry (0.6.2) -> S5 provenance sidecar + createdAt
passthrough (DS, CTO gates) -> demo custody (DE) -> 07-22 re-land readiness (0.6.2, tonight's 02:00Z).
**Band BF2 acceptance render PULLED FORWARD** (DE, now-when-ready — was mis-queued as "morning batch").
Also 0.5.0 AC5 13:30Z + B3 14:15Z keep their clocks. **STALE-HEARTBEAT NOTE:** CTO's "Publish FIRING"
summary was his own 01:31Z vintage (original page, not the band); my "serve-calculus surfacing" summary was
04:30Z vintage (discharged by Andrew "go"). Both corrected ~10:31Z — LD-0334 caught symmetrically. **No
band publish cites an incomplete COO co-sign; the band serves only on DE render + COO identities limb.**

**BATCH DELIVERIES (running, @~10:55Z):**
- **0.6.2:** never-retry DONE (qt_0722_reland re-mint-once-on-401 through every tokened call, ETag eded477d) +
  07-22 readiness CONFIRMED (self-gating script + mutual lift protocol with DS, ready for 02:00Z 07-24).
  **WS-1 ROOT CAUSE found + at CTO's gate:** the "fires-without-writing" is CTO's own 07-06 Lever A
  (OTP-skip on live-cookie probe, NO age bound, `lambda_function.py:213-227`) skipping the mint every night
  as ruled — not aging cookies. Plan (age-bound the lever + one interim hand-mint today + visibility rider)
  at CTO's gate (amends his own ruling). The larger `cot_bronze_ingest` daily-chain retry = CTO's lane (Rule 13).
- **DS:** 6d wiring half = git-apply-clean patch `@3e7a59502` -> 0.7.0 (owned-paths correctly split the AE
  lane) + S5 COMPLETE `@1351c74d9` at CTO's gate (sidecar + createdAt passthrough + force-guard, ONE pass;
  controls RUN: row-count parity 911==911, force-guard 07-21-refused exercised, grounded-negative on roster).
- **6d DISPATCHER — COMPLETE @~11:03Z (0.7.0, ledger 5/5), CLOCK DE-RISKED:** both halves landed (DS block
  `@4528fa154` + AE PYTHONPATH resolution), marker 7->11, ETag-verified. **NO TF, no schedule change** (Rule
  12 code path) — so no 02:04Z gate to race; tonight's 02:04Z nightly IS the exercise, outcome banked as a
  07-24 post-02:10Z trigger (keys_staged=11 + slice covered_dates nonempty = trend grew itself). The runner
  import chain was EXERCISED (not config-read) and caught 2 gaps: **`dim_mdpf_aum_metrics.py` ABSENT from S3**
  (would have killed tonight's 6d) staged from HEAD + an unlisted transitive dep (already on S3). Rule 22a
  earning its keep. **RESIDUAL CLOSED** (DS version-confirm 110340Z: md5 `a9dbddd0` == HEAD `@7c8320da4`,
  explicit-intended, import-safe + R-4 deploy-correct). 6d fully done; 07-24 post-02:10Z outcome trigger armed.
- **>> REMAINING CLOCK: S5 cutover** constant `2026-07-23` conditioned on the **lambda-twin deploying**
  before the next conversion (slips a day -> constant bumps, no frozen assumption). At CTO's TF apply gate;
  owner TBD (0.7.0 loosely available). **NO schema re-stage precondition** — a transient "5471afde predates
  S5, re-stage with the twin" note was RETRACTED (0.7.0 110534Z / DS self-correct 110454Z): the staged
  `rebalancer_schemas 5471afde` is ALREADY post-S5 (md5-verified vs HEAD AND vs pre-S5 `9d9fce12`; staged
  from HEAD after the S5 commit), and there is no runner-side skew tonight (converter never runs on that box;
  the lambda bundle carries its own copies, moves atomically under CTO's TF gate). The twin just deploys clean.

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
- **Remaining gates — ANDREW SERVE WORD GRANTED `@050247Z` ("go"); now TECHNICAL-ONLY, now-when-ready:**
  (1) **CVO blesses the WASHOUT-KEYED cap + signs the delta into the pin `@ec5ec79f3`** — against LANDED
  code + 16/16 green (a real verify-against-code); (2) **co-sign pair AT THE ARTIFACT** — DS BF1 + DE BF2
  acceptance render on REAL provenance, CTO co-signs, COO counter-verifies (canonical key-set + count-axis
  + identities + point_class labels + early-band confidence degradation, read-not-transcribed); then serve.
  **>> "go" discharged Andrew's WAITING, NOT the CHECKS <<** — gates 1-2 still bind; a failed check is
  fix-before-serve (CVO's ruling). No further Andrew round-trip. [CRO method-intent + cap CONFIRMED
  `@044637Z`; Andrew serve-calculus DISCHARGED `@050247Z` — both no longer pending.]
- **PROGRESS @~0530Z:** (1) CVO SIGNED the washout-cap delta into the pin `@8bbe49516` (verified+exercised
  against landed code, ran 16/16 himself). (2) **COUNTER-SIGN CAUGHT A STALE ARTIFACT:** the staged
  interpolated artifact was generated `04:21:30Z` — 27 min BEFORE the cap `@7abc02182` (04:48:47Z UTC) —
  carrying pre-cap emergent confidence (~0.50 early band). DS RE-EMITTED from the capped producer
  (`generated_at 05:19:42Z`). The cap BITES on the real blend: 18/46 early-band dates dropped ~0.50 ->
  0.01-0.054 (distant-terminal washout) — a ~50x over-claim prevented. **Confidence cell TRIPLE-verified,
  independent reads agreeing: COO + CVO (`@a09c4d816`/CVO bridge) + DS.** CVO side FULLY CLOSED. (3)
  **Remaining band gate: DE's BF2 render on the re-emit + the identities/point_class-labels limb of my
  counter-sign -> serve.** now-when-ready.
- **PROGRESS @~1120Z — SERVE HELD on a SECOND counter-sign catch (VALUE limb):** DE's BF2 render PASSED all 4
  confirms (vintage/confidence/permanent-wording/extent, grounded from bytes) + fixed 3 real render defects.
  BUT DE flagged the value shape, and I grounded it: **model_aua has a ~$108M ONE-DAY CLIFF** — 06-14 $114.4M
  (conf 0.051) -> 06-15 $6.1M (conf 0.944); early band 05-28..06-14 carries ~$105-116M at conf 0.01-0.05.
  DS grounded the MECHANISM (Rule 22): the absorbing sleeves (Sleeve-Equity/Core-MM/Tax-Free-Bond) were
  created **2026-06-15 = the exact cliff** — pre-06-15 every valued account force-matches into {Sat-80,LTC,LTA}
  = ~$105M of never-in-models accounts (a FORCED GUESS, not an estimate). Governing law: **YANG_SITTW**
  (emit null where the true value is absent; a label carries uncertainty, NOT a 20x known-wrong magnitude).
  **FIX = suppress forced guesses to absent** — DS: per-account washout-epsilon; CTO: confidence render-floor
  (convergent). **CRO EPSILON RULING @112655Z: both 0.10 and 0.50 are WRONG-AXIS** (0.50 = the confidence
  CEILING of a legit weak-real match -> over-suppresses, my concern-b confirmed; 0.10 under-suppresses).
  **Correct = MEASURED, not chosen: the VALLEY in the match-score distribution of KNOWN-REAL post-06-15
  members (ground-truth-calibrated, bimodal); suppress-to-absent below it.**
  **CVO R-5 BLESSED `@efa8a50bf` (byte-grounded):** custody is CONTINUOUS across the cliff (~$116->120M) —
  the assets didn't move, only the model/non-model CLASSIFICATION flipped; 06-15 confidently splits the same
  assets $6M model + $114M non-model = POSITIVE EVIDENCE the early $114M is ~20x wrong, NOT mere uncertainty
  (0.01 conf is the "which-model" axis; this is a "in-a-model-at-all" membership error a label can't cover).
  **>> PRODUCER-SIDE suppression is REQUIRED, not a choice (my "pick the mechanism" framing was WRONG):**
  `interpolated_estimate` is SUMMABLE into the Global sum, so a render-floor alone leaves the fabrication in
  the bytes + the Global model-AUM sum INHERITS it. Producer-side per-account suppression (model->absent in
  emitted bytes) = PRIMARY; CTO render-floor = defense-in-depth. **Pin mutants a/b/c (CRO) + d (CVO): after
  suppression the Global model-AUM SUM on a suppressed date carries NO fabricated value** (d proves the fix
  is producer-side, not render-only). Honesty invariant: absolute match-quality below the known-real-member
  floor -> `absent` (YANG_SITTW at account grain). **SERVE HELD until DS measures the valley + implements
  producer-side suppression -> re-emits -> CVO verifies (cliff gone / early model=absent where suppressed /
  genuine ~$0-6M ramp RETAINED / Global sum clean / a real weak match survives) + my value limb re-verifies.**
  Meta: the confidence cap is now an anomaly DETECTOR — 2 serve defects surfaced (stale-artifact, value-cliff)
  because the low confidence made them catchable. This is downstream of CVO's own candidate-restriction delta.
- **RE-EMIT VERIFIED @~1139Z (DS `@9ffa3ca6e`, 19/19 mutants incl. M6 valley-pin) — CLIFF GONE, byte-read:**
  measured epsilon = 0.10 landed in the bimodal valley `(0.056, 0.170)` (real-member match-scores: forced-era
  median 0.039 / p90 0.056; real-era p5 0.780 — cleanly bimodal, CRO's axis). Corrected band (my byte read):
  early 05-28..06-14 model **~$454K** (the 2 genuine accounts, was ~$105-116M) at real custody; NO cliff;
  ramp $2M(06-15) -> $27.8M(07-13) -> $122M(07-14) -> $124.7M(07-21) = served $124.4M; custody continuous;
  **$2.25B / 5,473 acct-dates suppressed** (verified by BEHAVIOR: model $105M->$454K + CVO mutant-d
  Global-sum-clean — **NOT documented in the artifact bytes**; CVO grepped the whole artifact, the figure
  is absent, I computed it externally from DS's run report. My earlier "reported in meta" was a FALSE
  PREMISE, RETRACTED @~1200Z — do NOT co-sign on "documented in the artifact"; NB-1: DS adds
  meta.suppressed_acct_dates + suppressed_value on next touch). 9 weekend/holiday dates honest-absent.
  **My value limb PASSES** (basis = byte-verified cliff-gone + behavioral suppression + mutant-d, all TRUE). TWO co-sign notes (neither solo-adjudicated): (a) **weekend/holiday WOBBLE** (06-19 Juneteenth
  + weekends dip to $454K, stale snapshots) -> DE trading-day-only x-axis (NEVER#1-aligned, render not data);
  (b) **07-14 ~$95M jump — RESOLVED (COO+DS converge, DS `@113952Z`):** the jump date = "Opal Ultra Short
  Term"'s bronze createdAt 07-14 = the EARLIEST-POSSIBLE-membership date (an account can't be on a strategy
  before it existed — same law as the early-band fix, keep-direction). A timing-smear would fabricate the
  unknowable true migration date (current-stamped), so the labeled STEP is the honest shape ("membership
  begins no earlier than here" = a true statement); 0.50 conf carries the residual. YANG_SITTW at the top end.
  CVO confirms in her 5-point. **NOTE (a) DONE:** DE applied the trading-day-only x-axis `@portal 58a38078`
  (render-only, NEVER#1-aligned; saw-tooth gone, May month-end bar shifted Sun 05-31 -> Fri 05-29) + re-verified
  all 4 confirms on the corrected artifact (confidence label SELF-re-derived to 0.50-1.00, zero code change).
  **>> BAND GREEN ON EVERY LIMB EXCEPT CVO'S BLESS: my value limb green, note (a) done, note (b) closed
  (COO+DS), DS half complete, DE re-verify passes. CVO's pin-bless (epsilon+M6+mutant-d) + 5-point re-emit
  verify is the LAST gate -> co-sign pair (DS+DE+COO green, CTO gates) -> SERVE.** No Andrew round-trip.
  Counter-sign discipline compounding: stale-confidence -> stale-artifact -> value-shape, 3 catches / 3 limbs.
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

### I. GLOBAL AGGREGATION — ACTIVE (Andrew-direct @050002Z, dispatched now, dependency-scoped)
- **Andrew-direct** (via CTO terminal, recorded `andrew_direct_20260723T0500Z...`): Global view aggregation
  is the next target after tonight's Cottonwood page. Dependency-scoped (G8): inputs = signed schema
  `@be91775dd` + the cottonwood artifacts already serving; builds now.
- **DS** (dispatched @050005Z): Global aggregator — point_class from partner/cohort provenance (any-cohort),
  additive, fee-basis 49F+model-INF+model-COT (section-1.3), R-4 current-snapshot guards, Cottonwood folds
  on serving artifacts. Staged-only, ETag control, zero bronze/silver write.
- **DE** (dispatched @050014Z): Global view — mixed-provenance overlay windows, radial+bell-curve gaining
  Cottonwood per fee-basis, honest-absent/labeled inherited; global-mdpf accessor branch inherits derived
  class (confirm vs real artifact).
- **Gate (CTO CONFIRMED @050048Z):** MEASURED Global fold serves on tonight's co-sign pattern VERBATIM
  (CTO co-signs with conditions; COO counters at the ARTIFACT — canonical key-set + count-axis + identities,
  verified-not-transcribed) PLUS the Global-specific law added to MY counter-sign set: **fee_basis_aum ==
  full-49F + model-INF + model-COT TO THE CENT on every date, basis labels present, a label-absent artifact
  FAILS** (3F-G4's acceptance line, live at the co-sign not a later gated TO). Interpolated/backtest bands
  ride their OWN delta+serve gates, NOT folded into the measured Global serve. Sequencing: DS aggregator ->
  DE render -> co-sign pair at the artifact -> serve.
- **PROGRESS @~0534Z:** DS BUILD SCOPE COMPLETE (log `@50ada78f8`): fold `@745572fe4` (cottonwood 3rd leg,
  structurally-absent-vs-gap discriminator, additive cohort_provenance[], per-firm fee_scope map) + R-4
  guards `@7c8320da4` (radial measured-frontier + bell-curve snapshot-source, +/- exercised) + FLAG-2
  preserve `@265e04607` + distribution `_units` sidecar `@fa491f9b6` (funded 7863 / $1.672B). Tonight
  cottonwood's covered set is EMPTY (axis 07-20) so the fold changes ZERO until the axis advances — no false
  fold. **Global aggregator SERVES nothing until its own co-sign pair** (DE render + my fee-basis
  counter-verify — cell loaded above).
  - **FLAG-2 co-sign `@265e04607` — COMPLETE @~0534Z (unblocks the 07-24 02:04Z nightly global rebuild;
    ~21h clock, no tonight pressure per CTO 053134Z):** CTO half = 051427Z ruling (5 conditions). COO counter:
    conditions 1-4 VERIFIED in code (enumerated `[opal_growth_sma, opal_div_sma]` beside the exemption list;
    `count_as_of` in-band set-only-on-preserve; preserve gated to the 2 keys; distribution map untouched ->
    (iii) rejected) + **condition 5 EXERCISED — I ran DS's committed test `@1e3999969`
    (test_global_fold_flag2.py) MYSELF: 5/5 exit 0, and read it to confirm real teeth (CASE 2 poison test
    fails loudly if a non-enumerated value-present/count-None survives).** CTO ruled the committed test
    REQUIRED (structural-safe-by-non-modification is corroboration, not exercise) — the M4/M5 bar is now the
    standing bar for every exercised condition. Minor obs (count_as_of entry-level granularity) pinned by
    test 2 + logged as a named delta if a mid-series SMA gap ever appears.

### J. BACKTEST PROJECTION — design at CRO, envelope FIRM (Andrew "go" @050247Z); COO decomposes when CVO-tandem'd design lands
- **Andrew-direct** (same relay): second next target. DESIGN at CRO (CRO -> CVO tandem -> COO
  decomposition). Envelope **FIRM (Andrew "go" @050247Z confirmed the read; visual STYLE still his at
  design review):** a THIRD provenance class `backtest_projection` (additive enum), composition-derived
  hypothetical pre-creation series, composition-vintage stated per date, NEVER blended with actuals classes,
  its own visual treatment. Wired to CRO @050618Z; I am the decomposition endpoint.
- **COO HOLD:** do not decompose until the CRO->CVO design lands (post Andrew-confirm on what "backtest
  projection" means). DE leaves a seam for the third class, builds nothing on it.
- **DE SEAM (named @050051Z, safe-by-default):** DE's PointClass enum is CLOSED
  ('measured'|'interpolated_estimate'|'absent'); the accessor renders any UNKNOWN enum as
  interpolated_estimate + loud warn. So a backtest point renders conservative + labeled (never unlabeled)
  until the enum + band treatment are extended DELIBERATELY by ruling. Safe by default, extended by ruling.

---
**Delete/prune each item as it closes. This file is the carrier, not the work.**  -- `2.0.0_SA_COO`, ~05:00Z
