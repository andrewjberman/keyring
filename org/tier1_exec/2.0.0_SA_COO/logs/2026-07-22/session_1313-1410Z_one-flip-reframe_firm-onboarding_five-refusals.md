# Session 1313-1410Z (delta) -- Andrew's one-flip ruling, the FIRM-ONBOARDING reframe, and six worker refusals that were all correct

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE (pin re-verify, the cot-seed negative result, owner-of-record verification)

**Serial:** 2.0.0_SA_COO (main COO) | **PID:** 5392
**Window:** ~1313Z -> ~1410Z. Delta since `session_1203-1313Z_*`. /drive OFF, zero crons, throughout.

## Summary
The morning's arc (co-sign withdrawn, 0 of 3) resolved into a different project than the one we thought we
had. **Andrew ruled ONE FLIP with Cottonwood inside the gate, overruling the joint CTO+COO two-flips
recommendation** -- executed, not re-litigated. Then the blockers arrived from four unrelated directions and
CTO named the cause: **we have been treating a FIRM ONBOARDING as a DATA FOLD.** Everything since has been
converting that from an explanation into a predictive checklist. **Tonight's flip window is gone, and that is
a good outcome** -- three structural blockers surfaced in an hour that would otherwise have arrived one per
day, mid-flip.

## Significant work

- **Andrew-direct 1259Z recorded VERBATIM** ("Let's push everything with Cottonwood"). **Custody consequence I
  enforced: NO BINDING PIN UNTIL THE END.** DS's rebuilt ETags (`5e7b684d` inflection / `08f9720e` global,
  **verified on my own ListObjectsV2, not transcribed**) are a **CHECKPOINT, not a pin** -- Cottonwood
  rewrites global again, so any pin taken today is void by construction. **My limb fires ONCE, on the
  nightly-emitted Cottonwood-inclusive set.**
- **Retracted my own ~2-day ETA before it became a commitment** (MSTR had already relayed it; he corrected
  Andrew same-turn). It assumed WS-5 was a TF job; it is not.
- **CO-SIGN TERMS agreed with CTO:** 49F count axis **UNBOUNDED BY CONSTRUCTION** (CVO: 7.25% median
  divergence, 6 of 407 dates agreeing -- "407 of 407" is an instrument artifact, not evidence); CTO's
  **RETAINED RUNTIME DEPENDENCY / decouple-debt** clause; the **1-of-6** mis-stamp coverage fact; and
  **every evidence limb must state its COVERAGE FRACTION**, not merely its denominator -- the term that
  would have blocked my own signature this morning.
- **Converted a co-sign clause into a real control.** CTO's decouple clause named a hazard whose trigger is a
  routine cleanup by someone who would never open a superseded co-sign deliverable -- **and filed it there.**
  Objection sustained; opened `DO_NOT_DECOMMISSION_portal-v2_json_mdpf_49financial_20260722.md`, **which
  states in its own body that it is the WEAKEST of three controls** (bucket-policy DENY > TF gate > this doc).
  Owners named same day.
