# TCKT_VNEXT decomposition -- ROUND 8, 2026-10-12, issuer 2.0.0_SA_COO~V2, dell2

**Authority:** the CTO's round-8 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_TCKT_VNEXT_ROUND_8_20261012.md`
@8cccf94651 (msg 6216), answering the round-7 slug `ledger/L10_SLUG_R7.md` @c3d96d5013. No PRD addendum came with it; one is owed
by the CTO after this round's read. PRD v0.4 stands, ratified-text half signed (@b667a5fb11, re-stamped @6839e70629).
FWD-1 is NOT REALIZED; the vendor path stays stopped; this is not a thread round. **Nothing is built in round 8.**

Ruled by the analysis and not cells: an absent or empty firm list keeps meaning every firm; a disabled row should not admit, but
no line is built before the addendum that says so is signed.

| cell | builds | list item | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|---|
| `R8-ds-1` | a READ in three parts: what the portal's sign-in and authorizer do with a disabled user, from code; the two disabled internal rows by digest and form; every status value on the PROFILE rows with counts summing to the denominator. A findings file, nothing built | 1, 2, 3 | FWD-2 (C-FENCE; row D2-S50) | cut | applier seat, read-only | LOCAL | -- | none |
| carried | the four staged reads; arm F2, `commentary_sent` on the page and row D2-S48 (`2.0.0_SA_COO~Y2`); the secret's readers and row D2-S46's census (the laptop); row D2-S49's data fix (its owner, through the manager); run 3's request id; the crawl and the staff list (Andrew) | -- | -- | each on its named event | -- | -- | -- | -- |

**Chains (M = 1):** {`R8-ds-1`}. **Fan-out: 0 workers; one read-only applier order.** The three list items are ONE cell because
they are one read of one population (the users table's PROFILE rows and the code that reads them) and the CTO's word is "one
read cell"; splitting them would put two seats on one table for no dependency.

**Why the applier and not a worker:** parts 2 and 3 are AWS reads, which a worker cannot make.

## Rule 24 record

- **MECE over the analysis's section 3.** Domain: its three numbered items. By subtraction: 1, 2 and 3 are the three parts of
  `R8-ds-1`. Nothing of section 3 is uncovered.
- **The status set is closed by subtraction, not by a forward list:** part 3 counts every distinct value INCLUDING an absent
  attribute, and its counts must sum to the PROFILE denominator (the order's check enforces the sum).
- **A correction this seat carries into the order:** the round-7 read (`R7-el-1`) said the portal authorizer is not in this
  checkout. It is: `infra/aws/users/lambda/portal-authorizer/index.mjs`, named by `infra/aws/terraform/portal-auth/lambdas.tf:61-63`.
  The worker looked under `infra/aws/lambda/` as its order told it to; the wrong folder was this issuer's. The three NOT_READ
  cells of that file stand as not read; this round's part 1 reads the authorizer for the status question only.

## Battery

comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: no IAM change; two table reads and one configuration read per function.
comp-adversary: DECLARED-NOT-APPLICABLE (a read).

Dry-run at the base (box/dell2, 2026-10-12 ~00:5xZ): `r8_ds1_read.py` FAIL (no result file), as expected.
