# DEPLOY-COMPLETION LEDGER — MDPF ATOMIC WINDOW (RP-W1 + RP-W2 + RP-W3)

**Opened:** 2026-08-11T01:50Z by 2.0.0_SA_COO (window caller/coordinator)
**Status:** **CLOSED 2026-08-11T034xZ** by 2.0.0_SA_COO (window caller) — see `## CLOSE` and the final line, *"THE WINDOW IS CLOSED. This ledger entry is discharged."*
> ⛔ **HEADER CORRECTED 2026-08-25T03:54Z by `2.0.0_SA_COO~Z`. THE WORK WAS NEVER OPEN AFTER 08-11 — ONLY THIS LINE WAS.** The original condition read *"OPEN — closes only when every leg lands + the post-window QA read completes, or on full rollback"*; it was satisfied that night (L-C re-fire GREEN 12/12, L-D CTO-verified 033621Z) and recorded in the body, **but this header was never updated.**
> **THE DEFECT IS TWO STATUS CARRIERS WITH NOTHING SYNCING THEM.** Closure goes in the body; every sweep reads the header — so a discharged ledger reports in-flight forever, and a NEVER#6 census over-reports. Found 2026-08-25 while sweeping for stranded deploys: **3 of 8 header-OPEN ledgers were already closed in-body, one of them 12 minutes after opening.** **This header is PRIMARY; close it when you close the body.**
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

---

## AMENDMENT 1 to the pre-registration (0618Z) — AE's MEASURED EXPECTED SIGNATURE, folded BEFORE the fire

`0.7.0_AE_CloudOps` delivered the discriminating read (061546Z to CTO, CC here) and **offered its
expected signature for pre-registration, timestamped, before the cycle.** Accepted — that is what a
pre-registration is for, and taking it now is the difference between a control and a post-hoc reading.

**WHAT AE MEASURED:**
- **(a) The 0318Z re-fire wrote NOTHING** — the fence held; it computed `partners=1 / $1.47B / ERROR` on
  a mid-landing read 5s after the 49financial feed landed.
- **(b) The `partners=0` MECHANISM is measured, not inferred:** exact-date feed reads + **no 08-09/08-10
  partitions for any firm** (inflection's positions feed is CHAIN-written, newest 08-06; the 03:30Z cron
  covers 49financial only, TUE-SAT) + **the pre-re-pin S2 wholly-empty SKIP carve-out** — a **vacuous
  `0==0` PASS**, now **RETIRED in the deployed re-pin** (RP-W5 item 4).
- **(c) FORWARD CALL FOR TODAY 13:30Z: zeros-with-PASS STRUCTURALLY CANNOT RECUR.** Served spine
  artifacts expected **HEALTHY NON-ZERO** (silver-fed; QA GREEN 12/12 this morning). The **A7
  dated-contract leg is expected to S2 ERROR and REFUSE THE WRITE** (deployed `main():1456`) because
  inflection's feed cannot exist chain-dark and the roll-forward source is poisoned by the zero priors.
  **Loud, no write; staging stays at the 08-10 zeros.**

### THE EXPECTED-SIGNATURE ROWS (these ADD to the table above; they do not replace it)

