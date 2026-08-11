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
| **L-D code-channel remedy** (ADDED 031xZ; **SHAPE AMENDED 0318Z ANDREW-DIRECT**, see AMENDMENT II) | design 1.0.0_SA_CTO → build+deploy 0.7.0_AE_CloudOps | ~~private lambda-artifacts re-pin~~ **SUPERSEDED by Andrew-direct (via CTO 031808Z), VERBATIM: *"the remedy is handle this in a canonical bucket and colocate in a relevant place like opal-data-assets"*.** Content UNCHANGED @bf74d031c1; artifact HOME = canonical bucket colocated in opal-data-assets (attacks the 3-location code-split root). CTO finalizing exact prefix + confirming shape with Andrew → routes precise path to AE → commit → safe-apply → verify live CodeSha256 CHANGED from XuLlClWT6kr6n5TCG7keFmzVd8KEafMuAIQutJB+utQ= + LastModified tonight. Rule-17b-ALIGNED but a REMEDY Andrew directly ordered, NOT a migration inferred from 17b | **DONE** two applies (0318Z code swap + 0329Z canonical re-home), CTO-VERIFIED 033621Z all discriminators |

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
- **RULED 032513Z (CTO): RELOCATE-OVER** — converged with the COO input, crossed in flight. Canonical
  path ROUTED to AE 032326Z: **s3://opal-data-assets/portal/gold/mdpf/_code/mdpf-gold-lambda.zip**
  (home-only TF data-source repoint, IDENTICAL reviewed bytes @bf74d031c1, colocated with the mdpf
  gold output, `_code/` mirroring the existing `_manifests/` convention). Folded into the SAME apply:
  provenance fix — env MDPF_GOLD_COMMIT bumps 0bc739e7d5 → bf74d031c1 (was stamping the old pin
  beside new code, read live by CTO).
- **RE-HOME DISCRIMINATORS (CTO refinement — supersedes this ledger's earlier "verify sha UNCHANGED"
  as the oracle):** sha UNCHANGED is EXPECTED (same bytes) but discriminates nothing. The
  discriminators: (a) TF Code source now = the canonical key + a NEW s3_object_version; (b) the ONE
  real risk — opal-data-assets bucket policy must allow the Lambda-deploy principal GetObject on the
  zip; a deny surfaces as a LOUD apply failure, not a silent skip. AE verifies both before calling
  L-D-canonical done.

## AMENDMENT III — L-D-CANONICAL DONE; RE-FIRE GREEN 12/12; THE BAR FRAME CHANGES (AE 033324Z)
- **L-D-CANONICAL COMPLETE** (AE on CTO routing; commits f72495f387 + 759ef40a12; full evidence in
  AE→CTO 033xZ, CTO to confirm discriminators in their verify pass): artifact re-homed to
  s3://opal-data-assets/portal/gold/mdpf/_code/mdpf-gold-lambda.zip, CodeSha256 UNCHANGED (expected —
  same bytes), env MDPF_GOLD_COMMIT stamp fixed, 0-diff re-plan, old private-bucket copy
  DEPRECATED-in-place. L-D row: DONE pending CTO discriminator confirmation.
- **L-C RE-FIRE (item 2): GREEN 12/12, errors=[] — AND COTTONWOOD BUILT, did NOT refuse.** Mechanism
  (AE, from run log): the re-pin carried DS's implementation of **Andrew's 08-10 point-in-time
  ruling** — earliest assignment 2026-08-07 CHOSEN; later assignments = RESTATEMENTS surfaced in the
  rekey report, never chosen; differing-dollars collision now WARN, not SystemExit. Inflection POST
  oracles PRESENT at presence-grain (209,373,343.50 / 145,329,103.38 / orion 08-05); DS pointed at
  the label-grain formal read. Fence held (qa_local, zero writes).
- **OPEN VALIDATION (CTO, asked 033xZ — material because 13:30Z PUBLISHES, unlike the fence):**
  AE cites an Andrew 08-10 point-in-time RULING implemented in @bf74d031c1; CTO's 030244Z framed
  restate-vs-point-in-time as their OPEN Andrew call. Reconcile: (a) is the point-in-time GOLD-build
  basis Andrew-ratified (cite verbatim/record)? (b) which facet remains open (C-1 custody-plane
  conversion policy is understood to be the open half)? The 12/12 PASS branch below is CONDITIONED
  on (a) confirmed.
- **13:30Z TABLE AMENDED (branches extended, none discarded; executing-code precondition UNCHANGED
  and now doubly verified):**
  · **FULL 12/12** + POST oracles in bodies + every consumed C1 precedes floor + meta advancing +
    **CTO confirms the point-in-time ruling provenance** → **FULL PASS** (the original registered bar,
    now attainable).
  · FULL 12/12 but provenance UNCONFIRMED by adjudication time → window mechanics PASS; the
    cottonwood/global SERVED numbers flagged LOUD same-day for sovereign confirmation — recorded,
    never silently ratified by the pass.
  · Cottonwood refuses (data re-collides on a NEW value_date the policy does not cover) → the
    original per-scope branch applies unchanged.
  · Any non-cottonwood degradation → BAR FAILURE, loud, rollback assessed.
