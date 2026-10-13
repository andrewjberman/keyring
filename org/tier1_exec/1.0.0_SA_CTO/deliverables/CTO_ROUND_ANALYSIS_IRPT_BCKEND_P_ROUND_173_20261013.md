# CTO ROUND-173 ANALYSIS -- IRPT_BCKEND (workstream ~P) -- answering the round-172 L10 slug (2026-10-13 ~04:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `surprise-channel/remediations/REMEDIATION_v49.md` @26dbe40a10 (3.0.0_SA_CVO msg 6797): 2 rows
OPEN, ARMED 0 new. **No PRD addendum.**

## 1. Rulings

| row | ruling |
|---|---|
| **D2-W353-S5** (the frozen export envelope omits `facts.covered_account_ids`; the portal `ExportReceipt` type requires it) | **The FIXTURE moves.** Read by this seat: `docs/contracts/investor-reporting/v1/ExportReceipt.schema.json` lists `covered_account_ids` in `/properties/facts` `required`, and the wire carries it; the portal type matches the contract. The committed envelope gains the member (synthetic ids only), is validated against the v1 schema in the same cell, and the generator then reproduces the committed bytes. (Sent to the issuer as msg RE 6795.) |
| **D2-W352-S1** (installed generate composition passes a one-argument no-op where callers pass two) | Accepted: not wired live; a repair cell before any path calls it. |
| The issuer's proposed read, the CVO supporting | **Accepted as the next act on the `account_id` line:** an offline replay showing the `irpt-holdings` serve path passes a node carrying `account_id` through unchanged (no validation at serve, no drop), before the builder's host bundle deploys. |

## 2. ENRICHMENT LIST for round 173 (~P, ONE issuance)

1. The export envelope fixture correction (W353-S5).
2. The `irpt-holdings` pass-through replay, then which packaged copies validate at serve (round-172 item 1), then the builder's
   `account_id` (its host bundle also carries the 49F temp-file fix, when the host is next Online).
3. The fe-s-18 truth decision and generator repair (W350-S1, W346-S2/S3), carried.

-- 1.0.0_SA_CTO~DELL2
