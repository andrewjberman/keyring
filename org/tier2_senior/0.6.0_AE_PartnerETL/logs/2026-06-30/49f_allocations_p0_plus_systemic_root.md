# 49F allocations certified-$0 P0 + systemic-root grounding + all-BD-silver restore

**archetype:** DIAGNOSE
**secondary_archetypes:** DEPLOY, COORDINATE
**serial:** 0.6.0_AE_PartnerETL | **date:** 2026-06-30 | **window:** ~18:53Z -> ~19:35Z (follows 49f_unfreeze_431167_provision_silver.md)

## Summary

Mid-evening, COO escalated a SECOND 49F P0: silver/allocations empty 06-26+ -> C_02 certified_aua would compute $0 tonight (silent-wrong, worse than the frozen $1.815B). Drove it to a verified restore, then grounded the SYSTEMIC root (one BD-pull instability ~06-26 starving multiple feeds) + restored ALL canonical-feeding BD dated-silver to 06-29. Outcome: tonight SAFE-HOLDS $1.815B (no $0); the clean ~$1.83B@06-29 un-freeze lands on TOMORROW's scheduled gold pending ~B's canonical-advance verify.

## Allocations P0 (restored + verified)

- ROOT: pull-STOPPED, NOT facts-empty. Allocations template 390224 facts INTACT (1 fact, id25 Market Value). The REST pull landed empty 4,592B freshest-date stubs 06-26/27/28 (T-1 timing, no retry-net) -> silver 46KB stubs -> certified $0.
- FIX (re-pull + merge, no re-provision): re-pulled 06-29 (32,633 rows/12.85MB) + 06-26 (32,634/12.79MB) on persisted 390224 -> landed ALLOCATIONS_DAILY_{06-26,06-29}.xlsx (overwrote empty stubs); cleared the stale 06-26+06-29 entries from incremental_allocation_manifest.json (backups .bak-20260630T19{00,16}Z; ~B GO'd me owning the clear); ran merge --allocations.
- VERIFIED: silver/allocations/2026-06-29.parquet = 6,812 rows / 1,200,866B / account_market_value SUM $1,828,446,414.98 (gross, 6,812 nonnull); 06-26 = 6,807 rows / 1.21MB. == healthy 06-24 grain (6,811 / 1.2MB) vs 46KB stub. => certified ~$1.8B not $0.

## Systemic root (grounded, COO's bigger ask)

ONE BD-pull instability ~06-26, SELECTIVE (not total): allocations + unrealized went empty 06-26+; transactions + realized kept flowing. Signature = the 3.5-day session dark gap 06-26..28 (secret-version history) + SS&C MFA fragility. => the persistent-login v2 design (a120ccfc8) is the SYSTEMIC durable fix (whole-firm multi-feed-freeze prevention), Andrew-sequenced into ADVI_BDAPIMIG.

## All-BD-silver-fresh (the 3rd-feed = gold canonical built FROM the silver)

Grounded (comp-pipescript io): canonical/holdings (B_00) <- A_03 positions_cube[<-alloc+unrealized] + silver/allocations + silver/realized + silver/unrealized; canonical/performance (C_00) <- B_03 account_gains[<- silver/transactions + canonical/holdings + B_02 canonical_lots]. So the "3rd feed" is NOT a separate pull -- it's the canonical built from the BD silver. Status of the canonical-feeding DATED silver @06-29: allocations (06-26+06-29 RESTORED), unrealized (06-29 RESTORED), realized (fresh), transactions (fresh -- CORRECTED an earlier misread: old TXN_DAILY naming stopped 06-18, but new TRANSACTIONS_DAILY REST is fresh 06-26..29; silver/transactions/06-29=15MB already landed).

GATE RESOLVED (~B 193624Z): the legacy silver/unrealized/unrealized_gain_loss.parquet is NON-GATING for the canonical DATE-advance. B_00 reads it ONLY for the CUSIP->asset_name bridge + account-self-heal (both try/except graceful, WARN+continue on empty). B_00's holdings DATE = latest_alloc_date = max(allocations) (B_00:217) = 06-29 = MY restored silver/allocations/06-29, and 06-29 is UNSEALED (max sealed=06-26) -> buildable. => canonical_holdings advances @06-29 on the restored allocations ALONE; the empty legacy compact does NOT block it. (The legacy-compact refresh = a LOW-PRI follow-on: ~B owns the B_02 repoint to dated partitions; I need not build a compactor.)

## Tonight = CONFIRMED-CLEAN (was planned safe-hold; ~B's grounding upgraded it)

- ~B CONFIRMED-CLEAN for tonight's 23:00Z: canonical advances @06-29 (from my restored allocations, the date-driver) -> client_perf @06-29 -> cert reads alloc/06-29 = ~$1.83B -> clean un-freeze. My BD-source restore (alloc 06-26+06-29 + unrealized 06-29) IS the fix; no separate positions pull needed.
- The only remaining decision = SERVE-vs-HOLD (Andrew's default HOLD until reconfirm; COO relaying). The advance is ~$1.83B@06-29 vs the held $1.815B@06-24 = not a surprise drop, a soft serve call. Floors intact regardless (~B's no-$0 guard b5a95c9f5).
- ~B co-verifies the canonical advance + served outcome on the 23:00Z run; I co-verify the served-flip + penny-test with CTO + 0.7.0.

## Compiler Tools

| run | result | note |
|---|---|---|
| comp-pipescript io C_00/B_00/B_03/B_01 | PASS | grounded the canonical dependency chain (BD silver feeds) + the legacy unrealized_gain_loss read; pinned that the "3rd feed" is the gold canonical, not a separate pull |
| comp-which (Schwab persist earlier) | n/a this window | provision/test-pull/merge/secret-forensics have no comp-tool -> rail-checked raw aws/SSM (the BD-REST + EC2-run + S3-version class) |

What worked: comp-pipescript io mapped canonical_holdings/performance inputs in 4 calls, refuting the "separate positions pull" framing. What failed: none. Gap: no comp-tool for BD-DataMining REST pull / EC2-run / silver-merge / S3-manifest forensics (the whole 49F restore class) -- candidate comp-tool family.

## Briefs written

49f_persistent_login_design_20260630.md (v2, a120ccfc8 -> CTO notes folded f7ff02eb7) -- the systemic durable fix; Andrew-sequenced into BDAPIMIG.

## Blockers

None. Remaining un-freeze step (canonical advance on tomorrow's scheduled gold + ~B's legacy-compact determination) is a legitimate external/other-lane gate, not an assumption-block.

## Current State (handoff)

- silver/allocations: 06-26 (6,807) + 06-29 (6,812) non-empty; silver/unrealized: 06-29 (102,862); silver/realized + silver/transactions fresh @06-29. All canonical-feeding DATED silver fresh.
- OPEN: silver/unrealized/unrealized_gain_loss.parquet = empty 7,573B @06-26 (legacy producer, ~B's lane) -- the potential last gate to tomorrow's clean advance.
- Manifests: incremental_allocation_manifest.json 06-26+06-29 cleared+reprocessed (backups taken). bd-allocations (i-0800437d1dbb0b5cc) STOPPED.
- Cert tonight: SAFE-HOLD $1.815B (guard + run/data-date mismatch). Tomorrow: clean ~$1.83B@06-29 pending ~B.
- SI2/Schwab (0.6.2 lane): 08242234 CRS20260629 landed in validation prefix; cadence resolved (daily/late, 20:35Z window, Andrew 08242234-only). RLW not-daily (Fri/weekly) -- flag for RLD ingest robustness. Separate from tonight's BD-fed un-freeze; I co-verify at S1-repoint.

## Next Steps

- **[0.4.0_DS_ClientPlatform~B]** confirm canonical/holdings + canonical/performance advance to 06-29 on tomorrow's gold from the restored silver; determine if the legacy unrealized_gain_loss.parquet is binding + its producer (refresh if so).
- **[0.6.0_AE_PartnerETL]** (me) co-verify the served-flip + certified penny-test tomorrow AM w/ CTO + 0.7.0; own the allocations RETRY-NET + the persistent-login/runner under ADVI_BDAPIMIG; co-verify 49F Schwab-scope at the SI2 S1-repoint; fold RLW-not-daily into the 49-schwab-conv RLD handling.
- **[2.0.0_SA_COO / 1.0.0_SA_CTO]** tomorrow's served-flip GREEN co-sign; sequence ADVI_BDAPIMIG (the durable session-hardening + runner productionization).
