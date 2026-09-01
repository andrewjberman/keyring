# D2 + D8 — EXPECTATIONS AND OUTCOMES, LOCKED

**Seat:** 1.0.0_SA_CTO (PRD/architecture author) · **Date:** 2026-09-01 · **Status:** LOCKED baseline
**Commissioned:** Andrew-direct 2026-09-01 ~00:2xZ — *"I want to make sure we are 100% locked in on our
expectations and outcomes from the D2 and D8 work so we can assess and adjust TOs as needed to get
there."*
**Consumer:** `2.0.0_SA_COO` decomposes and dispatches against this. This document does NOT dispatch,
cut TOs, or sequence — agent coordination is COO's function (Andrew-direct 00:1xZ).

⛔ **HOW TO USE THIS:** an outcome is DONE only when its ACCEPTANCE TEST passes as written. A TO that
does not advance a numbered outcome below is out of scope for these directives.

---

## PART 1 — D2: PERFORMANCE REPORTING

**Priority:** #1 across ALL directives (Andrew-direct 2026-08-31 23:1xZ).

**GOAL:** 49F performance reporting is displayed, correct, and provably matches Black Diamond.

Andrew named three axes: **DISPLAY**, **backend pipeline reliability**, **data parity with Black
Diamond**. Every outcome below sits under one of them.

### AXIS 1 — DISPLAY

**D2-1 — the cards render from SERVED leaves, not fixtures.**
- ACCEPTANCE: an authenticated DEV fetch returns 200 + body for each served perfrp key, AND a read
  render shows real producer figures drilled to the level the card claims.
- ⛔ **DENOMINATOR IS 10 OF 11, NOT 11.** `perfrp_transactions_relationship` carries `deferred` and
  fails closed by construction at `d_publisher_port.py:589-591`, tested BEFORE `--publish`, `--keys`,
  the grant env and the operator. **An acceptance read expecting 11 served keys scores a FALSE MISS on
  the one key a sovereign ruling deliberately withholds.**
- STATE: five cards bound against fixtures — PERFORMANCE +26.33%, GAIN/LOSS $109K, ALLOCATION $288K,
  TRANSACTIONS 21 rows; ACTIVITY SUMMARY correctly shell-only (no leaf is emitted for it, so its
  emptiness is a producer wait, not a build gap). Key-class precondition landed `@729b7617`. Serve
  AUTHORIZED. **Activation NOT fired.**

**D2-2 — the render path consumes what is actually served, end to end.**
- ACCEPTANCE: measured against **DEPLOYED BYTES**, not branch source.
- ⚠ **THIS IS THE OPEN HOLE AND IT IS NAMED HERE SO IT IS NOT INHERITED AS SETTLED.** The claim that
  PROD cannot render perfrp rests on `origin/PROD` SOURCE (1,564 lines, zero perfrp matches). **A stale
  deployed bundle reads identical.** If PROD exposure becomes load-bearing, the read happens against
  the deployed artifact.
- This is where Andrew's atom-decomp / comp-find frontend validation belongs (Part 3).

### AXIS 2 — BACKEND PIPELINE RELIABILITY

**D2-3 — producers current on the DEPLOYED plane.**
- ACCEPTANCE: `comp-pipescript deployed --pipeline advi` = 0 STALE, 0 TIMEOUT, denominator printed,
  **run TWICE.** ⛔ A TIMEOUT is not a MATCH; a single run of that tool returned `5 STALE + 1 TIMEOUT`
  where the TIMEOUT was the single most load-bearing file, and the second run returned `6 STALE`.
- STATE: `_code/` sync COMPLETE. Prior state was 71 checked / 68 MATCH / 3 STALE.

**D2-4 — production runs are SCHEDULED, not ad-hoc.**
- ACCEPTANCE: every production path fires on a schedule; ad-hoc runs are QA only and are never
  production evidence. Success-of-upstream as the ONLY trigger is a defect.

### AXIS 3 — DATA PARITY WITH BLACK DIAMOND

**D2-5 — the 5,309-account census completes.**
- ACCEPTANCE: landed-vs-requested with BOTH numbers; per-account `range_match` with the non-match
  count; criterion-3 before/after on the pinned prefix; the exact vendor-call count reporting **both**
  the data leg and the auth leg.
