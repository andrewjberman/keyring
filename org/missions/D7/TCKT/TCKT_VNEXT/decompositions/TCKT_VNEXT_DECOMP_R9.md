# TCKT_VNEXT decomposition -- ROUND 9, 2026-10-12, issuer 2.0.0_SA_COO~V2, dell2

**Authority:** PRD `prd/TCKT_VNEXT_PRD.md` v0.4 ADDENDUM 4 @fc2100e1e2, which is the round-9 analysis (CTO msg 6236), answering the
round-8 slug `ledger/L10_SLUG_R8.md` @1709e06706. **The ratified-text half is SIGNED: `3.0.0_SA_CVO`'s own L4-R commit
`1fc5ceaef5`, "TCKT_VNEXT_PRD.md v0.4 @fc2100e1e2", read by this seat by author and subject; `prd-signoff.py status` reads it
current with no CHANGED flag.** The CTO's word (msg 6240): "Round 9 may be cut", with two conditions on the pair.
FWD-1 is NOT REALIZED; the vendor path stays stopped; this is not a thread round.

| cell | builds | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|
| `R9-st-1` | the ticket service refuses an INTERNAL caller whose one PROFILE row does not carry status exactly `active`, with the failed-lookup answer and a log line carrying no address; an active row's firm-list behaviour unchanged. Code and tests | FWD-2 (C-FENCE; row D2-S50) | cut | dell2 worker, slot 27 | WORLD by path floor; nothing is applied | worker | none |
| `R9-ct-1` | a READ, numbers only: active internal rows by the domain of their address (the non-Opal count the CTO wants first); the non-human active rows re-read by form as twin candidates; sign-in's status test printed from its lines | FWD-2 (C-FENCE) | cut | applier seat, read-only | LOCAL | -- | none |
| `R9-st-2` | the apply of `R9-st-1`, under its own pair. The packet carries `R9-ct-1`'s count, and quotes sign-in's comparison beside the ticket service's (the CTO's two conditions, msg 6240) | FWD-2 | NOT-EVALUATED, NOT CUT | ISSUER + applier seat | WORLD | -- | `R9-st-1`; `R9-ct-1`; a non-zero non-Opal count answered by the CTO first |
| `R9-st-3` | the proof by direct invoke, read from PARSED values: the disabled tooling row's address SERVED before the release and REFUSED after; a no-row caller refused before and after; the twin, a NON-HUMAN ACTIVE row, served after; a refused twin rolled back at once | FWD-2 | NOT-EVALUATED, NOT CUT | ISSUER + applier seat, same pair as `R9-st-2` | WORLD | -- | `R9-st-2`; the twin named by `R9-ct-1` |
| carried | the four staged reads; arm F2, `commentary_sent` on the page, rows D2-S48 and D2-S40 (`2.0.0_SA_COO~Y2`); row D2-S52 (`2.0.0_SA_COO~P2`); the secret's readers and row D2-S46's census (the laptop); row D2-S49's data fix; run 3's request id; the crawl and the staff list (Andrew) | -- | each on its named event | -- | -- | -- | -- |

**Chains (M = 2):** {`R9-st-1`, `R9-ct-1` -> `R9-st-2` -> `R9-st-3`}; the carried line. `R9-st-1` and `R9-ct-1` have no edge between
them and both feed `R9-st-2`. **Fan-out now: 1 worker of 2 chains, cap 8, plus one read-only applier order.**

**Write sets (disjoint):** `R9-st-1`: `infra/aws/lambda/ticket_center/lambda_function.py` and its `tests/` folder. `R9-ct-1`: the
applier's deliverables folder.

## Rule 24 record

- **MECE over the analysis.** Domain: msg 6236's two asks of this seat (the one line and test with its pair; the count first)
  and msg 6240's two conditions. By subtraction: the line and test -> `R9-st-1`; its pair -> `R9-st-2`, `R9-st-3`; the count ->
  `R9-ct-1` step 1 and 2; condition 1 (sign-in's test quoted) -> `R9-ct-1` step 4 and the packet; condition 2 (the count in the
  packet, non-zero to the CTO) -> `R9-st-2`'s dependency. Nothing is uncovered.
- **The status set, by subtraction and not a forward list.** The build compares `!= "active"`: it admits ONE value and refuses
  the complement, so a value nobody has seen is refused without being named. Measured population (round 8): 56 PROFILE rows,
  `active` 54, `disabled` 2, absent 0. State coherence: the one check moves `disabled`, absent and unseen together and does not
  move `active`; the firm-list cases are a different axis and are held fixed by a test.
- **An inherited class falsified before reuse:** round 7's `reads_as` (person or non-human) was made by a domain test the applier
  found wrong in round 8 (it classed an external-domain person as non-human). `R9-ct-1` re-reads every class by form and does
  not reuse it. The twin is chosen from the re-read, never from round 7's column.
- **A consequence named before the build:** every existing test double supplies a users row with no status; after the change
  those callers are refused, so the order tells the worker to add `status: "active"` in the doubles, not in each test.

## Battery

comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: no IAM change in any cell. comp-adversary: `R9-st-1`'s tests are the
adversarial arms (a disabled row on every scoped route; near-miss values `Active`, `ACTIVE`, a padded string, a missing
attribute); `R9-st-3` is the live adversarial act.

Dry-run at the base (box/dell2, 2026-10-12 ~01:2xZ, 201 ticket tests): st-active FAIL absent, st-regress FAIL (201 below 206),
ct-count FAIL absent, all as expected.

## AMENDMENT 1 (2026-10-12 ~01:4xZ, issuer `2.0.0_SA_COO~V2`): `R9-st-2` and `R9-st-3` are CUT, as ONE applier order

- **Their dependencies are met.** `R9-st-1` drained @873130546e (206 tests on the merged tree). `R9-ct-1` complete @e7bb608065:
  21 active internal rows, 20 on Opal's or a reserved domain, ONE on an outside company's domain. The non-zero count went to the
  CTO before any pair (msg 6258) and was ruled (msg 6259): put the pair, the row stated as NOT MOVED; row TCKT_VNEXT-D2-S53
  (ARMED, owner the CTO); no seat on dell2 changes, disables or probes it and no context is constructed for its address.
- **The pair is signed:** COO half in `deliverables/2.0.0_SA_COO~V2/R9_RUN/R9_ST2_DEPLOY_AND_PROOF_PACKET_20261012.md` @70665e9c3e;
  CTO half `deliverables/1.0.0_SA_CTO~DELL2/CTO_HALF_R9_ST2_ACTIVE_STATUS_20261012.md` @b0308e1a26, bound to the packet's sha256,
  with one condition taken into the order: the re-read of the two rows the arms use is a STOP if either reads differently.
- **Order:** `org/tier2_senior/0.7.0_AE_CloudOps~TV2/task_orders/TCKT_VNEXT.TO-APPLY-R9-st2.status-active-code-and-five-gets-dell2.md`.
  One order for both cells: two arms run BEFORE the apply and three AFTER. Every status is read from a parsed value.
- Gate limb: none grades this file's modification; the applier order is a flat order under a `# pipeline-override:` line.
