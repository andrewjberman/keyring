# CVO CONSTITUTIONAL REVIEW -- spine amendments v3.2, v3.3, v3.4, v3.5 (2026-09-04)

**Reviewer:** `3.0.0_SA_CVO` (spine section 5: the CVO's constitutional review of an amendment is a role, not an
engagement). **Object:** `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md`, the diff `743d282408^..08f579d00e` (61
insertions, 62 deletions, one file), read whole at this seat. **Verdict:** **ACCEPT all four**, with one finding for the
scribe (F1, a conflict between two live laws) and two notes. Every clause below that this seat could exercise on its own
instruments tonight was exercised; the rest is read against the records the changelog cites.

## What the amendments do, and what this seat verified

| Clause (v3.5 text) | Verified how | Read |
|---|---|---|
| L6: the gate refuses a compound criterion, a mechanical criterion without exactly one invocation and one expectation, an issuance that leaves a cell unowned, a worker order without `<paths>` | `4.0.0_SA_CRO` 94129 on the CLDGRPH round-4 issuance @eedb24b906: 11 of 11 faces one-clause, every face with `<paths>`; the CRO's own parse, not the gate's | consistent |
| L7: the worker's write surface is its non-terminal order's `<paths>` at HEAD; no lane enumerates a worker | `4.0.0_SA_CRO` 94077 (scratch worktree, five arms) and 94129 (a real order: ~1 admitted on D-1's surface, ~3 refused); this seat's C-S4 on NFRA_COMPEFFICACY closed S36 on that evidence | consistent, exercised |
| L7: rows mint `<CODE>-W<n>-S<k>`; the gate refuses an id off the grammar, already carried by another document, or off its coordinate | the schema half @e3e999c139 and the gate half @6efb43b9d0 read at this seat; twelve `C` rows admitted tonight (CLDGRPH C-S1..C-S6, COMPEFFICACY C-S1..C-S6); the first `W` rows land with CLDGRPH round 4 | consistent; the W arm is the next read |
| L7, the drain: `.tools/safe-merge.sh` grades the merged index and aborts on a refusal | `2.0.0_SA_COO` 94103 (the fix after the first version graded nothing) and `4.0.0_SA_CRO` 94107 (red: an S40 cross-document collision refused by the script's own grade, MERGE_HEAD absent after; green: a non-colliding branch merged) | consistent, exercised by a seat other than the builder |
| L8: the send guard refuses a message from the CVO to any recipient but the CTO, at every stage | NOT exercised at this seat since the narrowing (this seat's last non-CTO send was 05:47Z, before v3.2 at 06:07Z); stated as APPLIED by the record @85bb815ad0, unexercised here | see F1 |
| L9: a new adjudication row off `<CODE>-C-S<k>` is refused; the census counts the investigation document's rows as items and reads the adjudication document for dispositions; an id two investigation documents carry is refused | the gate's own lines at this seat's commits: "37 investigation item(s) across 3 channel file(s) in the index, 0 undispositioned" with six `C` rows uncounted as items (@f4b41b1c20); the CVO's `adjudicates` on the worker's S34 landed on the worker's item with this document's S34 uncounted (C-S2) | consistent, exercised |
| L10: the items are the investigation document's rows; the CVO's own rows never count against the CVO's slug | the same gate lines; two slugs issued tonight on that precondition (@8fc3921769, @f4b41b1c20) | consistent, exercised |
| Section 4 at v3.5: the eight carriers and the drain refuser are built; one clause binds by reading (the step log's L7 read from git) | the changelog rows 3.2-3.5 cite each build and check-out; this seat's step log for round 6 (@22388f7195) reads L7 from the worker's commits, instance and report as the clause says | consistent; the compiler act is the scribe's |
| Vocabulary: a worker has no telemetry | the G-2 worker's five commits under its serial are its record; no runs.jsonl rows sought | consistent |

## F1 (for the scribe): the narrowed send guard and the Andrew-direct broadcast law contradict each other at the CVO

`org/XXX.md` and CLAUDE.md's law-edit clause require an Andrew-direct received at a seat's terminal to be **recorded
verbatim and broadcast the same turn** to the live seats -- this seat did exactly that at ~05:0xZ for "a for both"
(record @92af61a111; sends to the CTO and the CRO). Spine v3.2's L8 gate now **refuses a message from the CVO to any
recipient but the CTO, at every stage**. The next Andrew-direct at the CVO terminal therefore has no lawful carrier
to the CRO, the COO or MSTR: the broadcast law says send, the guard says refused and nothing written. Neither text
names the other. **Options, this seat's REC first:** (a) the guard admits a send whose subject carries the
`ANDREW-DIRECT` record marker and whose body names the record's path -- the broadcast is a relay of his word, not an
engagement, and it is the one class the spine's "engagement by message" exclusion was never aimed at; (b) the CVO's
broadcast goes to the CTO alone and the CTO relays, which adds a hop to a law that says "same turn"; (c) the broadcast
law is amended to exempt the CVO. The scribe rules; until then this seat will route an Andrew-direct broadcast through
the CTO (b) and say so in the record, so his word is never held in one seat's file.

## Notes (no ruling needed)

- **N1.** The spine's L9 text and the annex's section 9 agreed on the coordinate before the gate half landed only
  because the annex was amended first (v3.3 @e3e999c139) -- the CTO's 94064 read the schema at v3.2 and called the
  switch off when it was already on. Two records of one state, ten minutes apart, is the two-carrier shape the gate
  reads the STAGED schema to avoid; the annex's section 9 now states the built state (v3.4, this commit).
- **N2.** The in-place clock rule (a remediation row's three clocks advance, nothing else changes) is in the gate and
  in the annex and not in the spine's L9 sentence ("carries REMEDIATED and, if it was armed, DISARMED"). Exercised red
  then green at @8fc3921769. No amendment proposed: the spine names the states and the annex names the mechanism, which
  is the division section 1 of the annex draws.

## Not reviewed here

CLAUDE.md Rule 27's pointer (edited in the same commits) is a one-line stub and reads as the spine's version; the
`/dispatch` and `worker.md` edits are the COO's and the CTO's documents and are checked out by the CRO (94129).
