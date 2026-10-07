# IRPT_CUSTDY -- ROUND ANALYSIS, round 5

Author `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~13:2xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES. This answers `3.0.0_SA_CVO`'s slug (msg 607):
REMEDIATION_v5 @76a18c97db (merged @88a536197f). Grade file: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_CUSTDY_ROUND_5_L9_GRADE_20261007.md`.
W10-S1 closed; ARMED 0. **CU15-AC3 C-SHAPE MET**: the CVO checked the template against a real Black Diamond record's 75 keys, not the
worker's own deny list.

## 1. FWD-1 -- NOT LIVE; hop 5's server side is about to move

Hops 1-4 run on real data, and the 49F template exists (portal @99addd80, reviewed). Hop 5's served render needs the export to
accept a custody report. **IB-pr-336 (the `CUSTODY_REPORT` kind) ships inside IRPT_BCKEND's emergency fail-closed release**, whose
CTO half was widened to it (AMENDMENT 1 @4493cf1800). When that release lands, the server half of hop 5 is live. The page half
(PrintEntry, and this template) waits on Andrew's DEV-landing word.

## 2. Rulings

| row | ruling | owner |
|---|---|---|
| S10 | The tracer test is RETIRED. Its purpose (naming the seam line that refused) ended when IRPT_BCKEND made the guard case-insensitive (IB-pr-348). This is the second time it went red on an upstream fix. A test that exists only to observe a defect goes when the defect does | `~K2` |
| W13-S2 | `validate_document` admits a not-covered account, carrying its reason, without the per-household blocks. The producer does NOT fold a not-held account into another household, because that would put a client's account under someone else's household. The template renders it (this seat's review note on 99addd80) | `~K2` |
| W12-S1 | The SI anchor probe reads a manifest (or a narrowed prefix) instead of listing S3, so hop 3 runs inside its 120 s bound before it is ever scheduled | `~K2` |

## 3. Tooling finding, routed out

The surprise-row corpus gate reads the SHARED WORKING TREE, so one seat's uncommitted, malformed row refuses every other seat's
commit on dell2. It did so for about 10 minutes (S370's literal `%Y-%m-%dT...` timestamp, then S371). A gate grades what a commit
carries. Reading the working tree instead of the index is the defect. Routed to the laptop as the tool's owner. Until it is fixed, a
seat that writes a row commits it in the same turn.

## 4. ENRICHMENT -- round 6, ONE issuance by `2.0.0_SA_COO~K2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **Not-covered accounts, end to end** (W13-S2) | (1) `validate_document` passes a document holding a not-covered account with its reason and fails one with the reason missing; (2) the template renders "not covered: <reason>" for it, with a test (bun `--no-install`, inside `portal/`); (3) no not-held account appears under another household | LOCAL |
| E2 | **The tracer retired** (S10) | (1) the test is removed with a commit naming why; (2) the `irpt_custody` suite reads 0 failed on CLOUD | LOCAL |
| E3 | **The anchor probe bounded** (W12-S1) | (1) hop 3 completes in at most 120 s for the chosen advisor, timed; (2) SI labels are unchanged (14 of 14 accounts) | LOCAL |

-- 1.0.0_SA_CTO~DELL2
