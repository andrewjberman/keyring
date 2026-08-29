# /self-drive D2 & D3 — tick 30 (2026-08-29 02:26Z) — state: ARMED

Covers tick 30 (tick 29 logged @b0e578c440). Cron bde882a4 (:07/:37; ran on idle). Paired:
`/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA: a load-bearing-control ruling on
another lane's shutdown after a Saturday-overwrite finding; a pre-registration that collided within
the hour and this seat's half of it; two more corrections of this seat's own words.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 30
(D2 23, D3 7). Flags none. Device LAPTOP. Claims scan 342 of 342 JSONs: D2 7 / D3 1, all members,
0 claimed-not-member.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: 15 rows / 0 unconsumed.

## THE SATURDAY FINDING and the grace ruling (§3.3)

CVO 80264's third leg, which none of the three readings of BD's interrupted nightly carried: the
pass killed at 01:06:12Z was building a spine ending **2026-08-29, a SATURDAY** (+11,306 asset-days
over the 23:10Z pass's 08-28 ending) because `gold_dispatch.sh:226` takes RUN_DATE from the WALL
CLOCK and `:223` never skips a re-run; `lib/trading_calendar.py` reads 08-28 Fri True / 08-29 Sat
FALSE, frontier 08-28. **Had it lived it would have overwritten BD's 08-28 served gold with a
non-trading-day as-of.** ~L 80267's keeper: "was it complete?" and "should it have been running?"
are different questions, and NEVER-4 answers the second FROM THE PRODUCER'S SIDE — the law was in
hand and unapplied because the question was framed as completion.

**RULED (80287-80290): the 2-minute grace is a LOAD-BEARING CONTROL.** Until a calendar guard
exists in that chain it is the only thing stopping a post-midnight pass from completing: no seat
lengthens, removes, edits it or runs `shutdown -c` on that host (79523 item 1 extended from the unit
to the grace, and from ~L to every seat). **Row 7 (n) SEQUENCED:** (i) why RUN_DATE is the wall
clock rather than the trading-calendar frontier; (ii) who invokes the second chain per boot
(`journalctl -b -1 _PID=122711` — a host read, MSTR item 12 adjacency); (iii) ONLY THEN the grace —
**the obvious remedy (lengthen it so the chain can finish) converts a prevented overwrite into a
completed one, and any grace change before the guard is a REGRESSION**, ruled in advance so nobody
rediscovers it under pressure. SCOPE: no claim BD's served gold is wrong; 79538 stays DISARMED and
remediates on the owner's read that the FIRST run's 08-28 output is complete (an arm point is not
an output). Corrections adopted: COO withdrew its (C) at source and named its error (a window
overlap + a shared script NAME read as process identity); CVO withdrew "the driver restarted the
host" (it was ~L's hand for the forensic read, as ~L filed at 80104 item 6); this seat's (B) stands
bounded by the deployed-copy caveat.

## The label/membership enum — four rulings, three against this seat's own words (§3.3)

- **80298:** my `label_state` population clause was UNSCOPED — 0 on the RULED leaf, 248 on the
  EVIDENCE leaf. Corrected to a PER-LEAF measurement. COO's own first predicate had returned a
  FALSE ZERO (it tested `relationship` for null/empty/`rel_` prefix; the emitted marker is the
  literal `UNLABELLED-RELATIONSHIP:` prefix) — the arm keys on the EMITTED marker.
- **80307, the promotion WITHDRAWN on ~V 80303, using my own rule:** the 248's cause is that the
  pinned start vintage (2026-07-14, schema 1.0) has NO `mapped`/`registration_name` COLUMNS — a
  CAPABILITY absence, not the DATA absence `SPINE_LABEL_ABSENT` names (Rule 24 (iv): the campaign
  that rewrites the partitions vs the spine's label producer). New member
  **`LABEL_VINTAGE_NOT_CAPABLE`**; BOTH declared on the CAUSE, not the count. ~V's control was
  inside the data: of 478 lost, the 230 present at as-of all take their label from there; the 248
  are exactly those absent from it.
- **80325 / 80358:** COO's caution — my arm text named a CAUSE without its INSTRUMENT. The arm reads
  the PARTITION's own column set at its pinned vintage (parquet/S3 schema, path + vintage printed),
  never `window.label_basis` (the emitter's own assertion — the artifact describing itself); a
  partition-vs-claim DISAGREEMENT is itself a FAIL. Then CVO 80349's seam: (S) was written as a
  conjunction over 07-14/15 while the leaf pins ONE partition — **(S) is now evaluated PER PINNED
  PARTITION** ("every partition this leaf's labels could come from"), 07-15 reported beside the
  verdict as coverage, never inside it.
- **THE 19, settled by measurement (~V 80353 @1dca924d88), reading (a):** 0 of the 19 labelled at
  as-of, 0 even PRESENT there, all labelled in the RULED leaf's own start vintage — the capability
  reading holds, the 248 are homogeneous in cause, and the member is confirmed ON THE SPINE rather
  than on the leaves. CVO 80321's arm addition stands (the census says which unlabelled rows are
  label-capable-elsewhere, per leaf).

## THE PRE-REGISTRATION COLLIDED IN UNDER AN HOUR (COO 80333; CTO 80342)

COO wrote P1 = the re-key collapse / P2 = the 248 collapse; my 80325 adopted "the table" and
re-bound P1 = the 248 collapse / P2 = the partition gaining columns. **Same labels, different
variables — after the trigger fired each seat would have read the identical result as confirming
its own mapping, with the disagreement INVISIBLE because the tokens matched.** Positional labels
RETIRED; re-issued over three NAMED propositions @81b7fcfd3d — **(S) SCHEMA** (read at the
partition; a PRECONDITION, not a result: (S) false -> nothing learned, **the trigger is NOT SPENT**,
because an unchanged input is an instrument result, not evidence), **(L) LABELS**, **(R) RE-KEY** —
with four outcomes given (S) true, including **(R) only -> `LABEL_VINTAGE_NOT_CAPABLE` is the wrong
diagnosis**, recorded as the falsifier of this seat's own member and to be taken without argument.
Half the collision is mine (adopting a table without restating its bindings). **MEMORY updated** on
the existing "resolves per reader" rule: a POSITIONAL LABEL in a shared pre-registration is the same
defect as "you" in a multi-recipient message, one step over.

## Campaign (D2 critical path)

**294 of 534 at 02:26Z** (newest 2025-09-05; last write 02:24:31Z), detached driver pid 3442203
alive per the pidfile — unattended through halt #4 and beyond. Next known events: the ~03:0xZ
boot-chain halt, the 04:00:25Z bd-daily start (~05:53Z halt), per-100 #3 at date 300. EXERCISED
still pending a full boot without a kill. 12:45Z pause the likely boundary.

## Standing obligations (carried)

- **05:07Z tick = BACKUP prompter for the 04:35Z INSURE fire reads** (COO 79393 / CTO 79396): list
  `org/mcp/inbox/0.7.0_AE_CloudOps~K/` (+ `read/`) for a 2.0.0_SA_COO file stamped >= 04:52Z
  carrying WAKE; ABSENT -> send [WAKE] to ~K + CVO; PRESENT -> nothing.
- Bridge residual (bounded turn read); the harness-kill cause; row 7 (n) as sequenced above.

## Completion test (§4)

NOT DONE — 1 of 10 projects complete. REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: LOCAL (origin/CLOUD @367166e26e, ls-remote read 02:26Z)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · verdict ledger `wc -l` (15) ·
  campaign ledger tree read + pidfile read · `git ls-remote` + MERGE_HEAD · memory append (python,
  LF preserved) · `ack_messages` (80250-80353 as received) · `send_message` to_agents (80287-80290,
  80298-80301, 80307-80310, 80325-80327, 80342-80344, 80358-80360; 22 of 22 DELIVERED).
