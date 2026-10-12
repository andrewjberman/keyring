# TCKT_VNEXT decomposition -- ROUND 10, 2026-10-12, issuer 2.0.0_SA_COO~V2, dell2

**Authority:** the CTO's round-10 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_TCKT_VNEXT_ROUND_10_20261012.md`
@65e5badffb, answering the round-9 slug `ledger/L10_SLUG_R9.md` @f1fc3d6d07. No PRD addendum; PRD v0.4 stands with its
ratified-text half signed (@1fc5ceaef5). FWD-1 is NOT REALIZED; the vendor path stays stopped; this is not a thread round.
**Nothing is built in round 10.**

Rows by the analysis: D2-S50 CLOSED by the CTO on round 9's release; D2-S53 and D2-S46 stay ARMED, owner the CTO; D2-S54 is this
round's cell.

| cell | builds | list item | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|---|
| `R10-wr-1` | a READ in four parts: which attributes of the disabled tooling row changed at its two writes (names only) and what history the table holds; every writer of a PROFILE row from code, and whether a refused sign-in attempt writes the row; the sign-in function's invocation and refusal counts around the two times; whether a schedule or tool names the identity. A findings file with a verdict from a closed set of four. Nothing built, nothing enabled | 1, 2, 3, 4 | FWD-2 (C-FENCE; row D2-S54) | cut | applier seat, read-only | LOCAL | -- | none |
| carried | `commentary_sent` on the page (IRPT_ANLREQ.TO-AR-y-164) and row D2-S48 (TO-AR-y-163), arm F2, FWD-3 (`2.0.0_SA_COO~Y2`); row D2-S52 (`2.0.0_SA_COO~P2`); the four staged reads; the secret's readers and row D2-S46's census (READ at the laptop 01:52Z, unanswered); row D2-S49's data fix; run 3's request id; row D2-S53, the crawl and the staff list (Andrew) | -- | -- | each on its named event | -- | -- | -- | -- |

**Chains (M = 1):** {`R10-wr-1`}. **Fan-out: 0 workers; one read-only applier order.** The four list items are ONE cell: they are
one question about one row, parts 1 and 3 are AWS reads a worker cannot make, and the verdict needs all four in one head.

## Rule 24 record

- **MECE over the analysis's section 3.** Domain: its four numbered items. By subtraction: each is one part of `R10-wr-1`.
  Nothing is uncovered.
- **The verdict is a closed set with a remainder:** a tool rewriting its own row; a sign-in attempt writing the row; another
  writer; not determined. The third and fourth exist so that an answer outside the CTO's two readings is not forced into one of
  them. Same grain (one writer of one row at two times); one axis (who wrote); the remedy differs by value and none is taken here.
- **The search's domain is stated before a zero is used:** part 2 prints which folders were searched and how many files name the
  table; part 3 prints a positive control beside every zero (row D2-S51).

## Battery

comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: no IAM change; reads only. comp-adversary: DECLARED-NOT-APPLICABLE (a read).

Dry-run at the base (box/dell2, 2026-10-12 ~02:2xZ): `r10_wr1_read.py` FAIL (no result file), as expected.