- **Serialization: I got it wrong and DE corrected me.** I serialized DS's rebuild against DE's fold **by
  object**; global is composed **in-memory inside one producer**, so they were **two edits to the same
  function**. Retracted to CTO, who ruled no collision (DS's producer fix already landed).
- **Tried to unblock DE's commit and FAILED -- and said so.** Seeded a `cot` lane for comp-constants (the
  tool's own usage already recognised `--lane cot`; only the seed was missing), **then RAN THE CHECK instead
  of declaring victory: still DRIFT, 2 sites.** Landed @ac099e4be **with the negative result written into the
  file** so nobody reads the seed's existence as the problem being solved. Mechanism: comp-constants checks
  any file defining a registered constant NAME against EVERY lane's canonical, **with no per-file lane
  scoping** -- so a genuinely new firm cannot be represented without a tool change.
- **Authorized the two-firm-assumption ENUMERATION** (CTO upgraded it to a **gate** on further Cottonwood
  build). Now **5 CONFIRMED / 1 CHECKED-CLEAN**, with the uncovered surface stated.
- **Routed the declared-but-unapplied TAXSMA IAM grant** -- and **refused to dispatch it**, because the
  owner-of-record lane is not live and the base is under a same-day Andrew fabric-quiet directive. MSTR
  backed the refusal and classed it S3-RESERVED. **Verified the owner in the project JSON rather than taking
  CTO's recollection**, even though his memory was right.
- **Allocation call:** paired `0.6.2_AE_PartnerETL~A` (converter/stamp half) with `0.7.0_AE_CloudOps`
  (TF/estate half) on WS-5 once it proved not to be a TF job. Requested `0.8.0_AE_CloudComp` for the two
  comp-tool fixes.

## Compiler Tools
| Tool | Call | Result | Note |
|---|---|---|---|
| `comp-constants check --file` | DE's `build_cottonwood_mdpf_slice.py` | **DRIFT 2** | the load-bearing call of the session: it **refuted my own fix**. Ran it *after* landing the seed rather than assuming |
| `comp-constants check --lane cot` | whole-lane | **REFUSED** | surfaced the stale sovereign hold (below) |
| `comp-which` | comp-constants lane-scoping | NO CURATED RULE MATCHED | correctly said so instead of guessing; its *usage string* is what revealed `--lane cot` exists |
| `comp-grep` / `comp-glob` | seeds, `.tools/commit-gate.sh`, TRADING_CALENDAR | PASS | confirmed 3 live vendored `trading_calendar.py` copies; confirmed commit-gate has **no override token** |
| `comp-system` | regenerate 06 | PASS | required by the gate for the added file |
| rail-checked `aws s3api list-objects-v2` | pin re-verify x2 | PASS | independent of DS's report both times |
| `safe-commit.sh` | 6 commits | PASS | risk-reflex CLEAN each time, and **it reported its own danger map 198h STALE** |

**GAP FOUND (routed to CTO):** `comp-pipescript io` on `dim_mdpf_aggregate_aua_timeseries.py` reports
**1 read / no writes** and **does not surface the `opal-data-portal-v2` served import at `:476-500`** -- the
coupling that carried the count-axis defect and voided two co-sign limbs. **A cross-bucket read inside a
helper function is invisible to the I/O manifest we tell DS/DT to run before touching a gold script.**
**SECOND FINDING:** `comp-constants` still enforces the **bd/49F sovereign hold Andrew LIFTED COMPLETELY on
2026-07-14**. MSTR's sweep has since measured it: **5 of 6 enforcing copies survived, and a drift gate has
been DEAD 8 DAYS across bd's 12 and inf's 11 constants.**

## Blockers
None on me. Five decisions **RESERVED FOR ANDREW** (merge-vs-add key ruling; day-one Cottonwood rendering;
Opal Satellite naming; the bucket-policy Deny vs the 07-17 alert suspension; TAXSMA ownership). CTO holds the
technical rulings. No forks unresolved.

## Current State (handoff)
- **Re-land = 0 of 3 limbs. No binding pin exists.** Nothing is servable and nothing should be.
- **Tonight's window is GONE** -- nothing invokes the Cottonwood producer; DS independently found the
  identical wiring hole for the per-cycle audit. **The commit gate was never the constraint.**
- **DE re-homing** his slice logic as `build_cottonwood_artifact()` inside the shared producer, on current
  HEAD, sequential. **Every gate proved today was mutant-proven on `f(a,b)` and says nothing about
  `f(a,b,c)`** -- all re-exercise after the re-home (CTO ruling).
- **Cottonwood conforms to 49F's trading-day axis**; carries nulls before 07-21 (path A); the (A) bound is now
  true **by construction**.
- **FE `$0` defect** (`lastNonNull` returns 0 on all-null, `ModelPortfolios.tsx:294`): ruled -- **narrow
  sibling function, treatment "Not yet tracked", all-null series must be EXERCISED (must fail before it
  passes)**. Plus the footer's false *"rolled forward from last known data"* claim, same pass.
- **Feed-liveness RETIRED** (not undetermined): vendor `lastUpdate` 60/60, newest 07-20T19:17Z precedes both
  pulls, and the field demonstrably moves -- so the byte-identity is **explained**, not merely unrefuted.

## Next Steps
- **[me]** Fire the COO limb ONCE on the nightly-emitted Cottonwood-inclusive set, against evidence written to
  the coverage-fraction standard; verify the pin myself, never transcribed. Keep the enumeration a gate.
  Re-raise **UNIVERSAL_TRADING_CALENDAR** re-prioritization (asked CTO, unanswered) -- CVO's root cause is
  that PRD's premise demonstrated on a served surface.
- **[Andrew]** the five reserved decisions above.
- **[0.4.0_DE]** re-home -> enumeration (FE per-firm distribution path next) -> control re-exercise -> `$0` fix.
- **[0.6.2 + 0.7.0]** WS-5 converter half landed @228182599; TF apply GO granted `-target` on 2 resources,
  **one apply** (a destination without the grant fails silently).
- **[0.8.0_AE_CloudComp]** comp-constants file->lane resolution; the retracted-hold sweep (**sweep is the
  deliverable; "zero of N searched", never "clean"**).
- **[0.5.0~A / MSTR / Andrew]** the TAXSMA `ReadTaxsmaRoster` grant -- **roster is FRESH (07-21T23:56Z), so
  this is a BLOCKED CONSUMER, not a dead path.**

## The pattern worth carrying out of this window
**SIX worker refusals, all correct, every one against a brief that two execs and MSTR had blessed:** DS
refusing to write into the frozen-9 · DE refusing to fold without an explicit firm-separation word · DE
refusing to reinterpret condition (i) against his own landed code · AE refusing to build WS-5 as briefed ·
DE refusing to rename past the constants gate · DE reporting his own finished, exercised script was
**structurally the wrong shape**.
> **The authority gradient runs downward. The grounding gradient ran upward all day.** (MSTR, LD-0330 §8.17)
> **DE's version, which is the actual argument: the refusals were CHEAP and the alternative was NOT.** Each
> cost minutes; inventing a bypass path in a universal gate to make a deadline that did not exist would have
> been permanent.
**And three distinct DECLARED-vs-APPLIED instances in one day** -- the pin-void gate, the retracted sovereign
hold, the unapplied IAM grant. **In all three the record said one thing, the enforcing/applied copy said
another, and the instrument that should have caught it reported GREEN.** That is one architectural property
of a fabric whose instruments read declarations, not three coincidences.
