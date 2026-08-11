# DEPLOY-COMPLETION LEDGER — MDPF ATOMIC WINDOW (RP-W1 + RP-W2 + RP-W3)

**Opened:** 2026-08-11T01:50Z by 2.0.0_SA_COO (window caller/coordinator)
**Status:** OPEN — closes only when every leg lands + the post-window QA read completes, or on full rollback
**Authority chain:** Andrew plan-order (via CTO @dbbbfa9cd3) → Andrew all-four ruling ~2334Z (Call 1
route (b): W1+W3 one atomic change; clock floor 13:30 / pulls 13:02) → COO topology decision (W2 in
the atomic set) → gate 1 DS BUILD-READY @bf74d031c1 (004145Z) → gate 2 clock ruling (satisfied
~2334Z) → precondition RP-W5b PROVEN (AE 014529Z, ledger @0a00e8f572). Andrew's clock tonight:
"This needs to be fixed tonight."

## LEGS (both land inside this window; NEITHER SHIPS ALONE; either fails → BOTH roll back in-window)

| leg | owner | content | state |
|---|---|---|---|
| L-A code cp | 0.4.0_DS_ClientPlatform | 2-file cp to s3://opal-data-mdpf/code/scripts/gold/: dim_mdpf_aggregate_aua_timeseries.py + build_mdpf_spine.py (measured invoke set; NO trio mint) from @bf74d031c1; then comp-pipescript deployed check | **DONE** 025153-025157Z (COO-validated; see LEG CLOSES) |
| L-B cadence apply | 0.7.0_AE_CloudOps | RP-W3: mirrors ahead of floor; floor → 13:30Z; pulls → 13:02Z; cutover-gap plan STATED pre-apply; targeted apply, plan READ (no daily-aua row possible — declaration removed by W5b); RP-W4 selector apply may ride before/with | **DONE** applied ~0210-0224Z (CTO applied-truth 0-drift; see LEG CLOSES) |
| L-C QA read | AE fires, AE+DS read | ONE ad-hoc cycle post-L-A/L-B: (1) four scopes emit / which errored, (2) inflection legs carry corrected vintage, (3) inflection build reads zero smartx/** keys. FENCE: output never published, never the bar, discharges no acceptance | FIRED 0258Z; item-2 FAIL-as-measured (wrong-code-channel, see AMENDMENT); RE-FIRES once post-L-D |
| **L-D code-channel remedy** (ADDED 031xZ; **SHAPE AMENDED 0318Z ANDREW-DIRECT**, see AMENDMENT II) | design 1.0.0_SA_CTO → build+deploy 0.7.0_AE_CloudOps | ~~private lambda-artifacts re-pin~~ **SUPERSEDED by Andrew-direct (via CTO 031808Z), VERBATIM: *"the remedy is handle this in a canonical bucket and colocate in a relevant place like opal-data-assets"*.** Content UNCHANGED @bf74d031c1; artifact HOME = canonical bucket colocated in opal-data-assets (attacks the 3-location code-split root). CTO finalizing exact prefix + confirming shape with Andrew → routes precise path to AE → commit → safe-apply → verify live CodeSha256 CHANGED from XuLlClWT6kr6n5TCG7keFmzVd8KEafMuAIQutJB+utQ= + LastModified tonight. Rule-17b-ALIGNED but a REMEDY Andrew directly ordered, NOT a migration inferred from 17b | OPEN (AE held off the private-bucket path; COO 031158Z GO shape SUPERSEDED) |

## PRE-REGISTERED READINGS (decided before evidence)
- QA read shows scopes emitting but FEEDERS STILL FROZEN → EXPECTED (separate WS-lambda mechanism,
  AE-surfaced, routed) — NOT a window failure.
- Any leg fails → both roll back inside this window; ledger closes on rollback with reason; COO
  escalates loud (no stranded leg overnight).
- 13:30Z 2026-08-11 unattended scheduled cycle = the ONLY completion-bar evidence (12/12 A4, served
  meta advancing, never S3 mtime). COO adjudicates.

## RECOVERY ANNOTATION — 20260811T025xZ (2.0.0_SA_COO respawn, PID 5820)
- COO session CRASHED mid-window (after open + GO fire; last inbound acted-on evidence: AE pre-apply
  statement 015806Z found un-acted in read/). Respawned + re-registered ~0245Z. CTO held the recovery
  picture in the interim; DS + AE respawned and directed to sync with CTO.
- Leg state at recovery: **L-B** — AE stated the cutover-gap plan pre-apply (015806Z, criterion 2 met)
  and applied ~020xZ; CTO live read reports L-B LIVE (verification evidence pointer to follow from
  CTO/AE — row flips to DONE on applied-truth evidence, not self-report). **L-A** — OPEN; DS respawned,
  reading the un-acted 014749Z GO, landing before 13:30Z. **L-C** — OPEN; fires only after L-A.
- **WINDOW RULING (COO, window caller): the crash is a COORDINATION interruption, NOT a leg failure.
  The pre-registered rollback trigger ("any leg fails → both roll back") does NOT fire on it.
  FORWARD-COMPLETE ratified (CTO recommendation, COO concurs): L-A lands, then L-C, window closes on
  the normal bar. Rollback trigger remains an actual leg FAILURE only.**
- Completion bar UNCHANGED: 13:30Z 2026-08-11 unattended scheduled cycle (12/12 A4, served meta
  advancing, never S3 mtime). COO adjudicates.

## LEG CLOSES (COO-validated, applied-truth evidence)
- **L-A CLOSED 025326Z** (DS report; COO-validated): cp from the git BLOB bytes of @bf74d031c1
  (review/deploy split — deploys the reviewed artifact by construction). Pre-fire live-state check
  proved non-no-op (prior ETags 2b5bba70…/f52858d0…, pre-window vintage 08-10T13:16Z). Post-cp
  3-layer verify: head-object (dim e7b169a70b80353dcb010187ad6903cd 161,769B @025153Z; spine
  6ebc6a822c4d8f55634c070ab145b10b 8,033B @025157Z) + read-back cmp SERVED==PINNED byte-identical
  + comp-pipescript deployed --pipeline mdpf MATCH both files.
- **L-B CLOSED 025336Z/025421Z** (CTO + AE convergent live reads; COO-validated): all 6 cadence
  schedules LIVE == committed HEAD @9eff54d274, 0 drift, all ENABLED — pulls cron(2 13)Z · floor
  cron(30 13)Z · bridge cron(10 14)Z · publisher cron(20 14)Z · mirror-inf cron(5 15) · mirror-cot
  cron(30 18) America/New_York unchanged. W4 step-i selectors verified: mirror_inf Target.Input
  {"firm":"inf"}, mirror-cot {"firm":"cot"}. Sources: aws scheduler get-schedule / events
  describe-rule / list-targets-by-rule (025x-030xZ, this session) + terraform plan 0-diff on every
  cadence/selector resource across the 3 roots. Apply timestamps 0210-0224Z — applies COMPLETED
  before the crash (~0226-0231Z). Fenced caveat (AE): 3 PRE-EXISTING drift items in those roots
  (route_bindings S3 object; bd49f ReadTaxsmaRoster grant; 3 smartx lambda code-hash drifts
  vintage 07-16) — none touched by this window; enumerated in CTO copy 025405Z.
- L-C: UNBLOCKED as of L-A close — AE fires the one fenced ad-hoc QA cycle, AE+DS read.

## L-C QA READ (AE fired 025841-025856Z, qa_local mode — fence intact, zero S3 writes)
- 49financial EMITTED 3/3 · inflection EMITTED 3/3 (account-distribution 08-10, aggregate-aua-timeseries
  08-07, aum-metrics 08-07 each) · **cottonwood SCOPE FAILED (isolated)** — differing-dollars guard
  SystemExit at value_date=2026-08-06: 08-07 run 133,914,199.99 vs 08-08 run 139,213,957.62; refusal per
  CTO condition 1 (234639Z) — **the guard working as ruled** · global fold SKIPPED honestly (I-1 leg pins
  require cottonwood). Cycle: 6/12 A4, non-green. Log stream 2026/08/11/[$LATEST]31b81ca2a2a648528c3a5004c1e349fb.
- **CLASSIFICATION (AE, COO-validated): NOT a window failure.** The collision is between pre-window runs
  (08-07/08-08 valuations of the 08-06 snapshot) — the open cottonwood-causation thread (CTO). Neither
  L-A code nor L-B cadence caused it. Near the pre-registered EXPECTED class in mechanism (pre-existing
  feeder-side condition through a working guard); shape honestly stated as data collision, not feeder
  freeze — recorded plainly, not force-fit.
- Items 2+3 (inflection vintage; zero smartx/** reads): DS read PENDING (pointer delivered by AE).
- ROUTED: the collision (which valuation of 08-06 is correct) → 1.0.0_SA_CTO (cottonwood-causation
  owner) with the run-pair evidence. **No gate**: the CTO thread runs on its own clock; the window does
  not hold on it.

## 13:30Z BAR — INTERPRETATION PRE-REGISTERED (COO, 030xZ, BEFORE the evidence exists)
- **12/12 A4 + served meta advancing** (collision resolved pre-cycle) → FULL PASS as originally registered.
- **Cottonwood refuses on the SAME differing-dollars collision; every other scope emits fresh; meta
  advances; every consumed C1 precedes the floor** → **WINDOW CHANGES PASS PER-SCOPE**; the cottonwood
  data question stays its own routed item (CTO), not window scope; RP-W3 completion recorded with the
  residual NAMED. 
- **Any other degradation** (a scope that emitted in QA failing unattended · floor firing off-schedule ·
  meta not advancing · vintage regression on 49f/inflection) → **BAR FAILURE** — escalate loud, rollback assessed.
- Rationale: the bar exists to prove the WINDOW'S changes. A pre-existing data defect surfacing through a
  correctly-working NEW guard is not evidence against them — but that reading is only honest if chosen
  BEFORE the evidence, which is what this pre-registration does. (Per the pre-register-evidence-reads
  discipline.)

## WINDOW-EXISTENTIAL AMENDMENT — 20260811T031xZ (DS finding 030919Z, COO-validated; L-D added)
- **THE FINDING (3 independent derivations, Rule 22a):** the 13:30Z floor (post-L-B) fires
  **mdpf-gold-lambda**, whose package is ASSEMBLED FROM A PINNED COMMIT (build_package.py, spine baked
  flat at zip root) — pin @0bc739e7d5, deployed 08-07T03:52Z, **PRE-dating the fix @bf74d031c1**.
  (1) DECLARATIVE lambda-source-map pin/last_deployed; (2) APPLIED live get-function-configuration
  CodeSha256 XuLlClWT6kr6n5TCG7keFmzVd8KEafMuAIQutJB+utQ= == the 08-07 artifact, LastModified
  08-07T03:51:21Z, nobody redeployed tonight; (3) BEHAVIORAL the 0258Z qa_local invoke (post-L-A)
  emitted DS's documented PRE-fix values (inflection 08-07 custody 208,325,960.35 / model_aua
  144,545,199.97; D-4 anchor 209,431,383.43 still at the 08-05 mislabel). Consolidator calls
  spine.build_firm_timeseries directly (mdpf_gold_consolidator.py:778-781).
- **WHY EVERY INSTRUMENT READ GREEN:** L-A landed byte-identical on s3://opal-data-mdpf/code/scripts/gold/
  (the mdpf-daily-runner channel); comp-pipescript deployed MATCH is TRUE for that channel and
  **STRUCTURALLY BLIND to the Lambda zip channel**. Two code channels, one fix, landed on the one the
  floor does not read. **Instrument-coverage gap routed to CTO** (Rule 22: a comp-tool coverage gap is
  a DEFECT) — the gap record is post-window work, not tonight's.
- **COO RULING: NO LEG FAILED — the window SPEC was incomplete by one leg.** L-A is correct on its
  channel (nothing rolls back); L-B cadence is correct. The pre-registered fail-both clause does NOT
  fire on a spec gap. **FORWARD-COMPLETE: leg L-D added** (Lambda re-pin to the SAME reviewed artifact
  @bf74d031c1 + TF apply, AE lane per Deployment Rules 1/2/4/18). Window intent unchanged: the reviewed
  fix, landed on the path that EXECUTES, tonight.
- **L-C RE-FIRE AUTHORIZED (once, post-L-D):** the 0258Z cycle read the OLD code, so its item-2 purpose
  was structurally undischargeable. Same fence; **re-fire scope = ITEM 2 ONLY.** Item-1 mechanical
  findings (cottonwood guard refusal, global skip) stand — code-channel-independent.
- **L-C VERDICTS AS DELIVERED (DS 031xZ, COO-validated):** **ITEM 2 SPLIT** — (a) as-emitted by the
  0258Z cycle FAIL (PRE-fix values; mechanism = the 08-07-pinned lambda package, i.e. the wiring
  finding, NOT a code regression); (b) **on the LANDED code PASS** (instrumented run importing the
  deployed-channel bytes, cmp-verified == @bf74d031c1, import path asserted): POST anchors reproduced —
  custody 209,373,343.50 / model_aua 145,329,103.38, source_vintage 2026-08-07 == frontier,
  lag_vs_as_of_days=0 truthful, tdb=2 = the Monday convention, orion gap at TRUE label 08-05 (old code
  puts it at 08-06 — a second two-channel behavioral discriminator). **L-D therefore converges (a)→(b)
  by construction — the code being re-pinned is already behaviorally proven.** **ITEM 3 PASS, CLOSED**
  (no re-confirm needed — both code vintages agree): sharp leg = instrumented boto3 trace, DENOMINATOR
  987 S3 read calls, smartx keys touched 0, distinct targets exactly {eclipse/inflection/silver
  fact_portfolios_full · orion/inflection/silver fact_assets · inflection gold
  account_distribution.json}; supportive leg = lambda log stream (139 events, positive control
  present), smartx mentions 0. Pre-registered readings observed as expected (feeders frozen ·
  ROW11 stale known · cottonwood collision separate). Fence intact throughout.
- **INTERPRETATION TABLE AMENDED — EXECUTING-CODE PRECONDITION ADDED:** every PASS row of the 13:30Z
  pre-registration now additionally requires the cycle to have EXECUTED the @bf74d031c1 code:
  live CodeSha256 != the 08-07 value BEFORE the cycle, AND emitted bodies carry the POST-fix oracle
  values (inflection custody 209,373,343.50 / model_aua 145,329,103.38; D-4 anchor labeled 08-04).
  A 13:30Z cycle on the OLD sha is NOT adjudicable as a pass on any row — the original table silently
  assumed the executing channel carried the fix; that assumption is now explicit and testable.

## AMENDMENT II — ANDREW-DIRECT ON L-D SHAPE (via CTO relay 031808Z; COO 031158Z GO superseded)
- VERBATIM (recorded by CTO, carried here unparaphrased): *"the remedy is handle this in a canonical
  bucket and colocate in a relevant place like opal-data-assets"*.
- Binds the mdpf-gold-lambda code-channel REMEDY: artifact home = canonical bucket colocated in
  opal-data-assets with the mdpf gold data, NOT s3://opal-313476888478-lambda-artifacts. Fix CONTENT
  unchanged (@bf74d031c1). The 13:30Z executing-code precondition and the L-C item-2 re-fire are
  UNCHANGED — only the artifact HOME moves.
- Sequencing (dependency visible for the runway, ~10.1h at amendment): CTO designs canonical target +
  confirms shape with Andrew → routes precise path to AE → AE build+deploy (commit → safe-apply →
  sha-change verify) → L-C re-fire (item 2) → window close. AE held off the private-bucket path
  (CTO hold + this COO supersede — the two instructions now agree).
- Scope note per the no-adjudication rule: scope as CTO relayed it, not widened here — this is the
  L-D remedy shape, not a general migration order (Rule 17b's own ⛔ stands for everything else).
- **CROSSED-IN-FLIGHT (AE 031946Z, timeline-honest):** the COO 031158Z GO EXECUTED CLEAN AND FAST
  BEFORE the 031758Z hold landed — commit f72495f387, artifact 031636Z, targeted safe-apply ~0318Z
  (1 changed), **live CodeSha256 t0w3vTNV0CpImT1EqzIdtVhUZlkwNzCrx3zA0zpM8/c= @03:18:27Z = the
  reviewed @bf74d031c1 package EXECUTING.** No violation: a valid GO executed; the supersession
  arrived post-completion; AE reported with full timestamps. STATE: correct CONTENT live on the
  executing path (the 13:30Z bar would now run post-fix code); artifact HOME non-canonical
  (lambda-artifacts) pending CTO's canonical prefix + TF data-source change. AE HOLDS: L-C re-fire
  (NOT fired), tags, further TF. AE correctly NOT rolling back unilaterally (revert would re-expose
  the bar to the pre-fix spine). **CTO adjudicates relocate-over vs revert; COO coordinator input
  filed = RELOCATE-OVER** (Andrew's word binds the HOME, not the un-landing of correct content; a
  home-only repoint with identical bytes is DELTA=0 on content and keeps the bar protected).

## CLOSE-ITEMS CARRIED (not leg content)
- @9eff54d274 (+ window ledger commits) UNPUSHED — integrator push at window close per live-regime
  standing (lanes commit, integrators push); tags proposed at close (Deployment Rule 6).

## CLOSE
- Closed: PENDING
