# MDPF — CONSOLIDATED STOCK-TAKE + DIRECTED PLAN

**Andrew-direct 2026-07-22 ~1505Z:** *"we need to take stock of what is where in our MDPF work and create a
comprehensive, directed plan to efficiently address it."*
**Author:** `1.0.0_SA_CTO` | **State verified live at 1505Z, not recalled.**

---

## ⚠ PART 0 — THE ARMED HAZARD. READ THIS BEFORE ANY TERRAFORM WORK.

> ### **`infra/aws/terraform/portal-auth/` IS 9 BEHAVIORS AHEAD OF LIVE. AN UNTARGETED `terraform apply` IN THAT ROOT FIRES THE MDPF FLIP — THE ONE ROLLED BACK ON A P0 THIS MORNING — WITH THE CO-SIGN AT 0 OF 3.**

**Surfaced by `0.7.0_AE_CloudOps`; CTO re-verified both sides live at 1525Z rather than trusting the report:**

| | repo (`cloudfront-distribution.tf` @`328248c13`) | live (`EVTSA9VEHNZVH`) |
|---|---|---|
| `/api/general/{mdpf,portfolios}` behaviors | **9 declared** | **0** |
| `S3-opal-data-assets` origin | **declared** | **absent** |
| origin access control | **declared** | **absent** |
| total cache behaviors | 33 | **24** |

**WHY IT IS INVISIBLE AS A DEFECT — and this is the whole point:** *the divergence is INTENTIONAL.* The flip
was deliberately committed and deliberately not applied, pending a co-sign that then went to 0 of 3. **So every
routine instrument reads it as "repo ahead of live, apply to reconcile" — which is normally the correct
action, and here it is an unco-signed serve-widen of data we spent today finding a defect in.**

**RULES, binding until the co-sign is 3 of 3:**
1. **NO untargeted apply in `portal-auth`. Ever, by anyone, for any reason.** Any apply in that root is
   `-target`ed and named.
2. **A drift/reconcile report on this root is NOT an action item.** It is expected. Do not "fix" it.
3. **The only thing that fires this flip is the Phase-4 co-sign** — CTO + COO + Andrew, on the pinned
   Cottonwood-inclusive set, FE-first, rollback armed.
4. **Guard is a Phase-1 item** (a repo-level marker / apply-time refusal on this root). **Not built under the
   hold** — named here so it is not tribal knowledge, which is exactly how AE framed it and exactly right.

---

## PART 1 — WHERE WE ACTUALLY ARE

### 1.1 Served surface — UNCHANGED, KNOWN-GOOD
CloudFront `EVTSA9VEHNZVH` = **24 behaviors / 7 origins**, no assets origin, catch-all → `portal-v2`.
**Nothing has been served from the revamp. Nothing is stranded.** Both deploy ledgers closed.

### 1.2 Data — FIXED, STAGED, NOT PINNED
10 objects under `gold/mdpf_revamp/`. **3 moved today** (the count-axis fix):

| object | ETag | state |
|---|---|---|
| `inflection/aggregate_aua_timeseries` | `5e7b684d` | **REBUILT** |
| `global/aggregate_aua_timeseries` | `08f9720e` | **REBUILT** |
| `portfolios/aum-timeseries` (A2) | `ca0c6d1c` | **REBUILT** |
| `49financial/aggregate_aua_timeseries` | `aa5c5b85` | unchanged |
| `portfolios/aum-metrics` (A1) | `529b7c21` | unchanged |
| `global/non_model_assets` (A4) | `8a195549` | unchanged |
| `account_distribution` ×3 | `865919f2` / `afb964c4` / `b946d836` | unchanged |
| `non_model_assets_precutover_frozen` | `da2260f6` | reference, not published |

**This is a CHECKPOINT, not a pin — Cottonwood rewrites `global` again.** Co-sign is **0 of 3**.

### 1.3 What is genuinely FINISHED
- **Count-axis defect CURED AT SOURCE** — count and value now derive from the same eclipse snapshot for
  **all** dates, not date-scoped (CVO source-verified).
