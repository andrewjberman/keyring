# THE COMB — the 2026-08-25 spring-clean sweep, 99 closed projects sorted

**Author:** `2.0.0_SA_COO~Z` · **Date:** 2026-08-31 · **Authority:** Andrew-direct ~21:1xZ, relayed
verbatim by `0.0.0_AB_MSTR~Z` (msg 17128): *"i think on call 3 their task is going to be doing the
combing of call 2, that is their first job"*

## THE ANSWER

**Denominator 99** — the projects the 2026-08-25 sweep closed. Not the wrong set; the wrong set is
what was measured.

| Classification | Count | What the close means |
|---|---:|---|
| **MEMBERSHIP-ONLY** | **92** | The face declares work that had NOT happened. The close filed over live work. |
| FINISHED | 5 | Scope delivered; no committed remaining work. The close ratified a terminal state. |
| ABSORBED | 1 | Work carried into a NAMED live successor. Correctly closed; the work continues elsewhere. |
| SOVEREIGN-SUSPENDED | 1 | Andrew himself stood it down before the sweep. The close matches his own word. |

**92 of 99 were closed on membership alone.** Only 7 closures correspond to any work verdict, and
only 5 of those are "finished" in the plain sense.

- **FINISHED (5):** `ASTN_WSJFT` · `MKOV_RETFIX` · `NFRA_GENESIS` · `OPAL_BRDSEP` · `OPAL_PORTALREFRESH`
- **ABSORBED (1):** `EXPAND_MSCLOUD` → re-homed into `NFRA_MSGRAPH`, scope carried forward verbatim
- **SOVEREIGN-SUSPENDED (1):** `NFRA_GCONTR` — Andrew-direct 2026-07-20, verbatim *"rendered as
  indefinite/suspended i do not want to fucking hear about it again"*

Full 99-row table: `laneZ_COMB_20260831_spring_clean_99_classification.json`.

## THE ROOT FINDING — the predicate had a MEASURED 3.1% base rate, committed 14h22m before the sweep

