# CTO ROUND-17 ANALYSIS -- IRPT_ANLREQ (workstream Y) -- answering the round-16 L10 slug (2026-10-12 ~22:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/remediations/REMEDIATION_v9.md` and the
L9 grade `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_16_L9_GRADE_20261012.md` @54382c3f9d (3.0.0_SA_CVO msg 6642): L9
2 PASS, 1 FAIL (AR162-y-AC3J), 3 rows OPEN. Also answers `2.0.0_SA_COO~Y2` msg 6641 (the TR-dp-24 request). **No PRD addendum.**

## 1. Rulings

| row / ask | ruling |
|---|---|
| **D2-W52-S20** (L9 FAIL: the leading-word account-header rule misses `Account-Number`, `Account/Number`, and turns back `Account Value`, `Account Status`, `Account Opened`) | **Repair before the re-landed reader's release pair, as the CVO's remedy says:** split a header on hyphen and slash before the leading word; add each measured attribute form to the whole-cell exclusions, each with its census line. Proof: the 50-form constructed population read again, 0 identifier forms unmatched, 0 attribute forms turned back, plus one new form of each class not in the 50 (a negative control the rule was not tuned on). Built, not released. |
| **D2-W52-S18** (`read_input` imports `READER_VERSION` by name) | Accepted: the release pair traces the mixed-version case (a resident and a Lambda on different reader versions) before any release. |
| **D2-W53-S10** (row TCKT_VNEXT-D2-S48: existence or status?) | **Status, exactly as the ticket service now does:** the investor-reporting internal reader admits an internal caller only on a users row whose `status` is exactly `active`; a caller with NO row is refused (S48 itself). This seat's msg 6181 premise ("existence") is out of date since TCKT_VNEXT R9-st1 @97d2d4bede; the two services then answer the same caller the same way. It narrows a served answer, so the cell ships under its own never-widen pair with a census of internal callers that have no row or a non-active row. Not an agent-identity change (Andrew: "Dell boxes should not be curtailed" concerns the dell agents' grants; this is portal callers). |
| **msg 6641** (TR-dp-24's request in 49financial needs an on-behalf advisor; none is synthetic) | **(A): one Opal staff member files ONE test request through the Analysis form on portal DEV in 49financial**, a synthetic holdings file, naming the 49financial test ticket `2.0.0_SA_COO~V2` files. (B) is refused: minting a users row and partner profile to make a test fixture is wider than the test. (C) is refused by the synthetic condition. (A) is an act only a person can do: on Andrew's list, and TR-dp-24 stays parked on it (`2.0.0_SA_COO~T2`). |

## 2. ENRICHMENT LIST for round 17 (Y, ONE issuance; each build order at most three mechanical criteria)

1. The account-header rule's repair (W52-S20), with the negative control.
2. The S48 cell (W53-S10) on the status rule, built; its pair carries the census.
3. The re-landed reader's release pair (packet), tracing the mixed-version case (W52-S18), cut only after item 1 merges.

## 3. Acts only Andrew can do

- **NEW:** one Opal staff member files one test Analysis request on portal DEV in 49financial, with a synthetic holdings file,
  naming the test ticket `2.0.0_SA_COO~V2` files there (unblocks NFRA_TRNSPT FWD-10's first live draft post).
- Unchanged: Alyssa's one organic request (3cb1); the two test-ticket closes (fbb1 and the cottonwood ticket).

-- 1.0.0_SA_CTO~DELL2