| what 13:30Z shows | verdict |
|---|---|
| **ONE loud A7 `ERROR` line in the gold-lambda log, NO 08-11 staging write, served spine HEALTHY NON-ZERO** | ✅ **PASS — and the A7 refusal is CORRECT-BY-DESIGN, recorded as the guard WORKING, not as a failure.** A loud refusal that declines to write poisoned output is the behaviour we want; do not read the ERROR string as the finding |
| The A7 leg **WRITES** instead of refusing | ⛔ **FAIL** — the guard did not hold, and a write here propagates the zero priors forward |
| Served spine artifacts zero or absent | ⛔ **FAIL** — directly contradicts AE's measured forward call; the premise moved and the bar is un-adjudicable until re-grounded |
| ⚠ **NO A7 ERROR line appears at all** | ⛔ **NOT automatically a pass — INVESTIGATE BEFORE VERDICT.** Absence of the expected error means **a premise moved** (inflection's feed exists after all, or the leg did not run, or the guard was bypassed). **The absence of an expected loud failure is not evidence of health** — it is an unexplained state, and it is the one branch where a green-looking read is least trustworthy |

⛔ **NOTE WHAT AE's FINDING (b) ACTUALLY WAS: the old `partners=0 / reconciliation=PASS` was produced by a
"wholly-empty SKIP" carve-out — a VACUOUS `0==0` PASS.** That is the confirming-limb class **named at
source in the code**, and it is **already retired in the deployed re-pin.** So the row I pre-registered
at 0608Z described a real defect that had already been fixed hours earlier — **the pre-registration cost
nothing and the fix is independently confirmed. A control that fires on an already-closed defect is
cheap; the reverse is not.**

**The original five-case table STANDS UNCHANGED** — it governs if AE's forward call turns out wrong.
**These amendment rows govern if it turns out right.** Both are written before the evidence.
**Owner unchanged: `2.0.0_SA_COO`; a successor adjudicates from this file.**

---

## AMENDMENT 2 (0640Z) — A **SECOND HEALTHY BRANCH**, and AE's correction of their own mechanism claim

**This amendment exists because Amendment 1's row 4 did its job.** That row said *"no A7 ERROR line at
all → NOT automatically a pass, INVESTIGATE."* AE then read the deployed selection function and **named
what that investigation should find, before the fire.** *A row that forced a second healthy branch to be
written in advance is worth more than the row's own verdict.*

### ⛔ AE'S CORRECTION OF THEIR OWN 061546Z CLAIM (Rule 22 hygiene, unprompted)

Their earlier read said the A7 leg's roll-forward source was **"POISONED by the zero priors."**
**OVERSTATED, and they retracted it.** What was actually measured was the **03:31Z outcome**
(`partners=1`, ERROR, nothing rolled); **WHY the roll did not fire in that mid-landing run is
UNMEASURED** — the roll-forward log lines were never pulled.

### THE MECHANISM, READ AT SOURCE — THE SELECTION IS ALREADY VINTAGE-KEYED BY RULED DESIGN

`load_prior_partner_block` (deployed package `:549-583`; executor `:1072-1135`) reads each firm's block
from the partition at **that partner's own STAMPED last-good CONTENT vintage** (`detect_stale_partners`
resolves it over `VINTAGE_BEARING_FEEDERS`). **Its docstring carries the law verbatim: "KEYED ON THE
STAMPED DATE, *NEVER* `max(prior_dates)`"** — the 07-09 fabricated-residual incident is why.
**It does NOT read "the newest prior partition."**

> ✅ **THEREFORE THE ZERO ARTIFACTS CANNOT BE SILENTLY ROLLED, BY CONSTRUCTION.** A zero partition is
> touched only if a partner's stamp *points at* 08-09/08-10 — and a zero partition **carries no partner
> blocks**, so `load` returns `None` → the fail-safe leaves the partner absent → **Sentinel 2 ERRORS LOUD
> and the write is REFUSED. The worst these artifacts can cause is a loud refusal, never a wrong number.**
> **And `(c)` turns out to need ZERO CODE CHANGE** — there was no producer defect to fix and no archive
> edit to make. *The layer argument that killed option (b) was right, and it was also moot: I reasoned to
> the correct answer from a mechanism that did not exist. AE going to source is what established that.*

### THE 13:30Z A7 LEG NOW HAS **TWO** HEALTHY BRANCHES (both pre-registered, before the fire)

| branch | signature | verdict |
|---|---|---|
| **(i)** *(unchanged from Amendment 1)* | **S2 ERROR + WRITE REFUSED**, no 08-11 staging write, served spine healthy non-zero | ✅ **PASS** — the guard refusing to write poisoned output |
| **(ii) NEW — a FIRST-CLASS healthy branch** | **PASS with inflection ROLLED-WHOLE from published 2026-08-06** — log line `OK roll-forward: inflection block copied WHOLE from published 2026-08-06`, **a REAL NON-ZERO 08-11 staging write**, `as_of_by_partner` stamped | ✅ **PASS** — the guard **HEALING** exactly as the 07-09 CTO ruling designed |
| **DISCRIMINATOR for (ii)** | the **roll-forward log line** + `partners=2` **with one rolled** + honest vintage stamps | this is what row 4's "investigate" should FIND |
| **FAIL branches — unchanged** | a zero-write · a serve-zero · **or a write with `partners=1` and NO roll line** | ⛔ **FAIL** |

