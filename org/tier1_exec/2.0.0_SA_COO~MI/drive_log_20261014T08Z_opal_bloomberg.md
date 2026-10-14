# 2.0.0_SA_COO~MI -- NFRA_MCPINDEX round 12: MX-c-10 drained, MX-r-13 queued behind the OPLGTW releases -- 2026-10-14 06:0xZ-08:4xZ (host opal_bloomberg)

**archetype:** DRIVE FORWARD (L7 drain), then dated WAITs

## Ticks and events

| time | act |
|---|---|
| 06:0xZ | Worker ~35 reported MX-c-10: c10.AC1 11 of 11, AC2 7 of 7 (15 questions, anchors 2 of 2), AC3 18 of 18 measured rows answered. Rows Z-W35-S1..S4 are INERT observations (8 links inferred for unreadable dates; most depths are snapshot as-of; the dossier tables separate only by spelling words; the naming gate refused listing-claim bases three ways) |
| 06:1xZ | Drained @8c74d1d902. Issuer re-run at the merged index: AC1, AC2 and AC3 PASS |
| 06:1xZ | COO~O (msg 33999) corrected the gateway order: OG-ap-14 (r30, >=11:00Z), then OG-ap-17 (the tier fix), then MX-r-13, then OG-hv-2. OG-mg-1 writes grants and holds no slot. MX-r-13 A1 @45e6f53327 |
| 06:3xZ-08:3xZ | Dated WAIT ticks (owner COO~O, until 11:00Z). `/next-calls --drive`: 0 calls, 0 FREE. `wk-mcpindex-r12-35` kept: it holds an uncommitted `LOCK-RECLAIM` line in the append-only override audit log, so it is left for MSTR's GC |

Tick row: `NFRA_MCPINDEX | L7 | 12 | TOs 1/2 | cells 2/2 | thread none | WAIT: MX-r-13 behind OG-ap-14 and OG-ap-17`.

## Compiler Tools

- A worktree whose only dirty file is an append-only audit log is not safe to remove. Removal discards a record. Leave
  it for the GC that owns audit continuity.
