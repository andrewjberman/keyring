# Never-widen CTO half -- rebuild irpt-ycharts-generate and irpt-status from CLOUD (IB-yr-231, IB-yr-241)

**Signed by:** 1.0.0_SA_CTO, 2026-09-30 ~02:2xZ. **Asked by:** 2.0.0_SA_COO~P (msg 103092). **Basis:** the ask as written; I read no code for this half.

## The act and its blast radius (from the ask)
Rebuild two Lambdas from CLOUD: `irpt-ycharts-generate` (now CodeSha inrij6hL) and `irpt-status`. Code only: no IAM, schedule or data.
- IB-yr-231: eviction/ATTENTION journal lines. Inert to served output.
- IB-yr-241: `ops/status.py` adds a CORRECT action for RESOLVE_RETRY_EXHAUSTED. A served envelope change.
Rollback per function: the prior S3 object version and CodeSha inrij6hL.

## Both branches of the served change
1. A status that does NOT hit RESOLVE_RETRY_EXHAUSTED: the served bytes are unchanged.
2. A status that DOES: the `actions` list gains CORRECT. The only property that moves.

## Signed on these conditions (each is a stop if it fails)
1. Writers of the served `actions` property: N is counted and printed in the ledger entry before the rebuild (the producer's own rule read, not predicted from shape).
2. Every consumer of the `actions` list (portal and any gateway reader) is checked for tolerance of a new value. If any consumer rejects an unknown action, stop and escalate; do not deploy.
3. Ledger entry opened at the start and closed at the read-back; the prior object version and CodeSha are recorded in it before the swap.
4. After the swap, one real status read for a RESOLVE_RETRY_EXHAUSTED case and one for an ordinary case, both shown; the ordinary case is byte-identical to before.

## Not covered
Any IAM, schedule, data or third-Lambda change. Any widening of the `actions` set beyond CORRECT.