⛔ **ROW 4 OF AMENDMENT 1 IS NOT RETIRED — IT IS SHARPENED.** "No A7 error" is no longer an unexplained
state to investigate from scratch; **it is branch (ii) with a named discriminator.** But the discriminator
is load-bearing: **a quiet run that shows NEITHER the ERROR nor the roll-forward log line is still
un-adjudicable and still investigates.** *Silence with an explanation is a pass; silence without one is not.*

**TODAY'S 13:30Z RUN IS THE MEASUREMENT THAT CLOSES THE OPEN CELL** — AE reads its log lines against
exactly these branches at their 13:28Z wake. **X-ii-a's history leg is now COPY EVERYTHING VERBATIM, no
exclusions, and NO selection change rides the act** — any walk-back "improvement" would amend the ruled
never-`max` law and is deliberately not proposed.
**Owner unchanged: `2.0.0_SA_COO`. A successor adjudicates from this file, branches (i) and (ii) included.**

---

## AMENDMENT 3 (0845Z) — ⛔ **WHICH TABLE GOVERNS IS NOW CONDITIONAL, AND THE OBSERVATION ORDER DECIDES IT**

**AE landed the WS-A calendar fix** (@0e2dc070d3, ledger `20260811T0845Z_mdpf-chain-calendar-distribution.md`
opened+closed) after CRO~A surfaced that chain run `20260811_073903` **died 07:40:59Z in WS-A** —
`mdpf_calendar_binding` **fail-closed: CANONICAL CALENDAR ABSENT.**

### ✅ FIRST, A SCOPE CORRECTION THAT PROTECTS TODAY'S BAR

**P1-2 is NOT unlanded.** Its ruled scope was the **mdpf-gold-lambda PACKAGE**, and that **LANDED**
(@a4d71e954 v2.2.0) — AE verified the deployed lambda zip carries `trading_calendar.py` + the binding at
root. ⚡ **TODAY'S 13:30Z BAR FIRE IS NOT EXPOSED TO THIS DEFECT.**
**The real gap was a SECOND DEPLOY TARGET:** the EC2 chain code store needs the same calendar and **no leg
carried `lib/trading_calendar.py` there** (`lib/` sits outside `safe_deploy_core` homes). ** Atomic-commit-is-
not-atomic-deploy — the CPR-5 class, and single-homing instance EIGHT: one authority, two deploy targets,
one served. ** Fixed hash-tied to the ONE authority (sha256 `41b1c0c1…` @0cbb0ad174, byte-identical to the
lambda copy), download-back verified, coverage proven at three call sites.

### ⛔ BRANCH (iii) — FRESH-COMPUTED, and it INVERTS what counts as healthy

**The store fix makes a GREEN pre-bar chain run possible if INF's normal cycle completes again today**
(~13:01Z historically; **whether its 07:38Z completion was the recovery run is UNKNOWN**).

| condition | governing table | healthy signature |
|---|---|---|
| **NO new green chain run before 13:30Z** (no `run_id` later than `073903` completed GREEN) | **Amendments 1 + 2 EXACTLY as registered** — branches (i) and (ii) | loud A7 refusal **OR** roll-whole from published 08-06 |
| ⚡ **A NEW GREEN CHAIN RUN completed before 13:30Z** | **BRANCH (iii)** | **PASS with inflection computed FRESH from 08-11 feeds — NO roll line, real non-zero write, CURRENT vintage stamps** |

> ⛔ **UNDER BRANCH (iii), BRANCH (ii) BECOMES A DEFECT.** A roll-from-08-06 line, when fresh 08-11 feeds
> exist, is **surprising and wrong** — and branch (i)'s S2 ERROR likewise. ** So the same observation is
> HEALTHY under one table and a FINDING under the other. **

### ⚡ THEREFORE THE OBSERVATION ORDER IS ITSELF A CONTROL — read in THIS sequence

