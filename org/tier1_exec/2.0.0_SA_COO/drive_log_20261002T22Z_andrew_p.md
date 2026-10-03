# Drive log -- 2.0.0_SA_COO~P -- 2026-10-02 22Z (host andrew)

Substantive /canonical-drive IRPT_BCKEND ticks of the hour, from org/mcp/drive_ticks/2.0.0_SA_COO~P.md.

## tick 46 -- 2026-10-02T22:20Z -- lease FULL (both)
| IRPT_BCKEND~P | served act | 35 | IB-pr-221 SERVED (legs C1 S0 P2 P3 G1 F1 closed @8c10791252; A1 Monday) | covered | n/a | DRIVE FORWARD (the signed deploy) |
| IRPT_DASHBD B | L7 | 5-6 | DB-b-11 drained @0637b0787d; DB-b-12 running; DB-b-13 queued | covered | y | DRIVE FORWARD (drain + spawn) |
- Disk fell to 2.1 GB (another seat's 2.5 GB worktree + a 1.17 GB pack); MSTR told; MSTR then removed 6 worktrees and 14.8 GB of provider caches (incl. ours) -> 22-33 GB free. Andrew-direct ~20:3xZ: drained worktrees are removed by their owner -> coo-p-pr275 removed (its two edits proven equal to committed 2b3048bd22 and the held patch; branch merged).
- IB-pr-221 (both halves; CTO batch 185): C1 PASS + hashes equal; S0 @718716fb60; P2 49F producer kKgvbKtG (dry runs before/after identical, 7,570 rows); P3 Inflection 7 resources (dry run = rebuild census); G1 @2b3048bd22 under an audited lane override (IRPT_BCKEND_FAST_Y_TFPOLICY; CTO told) + IAM simulation (INF allowed, COT denied); F1 adapter /K1eLPu (probes equal; INF 226 YTD 0.0240 on deployed bytes = chain; 49F value unchanged, NET->GROSS; 10 clean log minutes). CTO told.
- DB-b-11: population 7,570; producer ~22 s/day; publisher must shard (8 x ~67 s); backfill ~1.1 h in-region; rows W1-S12..S14.
- Next: the mirror release packet (stray key skip + second schedule @2e00498347, its own packet after the serving packet).