- STATE: built, exercised, **ARMED AND UNFIRED**.
- ⛔ **CORRECTED 2026-09-01 00:3xZ — MY FIRST VERSION OF THIS LINE IMPLIED A ROTATION FAULT. THERE IS
  NO FAULT.** `bd-49f-session-trigger` RAN ON TIME at `2026-09-01T00:00:18Z`, probed the cookie, found
  it **POSITIVE-LIVE, and SKIPPED THE MINT BY DESIGN** — *"Lever A: cookie POSITIVE-live -> SKIP mint,
  direct-invoke bd-49f-runner"*, then invoked, status 202, no error. **THE MINT IS CONDITIONAL, NOT
  SCHEDULED-UNCONDITIONAL.**
- POSITIVE CONTROL, same function, previous night: *"cookie NOT positive-live (probe negative) -> full
  mint (fail-safe)"* — which is precisely why `LastChangedDate` reads `2026-08-31T00:03:47Z`. **Both
  branches observed on consecutive nights in one log group.**
- ⛔ **THEREFORE "WAIT FOR THE MINT" WAS WAITING FOR AN EVENT THE SYSTEM DELIBERATELY SUPPRESSES WHILE
  THE SESSION IS HEALTHY.** W2's blocker is DISSOLVED, not weakened. The secret-not-changing observation
  was TRUE; every implication drawn from it — mine included, in the first version of this document —
  was FALSE.
- ⚠ TRANSFERABLE: an absent event is not a failed event until you read the thing that would have
  emitted it. Four seats carried "the mint did not fire" as a finding before one log stream was read.

**D2-6 — every non-EXACT cell is explained or accepted.**
- STATE: probed **n=8** (5 from P1, 3 from the spot check). **12 open calculation differences.**
- ⛔ **STANDING SENTENCE, MANDATORY IN EVERY TO, PRD, FACE AND REPORT: "parity is PROBED at n=8 with 12
  open calculation differences; the census is armed and unfired."** NOT "proven." A single "parity
  rate" reports the opposite of what the distribution says.

**D2-7 — the period contract exposes only what we can honestly support.**
- RULED (this seat, 2026-09-01): **expose QTD, YTD, 1Y. Remove SI. Remove 3Y. Remove any calendar year
  before 2025.**
- WHY SI: 3,027 of 5,309 accounts (**57.0%**) were already running on our first data day 2024-07-08, so
  their inception is unobservable; and BD's SI field is not authoritative — measured **3 of 3** returning
  SI byte-identical to QTD because we sent a probe start, while the same payload said the account did
  not exist in 2024.
- WHY 3Y, **which the brief missed**: our span is 2024-07-08 → 2026-08-28. A 3Y window from 2026-08-28
  opens 2023-08-28 — before our first day **for every account in the book**. SI is unobservable for
  57%; **3Y is unobservable for 100%.**
- ⛔ **BLAST RADIUS — SI IS A DEFAULT, NOT AN OPTION:** `perfrp_emit_core.py` carries `period="SI"` as
  the DEFAULT PARAMETER at `:315 _performance`, `:1031 _book` and `:1927 build`. Every leaf emitted
  without an explicit period is an SI leaf. And `perfrp_contract.py:106` codifies the mislabelling:
  `"SI": "contract-defined", # pinned to SI_FLOOR_DATE, LABELLED`.
- ACCEPTANCE: `RULED_PERIODS` and `PERIODS` no longer carry SI/3Y; the three `period="SI"` defaults are
  removed; **and a control FIRES when an SI figure equals its own QTD figure** (the exact 3-of-3
  signature measured).
- ⛔ **DO NOT SOFTEN `parity_period_returns.py`'s REFUSALS** to make a column populate. That module is
  correct — it emits `UNAVAILABLE-NO-ANCHOR` / `UNAVAILABLE-NO-COVERAGE` and never approximates. The
  exposure decision is UPSTREAM of it.
- SEQUENCING: producer enum, served contract and card columns move TOGETHER. The card column contract
  is POSITIONAL and refuses on a count mismatch — correct behaviour, and it means a one-sided edit
  fails loudly instead of mislabelling. Units / Price / Amount under the wrong header is a financial
  misstatement that looks like data.

### D2 — OUT OF SCOPE (hard)
- **Frontend UI/UX design.** Andrew: it is its own project and FOLLOWS confirmation of the three axes.
  It must not absorb capacity now.
- **`ADVI_INSURE` beyond its scheduled fire.** Named distinctly lower priority and over-resourced.
  NOT cancelled, NOT stopped — it simply draws no seat, review cycle or senior hour away from D2.

### D2 — OPEN RULINGS OWED
| Item | Owner |
|---|---|
| The custodian limb: control contradicts itself (132 rows, three ways) | `0.7.0_AE_CloudOps~G` produces the read; CTO rules |
| The LARGE 1Y cell on 20277481 — a genuine calculation difference | P3-EXACT |

---

