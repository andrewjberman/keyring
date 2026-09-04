# 3.0.0_SA_CVO~Z -- work log 2026-09-04 13:00-15:00Z: the census Andrew asked for, and a constraint struck as unsatisfiable

**Seat:** `3.0.0_SA_CVO~Z`, L8 intake. **Prior log:** `work_0830-0900Z_*`. **Channel:** 150 rows, 41 this
seat's, ids contiguous. **Push state:** origin/SITEZ 360943fabb at 09:4xZ; local commits since then are
LOCAL and the count is the integrator's to read.

## 1. ANDREW-DIRECT, answered with a measurement

**Andrew, verbatim: "How many TOs remain for OPSEC? Why are they not actively proceeding?"**

Measured rather than recalled -- an earlier figure in this seat's own logs read "22 orders, 8 complete" and
was hours stale. `to-check.py --all --project` ignores the project filter and dumps the estate, so the census
was run directly over the tree:

**27 task-order files: 20 COMPLETE, 7 STAGED.** Remaining: S-10, S-10B, S-12, S-13, S-15-19, S-20, S-23.

⭐ **THE ANSWER TO THE SECOND HALF IS THAT THEY ARE NOT STALLED FOR LACK OF EFFORT.** Six of the seven carry
worker rows filed within hours, all from mandated pre-write reads, and **every one is halted at a NAMED
FINDING filed before anything was written.** Per-TO blockers, from the live ARMED set read against each row's
own `disarm_owner`:

| TO | blocked by |
|---|---|
| S-10 / S-10B | Z-S100 all consumers single-slot; **Z-S107 the set is FOUR not two and one is the SIGNER**; Z-S110 third verifier undeployable + no TTL; Z-S123 it is the busiest at 141,685 invocations/14d |
| S-13 | Z-S101 DNS+cert not executable from this fabric (GoDaddy, no ACM cert); Z-S102 no allow-list input; Z-S135 candidates residential/dynamic |
| S-15-19 | Z-S136 terraform is a second WRITER erasing the IP sets; Z-S145/146 fixture and observation share a partition key |
| S-20 | Z-S118 the only window is 97.8% our own probes, residual 15; no firm attribution in the source at all |
| S-23 | Z-S132 blocked BEHIND S-20 -- its criterion iterates a list that cannot be built |
| S-12 | no live row and no visible activity -- genuinely unstarted, dispatch is L6's |

⚠ **A read this seat did NOT over-claim:** the `<assignee>` tag is absent from all seven, and that is NOT
evidence of non-dispatch -- assignment is carried elsewhere in this project, and six have live worker rows.

## 2. C-4 RULED, and it re-shaped the answer within the hour

`1.0.0_SA_CTO~Z` @3c110831a8: **C-4 STANDS; its per-firm clause is STRUCK as UNSATISFIABLE BY CONSTRUCTION**
and replaced with "non-empty, carrying Opal's own known egress addresses (office / VPN), supplied by a named
human."

⭐ **So S-20's blocker changed KIND, not degree**: from "build a census the logs cannot support" to "one line
from a human". S-23 unblocks behind it, and OP-s-14's BLOCK arm with them. **Andrew was upheld on the merits
too** -- at the composed bar of three separate WAF rate trips (~300+ auth requests across three distinct
5-minute windows) a partner tripping the sentinel is not realistic on any evidence held.

**The ruling nearly went wrong twice and both catches are the CTO's own:** the relayed arithmetic measured a
WAF RATE RULE while C-4 governs the SENTINEL's block rows (right figure, wrong control); and its own first
reading took `SENTINEL_TRIP_THRESHOLD=3` as three failed logins when it counts three rate TRIPS (right
control, wrong unit) -- which "would have hardened the constraint on a misreading". Its first metric query
also returned empty for every series INCLUDING its control -- the absent Region dimension again, **third
independent instance tonight** -- and was discarded rather than believed.

## 3. /open-calls across the fabric: ZERO from this seat

`0.0.0_AB_MSTR~Z` consolidating for Andrew at the terminal. **This seat holds ZERO open sovereign calls**,
stated in one line as asked, with where I looked so the zero is checkable: the resolved-live ARMED set read
against each row's `disarm_owner`; this seat's own outstanding work; and today's four rulings used as a
filter.

⛔ **The one thing this seat owns is NOT a call:** the four closure rows are blocked on a gate version
carrying an already-RULED exemption that has not reached this checkout (`c3ef3a2530`, 0 occurrences of
`REMEDIATED`). **Mechanical propagation, nothing for a sovereign to answer.**

**Sent as a COVERAGE NOTE, explicitly not as cards:** four genuine Andrew-inputs are outstanding and every one
names `2.0.0_SA_COO~Z` as routing owner, so all four are that seat's to carry -- egress addresses, the alarm
recipient, the registrar decision, and go/no-go on the `opal-users` delete. **Verified still open against
today's five approved cards, which were different subjects entirely.** The note exists so the frame is checked
against a known count rather than trusted, which is the same reason a partition is reconciled to its
denominator.

## 4. Z-S150 -- corroboration of the right kind

`4.0.0_SA_CRO~Z` independently re-derived the `attempted_at` finding -- seven predicate sites plus the
renderer at `:211`, eight edits not one -- **while tearing down comp-read for a CRO brief, not while working
this project.** Different seat, different instrument, different reason for looking. **That is triangulation
rather than repetition**, which is the distinction this seat's standing caution exists to draw.

⭐ **Two practices in its RAVC close worth keeping:** it ran the mandated pre-write checks even though the
hazard they guarded had cleared overnight, and reported so -- *"a check that passes is only evidence if it was
actually run"*; and it put its OWN miscount in the row rather than quietly correcting it, naming the
mechanism (a bracket-access probe, never a predicate probe, whose denominator certified the SWEEP and was
attached to a different question). **Fourth instance tonight of a denominator certifying the sweep rather than
the pattern.**

## 5. State

**150 rows, contiguous, 41 this seat's.** Nothing waiting on this seat. **Blocked item unchanged.** L9 cannot
open until the 7 remaining task orders complete, and 4 of the 5 real blockers are one-line human inputs now
sitting in a consolidated frame in front of Andrew.
