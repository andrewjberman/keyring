# /self-drive D2 & D3 — tick 48 (2026-08-29 11:21Z) — state: ARMED

Covers tick 48 (tick 47 logged @81e4a1320d, marked in place @1a738b29d4; both LOCAL). Cron bde882a4
(:07/:37; ran on idle). Paired: `/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA: **an
arch-gate ruling of mine marked CONTINGENT and then discharged**, and **a live production defect on
the served plane**.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 29
(D2 22, D3 7). Flags none. Device LAPTOP. Claims scan **342 of 342 JSONs**: D2 7 / D3 1, all
members, **0 claimed-not-member**. No MERGE_HEAD. Inbox 0 unread. **Register unmoved.**

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: **15 rows / 0 unconsumed**
(CRLF 15 of 15).

## ⛔ MY ARMING RULING: MARKED CONTINGENT, THEN DISCHARGED

`3.0.0_SA_CVO`'s AC6 read — **whole-document key walk over all 17 files, explicitly NOT a scoped
accessor** (*"I made that mistake an hour ago and am not repeating it"*) — found **`contract_version`
17 of 17 and `window.upstream_pins` present, `campaign_ledger_commit` and `dates_complete_of_534`
ABSENT on 17 of 17.** ⛔ **A scoped accessor would have found the first and stopped; the absences are
visible only to a walk that does not know what it is looking for.**

⛔ **THAT EXPOSED A LAYER UNDER MY OWN RULING.** I ruled **which TOs the emission is IN-SUBJECT for**;
AC6 asks **whether it qualifies as "the arming emission" at all** — and my ruling **presupposed** the
answer. ✅ **So I marked "T1/T2 ARMED" CONTINGENT at 11:18Z, BEFORE the adjudication** — *a
contingency declared only once it resolves favourably is not a contingency.*

✅ **DISCHARGED at 11:20Z on `2.0.0_SA_COO`'s split: AC6 carries TWO requirements in ONE ROW** —
**AC6-ARMING (timing) SATISFIED and measured** (final row 09:59:16Z, pin @`9dd522c50d` 10:10:47Z,
leaves 10:31:37Z / 10:35:27Z) and **AC6-MANIFEST NOT satisfied, 2 of 4.** **Arming is the limb my
ruling rested on, so "T1/T2 ARMED" now stands UNCONDITIONALLY; the absent fields are a DELIVERABLE
DEFECT, not an arming disqualifier. P1/P2/P3 remain unarmed on SUBJECT grounds, untouched.**

⛔ **AND THE PATTERN IS THE KEEPER: `2.0.0_SA_COO` made the SAME Rule 24 fault TWICE, IN TWO
ARTIFACTS, INSIDE ONE HOUR** — the BDPARITY predicate (one event over a TO set spanning two
subjects) and AC6 (one row carrying arming AND self-description). **Two seats making one error each
is an accident; one author making the same structural error twice in an hour is a HABIT** — visible
only because it diagnosed the second itself, in the first's terms. **Form: when you write a
criterion, ask whether ITS SUBJECT IS ONE THING. A row that can be half-satisfied is two rows, and
whoever must score it discovers that at the worst moment.**

## ⛔ THE LIVE DEFECT — a gate whose skip exit is unreachable FOREVER

`0.7.0_AE_CloudOps` (gold-layer owner, seated 10:22:14Z) measured, and `2.0.0_SA_COO` confirmed the
mechanism: **`check_freshness()` takes `silver_latest` as the RAW MAX PARTITION** — live that is
**2026-08-29, a Saturday** — **and gates on `silver_latest > gold_as_of`.** ⛔ **So once gold reaches
its legitimate ceiling of 08-28, the gate reads 08-29 > 08-28 and PROCEEDS, FOREVER. The "no new
data, skip" exit is not merely unexercised — it is UNREACHABLE**, because **a raw partition maximum
is standing in for a trading-day frontier.** ⛔ **NEVER#4 living inside a GATE rather than inside a
stale-data claim.** **Owner's item; nothing in my lane blocks it; I proposed no fix.**

**And BD is serving 08-27 against a frontier of 08-28** — the defect that replaced the false one.

## The it-ran ruling completed — mine was only ever half of one

⛔ **I ruled *"the it-ran check must key on the SCHEDULE, never on the trigger's own metrics"* and
named NOTHING to key on instead.** `0.7.0_AE_CloudOps` measured the positive half:
**`bd-gold-trigger/lambda_function.py:67-80` writes a PENDING MARKER on `state == 'running'`** — an
oracle that existed in that Lambda the whole time and my ruling never sent anyone to find.
⛔ **A PROHIBITION WITHOUT A REPLACEMENT IS OBEYED UNTIL SOMEONE ACTUALLY NEEDS AN ORACLE, AND THEN
IT IS QUIETLY IGNORED** — whoever needs one uses what is at hand, and the metrics are always at hand.
**"Never use X" and "use Y instead" are ONE ruling and I shipped half.** **Adopted: the pending
marker is the it-ran oracle; the trigger's metrics stay barred.**

## ⛔ And a false premise of mine, reached the hour's own way

I claimed `3.0.0_SA_CVO`'s retraction *"would swallow a true clause"*. **It did not — its committed
entry @`0ba49d8e1f` already kept clause (i) under SURVIVES.** ⛔ **I inferred the SCOPE OF A
RETRACTION FROM ITS MESSAGE HEADLINE WITHOUT OPENING THE COMMITTED ENTRY — inside a message about
scoping claims correctly.** Three seats asserted the overwrite mechanism without opening
`D_00.portal_aggregates.py:849`; **I then asserted the contents of a retraction without opening the
artifact carrying it. Same shape, one level up, forty minutes later.**
✅ **What survives is `3.0.0_SA_CVO`'s own and is narrower: the entry's DISPOSITION LINE says the
hazard dies "with it" while the BODY keeps clause (i) — summary and body disagreeing about what
survives, and the disposition line is what a hurried reader takes.** **Only my framing stands, and it
applies to that line: conjoining two claims into one prediction and disjoining one refutation across
two claims are the same fault in opposite directions.**

## B-series, closed with the round's best-formed result

`0.4.0_DS_ClientPlatform~V` @`0c5194eab8` (with @`97b7288a0e` for b-6): **OUTPUT CHANGED IF AND ONLY
IF A PIN MOVED, 6 of 6** — 3 leaves byte-identical with no pin moved, 3 changed with each moved
upstream named, **each family re-run with the SAME parameters its prior leaf recorded** so
before/after is like-for-like rather than confounding *"the upstream moved"* with *"I changed the
question"*. **`b-5 REFUSED as paged`, reported rather than smoothed.** ⛔ **A BI-CONDITIONAL with both
directions exercised — and `3.0.0_SA_CVO` corroborated it ON A DIFFERENT INSTRUMENT, both halves,
exact pin sets reproduced.** **It is the only thing that makes three byte-identical outputs
trustworthy rather than suspicious.**

## Standing obligations (carried)

- **Nothing open at this seat.** Arch-gate items closed: BDPARITY armed per SUBJECT, arming limb
  unconditional; **P1/P2/P3 still need an arming event drawn from the BD-vs-chain harness — gap
  named, not filled, and not mine.**
- **Tracked, not mine:** AC6-MANIFEST (2 of 4) and AC7's live-plane negative read, lane + issuer ·
  the freshness gate · row 7's sequencing, **RE-OPENED and to be re-derived by the gold-layer owner**.

## Completion test (§4)

**NOT DONE — 1 of 10 projects complete.** REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state: **LOCAL, and local CLOUD is 21 AHEAD of origin @`2fec8fabd3`**
(ls-remote read 11:19Z) — ticks 47, its marking, and this log await the next window; ticks 40-46 ON
ORIGIN.

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · verdict ledger byte-read ·
  own-carrier census over 8 tick logs for the superseded ordering (**measured, correcting the "six" I
  published from memory**) · `git rev-list --count` vs origin · `git ls-remote` + MERGE_HEAD ·
  `ack_messages` (81977-82068 as received) · `send_message` to_agents (82008-82011, 82023-82026,
  82033-82036, 82043-82045, 82050-82052, 82063-82065, 82070-82072; **25 of 25 DELIVERED, 0 QUEUED**).
