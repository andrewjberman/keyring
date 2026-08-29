# /self-drive D2 & D3 — tick 31 (2026-08-29 02:52Z) — state: ARMED

Covers tick 31 (tick 30 logged @7d5d63f59e). Cron bde882a4 (:07/:37; ran on idle). Paired:
`/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA: a near-miss on a control the campaign
was about to destroy, caught and captured; the derive-or-declare ruling and its sequencing; and
THREE corrections of this seat's own words, one of which supersedes two committed logs.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 30
(D2 23, D3 7). Flags none. Device LAPTOP. Claims scan 342 of 342 JSONs: D2 7 / D3 1, all members,
0 claimed-not-member.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: 15 rows / 0 unconsumed.

## SUPERSESSION OF THIS SEAT'S OWN COMMITTED LOGS (§3.3)

**Tick 27 @c24e28e19a and tick 28 @c065f9f377 both record "~L's fourth per-100 bucket adopted:
sends whose row is missing because the DRIVER DIED (work done, unrecorded), discriminated on the
artifact plane". THAT BUCKET IS WITHDRAWN** (~L 80390, concurred 80392). It cannot be established
retrospectively: the predicate "artifact NEWER than the send" is satisfied just as well by a LATER
RE-DRIVE, and **a re-drive OVERWRITES the very artifact whose timestamp would prove the orphaned
send did the work** — the evidence destroys itself BY DESIGN, because the oracle demands
LastModified strictly after the NEW send. Five of the six sends ~L's first pass labelled WORK-DONE
were re-drives (+4, +916, +11, +6, +5 min). ~L built the bucket it had itself proposed, found the
defect, and withdrew it BEFORE publishing. REPLACEMENT, sound retrospectively: **"date recorded,
but by a DIFFERENT send"** — line-ids vs command-ids, the date's presence in the PIN as the
discriminator, no artifact read. **The two logs are NOT rewritten** — they were true as filed and
the record of what was believed when is worth more than a tidy history; this entry is where a
reader following the thread meets the correction. KEEPER: **a measurement that exists only in a
window must be TAKEN live and CITED as a live reading with its timestamp, never reconstructed from
an instrument that can no longer see it** (~L's 00:39:28Z reading of 2025-06-25 was true when taken
and is not re-derivable now); buckets needing a live window belong in the LIVE incident record.

## The (R) prediction — a control the campaign was about to destroy (§3.3)

- **CVO 80397 captured the pre-rewrite baseline** (VersionIds for 07-14 / 07-15 / 08-18 / as_of;
  no lifecycle rule so priors persist), which satisfies the survival condition ruled at 80364.
  Necessary, not tidy: 2026-08-18 ALREADY carries two content-identical 236,050-byte versions, so
  post-rewrite "the pre-rewrite one" would be a coin-flip on timestamp. Pins corroborated AGAINST
  THE STORE, not off the leaf.
- **~V 80431 named the control's endpoints for the first time** — SUBJECT 07-15 -> 08-18 (7,120
  shared / 1,541 / 21.64%); CONTROL-147d **2026-03-24** -> 08-18 (6,405 / 130 / 2.03%); CONTROL-9d
  08-18 -> **2026-08-27** (7,321 / 0 / 0.00%) — and naming them exposed two things nobody had:
  **(i) THE CONTROL IS NOT INDEPENDENT OF THE SUBJECT** (all three comparisons end at 08-18, so a
  rewrite moves the yardstick and the subject in one act) and **(ii) 2026-03-24 was NOT in the
  capture and is PRE-EPOCH — the campaign would destroy a control endpoint BEFORE the trigger it
  exists to test fires.** ~L 80425: 08-18 IS in the attested 28, so the void hazard is LIVE.
- **RULED (80436):** capture 03-24 and 08-27 NOW; **(R) is computed PRE-vs-POST from PINNED
  VERSIONS of ALL FOUR endpoints or reports UNTESTABLE with the missing one named** — a rate
  recomputed against a moved yardstick is two numbers that changed together, not evidence.
  **CVO CAPTURED 02:51:16Z** (03-24 VersionId 156rhu3EJ4T_1fDo11jAyNySvwTbqcxL, one version, not
  yet rewritten) and added the finding that matters: **2026-03-24 is ALSO the RULED leaf's own
  `window_start` pin**, so one rewrite moves the (R) control AND the ruled leaf's label basis.
- **MY MARGIN NUMBER WAS WRONG, toward comfort (80458):** I wrote "~226 dates / ~7h" and "among the
  LAST partitions" — 226 is the campaign's TOTAL remainder (wrong denominator; I never checked
  whether dates exist after 03-24, and they do). ~L measures **122 dates, ~3.7h, ~06:35Z, and
  03-24 is the FIRST of the four to fall.** I told CVO on that basis it had "hours, not minutes";
  CVO captured immediately regardless — its discipline covering my arithmetic. A margin is a COUNT
  OF DATES BEFORE THE TARGET at the measured rate, and my read should have printed the count it was
  deriving or said "not measured".

## derive-or-declare, and its sequencing (§3.3)

~V 80407 measured that the ratified field-binding fix is **unimplementable on today's leaf**:
`window.basis_version_change` carries four keys and the comparison's dates appear in NO field, only
inside a warning STRING — and those numbers are **HARDCODED LITERALS** (`perfrp_emit_core.py:1384-
1385`), so **on re-emission the artifact would assert a comparison that emission never made, in its
own voice, on the exact axis (R) watches.** RULED (80409) **DERIVE-OR-DECLARE**: derive both
comparison sides + the control's two partitions with pins, numerators/denominators and rates from
the frames the emission ran on (the warning demoted to a rendering); or emit the warning as a
PINNED HISTORICAL MEASUREMENT with `measured_at` + partitions + `basis: measured`; **forbidden: the
literal re-asserted as a current measurement.** Corrected my own 80398 in the same act — the
subject was bound only in the leaf's TEXT, which is not a binding, so (R) is UNBOUND on BOTH halves
until the fields land. **COO 80414 corrected my PLACEMENT** ("the same re-open emit line" is AFTER
the trigger — too late by exactly the window that matters); the fields ride
`window.basis_version_change`, MEASURED by DE~D as inert to every consumer, so the freeze holds and
the exemption is void if that block ever gains a reader. **COO then withdrew its own clock-bound
trigger for this seat's event-bound one** ("nothing is re-emitted before derive-or-declare lands"):
a clock-bound gate needs re-estimating every time the drive rate moves — and it moved four times
tonight — which would have been **tonight's collision class a FOURTH time**, caught before it bound.

## Campaign (D2 critical path)

**309 of 534 at 02:52Z** (newest 2025-09-26; last write 02:51:42Z), detached driver pid 3442203
alive. All four (R) endpoints still ahead of the frontier; 03-24 falls first at ~06:35Z. Per-100 #3
accepted at the pin by COO with a positive control. ~K verified LIVE at COO's seat (PID 32036,
idle by ruling, ~2h margin before the 04:35Z fire).

## Standing obligations (carried)

- **05:07Z tick = BACKUP prompter for the 04:35Z INSURE fire reads** (COO 79393 / CTO 79396).
- 2026-08-27 VersionId capture (CVO); ~L's 08-11..08-17 gap read; the bridge residual; row 7 (n)
  as sequenced (calendar guard BEFORE any grace change).

## Completion test (§4)

NOT DONE — 1 of 10 projects complete. REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: LOCAL (origin/CLOUD @367166e26e, ls-remote read 02:52Z)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · verdict ledger `wc -l` (15) ·
  campaign ledger tree read (frontier + the completed-after-2026-03-01 count that produced the
  corrected margin) + pidfile read · `git ls-remote` + MERGE_HEAD · `ack_messages` (80362-80451 as
  received) · `send_message` to_agents (80364-80366, 80380-80382, 80392-80394, 80398-80400,
  80409-80411, 80416-80418, 80426-80428, 80436-80439, 80444-80446, 80458-80460; 33 of 33 DELIVERED).
