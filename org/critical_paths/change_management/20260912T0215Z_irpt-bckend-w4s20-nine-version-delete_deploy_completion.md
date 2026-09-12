# CHANGE MANAGEMENT -- IRPT_BCKEND W4-S20: per-version delete of NINE noncurrent versions

**State:** OPEN (this entry and its sentinel are committed BEFORE the act, per NEVER-2)
**Opened:** 2026-09-12T02:15:00Z by `2.0.0_SA_COO~B`
**Class:** IRREVERSIBLE DATA DELETE. There is no rollback leg and this entry does not pretend to one.

## The act

Per-version delete (`s3api delete-object --version-id`) of the NINE noncurrent versions of the four synthetic
export `report.pdf` keys under `firms/49financial/generations/GENIBS14SYN/attempts/1/exports/` in
`s3://opal-data-ycharts`.

## Authorization

Andrew-direct 2026-09-12 ~01:5xZ at the `1.0.0_SA_CTO` terminal, VERBATIM AND ENTIRE: **"Approved all 9"**,
answering the card "The four synthetic export PDFs hold NINE noncurrent versions, not four. (a) delete all nine
(b) delete only the four named (c) leave them", REC (a). Relayed as msg 96050. Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260912_015xZ_ALL_NINE_NONCURRENT_VERSIONS_APPROVED.md`.

Row lineage: `IRPT_BCKEND-W4-S20` (the delete-marker-vs-destruction finding) -> `IRPT_BCKEND-S41` (this seat's
STOP: the four named ids resolved, but the set was short by five) -> `IRPT_BCKEND-S42` (`1.0.0_SA_CTO` disarming
S41 by carrying the corrected count back to Andrew).

## The authorized set, written as a SUBTRACTION and never as a list

A forward list of four remembered VersionIds is what failed the first time. Rule 24: the printed denominator
MINUS what is excluded.

```
DENOMINATOR  10 versions / 5 delete markers / 5 keys   (s3api list-object-versions over the exports/ prefix)
MINUS        probe/probe.txt -- 1 version, 5 B, not an export PDF, named nowhere in the row
= NINE       every noncurrent version of the four report.pdf keys
             r1 THREE  ·  v0-11-overview TWO  ·  v0-11-comparison TWO  ·  v0-11-multicomp TWO
```

## Pre-act gate (the count is perishable -- it was FOUR when W4-S20 was filed)

Re-read immediately before acting, 2026-09-12T02:14Z: `aws_rc=0`, 8808 bytes, `IsTruncated` absent,
**versions=10 deletemarkers=5 keys=5 target=9 excluded=1** -- matches the authorized subtraction exactly.
**VERDICT: PASS, the act proceeds.** Had it not matched, the standing instruction was to STOP again and return:
the authorization is over a MEASURED SET, never over the number nine as a target to be reached.

## NOT AUTHORIZED

- `probe/probe.txt`, any version of it, and its delete marker.
- Any other object, prefix or key in `opal-data-ycharts`.
- **The five DELETE MARKERS themselves** -- deleting a delete marker RESTORES a current object, which is the
  opposite of the intent and is not covered by "delete all 9".
- Any bucket-level change: versioning state, lifecycle rule, policy, replication.
- Any while-we-are-here cleanup.

## Close condition

A **by-VersionId** read returning `NoSuchVersion` on 9 of 9, plus a **POSITIVE CONTROL** read on
`probe/probe.txt`'s version `HoC7IAl6vkSq8u2D0v6bYbvmxTVskw8h`, which MUST still resolve.
**A 404 on the ordinary key proves nothing here** -- that was already true before the act, and it is the entire
reason this call existed.

## Legs

| # | leg | state |
|---|---|---|
| 1 | Andrew's word on the CORRECTED count, recorded verbatim | DONE |
| 2 | Ledger + sentinel committed BEFORE the act | DONE (this commit) |
| 3 | Pre-act gate re-read matches the authorized subtraction | DONE -- PASS |
| 4 | The nine per-version deletes, each response captured | PENDING |
| 5 | By-VersionId read: `NoSuchVersion` on 9 of 9 | PENDING |
| 6 | Positive control: `probe/probe.txt` version still resolves | PENDING |
| 7 | Delete markers untouched (5 still present) | PENDING |
| 8 | Ledger CLOSED and committed before the grading reads | PENDING |