1. ** READ CHAIN `status.json` `run_id` + `status` FIRST. **
2. ** SELECT the governing table from that read ** (no new green run → (i)/(ii); new green run → (iii)).
3. ** THEN read the lambda leg. **

> **Reading the lambda leg first risks adjudicating a true observation against the wrong table** — and it
> would look like a clean verdict. *This is the first pre-registration in this window whose ORDER OF READS is
> load-bearing rather than just its criteria: the terrain can change under the bar, so the first act must be
> to establish which terrain you are on.* **Surprise-channel rule unchanged: anything outside the governing
> table is a same-turn line to COO + CTO. The serve-green 12/12 limb is unchanged.**

### RE-DISPATCH POSTURE — COO ruling

**AE correctly refused to fire an ad-hoc pre-bar chain re-dispatch** (a pre-bar induced run is a terrain
change the bar owner owns). ✅ **MY RULING: NATURAL FIRE IS THE DEFAULT AND STANDS.** ** IF no natural INF
completion has occurred by the 14:10Z X-iii closer, a QA re-dispatch is AUTHORIZED AFTER that closer ** —
labelled QA, **its artifacts are NEVER production evidence** (ad-hoc runs are a QA instrument; the scheduled
run is the production path), and post-closer placement avoids bar contamination *and* exercises the
post-X-iii state. ⛔ **Nothing induced before 13:30Z.**

### ⚠ OPEN — AN UNIDENTIFIED WRITER TO A CODE STORE

**AE's own incident, self-reported: their pre-land `head-object` was CHAINED with the `cp`, so a 200 return
(the key ALREADY EXISTED — landed 08:33:17Z, ~3.5 min earlier, EMPTY metadata) did not stop the `cp`, which
overwrote.** ** The gate did not gate — the verify-live-state-before-mutation class, cited by the seat that
committed it. ** **BLAST ZERO:** versioning Enabled, both versions **ETag-identical** (the prior actor
uploaded the same authority bytes), prior version preserved. **AE's self-assigned rule, in their ledger:
state-gated mutations run as TWO tool calls — read, STOP, act.**
⚠ ** WHO UPLOADED AT 08:33:17Z IS UNKNOWN and not identifiable from S3 (bare `cp`, no metadata). ** Timing
fits a seat acting on CRO~A's 082623Z broadcast, or Andrew at the assessment terminal. **Asking the fabric to
claim it — not to assign blame (the bytes were correct and the blast was zero) but because an unattributed
write to a code store means we cannot tell a coordinated fix from a coincidence, and the dedupe of follow-ups
depends on knowing.**

---

## AMENDMENT 4 (0847Z) — ⚡ **BRANCH (iii)'s CONDITION IS MET AND EXCEEDED. (iii) GOVERNS; (i)/(ii) ARE NOW COUNTERFACTUAL**

*Landed minutes after Amendment 3 was committed. **The pre-registration's STRUCTURE held; only the selected
branch changed** — which is exactly what a conditional table is for.*

**CRO~A, on Andrew's live word at their terminal, drove the FULL RECOVERY PRE-BAR:**

| act | evidence |
|---|---|
| the 08:33:17Z upload | **CLAIMED by CRO~A** — ⚠ **the unattributed-writer question in Amendment 3 is CLOSED** |
| `mdpf-daily-trigger` re-invoked 08:34Z with the morning's recorded S3 event | run **`mdpf_daily_20260811_083449` COMPLETE** — **WS-A ok in 2s at the exact morning failure point**, STAGE6-REVAMP ok 72s |
| `mdpf-gold-lambda` manually invoked | **GREEN, 12/12 `a4_objects`** — against **3/12** on the 08-10 scheduled run |
| portal publisher invoked | **14/14 published**, manifest `20260811T084216Z-2be8c1a9` |
| platinum | serves **`as_of 2026-08-07`, all four scopes** |

### ⛔ THE GOVERNING TABLE FOR 13:30Z IS NOW (iii), AND IT INVERTS (i) AND (ii)

