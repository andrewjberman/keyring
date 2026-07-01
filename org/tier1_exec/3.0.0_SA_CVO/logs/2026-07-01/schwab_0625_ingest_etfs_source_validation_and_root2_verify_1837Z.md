# CVO session — ETFS source-validation (Andrew-challenged) + 49F Schwab 06-25 ingest + INFREF ROOT-2 verify

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, DEPLOY, COORDINATE

**Serial:** 3.0.0_SA_CVO | **Date:** 2026-07-01 | **Window:** ~17:00Z (last log: ETFS cert PASS) -> 18:37Z

## Summary

Andrew challenged my ETFS internal-scope cert ("you validated all the numbers?"). Correct challenge — my cert had validated INTERNAL CONSISTENCY (two rollups cross-footing) and over-labeled it "ingestion->presentation integrity." On the real SOURCE trace, all 3 firms tied to the cent; amended the cert honestly (49288d58a). The trace surfaced 3 data-completeness findings (49F Schwab freeze, inf 06-26 hole, cot producer gaps). Andrew then directed: (1) assess the Schwab EC2 box as a daily ETFS source, (2) ingest the 06-25 Schwab drop. Ran the 06-25 /49-schwab-conv (CVO under AE-exception) end-to-end. The Schwab freeze turned out to be a SHARED root behind DT's MDPF freeze + ETFS staleness + 49F custody-$0 — coordinated one fix (0.5.0 rolls 06-26..06-30). The inf 06-26 finding (ROOT-2) was root-caused + fixed by DS~A; I independently verified + RAVC-closed.

## Work done

### 1. ETFS cert — Andrew-challenged, source-validated, amended (49288d58a)
- Honest correction: the partner-rollup and ETF-rollup are the two MARGINS of the same per-partner-per-ETF matrix -> they sum to grand_total by construction (internal consistency), NOT source-correctness. Original cert overstated it.
- SOURCE TRACE (the real validation), all to the cent: 49F vs Schwab RPS (opal-data-bd/schwab/silver/rps/date=20260624) = $509,354,175.39 (+ distinct-account counts exact, caught 2 multi-lot dedup on PFDE/PFOE); inflection vs Orion holdings_2026-06-30 = $42,736,704.86; cottonwood vs Black Diamond holdings/2026-06-29 = $2,047,135.23. Grand total $554,138,015.48 source-grounded. Cert VERDICT (internal-scope PASS) STANDS + stronger.
- Method self-catches: 1st trace $0 (ticker fixed-width padding -> my join-key bug); 1st count off-by-2 (rows vs distinct accounts -> my error); missing-days first pass contaminated by `ls` mtime column -> corrected to filename-only.

### 2. Schwab EC2 box assessment (task #7)
- Box = i-0f3d57a97f14727af (SCHWAB_SSOT DERISK-1, Win Server 2022, SI2 UI-automation, acct 08242234). State running, 2d uptime, checks ok/ok. Daily accrual PROVEN 06-26 + 06-29 (full CRS incl RPS, T+1). RED FLAG: 06-30 partial (ACC+TRN only, no RPS) + ~13h stall since 04:36Z. Writes VALIDATION prefix (01_raw_quartz_validation/), not prod 01_raw/. Verdict: fresher than manual batch (RPS thru 06-29 vs 06-24) + directionally the right ETFS source, but NOT drop-in (validation-prefix, raw-not-silver, stability unproven, fragile GUI box). Durable answer = headless Path-C.

### 3. 49F Schwab 06-25 ingest (task #8, DONE) — see Deployment Sequence below
- Andrew's OneDrive drop = full 06-25 CRS set (12 files) + CRS20260630.RPS ("the single rps file"). Silver 6 tables 06-25 + rps also 06-30. Canonical 25/25. 49F ETFS positions now current to 06-30 (closes the 7d-stale).

### 4. INFREF ROOT-2 (inf 06-26 hole) — independently verified + RAVC-closed
- My 49288d58a finding (holdings_06-26 absent, silver present) -> DS~A root-caused (INF_B_00._bronze_assets_ok over-suppression: gate `overall==failure AND assets.status==fail`, and assets.status==fail is always-true expected_fail -> a TAX ReadTimeout holed 06-26) + fix 4cf997274 + re-emit. I INDEPENDENTLY verified against live: holdings_2026-06-26.parquet now EXISTS (re-emit 18:19Z), rows=11,482 / accts=796 / MV=$203,001,710.14 (ties to the cent). RAVC-CLOSED to DS~A. L6-residual (C_02/C_03 rolled series lack 06-26) -> SELF-HEAL on nightly (my call to COO; no ad-hoc force, aligns with my nightly-gated L6).

## Deployment Sequence + Verification (49F Schwab 06-25 ingest)

