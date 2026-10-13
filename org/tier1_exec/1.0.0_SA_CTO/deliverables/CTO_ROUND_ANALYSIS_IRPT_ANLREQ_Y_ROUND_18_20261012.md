# CTO ROUND-18 ANALYSIS -- IRPT_ANLREQ (workstream Y) -- answering the round-17 L10 slug (2026-10-12 ~23:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/remediations/REMEDIATION_v10.md`
@5cf791e25f and the L9 grade (3.0.0_SA_CVO msg 6674): L9 4 PASS; 5 rows OPEN, 2 ARMED (unreleased reader). **No PRD addendum.**

## 1. Rulings

| row / item | ruling |
|---|---|
| **D2-W52-S24** (ARMED; `Brokerage Account`, `Subaccount`, `Account Seq`, `Account Sequence` name accounts and are not matched, so a multi-account file under one of them passes as one account) | **WIDEN before the release pair, not a stated limit.** A multi-account file read as one account puts wrong holdings into a client's report; a limit stated in a pair does not stop that. Add `brokerage`, `ira`, `joint` as modifiers; `subaccount` as an account word; `seq`, `sequence` as identifier words; each with its census line and a negative control (a header with the word that is NOT an account column). **`No. of Accounts` is a COUNT, not an identifier:** a whole-cell exclusion when the account word after `no. of` is plural, with its own negative control (`No. of Account` still matches). |
| **D2-W52-S29** (ARMED; round-16 inputs stored NORMALIZED answer NORMALIZED on a same-token re-POST although the repaired reader would turn them back) | Accepted as the CVO states: count them, read-only, and disposition each before the release. Counts only, no account value. |
| **D2-W52-S28** (the Lambda carries a third, unversioned reader at 3f29017cfc) | Accepted: the release pair runs that case beside AR-y-174's four, and the resident and `irpt-ycharts-generate` move together to ONE pinned reader. |
| **D2-W54-S7** (two test arms do not bite on the check they name) | Accepted: a test cell makes each arm fail when its named check alone is removed. |
| **D2-W54-S5** (narrative's pinned `served.py`; owner this seat) | **The status rule ships to EVERY function that packages `served.py`, together, or the pair names each that stays.** This seat's census of `lambda-source-map.json` (235 functions): 8 package it -- `irpt-performance-adapter`, `irpt-directory-search`, `irpt-narrative`, `irpt-ycharts-generate`, `irpt-export-render`, `irpt-holdings`, `irpt-status`, `irpt-49f-reporting-read-lambda`. One internal caller must get one answer from all eight. The row was not found in the project's investigation file at this tree (the compile and the AR-y-172 proof cite it); it is ruled from the compile's words. |
| The status rule's pair (packet note) | It states the no-row and non-active internal caller population as **UNKNOWN** until counted, and the same cell adds ONE log line in `served.py` naming the caller CLASS only (row present / absent / non-active; no identity), so the population becomes measurable. A log line is not a monitor and raises nothing. |
| **D2-W52-S25** (dell2's client-data commit gate prints "hashed account-id list ABSENT") | **CORRECTED (~23:4xZ, `0.0.0_AB_MSTR~DELL2` msg 6677): blind BY DESIGN; nothing is placed.** This seat set the per-firm hash lists aside on 2026-10-11 (msg 4327) under `ANDREW_DIRECT_20261009_192xZ_CLIENT_DATA_IN_PRIVATE_GIT_NOT_WORTH_TIME.md`, Andrew VERBATIM "I don't care about the client data getting committed to Git...": the gate is WARN-only on dell2 and the WARN is that design showing. My routing earlier in this file forgot my own act. Disposition: dismissed with that reason. A dell2 commit's client-data line is still not evidence of a check, and no seat cites it as one. |

## 2. ENRICHMENT LIST for round 18 (Y, ONE issuance; each build order at most three mechanical criteria)

1. The vocabulary widening and the `No. of Accounts` exclusion (S24), with negative controls.
2. The round-16 NORMALIZED count and disposition (S29), read-only.
3. The test cell that makes each arm bite (S7).
4. The status rule's pair, re-cut: all eight functions named with their `served.py` pins, the caller-class log line, the
   population UNKNOWN until counted.
5. The reader's release pair (S28's third reader included), cut only after items 1 and 2 merge.

-- 1.0.0_SA_CTO~DELL2
