# Consolidation drive: C12 ruled additions EXECUTED, C10 cash-source GROUNDED, C6/C7 reconciled

**archetype:** VALIDATE
**agent:** 0.4.0_DS_ClientPlatform (respawn per Andrew-direct; watcher task b08ufy1ew) · **window:** 2026-07-17 16:10–16:45Z

## What landed

**C12 (ruling-20 + ruling-16 additions) — DONE, accepted by CTO 163535Z.** Addendum committed
`163d7027b` (inventory §3a + WP8-DECOM xref on §2). Read-only set-difference per the 257 method,
denominators 15,602 / 187 / 21 legacy objects vs flat 4,539 / 4,548 / 110 / 105. **Headline: the
ruling's legacy premise is FALSIFIED** — `bronze/orion-api/` and `bronze/orion-api-v2/` are written
THROUGH TODAY (tax_realized/tax_unrealized/billing/performance_dim daily; v2's two JSON types daily
since 04-29); only `bronze/orion/` is dead. Unique content massive (tax 2,090/2,117 dates, billing
1,577, performance_dim 2,146-of-2,200 absent from flat). Per ruling 20(ii): all three → **Andrew-class
carve-out**; CTO carries the call. Ruling-16 coerced-only survivors re-measured post INF-restoration:
now **9 dates** (assets 5: 07-11..15; positions 4: 07-01/03/04/05), meter STOPPED (flat raw through
07-17). Zero S3 writes, zero deletions.

**C10 (cot cash-source grounding) — GROUNDED at source + derivation exercised live.**
`silver/allocations` frozen at 2026-07-09; pulled that parquet myself: **0 rows / 59 cols**,
cash_market_value sum=0/non-null=0 — the zero-row freeze artifact verbatim. Nightly
`cash_coverage_summary.json` regenerates (07-17 02:07Z) against the frozen partition, so cash stays
honestly UNMEASURABLE until the standing cot zero-row incident (07-09, close-nothing-on-it, not my
lane) is repaired. Derivation run read-only on the latest real holdings date **2026-07-15**:
state=PARTIAL, **$435,714,870.67 FLOOR** (securities only), 16,615 positions / 845 accounts, none
sampled; cash NOT MEASURED with the refusal stated. Nothing emitted — emission stays gated on C11
(staged on C3+C6).

**C6/C7 — reconciled folded-into-V2-8.** C6 registry authored+mutant-exercised; V2-8 folds it
("deploy it, don't re-derive"); C7 author-half complete, deploy leg completes inside V2-8
(0.7.0/0.6.2 lanes active through 07-16). No silently-open DS cell found; `pending` remains correct.

**WP8-DECOM cell 4 — OWNED, ACK'd to CTO 161519Z.** B_02.canonical_lots re-point off the
decommissioning opal-data-schwab UPPERCASE silver/ULN; blocked on 0.5.0's D2 redirect-target ruling;
AC (date + row-count tie) stated at execution time.

## Blockers
None mine. External gates: Andrew carve-out ruling (CTO carries) · cot zero-row freeze repair (owned
incident lane) · C11 emitter gate (C3+C6 deploys) · WP8-DECOM D2 ruling (0.5.0).

## Next Steps
- **[me]** C11-adjacent emitter work when C3+C6 deploy gates open; WP8-DECOM cell 4 on the D2 ruling.
- **[1.0.0_SA_CTO]** Andrew-class carve-out for the three orion prefixes (accepted, his board).
- **[cot incident lane]** allocations zero-row freeze repair → flips C10 cash to COMPLETE for free.

## Compiler Tools
| Tool | Result |
|---|---|
| `comp-glob "silver_registry*"` | 6 files + systems context — located the C6 registry estate footprint |
| commit via `safe-commit.sh` (`-F` file) | surface-check OK, comp-pulse reflex CLEAN (1 file vs 1,239 danger nodes) |
| generic `aws s3 ls` / boto3 list-objects-v2 | operational enumeration per C12 mandate (un-nudged class); full pagination, denominators printed |
No comp-pipescript io run: no gold script was edited this window (C10 was a read-only exercise of an
already-landed script; C12 is doc-only).
