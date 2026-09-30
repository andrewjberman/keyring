# IRPT_BCKEND decomposition -- ROUND 27, WORKSTREAM ~M (2026-09-30, 2.0.0_SA_COO~M, on rows W84-S3 and W84-S4)

Cut on 0.9.0_WK_IRPT_BCKEND~84's report of TO-IB-m26-261 (branch wk-IRPT_BCKEND-84 @bb9e765c4d: AC1 9 passed, AC2
AGG-CENSUS, AC3 HALF-READY, proof VALID) and its two rows. Rounds 20-26 ~M are issued, so this rides round 27
(GATE (x)). Both cells are remediations of ~M's own earlier cells. The issuer rules them inside its decomposition.

- **Row W84-S3 (the issuer's defect, from cutting IB-mr-251).**
  - The 251 face said a security the table does not know "refuses loudly by name". The worker built a BUILD refusal:
    `classify_security` raises `ValueError: REFUSED`. That has two consequences.
  - (a) A no-ticker SECURITY node, such as a Schwab cash sweep with identity `UNKNOWN:schwab:CASH`, fails the whole
    build, with or without a backfill. The suite reads 6 failed / 9 errors, all from this one root cause.
  - (b) After the MDPF_SECCLASS backfill, 76-601 held tickers per firm still stay unresolved (backfill census,
    @d0e5b687f3). A refusing Holdings build would therefore never complete.
  - The rule that governs is MDPF_SECCLASS PRD FWD-2: "a security with no entry is shown as unclassified by name,
    never quietly put into some class".
- **Row W84-S4.** The irpt-holdings Lambda resolves its packaged contract copy first, and that copy is staged three
  commits stale: it lacks the CATEGORY node kind, assigned_strategy and source_vendor_keys.
  - Measured by the issuer: `validate_slice` has no caller in the handler path (holdings/snapshot.py; only
    tests/test_snapshot.py:315 calls it), so the stale copy refuses nothing at serve time. The 2026-09-30 14:15Z
    fire is not at risk from it.
  - It is still a drift that 261's two new properties would widen, so it is re-staged here.

| cell | item | outcome | risk | depends on |
|---|---|---|---|---|
| `IB-mr-271` | The Holdings classifier serves a security the table lacks as UNCLASSIFIED BY NAME (no build refusal, no guess), and never looks up a node with no ticker (non-TICKER identity keeps its pre-251 path); the full investor_reporting suite passes whole; a real-build census at three firms | FWD-5 (Holdings classes) | WORLD (reads the table and firm buckets) | IB-mr-261 (same file) |
| `IB-mr-272` | Re-stage the irpt-holdings Lambda's contract copy from docs/contracts with the sanctioned stage tool; STAGE_MANIFEST carries the current pin; the Lambda's own suite stays whole. No deploy | FWD-5 | WORLD (gate floor for an infrastructure path) | IB-mr-261 (the contract it stages) |

Chains: A = 261 -> 271 -> 272 on slot `0.9.0_WK_IRPT_BCKEND~84`, in worktree wk_irpt_bckend_84. 271 edits 261's file,
and 272 stages the contract 261 changed. All of 251, 261, 271 and 272 stay HELD from CLOUD until the MDPF_SECCLASS
backfill writes (ruling @469c404474), and they drain together.