- **Enumerated 20-date exemption** landed + independently exercised (4 controls incl. remove-a-listed-date).
- **Cottonwood WS-1 bronze** live, **unattended fire proven** 07-22 06:00Z (31 objects, both gates, 296 reconciled).
- **WS-2 silver + WS-3 gold** complete. Conservation proven: 296 accounts' holdings vs dim sum differ by **$0.02**, pure rounding.
- **WS-5 converter half** landed; **event path + sweep backstop land together.**
- **Import-closure gate** live; **eclipse landmine disarmed** (inert — module vendored, converter NOT upgraded, STALE signal deliberately preserved).
- **FE `$0` defect fixed** (portal DEV `08c6d8b2`) — including the false *"rolled forward from last known data"* claim.
- **Andrew's 6 rulings applied:** one-flip · merge CG→LTC · satellites unlabelled / primary keys only · Income = non-model · gate-not-alert · "Not yet tracked".

### 1.4 The REAL blockers — all of one family
> **Everything built works. Almost nothing is WIRED. The estate encodes "there are exactly two partner firms"
> in several independent places, and each must be opened for a third.**

| # | Blocker | Owner | Status |
|---|---|---|---|
| B1 | `revamp_stage()` has **no Cottonwood leg** — DE's producer is a standalone script nothing calls | DE + AE | open |
| B2 | The per-cycle **source audit is not invoked** by the nightly | DS → AE (diff ready) | open |
| B3 | ~~`lambda_entry` has no destination-envelope branch~~ — **CLOSED `@6d1a15ef2`.** CTO verified: the branch exists **and honours R4** — a POSITIVE match (`isinstance(event.get("requestContext"), dict) and "responsePayload" in event`, `:1033-34`), **not** a catch-all `else`, and it **raises** on a missing `as_of` rather than silently no-op'ing. 0.6.2 built it to the ruling before resetting. | 0.6.2 | **CLOSED** |
| B4 | `build_global_artifact(49f, inflection)` is a **hardcoded 2-arg call** | DE | open |
| B5 | **Enumeration** of two-firm assumptions incomplete — **4 confirmed, 1 checked-clean, infra/publisher/remaining producers NOT covered** | DE | **precondition** |

### 1.5 Known and ACCEPTED, not open
- **49F count axis:** measured defect (07-17, −10 accounts), mechanism **UNDETERMINED**, **no assurance
  instrument exists** — no historical source, artifact-internal checks structurally blind. **Monitored
  prospectively; declared, not cleared.** Decouple is a prerequisite for Global count completeness.
- **Global count axis** will ship with **20 enumerated gaps** — the trading days legacy omits. Honest absences.
- **Day-one Cottonwood** = 1–2 points at the right edge, **zero overlap** with the existing 427-date series →
  **every pre-07-21 Global value is byte-identical with Cottonwood absent, BY CONSTRUCTION.**
- **~$126.4M step** enters Global on 07-21. Real, labelled, not smoothed.

---

## PART 2 — THE DIRECTED PLAN

**Ordering principle: the enumeration gates the build; the wiring gates the emit; the emit gates the pin;
the pin gates the co-sign. Do not invert these — every inversion today cost a re-do.**

### ⛔ STATUS: HELD PENDING ANDREW'S ADVISORY (his ~1408Z directive, CTO scope ruling 1516Z)

**Andrew-direct ~1408Z, VERBATIM:** *"We are going to create a plan on how to efficiently guide the whole
fabric on the remaining open MDPF items rather than keep firing from the hip... hold for further advisory."*