## PART 2 — D8: AUTH_SELFHEAL + MDPF_HEALGAP

**GOAL:** no Opal pipeline silently loses a day because a vendor session died and nothing retried.

**THE SPLIT, ratified and on the register row:** `MDPF_HEALGAP` = THE INSTANCE (the Cottonwood runner's
missing date, its schedule ordering, its recovery gap). `AUTH_SELFHEAL` = THE PATTERN (auth self-healing
+ consumer retry across every cookie-riding consumer, both firms). The tell that the split is right:
moving one `schedule_expression` fixes the instance and makes no other pipeline safer.

**D8-1 — consumer inventory complete.** Every cookie-riding consumer, both firms, denominator printed.

**D8-2 — a VALIDATED ordering rule between schedule fire and session mint.**
- ACCEPTANCE: the margin is MEASURED, not asserted. ⛔ The "~18 h session lifetime" hypothesis is
  **FALSIFIED** as an absolute ceiling — the 49F session served tokens at 21.59 h and again at 23.83 h.
  No ceiling may be asserted; session-age-at-failure is an OPEN QUANTITY.

**D8-3 — a stated position on re-mint.** Who may re-mint. Measured today: `bd-cot-keepalive-role` holds
`GetSecretValue` ALLOWED, `PutSecretValue` / `UpdateSecret` implicitDeny — it can extend but cannot
re-mint.

**D8-4 — the 2026-08-31 cot hole closed.**
- STATE: **OPEN.** The one-shot fired 23:27:25Z, auth SUCCEEDED (the failure class that created this
  project did NOT recur), then the COUNT-RECONCILE self-gate fail-closed. 6 of ~89 objects, no
  complete-stamp.
- DIAGNOSED at zero vendor cost: an account left the book (950 → 947 rows); BD's **accounts** endpoint
  reflects it, BD's **roster** endpoint does not (still 15). **A vendor-side internal inconsistency,
  not a defect in our pull.** A re-fire against unchanged vendor state fails identically.

**D8-5 — retry/recovery lives IN the consumers**, not bolted alongside.

### D8 — OUT OF SCOPE (hard)
- ⛔ **DETECTORS, ALARMS, NOTIFICATIONS.** Standing moratorium. From the brief's own scope guard: *"this
  project FIXES, it does not NOTIFY."* A retry is a fix; a detector is an alarm and is HELD. **A
  deliverable that drifts from retrying/reordering into detecting-and-reporting has changed category
  and needs a new word.**
- Widening any fail-closed gate without a measured cause.

### D8 — OPEN RULINGS OWED
| Item | Owner |
|---|---|
| Should a NON-Opal strategy (`Core \| Satellite 60`) be able to fail-close an entire bronze date? | CTO |
| The gate's error text says `wrong/truncated pull` — it MISATTRIBUTES a vendor disagreement to our side | CTO |

---

## PART 3 — FRONTEND VALIDATION (Andrew-requested)

Andrew: *"maybe do additional atom-decomp and comp-find scanning/analysis to validate on the frontend."*

**The question worth that spend is D2-2: does the render path consume what is actually SERVED, on the
DEPLOYED bundle?** Everything proven so far is fixture-render or branch-source. Specifically unproven:
1. deployed portal bundle vs `origin/DEV` — a stale bundle reads identical to a current one;
2. an authenticated fetch of each served key returning 200 + body (GATE A until activation);
3. that each card's consumed key equals the publisher's written key **after** the `@729b7617` change.

---

## PART 4 — THE ANTI-THRASH RULE

Andrew: *"directives and [STOP] alarms are reverberating and thrashing all over the fabric ... not a
proper way to operate."*

**ROOT CAUSE, measured: three preconditions were discovered AFTER a GO** (the stale core, the key
mismatch, the serve precondition). Each triggered a halt cycle, a correction, and a fan-out. Both GOs
issued that night asserted work state that was already stale — "wire the four panels" when half were
wired, "the wiring is buildable" when it had already landed.

```
  1  A GO ENUMERATES ITS PRECONDITIONS BEFORE IT IS ISSUED.
     No seat is GO'd on an unmeasured premise.
  2  [STOP] IS COO's, AND ONLY FOR AN IRREVERSIBLE ACT ALREADY IN FLIGHT.
     Not in flight -> a HOLD to the executor alone. [STOP] hard-blocks deploys fabric-wide.
  3  VERIFY THE PREMISE BEFORE ESCALATING when verification is under five minutes.
  4  ADDRESS THE EXECUTOR, CC THE ISSUER. Record seats get a digest at decision points.
  5  ONE CORRECTION PER FINDING, from the seat that OWNS it.
```
