# THE COMB — the 2026-08-25 spring-clean sweep, 99 closed projects sorted

**Author:** `2.0.0_SA_COO~Z` · **Date:** 2026-08-31 · **Authority:** Andrew-direct ~21:1xZ, relayed
verbatim by `0.0.0_AB_MSTR~Z` (msg 17128): *"i think on call 3 their task is going to be doing the
combing of call 2, that is their first job"*

## THE ANSWER

**Denominator 99** — the projects the 2026-08-25 sweep closed. Not the wrong set; the wrong set is
what was measured.

| Classification | Count | What the close means |
|---|---:|---|
| **MEMBERSHIP-ONLY** | **≤ 92** | The face declares work that had NOT happened. The close filed over live work. |
| FINISHED | 5 | Scope delivered; no committed remaining work. The close ratified a terminal state. |
| ABSORBED | 1 | Work carried into a NAMED live successor. Correctly closed; the work continues elsewhere. |
| SOVEREIGN-SUSPENDED | 1 | Andrew himself stood it down before the sweep. The close matches his own word. |

**Up to 92 of 99 were closed on membership alone.** Only 7 closures correspond to any work verdict,
and only 5 of those are "finished" in the plain sense.

⚠ **READ AMENDMENT 1 BEFORE QUOTING THE 92.** Both instruments are face text and share one failure
mode — a stale face reads "work remains" whether or not work continued — so **92 is an UPPER BOUND on
the wrong set, not a measured count.** The bound runs in the direction that inflates the number.
Raised by `1.0.0_SA_CTO~Z`; accepted in full. The root finding and the recommendation are unaffected,
for reasons given there.

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

---

# AMENDMENT 1 — 2026-08-31 ~21:5xZ: **92 IS AN UPPER BOUND, NOT A MEASURED COUNT**

Raised by `1.0.0_SA_CTO~Z` (msg 17137) as the D-family ruling seat, after independently re-deriving
the root finding at source with a negative control. **The correction is accepted in full and the
headline above is qualified accordingly.**

## The bound I did not close

Both my instruments — the preserved `Prior phase:` state and the `blocking` field — are **FACE TEXT**.
They were written at different moments, which is why they corroborate rather than repeat. But they
**share one failure mode**: if a project's face went stale (work continued and finished, nobody
updated the record), *both* fields still read "work remains" and the row lands MEMBERSHIP-ONLY.

**Neither instrument can see work that happened after the face was last written.**

So **92 is an upper bound on the wrong set**, not a measured count of it. That is the direction that
inflates an alarming number — and per this estate's own banked lesson, an undercount announces
itself while an overcount never does. My overcount control tested face-text-vs-face-text; it could
not test face-vs-world.

## Why the finding is unchanged

1. **The predicate's lack of discriminating power rests on `e0854c5027` alone** and does not depend
   on the size of the wrong set at all. 3.1% membership is measured, published and committed.
2. **The refinement path is already recorded and costs nothing to take later:** wave B (43) carries
   *independent* corroboration that work remained — its live task orders were closed IN THE SAME ACT,
   which is a fact about the sweep, not about the face. **The staleness risk therefore concentrates
   in the WAVE A subset (56)**, where face text is the only instrument. Recorded here as the
   available refinement; NOT taken, and no re-run requested.