**CTO RULING — the hold binds FABRIC-WIDE on MDPF-scoped work** (the planning clause names *"the whole
fabric"*; latest + most-restrictive binds). **HELD:** initiating new MDPF work · taking a pin · publishing ·
moving any `gold/mdpf_revamp/*` ETag · firing a co-sign limb · the Cottonwood fold · any apply on the MDPF
serve path. **Finish nothing that would create a half-landed step — there is currently NONE and NEVER#5 is
NOT engaged.**
**CARVE-OUT 1 — REVISED 1525Z, NARROWED. CTO CORRECTING HIS OWN RULING.** I originally carved out the
`portal-v2 json/mdpf/**` **deny** as PROCEEDS, on the ground that Andrew ordered it built at ~1425Z, **17
minutes after** the planning directive. **`0.7.0_AE_CloudOps` parked it anyway and flagged the judgement
rather than deciding quietly, and his reasoning is better than mine:**
> *"A GO issued before the hold does not authorize firing now — the sequencing is being re-planned above the
> lane that issued the GO, so executing a pre-hold GO is precisely the firing-from-the-hip you're stopping."*
**ADOPTED. The deny's APPLY is HELD.** Andrew's 1425Z answer settled *whether it should exist* (a design
question I had put to him); **it did not authorize firing an apply under a planning hold** (a sequencing
question, which is exactly what the hold governs). **Drafting, exercise-design and grounding continue; the
apply waits for the advisory.** Nothing is lost — the deny protects against a decommission that is not
happening today. **Also parked on the same reasoning: the silver-family catch-up and DS's mutants.**
**(2)** off-path
**reversible** work continues (comp-constants, collection repair, sovereign-predicate sweep, import-closure
census) — none touches MDPF data or the serve path; (3) **read-only MDPF ANALYSIS continues, especially
Phase 0 below — enumerating is not initiating**, and it is the input the advisory needs.

**This plan is the INPUT to that advisory, not a substitute for it.**

### PHASE 0 — CLOSE THE ENUMERATION *(gates everything; the only real unknown)*
**Owner DE.** Finish the census of every place "exactly two firms" is encoded — **with a stated denominator
and an explicit not-covered list.** Must reach: `infra/` dispatch + IAM, the publisher/promote path,
`dim_mdpf_account_distribution.py`, `dim_mdpf_aum_{metrics,timeseries}.py`, the FE per-firm distribution path.
**Exit: the list is closed and priced. This is what sets the date — nothing else is unbounded.**

### PHASE 1 — BUILD *(parallel, all unblocked)*
- **1a · DE** — re-home Cottonwood as `build_cottonwood_artifact()` **inside the shared producer** (the
  standalone script structurally cannot feed an in-memory composition); change the `build_global_artifact`
  signature; extend `--firm` + `want` sets. **Cottonwood JOINS the existing trading-day axis — global does
  not become a multi-axis join.**
- **1b · 0.6.2** — `lambda_entry` destination branch, **POSITIVE envelope match** (`version` +
  `requestContext` + `responsePayload`), never a catch-all `else`. → unblocks **1c**.
- **1c · 0.7.0** — WS-5 apply (`-target`, 5 conditions) → deploy blackdiamond-only artifact **past
  `7aa7e645f`** → exercise on the **`mode == "event"`** discriminator.
- **1d · 0.7.0** — Deliverable 2 `portal-v2 json/mdpf/**` deny **+ the lifecycle limb**; exercise = denied
  delete naming the policy + isolated positive control. *(Independent of everything else.)*
- **1e · DS → AE** — wire the audit into `revamp_stage()`: **inflection FAILS the stage, 49F REPORT-ONLY**
  (it has a known defect and would fail every night), placed **before** the completion marker; fold verdict +
  coverage into `cycle_complete` so the running count **accrues**.
- **1f · 0.7.0 — CENSUS DELIVERED (1459Z), and it RE-SCOPED ITSELF.** Coverage stated as required: **9 of 192
  reachable, 183 explicitly NOT clean.** **Finding: vendor staleness is a SILVER-FAMILY problem — 4 of the 9,
  with `silver_registry.py` as the common axis — NOT an eclipse quirk.** So the catch-up is a family-wide
  workstream, not a one-package fix. *(The census did the job it was staffed for: it turned one instance into
  a population with a named axis.)* **The silver-family catch-up is PARKED under the hold.**

### PHASE 2 — WIRE THE NIGHTLY *(the step that makes an emit possible at all)*
Add the **Cottonwood leg** to `revamp_stage()` (B1) alongside 1e's audit wiring. **Until this lands, no
nightly can produce a Cottonwood-inclusive set and there is nothing to pin.** *(This is what killed the
2-day estimate — it was never in anyone's scope.)*

### PHASE 3 — EMIT + VERIFY
**The scheduled nightly emits** the Cottonwood-inclusive set. **No hand-staging** — a hand-staged artifact
proves the code works, not that the production path emits it, and that is the exact masking class we found
in WS-5. → **CTO pins the emitted ETags** → **fresh 3-pass**: DS producer-validate (incl. hand-run audit on
the pinned set), CVO from-scratch re-derive, DT consistency.
**BINDING:** every gate is **re-exercised against the THREE-firm artifact — none of today's proofs transfer**
(all were mutant-proven on a two-firm global). Every limb states its **coverage fraction against the
defect-capable population**, never a percentage. **49F COUNT-mode render cell cannot be waived** — it is the
only non-degenerate instrument left pointed at that firm.

### PHASE 4 — CO-SIGN + FLIP
Fresh **CTO + COO + Andrew** never-widen co-sign on the pinned set, carrying the declared terms (49F
unbounded-by-construction; retained legacy runtime dependency; 20-date Global gap; 1-of-6 historical
coverage). → **FE-first promote** → AE `-target` apply → **immediate revert-plan hard gate** → verify-before-serve
→ rollback armed until explicit disarm.

---

## PART 2b — STANDING CTO RULINGS THAT HAD **NO DURABLE CARRIER** *(landed here 1520Z)*

**Andrew is resetting context on every fabric worker with clean handoffs and pause orders.** A reset agent
inherits **only what is on disk**. **Every ruling below was issued today and existed ONLY in an MCP thread —
they would have died at the reset, silently, and the work would have been rebuilt against a different
decision.** MSTR caught the first one; this is the sweep it implied. **These BIND the resumed work.**

| # | Ruling | Binds | Owner |
|---|---|---|---|
| R1 | **The count-axis audit wiring lands before the SECOND post-flip cycle**, preempting WS-5 if needed. The first cycle may be covered by a hand-run; the second may not. | any flip re-sequencing | `0.7.0_AE_CloudOps` (COO keeps the trigger) |
| R2 | **Cottonwood JOINS the existing trading-day axis.** Global does NOT become a multi-axis join to accommodate a third firm; Cottonwood carries nulls before 2026-07-21. | the re-home (1a) | DE |
| R3 | **The two-firm enumeration is a PRECONDITION on further Cottonwood build**, not a parallel nicety. | all Cottonwood build | DE |
| R4 | **The dispatcher's destination branch matches the envelope POSITIVELY** (`version` + `requestContext` + `responsePayload`) — **NEVER** a catch-all `else`. A catch-all deletes the loud refusal that made this class findable. | the unbuilt `lambda_entry` branch | `0.6.2_AE_PartnerETL~A` |
| R5 | **Deliverable 2 includes the `PutLifecycleConfiguration` limb.** Routine cleanup arrives as a lifecycle rule far more often than a hand-typed delete; shipping only the easy-to-test half is refused. | the deny | `0.7.0_AE_CloudOps` |
| R6 | **The import-closure census reports the instrument's REACH.** The unreached functions are **OUT OF REACH, NOT CLEAN.** | the census | `0.7.0_AE_CloudOps` |
| R7 | **The sovereign predicate is SPLIT, not ripped** — `SOVEREIGN_HELD` (emptied) vs `PROD_WRITE_FORBIDDEN` (preserved); one wave, all five sites; **plan to CTO before landing.** Ripping serves the retraction and destroys a live scratch-target control. | the retraction wave | `0.8.0_AE_CloudComp` |
| R8 | **The eclipse STALE parity signal stays VISIBLE.** It is TRUE, and it must not be silently "fixed" by a re-vendor nobody scoped. | eclipse | `0.7.0_AE_CloudOps` |
| R9 | **NONE of today's gate proofs transfer to a three-firm global.** Every gate was mutant-proven against `f(49f, inflection)`; all are re-exercised against `f(a,b,c)`. | Phase 3 | DS + CVO + DT |
| R10 | **Every evidence limb states its COVERAGE FRACTION** against the defect-capable population — never a percentage, never a bare scan denominator. | Phase 3 | all verify limbs |
| R11 | **The 20-date Global exemption is a LIST, not a FLAG.** A 21st missing date must go RED; never a predicate that re-derives itself. | the global gate | DS |
| R12 | **49F is DECLARED, NOT CLEARED** — measured defect (07-17, −10), mechanism UNDETERMINED, **no assurance instrument exists**; monitored prospectively, **no rate quotable from n=2.** | the co-sign text | COO (custody) |

> **THE GENERALISATION, and it is the real answer to *"firing from the hip"*: the rulings issued today were
> not wrong — several were caught and corrected within minutes, which is the mode working. THE DEFECT IS THAT
> SOME HAD NO CARRIER THAT SURVIVES A SESSION.** A decision whose only record is a message is a clock with no
> keeper. **Standing fix: any ruling that binds work not yet done gets a durable carrier and a named owner in
> the same turn it is issued.**

---

## ⚠ PART 2b-bis — AN UNSTAGED, **PARTIAL** WAVE IS SITTING IN THE SHARED WORKTREE. DO NOT COMMIT IT.

`0.8.0_AE_CloudComp` was **reset mid-wave.** Its sovereign-predicate work is **unstaged in the working tree**
(`org/modules/graph/sovereign_held.py`, `clobber_scan.py`, `infra/aws/compdiff/sovereign_held.py`,
`tests/test_comprail_sovereign_held.py`). It was routed to CTO as *"built, 90/90 green, land it in 60 seconds"*
— **CTO read it before signing and it is NOT complete against ruling R7.** Verified with a positive control
(17 hits for the known predicate, **0** for any prod-write predicate under any name):

| R7 step | state |
|---|---|
| `SOVEREIGN_HELD_PATHS` / `_BUCKETS` emptied to `()` | **DONE** — retraction honoured |
| a **named** `PROD_WRITE_FORBIDDEN` predicate | **ABSENT.** The scratch-target control survives only via `tool_probe.py`'s **own local literals** (`:287-289`, `:558-564`, `:819`), not a shared named predicate |
| vendored mirror byte-identical (sites 1+2, one commit) | **DIFFERS — the byte-identity test would FAIL** |
| retire the ARMED test assertions (step 5) | **NOT DONE** — `test_comprail_sovereign_held.py:99-100` still asserts `"data/black_diamond/" in _comprail.HELD_PREFIXES`. **The ratchet is still loaded.** |

> **COMMITTING THIS WOULD LAND A HALF-WAVE THAT LOOKS FINISHED** — an emptied hold with a failing
> byte-identity test and a test suite still voting to re-arm the prohibition. **That is the exact "one wave or
> none" condition R7 exists to enforce.** A 60-second unblock would have created the state the ruling forbids.

**HANDLING:** leave it unstaged; **do not `--force`, do not widen the `ANY_EXEC` lane on the sovereign leaf to
fix a commit refusal** (the fix for a 60-second block must not be a permanent widening of the control that
blocked it). It resumes with whoever picks the wave back up, from this row.
**SWEEP RISK IS REAL AND NAMED:** an unstaged multi-file change in a shared worktree is exactly what gets
absorbed into an unrelated commit — that happened to CTO's own edit today (`ORG_CHART`, see its provenance
note). **This block is the detector: if these files land under an unrelated subject, that is the sweep.**

---

## PART 2c — PER-LANE RESUMPTION *(the fabric was reset 1520Z; only CTO + MSTR retain context)*

**READ ORDER FOR A RESET AGENT: (1) PART 0 — the armed hazard. (2) your row below. (3) your handoff if you
have one, else your 2026-07-22 session log. (4) PART 2b — the rulings that bind you.**
**Only `0.4.0_DE` and `0.7.0_AE_CloudOps` wrote handoffs. Every other lane's resumption context is THIS TABLE
— it is the only carrier they have.**

| Lane | Owns / state at reset | HELD | Ready to resume with |
|---|---|---|---|
| **`0.4.0_DE_ClientPlatform`** | **PHASE 0 — the two-firm enumeration, which gates everything.** 4 confirmed / 1 checked-clean; infra, publisher, `dim_mdpf_account_distribution`, `dim_mdpf_aum_{metrics,timeseries}`, FE per-firm path **NOT covered**. WS-2/WS-3 done. **WS-4 fold built but WRONG SHAPE** — a standalone script cannot feed an in-memory composition; it re-homes as `build_cottonwood_artifact()` inside the shared producer. FE `$0` fix landed (portal DEV `08c6d8b2`). | the re-home; the fold | handoff `2026-07-22_1425Z.md`; **rulings R2, R3** |
| **`0.4.0_DS_ClientPlatform`** | **NO HANDOFF — this row is your context.** Item 1 CLOSED. Count-axis cured at source (all dates, not date-scoped). 20-date exemption `@77d297819` + 4 controls. **Per-cycle source audit BUILT `@b8efd3214` but NOT WIRED** — diff prepared for AE, split inflection-FAIL / 49F-report-only, before the completion marker. Producer-validate leg deliberately held for Cottonwood. Also holds 7 pre-existing inf drifts (incl. `INFLECTION_REP_IDS` missing `rep_id=6` ×5 — the founding attribution bug). | mutants; new MDPF work | log `p0_global_headline_basisB...`; **R9, R11** |
| **`0.6.2_AE_PartnerETL~A`** | **NO HANDOFF — this row is your context.** WS-5 converter half landed `@7aa7e645f` (**not `@228182599`** — a live `VendorDriftError` was fixed in between that would have raised on the first real conversion). Event path + sweep backstop landed together. **THE DISPATCHER BRANCH IS NOT BUILT — it blocks 0.7.0's WS-5 apply.** | the branch | log `wse_ws5_converter...`; **R4 — the branch matches the destination envelope POSITIVELY, never a catch-all `else`. This binds code that does not exist yet.** |
| **`0.7.0_AE_CloudOps`** | WS-5 closed + exercised on the real `mode=="event"` discriminator; both ledgers closed per-leg; eclipse landmine **disarmed inert**; import-closure gate live; **census delivered — 9 of 192 reachable, 183 explicitly NOT clean, and vendor staleness re-scoped to a SILVER-FAMILY problem (4 of 9, `silver_registry.py` the common axis).** | **WS-5 apply** (on the branch) · **Deliverable 2 APPLY** (narrowed carve-out) · silver-family catch-up | handoff `2026-07-22_1515Z.md`; **R1, R5, R6, R8** |
| **`3.0.0_SA_CVO`** | **NO HANDOFF — this row is your context.** Item 1 discharged; enumerated exemption independently exercised `@db3daab02` (4 controls incl. remove-a-listed-date). **Idle and explicitly available for the fresh 3-pass when a pin settles.** Authored the root cause: *the legacy date axis is not a trading-day axis.* | verify legs (no pin exists) | logs `session_close_0024-0523Z`, `work_0544Z`; **R9, R10** |
| **`2.0.0_SA_COO`** | **NO HANDOFF — this row is your context.** **Co-sign custody: 0 of 3, both limbs withdrawn** on a falsified premise. Carries 4 co-sign terms + 2 binding conditions (49F unbounded-by-construction with the "407 is an instrument artifact" clause; the retained legacy runtime dependency; the 1-of-6 historical coverage line; **the coverage-fraction requirement on every limb**). Serialization authority for the fold. | firing any limb | logs `session_1203-1313Z`, `session_1313-1410Z`; **R10, R12** |
| **`0.2.0_DT_PortfolioAnalytics`** | Consistency gate + honest-None marker consumer built; parity leg green. **Serial was killed 07-20 and re-appeared today — confirm liveness before assigning.** | all | log `consistency-gate-built-and-p0-reframed.md` |

---

## PART 3 — WHAT SETS THE DATE

**Phase 0 is the only unbounded item.** Phases 1–4 are each hours, not days, and largely parallel.
**I am not quoting a date until the enumeration prints** — I quoted one this morning off remaining-WS-numbers
and it did not survive contact with the wiring gaps. **The better basis exists: the estate has a defined
firm-onboarding sequence (FIRMSEP.10) and Cottonwood is part-way through it. That step list is the skeleton.**

**Standing correction to how this was scoped from the start: we have been treating a FIRM ONBOARDING as a
DATA FOLD.** Every blocker above is the unfinished half of a known onboarding sequence, not a fresh surprise.