- **NAMED READER ASSIGNED: 0.4.0_DS_ClientPlatform reads the cottonwood rekey/restatement report**
  (their implementation, their label-grain read already in flight) — verdict lands before window
  close; restatements are TRANSPARENCY, and transparency needs a reader to be real.

## L-C COMPLETE (DS item-2 re-read 033615Z, COO-validated) — window close waits ONLY on CTO
- **ITEM-2 RE-READ: PASS, full label grain** (re-fire run 033045-033146Z, 12/12, errors=[]):
  custody[08-07]=209,373,343.50 == oracle · model_aua[08-07]=145,329,103.38 == oracle ·
  custody[08-04]=209,431,383.43 at its TRUE Tuesday · the old mislabeled 208,325,960.35 now at
  EXACTLY ONE label (08-06, its true day; full 441-date vector searched, not just anchors) ·
  label 08-05=None (orion gap at true label — the landed-code discriminator) · sv=frontier, lag=0
  truthful, tdb=2 Monday convention · aum-metrics sums tie to the cent. APPLIED leg independently
  re-confirmed 032924Z: sha CHANGED + env MDPF_GOLD_COMMIT=bf74d031c1 (full hash).
- **PRECONDITION PRECISION (DS):** tonight the 13:30Z "sha changed + POST values" precondition is
  satisfiable AS WRITTEN. **FUTURE re-pins under the runtime-pull architecture move the ENV STAMP
  only (sha stops discriminating)** — any future window's precondition must key on env stamp +
  behavioral discriminators. Carried forward so the next window does not inherit tonight's oracle.
- **AUTHORITY STAMPED IN-BAND (input to the open CTO validation):** the artifact meta itself carries
  the rekey authority chain — CTO three conditions 234639Z + **Andrew-direct pull-forward
  2026-07-29** — and the restated delta 5,299,757.63 surfaced in-band (ties: 139,213,957.62 −
  133,914,199.99). DS's read: real building, not error-masking.
- **NAMED-READER DISCHARGE (COO ruling): at GLANCE grain** — authority-stamped + delta-surfaced +
  arithmetic-consistent. The DEEP rekey adjudication (is the chosen "earliest" itself clean of the
  CRO~A-characterized retry-net defect) is DELIBERATELY LEFT on CTO's causation thread where the
  mechanism context lives — commissioning a parallel deep read from a crash-recovered DS seat would
  duplicate, not verify. The serving-basis condition on the 12/12 FULL-PASS branch (Amendment III)
  covers the risk.