**HEALTHY = REPRODUCING THE RECOVERED-MORNING SHAPE:** green · **12/12-class objects** · real non-zero write ·
**inflection computed FRESH** · **NO roll line** · current vintage stamps.

> ⛔ **AN S2 ERROR, OR A ROLL-FROM-08-06 LINE, AT 13:30Z IS NOW A GENUINE DIVERGENCE — STRAIGHT TO THE
> SURPRISE CHANNEL.** Both were the *healthy* signatures under the pre-recovery terrain. **Branches (i) and
> (ii) govern only in the now-counterfactual no-recovery world.** *The same observation flipped from
> healthy to defect in under an hour, without the criteria changing — because the terrain moved and the
> table said which terrain it applied to. A single-branch pre-registration would now be actively
> misleading.*

### ✅ THE AD-HOC / SCHEDULED SPLIT HOLDS, AND IT IS THE POINT

**The manual invokes are RECOVERY INSTRUMENTS. They are NOT the bar and NOT the production evidence.**
** THE 13:30Z SCHEDULED LEG REMAINS BOTH. ** *A green manual run proves the fix works; only the scheduled
fire proves the pipeline works. Those are different claims and tonight's whole discipline rests on not
conflating them.*
✅ **The QA re-dispatch question in Amendment 3 is MOOT** — the run happened, Andrew-directed.

### ⚠ PRE-REGISTERED SO NOBODY CALLS A FALSE OUTAGE AT 13:30Z: `as_of 2026-08-07` IS **VENDOR CADENCE, NOT STALENESS**

On an 08-11 read, a **4-day-old `as_of`** will look like a stale pipeline. **It is not.** The ceiling is
**vendor delivery cadence** — cottonwood's Monday file lands ~03:30Z tomorrow, schwab's ~10:16Z today.
> **This is the trading-calendar rule's cousin and it earns a row for the same reason: an old timestamp is
> not a finding, and the instrument that reports it cannot tell cadence from breakage.** ⛔ **Do not raise a
> staleness finding on the `as_of` without first resolving vendor cadence.**

### HOUSEKEEPING — closures folded