3. **The symmetric risk on FINISHED is small but not zero.** A face can also go stale *terminal-side*
   — `NFRA_TOOLHEALTH`'s own history is this estate's precedent for it ("terminal status + a blocking
   field describing work not yet done"). My 5 FINISHED rows each passed two instruments, and one
   (`OPAL_SQSCHAT`) was caught and flipped by exactly that check — but 5 is the exposure.

## What this does NOT change: the recommendation

**Rec (3) is immune to this bound**, which is the property that makes it the right call on a number
carrying a one-directional error. The sharp instances rest on **Andrew's own words** — *"SYSPARITY is
ongoing"*, *"THE PROJECT IS NOT CLOSED"*, *"ON-HOLD, NEVER CLOSED […] Resumes on Andrew's word only"*,
a sovereign override that RE-OPENED a phase. **A sovereign ruling does not go stale the way a phase
note does.** The recommended action therefore does not depend on the exact size of the wrong set.

`1.0.0_SA_CTO~Z` concurs with (3)-now / (2)-standing, unchanged.

# AMENDMENT 2 — THE FORWARD QUESTION: CAN THE PREDICATE FIRE AGAIN?

Raised by `1.0.0_SA_CTO~Z`. **"Do not re-run the predicate" and "can the predicate fire again" are
different questions, and this comb answered only the first.**

If the spring-clean mechanism is still live and still keyed on directive membership, then every
project minted since — **and every project reopened under rec (3)** — is exposed to closure on the
same property that has already been measured to have no discriminating power. That would make the 92
a **recurring class rather than a one-time event**, and it would change the disposition from cleanup
to control.

⛔ **UNMEASURED AND NOT CHASED.** Neither seat has measured whether the mechanism is a standing job, a
one-off script, or a hand-run act, and neither is guessing between them. Surfaced as an **open
question for Andrew's disposition alongside the 92**, because it is cheap to ask now and expensive to
discover after 92 rows have been reopened into it.

**This remains a finding, not a build.** No monitor, no alarm, no gate is proposed — the standing
moratorium binds and all alarms are held pending GLOBALALARM.

---

# AMENDMENT 3 — 2026-08-31 ~22:5xZ: **WAVE A IS NOT SAFELY READABLE AS "PROBABLY FINISHED"**

Raised by `1.0.0_SA_CTO~Z` against **its own** Amendment-1 bound, from a counter-example that fell out
of unrelated work. Accepted, and it belongs at the headline's side rather than in a thread.

## The inference Amendment 1 invites, and why it is wrong

Amendment 1 says staleness risk **concentrates in the WAVE A subset (56)**, because wave B's 43 carry
independent corroboration (live TOs closed in the same act) while wave A has only the face. That is
true. But it invites a next step a reader would reasonably take: *"so start by discounting wave A."*

⛔ **THAT INFERENCE NOW HAS A CONCRETE COUNTER-EXAMPLE FROM INSIDE WAVE A.**

**`ADVI_PRVSYS` is wave A** — *"carried ZERO open task orders at close"* — and its PRD carries live,
unbuilt, load-bearing design that a directive **minted six days later** needs:
`ADVI_PRVSYS_PRD.md:30` specifies the scoped partner-admin page (`firmRole=admin`, own firm only) and
`:77` carries the exact control D12's WS-5 requires — *"gates the page AND the API (both — never
page-only; the API independently re-checks the JWT, **a hidden page is not a control**)."*

> ### ZERO OPEN TASK ORDERS MEANT NOBODY HAD CUT THE TOs YET — NOT THAT THE WORK WAS DONE.

So wave A is **simultaneously the least-corroborated subset AND not safely readable as "probably
finished."** Those are not in tension: both follow from wave A having only one instrument. Amendment
1's bound **stands unchanged and is not withdrawn** — ≤92 is still a ceiling. What is withdrawn is any
reading of it as a ranking of where to look first.

## The part that should worry a decision-maker most

Three instances of "a live directive needs a wrongly-closed project as prior art" are now known:
`PORTAL_AUTHHARD` (D12), `OPAL_TICKET` (D7), `ADVI_PRVSYS` (D12 again).

**Two of the three were surfaced by a readback of Andrew's own transcripts. The third fell out of
someone working the directive.** None was found by looking for wrong closures.

⛔ **THERE IS NO REASON TO THINK THE OTHER 89 DIFFER IN KIND, AND NO INSTRUMENT CURRENTLY LOOKS FOR
THEM.** The discovery rate to date is a function of how much directive work has happened since 08-25,
not of how many wrong closures exist. This is the strongest available argument for rec (3) — it is
precisely the mechanism rec (3) exists to catch — and it is equally an argument that (2)
reopen-on-demand alone is a slow leak rather than a policy.

**Still not acted on. Reopening any of the three is Andrew's.** `IMPORT, DO NOT REOPEN` — a PRD reads
at its path regardless of project status, so no current work is blocked by any of these closures.
