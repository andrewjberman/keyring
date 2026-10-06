# IRPT_YCDGEN -- DECOMPOSITION, ROUND 6 ADDENDUM D: the Opal PDF under its own policy row, and retention resolving a policy from the reference

```json
{
 "project": "IRPT_YCDGEN",
 "round": 6,
 "addendum": "D",
 "prd_ref": "org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md (v0.6; ENDPOINT unchanged since v0.5 @e6a801f7f0)",
 "prd_version": "v0.6",
 "endpoint_outcomes": ["FWD-1"],
 "round_scope": ["FWD-1"],
 "author": "2.0.0_SA_COO~Y",
 "cells": 1,
 "chains": 1,
 "join_cells": 0,
 "frozen": true,
 "revision": "1.0",
 "parent_decomp": "org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6B.md",
 "ruling": "org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md batch 269 (msg 105429)",
 "cell_ids": ["YCD-l-6"]
}
```

**Why an addendum.** Cell i-6 (merged @14eb4d115d, deployed nowhere) added family `OPAL_REPORT_PDF` to the policy whose revision is `irpt-x10-v1`, moving its
`policy_sha256` (e0046398 to a65635d3). `reports/retention.py:108-113` refuses a retention row whose stored digest differs from the deployed policy's, so shipping
that change would refuse every retained artifact written since 2026-09-24. The CTO ruled route (b) (batch 269, msg 105429): the v1 policy's bytes go back to what is
deployed; the Opal PDF is retained under its own policy row; the retention check resolves the policy from the reference's own `policy_revision` among the ACTIVE
registered revisions; no existing row is rewritten. Worker row IRPT_YCDGEN-W3-S14.

**Issuer's pick (batch 269 item 2 asks the issuer to say which):** the existing row `irpt-ycdgen-research` (revision `irpt-ycdgen-research-v1`, family
`YCHARTS_OPAL_REPORT`) serves; no new row is registered. It is PENDING_ENFORCEMENT today; going ACTIVE is the CTO's acceptance (item 5), on the issuer sending the row
and its enforcement revision, which follows this cell's merge. The spill of the Opal document stays on the already-registered v1 family `EXTRACTION_EVIDENCE`
(a registered family, no digest change).

## Cell

| cell | hop | writes | reads | depends on |
|---|---|---|---|---|
| `YCD-l-6` | 7 Persist (policy) | `infra/logic/registry/reporting_policies.json`, `lib/tests/test_irpt_destination.py`, `reports/retention.py` and `reports/tests/test_retention.py`, other `reports/*.py` and `reports/tests/*.py` only where the policy lookup forces it, `ycharts/research/opal_producer.py` + test, `ycharts/generate/publisher.py` + test, `ycharts/generate/publication_worker.py` + test (base `infra/aws/lambda/investor-reporting/`) | batch 269, i-6 (merged) | none open |

**Writer read (batch 269 item 3).** `reports/retention.py` and the registry file are in `2.0.0_SA_COO~P`'s lane; a scan of 4,241 task-order files (both roots) for a non-terminal
order whose `<paths>` names `reports/retention.py`, `reports/tests/test_retention.py`, `infra/logic/registry/reporting_policies.json` or `lib/tests/test_irpt_destination.py` found 0
hits: no order of any seat writes them this round. This order is their only writer.

**Contract R12.** (1) `OPAL_REPORT_PDF` is removed from `irpt-x10-v1`; the policy reads exactly as deployed: its `policy_sha256` equals the value the base before i-6 computed
(e0046398 prefix; the worker reads the full value from the test constant at `git show 14eb4d115d^:lib/tests/test_irpt_destination.py`); `lib/tests/test_irpt_destination.py` returns
to its pre-i-6 family census for that policy. (2) The Opal PDF is retained through the repository under policy revision `irpt-ycdgen-research-v1`, family `YCHARTS_OPAL_REPORT`;
the producer, the publisher and the publication worker name that family where they named `OPAL_REPORT_PDF`. (3) `reports/retention.py` resolves the policy from the reference's
own `policy_revision` against the set of ACTIVE registered revisions, in place of the pinned `POLICY_REVISION`; a v1 reference validates exactly as today; an Opal reference
validates against its own row; a revision that is not registered, or registered but not ACTIVE, is refused. Every existing retention test passes untouched.

## Edges and fan-out

M = 1, serial before k-6 (the join), which depends on the final family and policy wiring. fanout: 1 of 1 chain, cap 8, reason: one rework cell on the persist hop.

## Four-postulate record (Rule 24)

MECE: the persist hop's artifacts (R6B/i-6) are reworked in one place; the retention check, the registry and the three persist modules each have one writer (this cell).
Same grain: one policy decision. Intent: one outcome (the v1 policy is bytes-identical and the Opal PDF has its own row). State: no stored row is touched; the
v1 digest does not move; the research policy's ACTIVE flip is the CTO's, not this cell's.

## Battery

comp-schedule, comp-iam and comp-adversary DECLARED-NOT-APPLICABLE (thread round, no grant change). The proof the CTO asks before release (batch 269 item 4: a stored v1 row
read from the live index validates under the new code; the built registry's v1 digest equals the deployed one) is the issuer's read at the close.