- **Who uploaded at 08:33:17Z: CLOSED** (CRO~A, on Andrew's live word).
- **QA re-dispatch: MOOT.**
- **CTO ruled both AE roster candidates (084332Z):** the **calendar second-target BATCHES with the CPR-5
  `safe_deploy_core` row** (DS map change + AE verify — **sequences with me in P3**) · the **`comp-freshness`
  canonical ADD** is worded to AE for **post-window** execution (**trading-day-frontier basis MANDATORY**;
  legacy entries stay until P5).
- **AE's observation order stands unchanged** and is now more important, not less: **chain telemetry FIRST →
  select the governing table → then the lambda leg.**

---

## AMENDMENT 5 (092730Z) — ⚠ THE `ending_mv` ABSENCE MECHANISM IS SOURCE-CONFIRMED, AND IT **SELF-HEALS UPWARD ON ITS OWN**. PRE-REGISTERED SO NOBODY READS BENIGN DRIFT AS EITHER A DEFECT *OR* A FIX

**Grounding (MSTR, Andrew-granted Orion egress, record `@dbddd3fe52` / `ENDING_MV_ORION_WHY_20260811.md`):**
the billing extract's `Activity: Ending Market Value` is Orion `Activity.Value` over the pull's
**ROLLING-3-YEAR window** — `orion_billing_dim.py:62 DEFAULT_WINDOW='3y'` @dbddd3fe52 — and Orion's
Activity engine returns **EMPTY** for any account whose `accountStartDate` **postdates the window start**.
**PERFECT SEPARATION, ZERO EXCEPTIONS:** all **312** absent-with-assets started **after 2023-08-11**; all
**485** populated started **on/before 2023-08-04**. **PREDICTIVE CONTROL:** 22/27 in-window anniversary
accounts flipped absent→populated within ±3d of exactly `start + 3y`. Nothing is wrong at Orion or at the
accounts (probed: reconciled, in-balance, `currentValue` correct). This is a **mechanism**, source-confirmed
with a vintage — the reserved word is earned here.

### ⛔ THE ROW THAT MATTERS AT THE BAR: **FEE-EARNING AUA DRIFTS *UPWARD* WITH NO CODE CHANGE, NO DEPLOY, AND NO FIX**

~27 accounts crossed their 3-year anniversary Apr–Aug. Each crossing moves an account from
absent-coerced-to-`$0.00` into populated **by itself**.

| Observation at 13:30Z | ⛔ WHAT IT IS **NOT** | ✅ THE CORRECT READ |
|---|---|---|
| fee-earning AUA **higher** than a prior read | **NOT evidence a fix landed.** Nothing has been fixed — both builder defects are still queued. | Anniversary self-heal. Expected, benign. |
| fee-earning AUA **higher** | **NOT a defect or a jump to investigate.** | Expected, benign. |
| accounts moving `$0.00` → populated | **NOT evidence the absence class is closing.** The class is **fully live**; individual accounts age *out* of it one at a time. | Per-account aging, not remediation. |
| an account still at `$0.00` | **NOT a new failure.** | Its `accountStartDate` is simply < 3y old. |

**THE DISCRIMINATOR, pre-registered:** an **anniversary flip is per-account and dated at `start + 3y`**. A
**fix** would move accounts whose start dates sit **nowhere near** an anniversary. So before crediting any
change to a remedy: **check the flipped accounts' start dates against `today − 3y`.** If they cluster there,
nothing was fixed.

> **WHY THIS EARNS A PRE-REGISTRATION ROW RATHER THAN A FOOTNOTE: a metric that improves on its own is the
> single most seductive false confirmation available tonight** — it will move in the *same direction* a real
> remedy would move it, on a bar day, while a remedy for that exact class sits queued. **A self-healing
> defect manufactures evidence for whatever anyone happens to have just done.** This is Amendment 4's lesson
> generalised: the observation does not carry its own frame, so the frame is written down *first*.

### P1 DESIGN CONSEQUENCE — a NAMED DECISION, owner CTO + Andrew, **NOT** a builder's call
The window choice is now an explicit design fork: **(a)** an **inception-anchored** window, or **(b)** read
**Portfolio-domain `currentValue`** raw — the raw-from-endpoint (atom 8) answer, and the roster endpoint
returns it for **all 3,169 accounts in one call**. **Plus** the already-routed absent-vs-zero nullable fix
(Rule 17: coercing absence to `0.00` in *silver* is a `fillna`, so preserving absence is law, not preference).
⛔ **A lane does not pick (a) or (b) mid-build.**

### INSTRUMENT NOTE — **FOURTH capped-stream sighting today**
`orion_endpoint_probe.py get` caps output at `:3000` (DS-lane fix). Same class as my own `| head -12`
ABSENT read this session. **Four in one day is not four mistakes — it is a tooling default.** ⛔ **Never
conclude ABSENT from a capped stream**, and print the cap beside any absence verdict.

---

## ✅ ADJUDICATION (2026-08-11T14:25Z) — THE BAR FIRED. VERDICT: **GUARDS WORKING.** And the two named gaps are **TWO CLASSES**, only one of which is cadence

**The pre-registration did its job in the way that matters: the structure held while the observation moved.**
AE brought the result **un-adjudicated on the SURPRISE CHANNEL** rather than forcing it into a branch — which
is the table's own rule, exercised. The folded observation order (chain telemetry FIRST → select the table →
then the lambda leg) is what made the divergence *legible* instead of confusing.

### OBSERVED vs TABLE (iii)

| limb | observation | verdict |
|---|---|---|
| **A7 leg** (what (iii) was written for) | `partners=2` · `reconciliation=PASS` on a **real non-zero write $1,786,341,788.10** · **NO roll line** · fresh computation | ✅ **(iii)-HEALTHY, exactly as pre-registered** |
| **cycle shape** | `6/12 A4 objects built; errors=['inflection','global']` | ⚠ **DIVERGENCE** from (iii)'s 12/12-class signature |
| inflection | `CROSS-AXIS COHERENCE GATE FAILED — REFUSING TO EMIT`; custody 440/442 axis dates, 2 NAMED gaps | ✅ correct refusal |
| global fold | `SKIPPED: contributing leg(s) ['inflection'] failed` — *"an ineligible fold is recorded, never fabricated"* | ✅ correct |
| serve | 08:42Z publish (14/14, manifest `20260811T084216Z-2be8c1a9`) stands | ✅ intact **BY CONSTRUCTION** |

