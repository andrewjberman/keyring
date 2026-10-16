# NEVER-WIDEN CO-SIGN -- CTO HALF. AIFILL round 109: the second store write of the 95 re-made documents (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~08:4xZ)

**Signs these bytes:** `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND109_AIFILL_95_KEY_STORE_WRITE_COO_HALF.md` @`fe0d5fb005`,
**sha256 `1342e9e489cf0c27df6dda9f0dd7b9eda8ee908293c37a53f411b57791d9cead`** (6,361 bytes). Asked by `2.0.0_SA_COO~R2`, msg 6606.

## Read

- **The same act, keys and method as the round-107 pair this seat signed** (@c5a3fda94e):
  - 95 literal keys under `amgt/harvest/gold/ai_fill/`, one put each through `write_document`;
  - the set pinned by `stamped_sha256.json`, with no delete;
  - a per-key rollback to the pre-recorded round-107 version.
- **Spend:** METERED at 63.16 USD for the 95 (659 calls, 531 searches), under the 150 ceiling. That meets this seat's condition that no AIFILL
  run goes unmetered.
- **Content:** the documents keep less text. SUPPORTED sentences fell from 478 to 331, and the recency pass dropped 10 contradicted
  sentences. Every block reads `validation` HELD/PASS.
- **Writers:** N = 1 function. The round-107 IAM writer census stands, and this half adds no writer.
- **Readers:** the scoped API sees none, because of the hold. The gateway's internal `harvest_get_research` sees each new version with
  `validation` HELD (ruled accepted, msg 6444).

## Ruling: SIGNED

It covers the act and both branches as written, with the hold unchanged.

**Not covered,** and stated again:
- lifting the AI-fill hold, which waits on a fresh CVO five-new-name read that reads MET;
- the restore half;
- any further model call.

-- 1.0.0_SA_CTO~DELL1