| Step | Command | Result |
|---|---|---|
| Sync (dry-run) | sync_schwab_onedrive_to_s3.py --since 20260625 | 12 CRS files pending, all 06-25 + CRS20260630.RPS |
| Upload | sync_schwab_onedrive_to_s3.py --upload --since 20260625 | 12 -> 01_raw/, 2 -> bronze/rps/ (exit 0) |
| acc | convert_schwab_acc_to_parquet.py | OK 20260625 (6,995 accts) |
| rps | convert_schwab_rps_to_parquet.py | OK 20260625 (91,137) + OK 20260630 (91,287) |
| trn | convert_schwab_trn_to_parquet.py | OK 20260625 (5,545) |
| trn_nna | convert_schwab_trn_to_nna_silver.py | OK 20260625 (126: 105 in / 21 out) |
| uln | convert_schwab_lots_to_silver.py uln | OK 20260625 (252,299 lots) |
| rld | convert_schwab_lots_to_silver.py rld | OK 20260625 (1,017 lots) |
| verify | s3 ls silver/{6 tables}/date=20260625 | all 6 non-zero; rps also date=20260630 |
| canonical | build_canonical_daily.py --date 2026-06-25 --upload | 25/25 steps OK (after date-format retry) |

**Finding (flagged, not patched — verifier lane):** `build_canonical_daily.py --date` needs HYPHENATED (`2026-06-25`); the skill's Step-7.5 example shows compact, which CRASHES `position_t0` (strptime %Y-%m-%d) + throws a gold_holdings NoSuchKey. Flagged to 0.5.0 (their roll-forward) + COO; updated the skill's last-known-state line.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| comp-which (ETFS artifact / Schwab box / inf CDN) | route | PARTIAL — routed to backstops (comp-freshness/comp-platinum/comp-routes); no comp-tool models the etfs artifact body, Lambda invoke, SSM, or a `_rebuild/`/validation staging prefix -> rail-checked raw S3/aws |
| comp-routes behaviors | ground the platinum CDN cache path (ETFS verify-channel edge) | PASS — [AUTH]-gated scoped behaviors + cache-control-injector confirmed |
| comp-glob (value_parity/silver/rebuild/etf scripts) | locate producers + configs | PASS |

What worked: source-tracing each ETFS cell to its firm's custodial holdings (Schwab RPS / Orion / Black Diamond) was the decisive validation — internal cross-foot could not catch a wrong-but-consistent source number. What failed: nothing broke. Gap: comp-freshness has NO Schwab coverage (consistent with prior notes); the etfs-ownership artifacts + the Schwab quartz raw are un-modeled by comp-tools — a coverage gap for a growing surface.

## MCP traffic

~24 messages. Significant: Andrew-direct (ETFS challenge + Schwab-assess + 06-25-ingest, via chat); DT cross-link (MDPF shares Schwab-freeze) -> I corrected 2-roots + RAVC; COO (holds MDPF dispatch / splits 06-26..06-30 to 0.5.0 / ROOT-2 driver / L6-timing ask); 0.5.0 handoff (collision-avoid, quartz-promote held for Andrew nod); DS~A ROOT-2 RAVC (verified + closed); notifies COO/DS/MSTR/0.5.0 on ingest completion.

## Blockers

None. Open GATES (external, not blocked): 0.5.0's 06-26..06-30 roll-forward pending Andrew's quartz->01_raw promote authorization; my L1/L6 + 49F /Advisors render-confirm + TAGATTR/cot served-verifies all gated on tonight's nightlies / the DT push.

## Current State (zero-context handoff)

- **49F Schwab silver:** complete through 20260625 (all 6 tables, opal-data-bd/schwab/silver/); rps ALSO 20260630. Canonical (opal-data-bd/canonical/schwab/{silver,gold}/) built for 06-25 (25/25). 49F ETFS positions now current to 06-30.
- **Remaining Schwab freeze:** 06-26..06-30 owned by 0.5.0_AE_OpalETL; raw in opal-data-schwab/01_raw_quartz_validation/ (needs promote to 01_raw/ — Andrew's held cutover-prefix decision).
- **ETFS cert:** internal-scope PASS + amended source-validated (aaec39a83 + 49288d58a). Push/SES = separate Andrew gate.
- **INFREF ROOT-2:** inf holdings_2026-06-26 re-emitted + CVO-verified ($203,001,710.14). L6-residual (C_02/C_03 06-26 row) self-heals on nightly. ROOT-2 was an INFREF registry-flip blocker -> now clear on the per-date layer.
- **Schwab quartz box:** i-0f3d57a97f14727af running, daily-accruing to validation prefix; 06-30 RPS stalled ~13h (0.6.2 owns; flagged to Andrew).
- **My open tasks (all external-gated):** #1 49F /Advisors render (DT push), #2 INFREF L1 (inf nightly), #3 INFREF L6 (inf nightly + confirm 06-26 in rolled C_02/C_03), #4 TAGATTR served-verify (bd nightly), #5 cot client_directory (cot nightly), #7 Schwab-box fitness (monitoring).

## Next Steps

1. **[Andrew]** authorize the quartz->01_raw promote when 0.5.0_AE_OpalETL asks (unblocks 06-26..06-30 roll-forward = rest of the shared freeze).
2. **[0.5.0_AE_OpalETL]** roll 06-26/06-29 (full) + 06-30 {acc,trn} from the quartz validation prefix (hyphenated canonical --date); RAVC COO.
3. **[2.0.0_SA_COO]** drive the downstream MDPF re-run (BD fees-gate + allocations recompute) once Schwab silver is 06-25->06-30.
4. **[3.0.0_SA_CVO]** on tonight's inf nightly: L1 pull-stage parity + L6 temporal-stability (incl. confirm 06-26 landed in rolled C_02/C_03); on DT push: 49F /Advisors render-confirm.

-- 3.0.0_SA_CVO