**So the divergence is at the CYCLE level, not the LEG level.** Branch (iii) held where it applied.

**⚠ THE SERVE CLAIM'S CONFIDENCE LEVEL, recorded as AE stated it:** platinum was **NOT re-listed**, so
"serve intact" rides the publisher's **refusal-emits-nothing MODEL**, not a read of the served plane. That is
a model-grounded claim, not an observed one. **Do not upgrade it without the listing.**

### ⛔ THE LOAD-BEARING CORRECTION — TWO GAPS, TWO CLASSES, ONE ERROR MESSAGE

AE read both gaps as possible vendor cadence (*"the as_of row's cousin"*). **Resolved against the calendar
rather than eyeballed:**

| gap | day | elapsed | class |
|---|---|---|---|
| `2026-08-10` | **Monday** | 1 trading day | ✅ **plausibly VENDOR CADENCE** — may self-heal tomorrow, no action |
| `2026-08-05` | **WEDNESDAY** | **4 TRADING DAYS** | ⛔ **NOT cadence. A REAL absent partition. Will NOT self-heal.** |

> **WHY THIS IS THE WHOLE POINT OF THE ADJUDICATION: if both gaps are filed as cadence, tomorrow's cycle
> refuses again with 08-05 still missing — then a third refusal, then a fourth. At that point the pressure
> is not to fix Orion's 08-05 partition, it is to WIDEN THE COHERENCE GATE so the cycle goes green. THAT IS
> GUARD REMOVAL**, and it is precisely the harm CLAUDE.md's first NEVER rule names: *a misread cadence
> signal manufactures pressure to "fix" a pipeline that is working.*
> **THE GATE IS CORRECT. THE DATA IS MISSING. Conflate those two facts and the gate gets edited.**

**Disposition:** `08-10` → watch tomorrow, no action. **`08-05` → A FINDING, needs an owner today, does not
self-heal.** Not chased pre-window (AE's call, correct).

### THE THIRD CHAIN RUN — an unexplained extra run SURFACED a real defect

`mdpf_daily_20260811_102045` (COMPLETE 10:23Z) processed the **SAME** 07:38:42Z sentinel event — same ETag
`70060df4`, same sequencer. At-least-once redelivery or another manual replay; **the invoker is NOT
distinguishable from the trigger log and is not treated as identified.** Its gate passed honestly
(`49financial fact_rps` latest 2026-08-10, `trading_days_behind 1` = **healthy T-1**, the calendar law
working). **What it DID: advanced the axis frontier to 442 dates — which is what exposed gaps the narrower
08:42Z axis never required.** Mechanism INFERRED (log-grounded, not source-confirmed) and stays labelled;
the finding it produced is real regardless of who fired the run.

### AMENDMENT 5 STATUS
The anniversary self-heal drift band did **not** fire this cycle (no `total.aua` movement attributable to it
in the A7 leg — the write was a fresh computation, not a roll). **The band stays armed** and retires only
when the raw-`currentValue` fix lands, per its own expiry clause.

### ⛔ X-iii — PROCEEDING WAS CORRECT, AND FOR THE RIGHT REASON
AE stated rather than asked: *"holding it on an unrelated scope's refusal would be a self-manufactured
gate."* **That is the rule, not an exception.** Closed @a3e85d472b, 5 legs proven, `CodeSha256` **computed
not eyeballed**, DryRun 204.
⚠ **Process residue, AE self-surfaced:** their directory pathspec swept **~36 pre-existing uncommitted
completion records** into the close commit — `safe-commit` commits the files you NAME, not the files you
CHANGED, rc=0 either way. Those are likely the same records the ledger reports as **UNINDEXED**, so the
sweep may have landed them in git — but **COMMITTING IS NOT INDEXING**, and the 21 RED alerts will keep
firing every cycle until the index sees them.

**THE WINDOW IS CLOSED. This ledger entry is discharged.**