I did not re-run the predicate (Andrew's explicit ruling). I did not have to: **the register's own
owner already measured it, and committed the measurement the same day.**

`e0854c5027` — author `0.0.0_AB_MSTR`, **committed 2026-08-25T04:02:01Z**:

> "MEASURED: 10 of 327 project files are a member of ANY directive. A 3.1% membership rate. **NOT
> BEING A DIRECTIVE MEMBER IS THE NORM FOR 317 OF 327 PROJECTS, NOT AN ORPHAN CONDITION.** […] A
> future reader must NOT take 'this project is in no directive' as evidence that anything is wrong."

The sweep ran at **~18:24Z the same day — 14h22m later** — and used exactly that property as its
close predicate. It selected on a property ~97% of the estate's projects shared, healthy or not.

That is why the wrong set is 92 and not a handful: **the test had no discriminating power**, so its
output is essentially the register's membership shape, not a work verdict. The sweep's own text says
so on every face it wrote — *"Selected on MEMBERSHIP, not age"*, *"NOT a work verdict"*.

⚠ **ORDERING, NOT AWARENESS.** The correction commit precedes the sweep by 14h22m. I have **no
evidence** the sweep's operator read it, and I am not claiming they did. Two acts, one day; the
ordering is measured, the awareness is not.

Corroborating, same register, `a6d0261752` @2026-08-25T19:04:30Z: D10 was minted with an empty
member set deliberately *"so a D10 project cannot be swept on day one"* — the register owner
working around the sweep's hazard within the hour.

## METHOD, AND WHAT IT IS NOT

**The predicate was NOT re-run.** I audited the sweep's OUTPUT. Every input is the sweep's own text
plus fields it did not overwrite.

- **Denominator, two independent markers, zero disagreement:** 99 faces carry `closed: 2026-08-25`;
  the *same* 99 carry `SPRING CLEAN`. Neither set has a member the other lacks.
- **Primary instrument** — the pre-sweep work state the sweep preserved after `Prior phase:`
  (97 of 99 carry it).
- **Second instrument** — the `blocking` field: a *different field* written at a *different moment*,
  so it corroborates rather than repeats.
- **Discriminator, declared before reading** so it could not be fitted to what I found: *at the
  moment of close, was the project's own declared work state terminal?*

### Controls

1. **Known-wrong reproduced.** `PORTAL_AUTHHARD` (WAVE-2 OPENED) and `OPAL_TICKET` (NEXT: P1/P2/P3,
   TAC-4 OPEN) both land MEMBERSHIP-ONLY on the instrument alone, without being told to.
2. **Overcount control — the direction that ADDS rows.** An undercount announces itself; an
   overcount never does. I re-read all **27** membership-only rows whose `blocking` opens
   "None"/"Nothing". **All 27 name remaining work in the same field. Zero moved to FINISHED.**
3. **The second instrument changed a verdict**, which is the evidence it was doing work:
   `OPAL_SQSCHAT`'s phase reads *"FUNCTIONALITY CLOSED-AS-ACCEPTED by Andrew"* — but its `blocking`
   field reads **"THE PROJECT IS NOT CLOSED"**, with Terraform open and Andrew ruling *"T1 SHIPS, IT
   IS NOT DROPPED."* On the phase text alone it would have been filed as finished.

### Two traps banked

- ⛔ **`blocking: None` means no BLOCKER, not no WORK.** All 27 controls named remaining work in the
  same breath. Structurally identical to `1.0.0_SA_CTO~Z`'s warning (msg 17131) that **zero open TOs
  is not "done"** — and I used neither TO counts nor `to-check.py --project`, which does not filter.
- ⛔ **The sweep built a TO-state distinction into its own text, and it is not a completion signal.**
  Wave A (56): *"carried ZERO open task orders at close."* Wave B (43): *"Its open task orders were
  closed IN THE SAME ACT."* Wave B closed 43 projects' live task orders as part of the membership
  close. Useful as provenance; **not** used as the discriminator, for the reason above.

## THE SHARPEST INSTANCES

Projects whose own face contradicts its closure in the sweep's own words:

- **`OPAL_SQSCHAT`** — face: *"THE PROJECT IS NOT CLOSED."* Andrew ruled T1 ships; Terraform open.
- **`NFRA_VELOCITY_CORE` + `NFRA_VELOCITY_ESTATE`** — face: *"ON-HOLD, NEVER CLOSED […] Resumes on
  Andrew's word only."* Both closed. Reserved-pending-his-word, not closable.
- **`YALP_MACROS`** — Phase 2 **RE-OPENED by Andrew-direct sovereign override**; closed anyway.
- **`NFRA_SYSPARITY`** — Andrew-direct verbatim *"SYSPARITY is ongoing."* Closed.
- **`NFRA_TOOLHEALTH`** — already once wrongly flipped terminal, **reopened on Andrew's 07-09
  ruling** against premature flips; the sweep closed it again. Its own face names the signature:
  *"terminal status + a blocking field describing work not yet done."*
- **`MDPF_PIPELINE_TRUTH`** — carries OPEN HIGH-severity defects and a
  `PHASE_0_BLOCKING_DECISIONS_AT_ANDREW` repair sequence. Decisions awaiting him, closed.
- **`ADVI_COTETL` + `COT_CANON458`** — the only two of the 92 named in the live directive register,
  and both are named *in the very correction note that falsified the predicate*.

## THINGS I DID NOT DO

- **Did not re-run the 08-25 membership predicate** (Andrew-direct). This audits its output.
- **Did not decide placement.** No device ownership is assigned or implied anywhere in this
  deliverable or its JSON. That is a whole-register decision, after the comb, then `/integrate`-parity'd.
- **Did not build or propose an alarm.** `OPAL_ALERTS` and `OPAL_SCHEDULE` sit in the wrong set and
  are alarm/schedule-shaped; they are reported as findings only. All alarms are held pending
  GLOBALALARM.
- **Did not reopen anything.** Reopening 92 projects is a sovereign call, not a COO act.

## MEASUREMENT BOUNDARY

`GLOBALALARM`, `PLATFORM_OPS_USERMGMT` and `D12` are **absent from this SITEZ tree** (measured: not
present in `org/missions/DIRECTIVES.yaml`, which carries 12 rows D0–D11). They are laptop-side. That
`D12` needs `PORTAL_AUTHHARD` as prior art and `D7` needs `OPAL_TICKET` is **relayed by
`0.0.0_AB_MSTR~Z`, not measured here** — consistent with parity (CLOUD keeps moving).

## THE OPEN CALL AT ANDREW

The comb is done; the disposition is his. **92 projects are closed with live work on their faces.**
Options, each independently coherent:

1. **Bulk-reopen all 92** — restores the board; re-floats 92 rows nobody is staffed to drive.
2. **Reopen on demand** — leave closed, reopen when a directive needs one (the `PORTAL_AUTHHARD` /
   `OPAL_TICKET` pattern). Cheapest; relies on someone knowing to look.
3. **Reopen a named subset** — e.g. the sharpest instances above, where the face contradicts the
   closure in his own words.

**My recommendation: (3), then (2) standing.** The sharpest set is small, each row carries its own
sovereign-word contradiction, and it does not re-float 92 rows into a two-seat fabric. (1) creates a
board nobody can drive; (2) alone leaves his own reversed rulings sitting closed.
