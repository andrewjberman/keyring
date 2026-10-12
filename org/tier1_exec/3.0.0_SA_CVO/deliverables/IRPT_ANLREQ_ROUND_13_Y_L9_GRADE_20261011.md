# IRPT_ANLREQ round 13, workstream Y -- L9 grade of AR131-y-AC3 and AR132-y-AC2

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T21:02:29Z. Row IRPT_ANLREQ-D2-S62.
**Input:** `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND13_Y_L8_COMPILE_20261011.md @6d2fa01d99 (msg 5839)`.

| criterion | verdict |
|---|---|
| AR131-y-AC3, the queue age's unit and its statuses | **MET; one clause of it cannot be met as written** |
| AR132-y-AC2, the read of the one-account check | **MET; one proposed finding needs a ruling before it is built** |

## AR131-y-AC3

Read on portal DEV d3ef4a5d88.

- **The unit.** Hours are shown below 72 hours and whole days from there. A ticket waiting 47 hours now reads `47 hours`. From 72
  hours the age is again rounded down to a day, so 95 hours reads `3 days`: that hides under a day on a ticket already three days
  old. A person ranking the queue is not misled.
- **The statuses.** The age shows for `open` and `in_progress`, a closed list, decided by membership. A status added later shows no
  age until someone adds it on purpose. Both of those are a ticket waiting on Opal.
- **"Read from the ticket type's definition" cannot be met:** there is no per-type definition. This seat printed both lists, the
  portal's type and the service's, and each holds exactly `open`, `in_progress`, `completed`. The list was read from what exists.

Not looked at as a page this round, by the issuer or this seat.

## AR132-y-AC2

**Enough to cut the build: yes.** The record names the door the form actually reaches, what it does today on four sheets, seven
signals each with where it was seen and what it would wrongly catch, five cells with their files, and four questions a ruling
must settle first. Its most useful result is the first: the order and two earlier reads named the wrong file, and a check built
there would never have run.

**No signal a one-account sheet would commonly trip: yes for the two offered as rules.** An account-named column counts only when
it holds two or more distinct values, and the header is matched as a whole phrase; a repeated header row is to be worded as that
and not as several accounts. The three signals with a high false-positive risk are rejected, each against a fixture in the
repository.

**One finding in the proposed cells is not among the two offered rules.** Cell 2 lists `EXTRA_HOLDINGS_SHEET` as an error. The
record rates the more-than-one-worksheet signal as medium risk, and the repository's own multi-sheet fixture is a workbook whose
second sheet is named for a sleeve, which the record's first signal says is a split inside one account. Built as an error, that
finding would turn back the repository's own example of one account. Today the door reads the first sheet and ignores the rest in
silence, which is also wrong. Whether a second holdings sheet is turned back, and in what words, is a fifth question for the
ruling. This seat did not open the fixture; the reading is from the record.

Limits the record states and this grade repeats: both offered rules are inferred, since the repository holds no example of
either; the provider was a stub; no real sheet was used.
