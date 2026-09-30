# Never-widen sign-off packet -- WINDOW 26: Andrew's three-variant automated-submission proof, one principal that OUTLIVES its jobs

Author `2.0.0_SA_COO~Y`, 2026-09-30 ~05:4xZ. **Halves owed: `1.0.0_SA_CTO` and `4.0.0_SA_CRO`** (or a live
`2.0.0_SA_COO` not holding this round, per the L4-R rule as the prior windows applied it).

## Why this window exists, verbatim

**Andrew-direct 2026-09-30 ~04:4xZ, at this terminal:** *"What is preventing us from getting the capture here? Is it
actually an auth failure, or are we sending the shape to Ycharts incorrectly? I think we need to do a test to actually
prove an automated ycharts submission for each of the three variants right now ad hoc and see if we even get a
generated export."*

And **Andrew-direct 2026-09-30 ~04:3xZ** (record
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260930_043xZ_YCHARTS_OWNER_IS_COO_Y.md` @fe6326f6b0):
*"the owner of YCharts is COO~Y as it has always been"* -- which is why this seat authors the packet.

**The first two of his three questions are already answered and this window does not re-ask them:**

- **NOT the shape.** `host_capture.run_capture()` must return a session BEFORE `recipe.generation_body()` is built.
  W25's job died with its body never sent, so the three-variant shape **has never reached the vendor by this path at
  all.** That is what this window is for.
- **NOT the credential.** Row `IRPT_BCKEND-S230`: one capture on the canonical wrapper at 04:58:12Z returned **rc=0**,
  receipt `{ok: true, task: probe, authenticated: true}`, first attempt, `otp_branch=ABSENT`.
- **What W25 actually hit, and this packet FIXES rather than repeats:** row `IRPT_BCKEND-S231`. The resident refused
  the retained job `class=CurrentAuthorityRefused code=ACTOR_NOT_FOUND` because the window principal had been deleted
  while the job was still queued (`current_authority.py:86` resolves the accepted record's `owner.principal_id`).
  **Principal lifetime was window-scoped; job lifetime is queue-scoped.** See W26-3.

## W26-1 -- the pins, re-read at create

Read again at create and recorded in the ledger, never inherited from this file:

| pin | value at authoring | instrument |
|---|---|---|
| resident root | `/opt/irpt-resident/fe64236bbb-st5` | the unit's `ExecStart` |
| resident worker sha256 | `8d1f5431276e406c...`, **equal to CLOUD HEAD** | `sha256sum` on the host + `git show HEAD:` |
| resident unit | `active`, pid 313525 since 05:13:31Z | `systemctl is-active` |
| `irpt-ycharts-generate` | `inrij6hL...` / 2026-09-29T15:00:32Z | `get-function-configuration` |
| `irpt-generation` | re-read at create; the SOLO GATE is restated in W26-5 -- queue depth alone cannot express it | `get-queue-attributes` + an `irpt-jobs` scan |
| `irpt-generation-dlq` | **1** -- the baseline; ANY growth is a BLOCKING row the same tick | `get-queue-attributes` |
| the stranded job | `REQ-86f1ce7062356bc5c109ce12`, `SUBMITTING`, unrunnable (S231) | consistent `irpt-jobs` read |

## W26-2 -- the three bodies, one per variant, SERIALIZED

The variants are the template's own, and the counts are `templates.json`'s `comparison_securities` bounds -- not a
choice made here: OVERVIEW `{min 0, max 0}`, COMPARISON `{min 1, max 1}`, MULTI `{min 2, max 5}`.

| # | variant | body | firm | comparisons |
|---|---|---|---|---|
| Y1 | **OVERVIEW** | the W15 CSV (`aapl-vnq-12.03.csv`) | cottonwood | none |
| Y2 | **COMPARISON** | the same CSV | cottonwood | `opal_long_term` (exactly 1) |
| Y3 | **MULTI** | the same CSV | cottonwood | `opal_short_term,opal_intermediate_term` (2) |

- **One login. Three K4/K5 pairs. No retry of any body.**
- **SERIALIZED ON THE `irpt-jobs` TERMINAL**, per `1.0.0_SA_CTO`'s W24 condition 1 -- not on the NORMALIZATION row.
  `job_terminal_wait.py` exists for this and `live_chain.py` returns at K5 acceptance, which is not an outcome.
  **Rationale is measured, not stylistic:** row `S206` established that `PROVIDER_READ_UNAVAILABLE` tracks whether
  other work is in flight, so two bodies in flight reproduce concurrency instead of measuring the variant.
- **The SOLO GATE is W26-5's, not a queue depth.** Read it immediately before each K5.
- **The same CSV for all three on purpose:** the variable under test is the VARIANT, and holding the portfolio fixed
  is what makes a difference between Y1, Y2 and Y3 attributable to the comparison shape.

**What each arm must produce to count as proof, in Andrew's own terms (*"see if we even get a generated export"*):**
a terminal `irpt-jobs` state by name, and for a READY job the `ORIGINAL_VENDOR_PDF` object plus the certified report.
A vendor-side refusal is also a result and is recorded as one -- it would be the FIRST measurement of this body shape
against the live vendor either way.

## W26-3 -- the interval, the principal, and THE ONE THING THIS PACKET CHANGES

- Opens once both halves are at HEAD. **Cap 150 minutes**, and the arithmetic is stated rather than rounded to a
  habit: W22 measured its slowest job at ~31.5 min; three serialized arms at ~32 plus login, three K4s and the
  terminal waits is ~110, and 150 leaves margin without licensing a fourth arm.
- K1 + K1-CRED created at open with `walk_principal.py --kind=uiwalk create <epoch>` (the v3 shape). The password is
  written only to the SecureString and never printed.
- **CREDOFF BEFORE THE VENDOR CALL, AND BY A SECOND SEAT.** `~Y` logs in with `WALK_PW_RETAINED` unset; the moment
  its login line prints, **`0.0.0_AB_MSTR`** runs `walk_principal.py --kind=uiwalk credoff <epoch>` and reads back
  `ParameterNotFound`; `live_chain.py` polls for that before K4. **Naming the change:** prior windows had
  `2.0.0_SA_COO~P` do this, and `~P` now takes no YCharts work (Andrew-direct above). If `~Y` did both halves the
  two-party property would be lost -- the walker could re-login -- so it moves to the integrator rather than
  collapsing onto the walker.
- **K1 IS DELETED ONLY WHEN ALL THREE JOBS ARE TERMINAL -- not at window close.** This is S231's remedy (a), folded
  into the test instead of being cut as a separate cell afterwards.
  - If the cap arrives with a job non-terminal, **the principal is RETAINED past the cap** and the window records
    CAP-TRUNCATED with the job id. The credential is already gone, so a retained K1 cannot log in -- it only lets the
    resident RESOLVE the job's recorded owner.
  - **Deleting K1 over a live job is what made `REQ-86f1ce70` permanently unrunnable**, and this clause exists so the
    window cannot repeat it.
  - A retained K1 is deleted in a later act, once its jobs are terminal, under its own one-line ledger note.
- **Before and after:** the users census (count + digest), `walk_window_census.py`, and the DLQ count. DLQ growth over
  the baseline of 1 is a BLOCKING row the same tick (the CTO's W22 condition).

## W26-4 -- blast radius, both branches

- Every arm is a write the principal owns (its portfolio, its three REQ rows, its reports) plus reads. **Nothing
  served for any other user moves.** No code change, no IAM change, no schedule change, no deploy.
- **No resident restart is in this window.** The resident is already `active` on st5 under a CLOSED ledger
  (`irpt-resident-restart-3variant-20260930`, 3/3 legs). Rolling back to `fe64236bbb-st4` stays its own act under that
  ledger's rollback root.
- **If an arm FAILS:** its REQ stays as evidence, a BLOCKING row lands the same tick, no retry is fired, and the
  **remaining arms still run** -- a vendor refusal on COMPARISON is not a reason to leave MULTI unmeasured, and three
  independent results are the point.
- **If the resident misbehaves** (traceback loop, or a hang past the cap): the window closes, the principal is
  retained per W26-3, and nothing is deployed inside the window.
- **REQ-86f1ce70 is NOT revived and NOT deleted in this window.** It stays as the evidence for S231. Its refusal costs
  no vendor call (`current_authority` refuses before any capture), so it can keep cycling harmlessly.
- **Reachable:** one login, one vendor session, three jobs for the cottonwood firm under one principal.

## What the halves sign against

This file's committed blob; Andrew's two directs quoted above; rows `S230` (the credential authenticates) and `S231`
(the deleted-principal cause) at their committed ids; W25's text
(`IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W25_20260930.md`) with its conditions as narrowed here; the pins in
W26-1; the three bodies, their comparison counts and the serialization in W26-2; and the interval, the second-seat
credoff and **the principal-outlives-its-jobs clause** in W26-3.

**What this packet does NOT ask for:** a fourth arm, a second login, a retry of any body, a resident restart, any code
or IAM change, or a new vendor account. If a half wants the window narrower, the arms are independent and dropping Y3
costs the MULTI measurement only.

## W26-5 (amendment 1, 2026-09-30 ~05:5xZ) -- THE SOLO GATE, RESTATED, because as written it could never pass

`4.0.0_SA_CRO` signed on blob `0b209ba626` and its condition 1 named a defect in my own packet: `irpt-generation`
reads **0 visible / 1 in flight**, so *"must be 0/0 before each K5"* **cannot pass**. The CRO is right, and the fix is
not to relax the gate but to measure what the gate MEANS.

**Queue depth was always a proxy, and a permanently stranded message poisons it forever.** What `S206` actually
requires is that **no OTHER job is working the vendor** while an arm runs. So:

> **SOLO GATE.** Immediately before each K5, scan `irpt-jobs` for any job in `QUEUED`, `CLAIMED`, `SUBMITTING` or
> `SUBMITTED` and subtract (a) this window's own arms and (b) the two KNOWN-STRANDED jobs named below. **The remainder
> must be empty.** The queue's in-flight count is printed beside it as context, never as the gate.

**The two known-stranded jobs, measured at 05:5xZ, both `SUBMITTING`, both unable to reach the vendor:**

| job | window | why it can never run |
|---|---|---|
| `REQ-86f1ce7062356bc5c109ce12` | W25, tonight | `ACTOR_NOT_FOUND` -- its principal was deleted at 03:45:34Z (S231) |
| `REQ-3a1b73a8dead02a17a09043b` | **W6, 2026-09-27** | **the job S151 names**: its one-use session-refresh intent was spent and never replaced |

**This strengthens `S231` and closes `S151`'s loop.** S231 recorded *"NOT MEASURED ... how many earlier jobs died this
way"* and reasoned tonight was the first. **Measured now: at least TWO, three days apart** -- and the earlier one is
S151's own job, which therefore never completed and never can. The window-scoped-principal defect is not a one-off
tonight; it has been silently stranding jobs since W6.

**Neither stranded job is revived or deleted by this window.** Both refuse before any vendor call
(`current_authority` for one, a spent intent for the other), so they cost nothing and stay as the evidence for S231
and S151.

**BLOB CHANGE, stated rather than hidden:** this amendment changes the file, so the halves signed against
`0b209ba626` no longer bind the current bytes. **The change is a NARROWING** -- a stricter, measurable gate plus two
named exclusions -- and it adds no arm, no login, no retry and no new reach. Both halves are asked to re-affirm on the
new blob; the CTO's eight conditions and the CRO's six are untouched in substance, and the CRO's condition 1 is what
this amendment answers.

## W26-6 (amendment 2) -- CTO condition 9: the non-terminal enumeration, DERIVED and printed

`1.0.0_SA_CTO` 103186 re-affirmed on blob `1c88bb49` and added condition 9: derive the non-terminal job states from
the state machine's source and print the enumeration beside the gate. **Doing so found my own filter wrong twice.**

**THE AUTHORITY is `ycharts/generate/durable_job.py:16`**, an 11-member frozenset:

`RECEIVED, CLAIMED, SUBMITTING, SUBMITTED, UNCERTAIN, DOWNLOADING, EXTRACTING, CERTIFYING, READY, FAILED, ATTENTION`

`job.py:64` carries a narrower 8-member tuple (no `RECEIVED`, `EXTRACTING`, `CERTIFYING`) and calls itself *"A CLOSED
set: a state a reader has never seen is a state nobody wrote a recovery for."* **The gate uses the durable 11**, since
a job row is what the scan reads.

**BY SUBTRACTION from those 11, terminal first:** `READY`, `FAILED`, `ATTENTION` are terminal -> **the other 8 BLOCK**:

`RECEIVED, CLAIMED, SUBMITTING, SUBMITTED, DOWNLOADING, EXTRACTING, CERTIFYING, UNCERTAIN`

`UNCERTAIN` blocks deliberately, fail-closed: `owned_status.PHASES` maps it to
`ANALYSIS_UNCERTAIN_REQUIRES_RECONCILIATION`, so whether that job could still touch the vendor is unknown, and unknown
is not permission.

**MY FILTER WAS WRONG TWICE, and this is why the condition exists.** W26-5's own text listed four states, and the scan
I ran at 05:5xZ used `QUEUED, CLAIMED, SUBMITTING, SUBMITTED`. **`QUEUED` is not a durable state at all** -- it is a
PUBLIC label from `owned_status.PHASES` (`RECEIVED` -> `QUEUED`) -- and the filter missed four real non-terminal states
plus `UNCERTAIN`. The earlier count happened to be right; it was not right *by measurement*.

**RE-MEASURED with the derived 8, denominator printed: 17 of 17 rows scanned, 2 matched** -- exactly
`REQ-3a1b73a8dead02a17a09043b` and `REQ-86f1ce7062356bc5c109ce12`, both `SUBMITTING`, both excluded by exact id.
**SOLO GATE: PASSES.**

`RESOLVING`, which 103186 asked about, is **not** a job state: it is an UPLOAD state on the `irpt-requests`
`NORMALIZATION#` row. It has no place in this scan, and saying so is part of answering the condition.

**Standing to re-read:** this enumeration is derived, not remembered, and the scan is re-run immediately before each
K5 -- a job entering any of the 8 between arms blocks the next arm.
