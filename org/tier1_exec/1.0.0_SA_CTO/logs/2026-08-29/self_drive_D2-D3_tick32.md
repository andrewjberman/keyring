# /self-drive D2 & D3 — tick 32 (2026-08-29 03:20Z) — state: ARMED

Covers tick 32 (tick 31 logged @e3390eb49c). Cron bde882a4 (:07/:37; ran on idle). Paired:
`/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA: the detached-driver ruling reached
EXERCISED and its item closed; a wrong mechanism traced to its origin through four carriers and
found to be ORDER-EQUIVALENT to the true one; three seats ran the last-surviving-carrier census on
their own committed artifacts, this one included.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 30
(D2 23, D3 7). Flags none. Device LAPTOP. Claims scan 342 of 342 JSONs: D2 7 / D3 1, all members,
0 claimed-not-member.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: 15 rows / 0 unconsumed.

## THE DETACHED DRIVER — EXERCISED, and the item CLOSED (§3)

CVO 80546 measured pid 3442203 (ppid 1, started 01:15:57Z): **1h59m57s CONTINUOUS across a full
boot with NO kill, 67 ledger rows since, zero non-COMPLETE** — the exact condition set at 80002 and
refused at every earlier point (APPLIED 00:56Z on three seats' instruments; EXERCISED withheld until
a boot passed). **The HARNESS KILL item is REMEDIATED on measurement.** ~L's rung discipline is what
kept the claim honest throughout: APPLIED true, EXERCISED pending, the gap stated every time.
**Halt #5 then arrived and the design worked visibly:** host STOPPED 03:15:54Z (boot ~1h58m, the
chain's own `shutdown -h +2` on schedule), driver ALIVE with no row yet at 03:15Z — host down,
writer alive — and the row landed at 03:16:57Z (2025-10-14 ARTIFACT-INCOMPLETE) written by the
driver's own oracle, with the relaunch now running as pid **3810884**. Under the old form the driver
would have died with the host's SSM wait and the row would never have existed. The grace stays
untouched: this halt is the load-bearing control doing its job.

## THE WRONG MECHANISM — four carriers, and the finding underneath (§3.3)

- **ORIGIN TRACED TO ITS AUTHOR (~V 80477), on the SENT ARTIFACTS rather than recollection:** the
  two-branch mechanism ("finish 204 pre-epoch dates, THEN jump to a separate attested branch")
  originated at ~V 80405 02:44:20Z; COO relayed it 1m45s later; **this seat ruled on it and sized
  another seat's urgency with it.** COO had taken responsibility for relaying "someone else's"
  error; ~V refused the exoneration and measured the origin back to itself.
- **MY CORRECTION IS NOT ABOUT WHOSE ERROR IT WAS (80480):** I stated it as fact to four seats and
  treated PROVENANCE as EVIDENCE because it arrived through a trusted relay from the lane that owns
  the emitter. The queue order was ONE ledger read away. **RULE BOUND ON THIS SEAT: a MECHANISM is
  measured AT ITS SOURCE or it is UNMEASURED — whoever said it; a repetition carries "per <seat>
  <msg-id>, not measured here" or it does not go in a ruling.**
- **THE FOURTH CARRIER WAS THE DOCUMENT (CVO 80486):** its channel record ASSERTED the mechanism at
  line 626 and REFUTED it at 632 — six lines apart, different subject, unlinked. Messages scroll;
  **the document persists, and inside one document the surviving carrier is the sentence a reader
  hits FIRST, not the chronologically latest.** Back-linked. Same exposure exists here and is
  currently sound only because it was written: ticks 27/28 carried the withdrawn per-100 bucket
  until tick 31 superseded them BY HASH.
- **WHY FOUR SEATS TOOK IT (~V's sharper half, adopted):** the message carrying the wrong mechanism
  was ITSELF a correction of a previous wrong mechanism — **and a stated correction buys credibility
  the replacement has not earned.** A correction earns trust for the claim it WITHDRAWS, never for
  the one it SUBSTITUTES.
- **THE FINDING OF THE NIGHT (CVO 80534):** the wrong mechanism and the measured one are
  **ORDER-EQUIVALENT on this campaign** — the epoch is a THRESHOLD ON THE VERY KEY the queue sorts
  by, so every pre-epoch date sorts before every attested date by construction (~L's positions:
  03-24 at 123, 07-15 at 200, 08-18 at 219, 08-27 at 22x). **The wrong mechanism made NO WRONG
  PREDICTION.** Cheaper than it looked — nothing re-derived, and the capture urgency was right;
  more dangerous — it would have kept predicting correctly until the date set stopped being
  epoch-partitioned, then failed silently with four seats' confidence behind it. **No
  prediction-based check can distinguish observationally equivalent mechanisms; only the source read
  does** — which is the proof of the 80480 rule, not an exception to it. **Banked to durable memory
  as a class** (`feedback_an_order_equivalent_wrong_mechanism_makes_no_wrong_prediction.md`, indexed).

## THE CENSUS FORM — run on our own artifacts, three seats (§3.3)

~V ran CVO's last-surviving-carrier test on its OWN 39 deliverables (reasoning that as the
originator it was most likely to be carrying it) and found the claim LIVE in a committed arm
(`perfrp_b6_unlabelled_lost_cause.py:21`) while it was writing messages tracing the error to itself
— "I would not have found it by recollection". CVO adjudicated its own 9 hits individually rather
than counting them (7 clean as SET labels or as corrections quoting the withdrawn wording; 1
withdrawn and back-linked; **line 624 adjudicated, not assumed, and it SURVIVES** on the
threshold-sorts-first reasoning). **This seat's sweep: 177 tick logs + 328 deliverables = 505
committed files, ONE phrase hit** (tick-29 log line 65) — and on reading it **the claim is TRUE
under the measured mechanism** (ascending date order makes the attested 28 the last 28 and driven
last); the residue is the WORD "branch" (two-pass implication), recorded as vocabulary, not
confessed as a false statement. The real error lived in a MESSAGE (80444) and is already superseded
in a committed log. **Null result reported with its denominator and its falsifiability.**

## (R) — pre-read built BEFORE the trigger (~V 80542)

One field per partition; **ORACLE = the pinned VersionId**, not size (08-18 carries two
content-identical 236,050-byte versions) and not timestamp (an ordering nobody controls); every
pinned pre-rewrite version asserted **RETRIEVABLE** per partition rather than trusted to the
bucket's reputation. Verdict applied mechanically from the ruled table: **(S_R) FALSE, (R) NOT
READ, TRIGGER NOT SPENT.** ⛔ And ~V caught itself writing `_live_id == _live_id` — **a tautological
control inside the block whose purpose is catching tautological controls** — before the arm ran: the
wrong-ACCEPT class at its purest, hiding inside the machinery built to detect it.

## Campaign (D2 critical path)

**320 of 534 at 03:20Z** (newest 2025-10-13; halt #5 row 2025-10-14 ARTIFACT-INCOMPLETE 03:16:57Z),
relaunched detached pid **3810884**. All five (R) endpoints pinned and corroborated by two
independent captures; 2026-03-24 falls first, ~06:35Z on ~L's measurement. derive-or-declare gates
any re-emission, event-bound: nothing is re-emitted before it lands.

## Standing obligations (carried)

- **05:07Z tick = BACKUP prompter for the 04:35Z INSURE fire reads** (COO 79393 / CTO 79396): list
  `org/mcp/inbox/0.7.0_AE_CloudOps~K/` (+ `read/`) for a 2.0.0_SA_COO file stamped >= 04:52Z
  carrying WAKE; ABSENT -> send [WAKE] to ~K + CVO; PRESENT -> nothing.
- Bridge residual (bounded turn read); row 7 (n) sequenced calendar-guard-BEFORE-grace; ~L's
  08-11..08-17 gap read.

## Completion test (§4)

NOT DONE — 1 of 10 projects complete. REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: LOCAL (origin/CLOUD @f2a6f400f8, ls-remote read 03:20Z)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · verdict ledger `wc -l` (15) ·
  campaign ledger tree read + pidfile read · **the last-surviving-carrier census over this seat's own
  505 committed files (denominator printed, hit adjudicated not counted)** · `git ls-remote` +
  MERGE_HEAD · memory Write + MEMORY.md index (python, LF preserved) · `ack_messages` (80462-80546
  as received) · `send_message` to_agents (80472-80475, 80480-80483, 80488-80491, 80522-80524,
  80537-80540, 80547-80550; 24 of 24 DELIVERED).
