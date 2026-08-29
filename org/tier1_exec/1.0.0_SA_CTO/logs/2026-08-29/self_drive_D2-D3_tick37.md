# /self-drive D2 & D3 — tick 37 (2026-08-29 05:53Z) — state: ARMED

Covers ticks 36-37 (tick 35 logged @b9c338a061, ON origin; tick 36 QUIET — no call, no verdict, no
driver act, floor not reached, so nothing written per the delta rule). Cron bde882a4 (:07/:37; ran
on idle). Paired: `/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA and on a CLOSE: **the
INSURE leg's first scheduled fire PASSED on two independent instruments and TO-A4-AEC is COMPLETE**
— D2 open TOs 23 -> 22.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). **Open TOs 29
(D2 22, D3 7)** — down one on TO-A4-AEC's close. Flags none. Device LAPTOP. Claims scan 342 of 342
JSONs: D2 7 / D3 1, all members, 0 claimed-not-member.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: 15 rows / 0 unconsumed.

## ✅ ADVI_INSURE TO-A4-AEC COMPLETE — the leg fires, serves and verifies

**COO 81009 accepted AC4 and closed the TO @f87c558e2d.** The chain this seat ruled onto the
canonical 49F session route on **Andrew's 17:40Z word** ("this would be a pipeline function, not an
agent … in the same bd api lambda route that is canonical") fired on schedule at **04:35Z**,
unattended, **across a seat death inside its own acceptance window**, and passed on two genuinely
independent instruments:
- **~K (executor, 80965):** all 5 arms, proof instance 5/5 @fe060aa6cf (**ON ORIGIN** — ~K corrected
  its own earlier LOCAL push-state claim).
- **CVO (certifier, 80985 @2c67a5ed4a):** all four pre-registered planes; **completeness
  RECOMPUTED — 50 + 27 = 77 = the VENDOR's own total parsed from the raw bronze bytes**, not the
  Lambda's word. P1's control is the right shape: the prior marker version reads `runner=main`, the
  new one `runner=insurance` — **the field that should change is the field that changed**.
- **~K named which halves are corroboration and which are repetition** rather than banking the
  agreement: CVO's object-VERSION read and CloudWatch metrics sit on planes ~K never touched
  (corroboration); the shared head-object arm is repetition and was NOT banked. **And CVO's read is
  strictly STRONGER on the residual ~K had itself declared uncovered** — ~K's addendum conceded that
  summing rows from object metadata cannot catch a vendor-side undercount, since attested-total is
  stamped by the process that writes the log line (two carriers of one self-report). The vendor's own
  total closes it.
**~K HOLDS IDLE, not released** (COO). Nothing owed by this seat on INSURE.

## THE FINDING WORTH MORE THAN THE PASS: a measured two-seat CORPUS pattern

- **CVO (80985):** P3 scoped to `blackdiamond/49f/` measured **ZERO 38 minutes after a fire that had
  landed all three keys** — the leg writes `blackdiamond/49financial/`. **One step from REFUSED on a
  fire that worked** — and its control (the 00:00Z main fire) **also read zero, sitting in the same
  wrong corpus.**
- **~K (80993):** hit the SAME class in the **ORTHOGONAL coordinate** — right key-prefix, **wrong
  bucket** (`opal-data-bd` for `opal-data-assets`, the reporting-pull's own `MONOLITH_BUCKET`).
  **Two independent, carefully written pre-registrations, both carrying a corpus defect no planned
  control could catch. "Both of our zeros were syntactically perfect."**
- **RULED (my 80996-81003), standing at this seat:** ⛔ **a pre-registered arm fixes the QUESTION and
  the EXPECTED VALUE but CANNOT fix the CORPUS, and a corpus error is invisible to every control
  drawn from that corpus** — so a pre-registration **NAMES ITS CORPUS** (as we now name class,
  tokens and denominator) and **requires at least one arm on a plane that does not share it**; and
  **an S3 arm declares BUCKET and KEY-PREFIX as TWO SEPARATE FIELDS**, since tonight demonstrated
  both halves failing independently and one "path" string hides which half is wrong.
- ⛔ **THE DEEPER HALF IS ~K's: THE CORPUS IS READ FROM THE LIVE PRIMITIVE, NEVER INHERITED FROM A
  DOCUMENT.** CVO was rescued by the Lambda's own LOG; ~K by its own ENV
  (`get-function-configuration` -> `MONOLITH_BUCKET`). **~K refused credit for its escape** — it had
  not yet run a control, and one would have agreed with the wrong bucket. **Virtue saved neither
  seat; going to the primitive did.**
- **AND THE RULE IMMEDIATELY TURNED ON ITS AUTHORS.** COO 81009: the disclosure "closed a gap in MY
  OWN pre-registered table, which now names its CORPUS". CVO 81010 @78bc7e8fcf: every
  (S_L)/(S_R)/(L)/(R) arm read one of two surfaces, **so it named both and ADDED THE CROSS-PLANE ARM
  (the campaign ledger), run NOW at the pre-state as its own control** — which is the clause I
  ruled, exercised before the trigger rather than promised.

## Liveness instruments — corrected twice in one hour (§3.3)

- **COO 80936:** the fused scan's `deaf` bucket is a **MAIL detector, not a liveness detector** —
  natural control pair: two seats dead on the process plane, only the one with unread mail flagged
  (`deaf=1` while TWO were dead). **RULED (my 80951): `deaf=N` is never read, quoted or relayed as a
  death count at these lanes.** The shape is the finding: **a seat that finishes tidily and then
  dies is the least detectable seat on the fabric** — DE~D closed clean, so nobody mails it, so its
  inbox stays clean, so it never trips the bucket.
- **THEN MSTR BOUNDED THE REPLACEMENT AND I AMENDED MY OWN RULING FOUR MINUTES LATER (80973):** the
  send receipt measures **REGISTRATION**, and on a CODEX seat registration and readership are
  DIFFERENT PROCESSES — a dead heartbeat sidecar prints QUEUED while the seat reads normally.
  **`QUEUED` = NOT REGISTERED, full stop; a liveness claim NAMES THE SEAT KIND.** I had ruled that
  `deaf=N` "measures a different subject than its name claims" and in the same message adopted a
  replacement whose subject I had not checked — **a correction is not exempt from the class it
  corrects.**
- **~V and DE~D remain DEAD and deliberately UNSEATED** (all their work is event-gated). **~V's
  deadline stands and is MINE to answer for, because my 80410 created the dependency: seated BEFORE
  the campaign reaches 2026-07-14, with margin to WRITE the emit line, not merely to exist at the
  trigger.** Both deadline-bearing items are now DURABLE at `c05cec1dcb` (MSTR) — the obligation no
  longer dies with a session.
- **Scanner-self artefact at FOUR instances tonight** (a heartbeat read matching its own launching
  shell; a `grep` matching itself in a process count; two earlier): **a probe that can match itself
  has an untested negative control.**

## Campaign (D2 critical path)

**394 of 534 at 05:53Z** (newest 2026-01-29; last write 05:52:51Z), driver **pid 4099101 ALIVE** on
the cadence+pid oracle — the sixth halt (2025-12-30 ARTIFACT-INCOMPLETE 05:17:16Z, re-driven
COMPLETE 05:21:37Z) was handled between ticks. **140 dates remain (~4.3h + halts).** All five
partitions pinned; (S_R) FALSE, trigger NOT SPENT; derive-or-declare event-bound.

## Standing obligations (carried)

- ~V seated before the campaign reaches 2026-07-14 (above); MSTR's gold-layer owner seating before
  the ~23:00Z boot preceding Monday; row 7 (n) sequenced (calendar guard FIRST, it-ran check keyed
  to the SCHEDULE and never to the trigger's own metrics, grace untouched); the bridge residual;
  the driver's retry-on-transient fix; the memory carrier unswept for the set-label class.

## Completion test (§4)

NOT DONE — 1 of 10 projects complete. REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: LOCAL (origin/CLOUD @2c67a5ed4a, ls-remote read 05:53Z;
ticks 33-35 ON origin)

## Compiler Tools

- `python .tools/directives-check.py --json` (open TOs 23 -> 22, the delta) · claims scan 342 JSONs ·
  verdict ledger `wc -l` (15) · campaign ledger tree read + pidfile + `ps` (the cadence+pid oracle) ·
  `git ls-remote` + MERGE_HEAD · `ack_messages` (80903-81010 as received) · `send_message` to_agents
  (80909-80912 [1 QUEUED — the receipt that corroborated ~V's death], 80919-80922, 80951-80954,
  80973-80976, 80996-80999, 81000-81003; 27 of 28 DELIVERED, 1 QUEUED, denominator printed).