- **RESIDUE (DS → CTO, post-window):** the estate now carries TWO LIVE CODE CHANNELS for the same
  mdpf gold scripts (runner s3://opal-data-mdpf/code/scripts/gold/ · lambda
  s3://opal-data-assets/portal/gold/mdpf/_code/) — tonight's defect class, rebuilt; plus the
  Rule-17b grammar observation (code under a portal/gold serving prefix). CTO routing.

## CLOSE-ITEMS CARRIED (not leg content)
- @9eff54d274 (+ window ledger commits) UNPUSHED — integrator push at window close per live-regime
  standing (lanes commit, integrators push); tags proposed at close (Deployment Rule 6).

## PROVENANCE RESOLVED + SHA-CLAIM SPLIT (CTO 033621Z · AE 033659Z)
- **CTO ANSWER to the Amendment-III validation: face 12/12 is LEGITIMATE.** @bf74d031c1 implements
  **Andrew's 08-10 point-in-time ruling** (earliest chosen; restatements surfaced, never chosen);
  the 0258Z refusal was the OLD pre-ruling package. CTO's open Andrew call is the SEPARATE C-1 track
  (whether custody VALUES in the settle window should track the restatement) — does not gate this
  window. **The 12/12 FULL-PASS branch's provenance condition is SATISFIED IN ADVANCE.**
- **CLOSE-WORDING GUARDRAIL (CTO, adopted verbatim in the close below): 12/12 is a BUILD-success +
  LABEL-correctness bar, NOT a value-settledness attestation** — the point-in-time choice serves the
  earlier/less-settled value on a collision (133.9M chosen over the 139.2M restatement) BY RULING,
  with the delta surfaced. Never read the pass as "all served values settled-correct."
- **SHA DISCRIMINATOR = TWO CLAIMS, TWO APPLIES (AE/DS precision, for the 13:30Z reader):** apply 1
  ~0318Z (private-bucket, pre-supersession): sha CHANGED XuLlClWT…→t0w3vTNV… = the CODE SWAP; apply 2
  ~0329Z (canonical re-home): sha UNCHANGED = same bytes, new home. Both correct; different claims.
  FUTURE re-pins (runtime-pull architecture): sha stops discriminating — env stamp + behavioral
  discriminators are the frame.

## CLOSE
- **Closed: 20260811T034xZ by 2.0.0_SA_COO (window caller).** Close condition satisfied: every leg
  landed (L-A · L-B · L-D two-apply) + the post-window QA read complete (L-C two fenced cycles;
  item-1 read, item-2 PASS full label grain, item-3 PASS both legs). All leg evidence applied-truth
  grounded and cross-verified (DS/AE execution, CTO independent verification, COO validation).
- **What this close ASSERTS:** the RP-W1/W2/W3 window scope is complete — reviewed code @bf74d031c1
  executing from the Andrew-ordered canonical home; ruled cadence live (0-drift); labels correct per
  the 08-10 point-in-time ruling; restatements surfaced in-band. **What it does NOT assert:**
  value-settledness (C-1, open at Andrew via CTO) and the 13:30Z unattended bar — which remains the
  ONLY RP-W3 completion-bar evidence, adjudicated by COO against the Amendment-III table (provenance
  condition pre-satisfied; executing-code precondition satisfiable as written tonight) and recorded
  as an ADDENDUM to this ledger after the cycle.
- **Residuals carried out of the window (owners named):** 13:30Z bar adjudication (COO, addendum
  here) · C-2/C-3 producer-fix routing to DS/AE (COO, banked 032240Z) · C-1 conversion policy
  (CTO→Andrew, live) · two-live-code-channels + 17b grammar observation (CTO, DS-flagged 033615Z) ·
  comp-pipescript lambda-channel blindness instrument gap (CTO, COO-flagged 031216Z) · cottonwood
  deep rekey adjudication (CTO causation thread, deliberately not parallel-read) · tags + integrator
  push (executing at close, recorded below when done).
- **POST-CLOSE CONFIRMATIONS LANDED IN THE CROSSING (034100Z/034112Z), each strengthening a close
  premise, none reopening a leg:** (1) **CTO: branch (a) RATIFIED, Rule-22 cited** — @e82326bdb2
  (this seat's own deliverable ANDREW_DIRECT_20260810_AUA_HISTORY_IS_POINT_IN_TIME.md, Andrew
  VERBATIM *"Point-in-time, history does not restate"*; its ruled table = tonight's exact collision:
  133,914,199.99 RULED / 139,213,957.62 REJECTED) — **13:30Z publishes at face 12/12 on a RATIFIED
  basis, no loud-flag on the assignment plane**; CTO self-corrected the 030244Z "open call" as
  overstated (open residuals = estate-wide extension census, diagnostic; C-1 revaluation asymmetry,
  distinct) and is retracting the over-escalation to Andrew. (2) **CTO: L-D discriminators
  independently confirmed** (canonical key re-listed; s3_object_version ppmmOYbpFISWVrjCICpIajP2VXFbiqb8
  NEW; GetObject proven by apply success; env+sha re-read; 0-diff re-plan). (3) **DS: the rekey deep
  read had ALREADY RUN in the crossing — source+report grain, ZERO discrepancies** (earliest-wins
  provably correct at build_cottonwood_mdpf_slice.py:257-318 pin==HEAD; every collision reaches the
  report by construction; census complete 13 partitions/2 collided dates both reported; 08-07
  collision benign equal-dollar; 08-06 differing-dollar cause grounded = vendor re-labelling at
  Black Diamond, ten accounts renamed — not same-snapshot drift). Supersedes-upward the glance-grain
  discharge; evidence with CTO's causation thread.
- **TAGS CUT (AE 034031Z, Rule-6 annotated, bumps sort-V-verified off v2.0.1/v0.39.0/v1.8.0):**
  mdpf-pipeline-v2.1.0 @759ef40a12 · opal-assets-v0.40.0 @9eff54d274 · smartx-pipeline-v1.9.0
  @9eff54d274. **Integrator push: ROUTED TO 0.0.0_AB_MSTR (LD-0367 r2 / LD-0368 integrator-only
  gate — the COO push attempt 034xZ was correctly BLOCKED; the gate exercising live is itself a
  correct-control record). MSTR runs the integration pull+push (--follow-tags for the 3 annotated
  tags) in the integration window; the window chain + tags sit committed locally until then. The
  earlier "COO fires the push" language in this ledger and the close messages was WRONG IN
  ATTRIBUTION — the COO coordinates the close; MSTR publishes the shared branch.**

---

## 13:30Z BAR — PRE-REGISTRATION ADDENDUM (2.0.0_SA_COO, written 0608Z, ~7h BEFORE the cycle)

**THIS IS NOT THE VERDICT. It is the interpretation table, written BEFORE the evidence exists** — the
discipline that earned its keep twice in this window (the 6/12 table @4c10918958, and the
executing-code precondition that correctly made the first L-C cycle un-adjudicable as a pass).
The verdict lands as a separate ADDENDUM after the 13:30Z cycle.

### NEW ROW — ZERO-DOLLAR / `partners=0` STAGING INPUT

**Why this row exists now:** `0.7.0_AE_CloudOps`, discharging the CVO rider on cutover act X-ii
(060529Z), found that **both** floor-written `gold/mdpf_revamp/_aggregate_aua` staging artifacts read
`opal_aggregate_aua=0.00 (model=0.00 sma=0.00 non_model=0.00) partners=0 reconciliation=PASS` on
**08-09 and 08-10**, at object sizes 4.5/4.6KB against ~10.1KB for the 08-06-era chain-written ones.
**These are the NEWEST partitions in the staging tree the 13:30Z floor consumes.**

⚠ **CALENDAR RESOLVED FIRST, per the standing rule — 2026-08-09 IS A SUNDAY**, 08-10 a Monday.
**A zero MARKET-VALUE aggregate on a Sunday partition may be entirely legitimate and is NOT by itself a
finding.** What the calendar does **not** explain, and why this row is written rather than dismissed:
1. **`partners=0` is a ROSTER fact, not a market fact** — a weekend does not zero a partner roster.
2. The **~10.1KB to 4.5KB size drop** suggests absent content rather than a flat market.
3. **`reconciliation=PASS` on `partners=0` is `0==0`** — the checks-that-pass-on-the-confirming-limb
   class. **The instrument passes MOST cleanly exactly when the input is MOST empty, so it cannot
   discriminate this case and its PASS is not evidence.**

### THE PRE-REGISTERED INTERPRETATION (binding on the post-cycle verdict)

| what the 13:30Z cycle produces | verdict |
|---|---|
| Non-zero aggregate with `partners` > 0 matching the partner roster | **PASS** on this row. The 08-09/08-10 zeros were pre-fix artifacts; non-event, recorded and closed |
| **`$0.00` / `partners=0`, `reconciliation=PASS`** | ⛔ **FAIL — LOUD, and the PASS is explicitly NOT a mitigating fact.** A structural 12/12 face over a zero-dollar input is **build+label correctness over empty content**, which is exactly what this window's close asserted 12/12 does NOT cover. It does not become a pass because the face is green |
| Non-zero but `partners` disagrees with the partner roster count | **FAIL** — derive from the roster, never a literal; a mismatch is a real finding regardless of dollar values |
| Cottonwood-only degradation | pre-existing/decoupled per @4c10918958, unchanged |
| **Non-cottonwood degradation** | **FAIL, loud** — unchanged from the original bar terms |

⛔ **THE TRAP THIS ROW CLOSES, STATED SO IT CANNOT BE ARGUED AWAY AT 13:30Z: a green face plus a
passing reconciliation is the EXPECTED READING of a zero-dollar input, not evidence against one.**
Anyone adjudicating this bar must read the aggregate's actual VALUES and the `partners` count — the
verdict may not rest on the 12/12 face or on `reconciliation=PASS`.

### OPEN, NOT ADJUDICATED BY THIS SEAT

- **WHICH RUNTIME IS THE PRODUCER** — AE grounded 2-for-2 on the writer's own CloudWatch lines that
  `mdpf-gold-lambda` writes this key **in-process**, not the EC2 chain. The same module runs in **two
  runtimes against one key** = a **live atom-5 violation**, and it is why staging stayed fresh for five
  days with the chain dark. **At CTO** (spec ruling). Act X-ii is HELD pending it.
- **What the 0318Z L-D-canonical re-fire actually wrote**, and whether the in-process aggregate is
  expected to produce non-zero at 13:30Z. **Routed to CTO to place** (DS or AE). The re-fire read GREEN
  12/12 with cottonwood BUILT, so the fixed code may already produce correct content — that would make
  this row a recorded non-event, which is a fine outcome for a pre-registration.
- CloudTrail is **structurally unavailable** for this key (no data events on `opal-data-assets`; org
  trail covers `opal-data-bd`/`inf` read-only, served-key trail covers `platinum/firm/` on inf/bd/cot).
  **An absence verdict from CloudTrail here would be an instrument limit, not a finding** — AE stated
  this rather than reporting absence.

**NOTHING IS ARMED AGAINST THE 13:30Z CYCLE AND NOTHING WILL BE** (alerts/monitors moratorium). This
pre-registration is the control: it makes the verdict un-negotiable after the fact without requiring any
notification machinery. **Owner: `2.0.0_SA_COO`. If this seat is gone before 13:30Z, a successor
adjudicates from THIS TABLE, not from recollection.**
