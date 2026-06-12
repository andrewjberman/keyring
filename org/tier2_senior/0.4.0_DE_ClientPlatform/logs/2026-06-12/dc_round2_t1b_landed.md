# DC-round-2 (29 dead fns) LANDED + T1b RESOLVED (tool false-positive)
**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, VALIDATE
**serial:** 0.4.0_DE_ClientPlatform
**window:** ~2122Z -> 2155Z 2026-06-12

## Summary

Post-PORTALSWEEP follow-ups (v2.1.123). DC-round-2: removed 29 dead exported functions from the
shared advisor-intelligence.ts (Andrew-smoked on 5173, landed 0ac642ad). T1b: VERIFY-BEFORE-FIX
proved the "schema drift" is a comp-adapter-audit tool bug, NOT a portal drift — no portal change.

## DC-round-2 (DEV 0ac642ad)

- Scope grew 4->31 (RD page_inventory re-audit 6682c3d2c: 57 exports = 26 live/31 dead).
- Method: independent DE reachability census (external-importer + internal-call-graph -> fixpoint),
  resolved-path-verified, tsc as the net. Removed 29 dead fns; cleaned 20 orphaned type imports.
- tsc-net CAUGHT 3 false-positives: TIMESERIES_DIMENSIONS/SNAPSHOT_DIMENSIONS/VALID_DIMENSIONS back
  exported types (typeof X[number]) -> KEPT (census tracks calls, not const-refs). Reconciled dead
  set = 29 fns, not 31 (RD's 31 likely counted the 3 live consts).
- An automated brace-matching remover first corrupted the file (multi-line fn signatures); restored
  from backup, fixed the remover (paren tracking), re-ran clean. tsc/eslint/vite all green.
- Andrew smoked on local 5173 = zero regression (all 29 were 0-consumer). VALGATE D-1 PASS.

## T1b — getPlatinumClientDetailStatic "schema drift" = TOOL FALSE-POSITIVE (no portal change)

- comp-adapter-audit reported 43 SCHEMA-DRIFT WARNs (advisor-shaped fields book/role_breakdown/
  fee_summary/... "missing" from the client type InflecClientDetailRaw; real client fields
  household_id/display_name/accounts flagged TYPE-ONLY).
- ROOT CAUSE: adapter_audit_cli.py `_fetch_s3_raw_fields` (lines ~151-156) HARDCODES the S3 prefix
  to `platinum/advisors/{inflection_wealth_management,peter_lee}/` and fetched `{advisors}/detail.json`
  — but the fn reads `clients/{hhId}/detail.json`. It diffed the ADVISOR envelope against the CLIENT
  type. The "drift" fields are exactly getPlatinumAdvisorSummary.yaml's 16.
- GROUND TRUTH: `aws s3 cp s3://opal-data-inf/platinum/clients/100/detail.json` top-level keys =
  [accounts, advisor_key, data_as_of, display_name, firm_id, generated_at, household_id, summary]
  = EXACT 8/8 match to InflecClientDetailRaw. Portal type CORRECT.
- A blind T1-style backfill would have CORRUPTED the client adapter with advisor fields.
- Resolution: portal = no change (closed). Tool bug + stale YAML routed to graph/NFRA_GRAPHS owner.

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| comp-transform schema-check | AdvisorBookView/ClientsTab | PASS | live AI surfaces unaffected by DC-round-2 removals |
| comp-adapter-audit | getPlatinumClientDetailStatic | FALSE-POSITIVE | hardcoded advisors/ prefix -> wrong-envelope diff; root-caused |

What worked: tsc-as-the-net caught the 3 live DIMENSIONS consts a call-graph census missed; real-S3
ground-truth disproved the T1b "drift". What failed: automated brace-remover on multi-line sigs (fixed
with paren tracking). Gap found: comp-adapter-audit hardcodes the advisors/ S3 prefix -> false drift
on every non-advisor adapter; cached adapter-audit YAMLs for client adapters are unreliable.

## Files Modified

portal DEV 0ac642ad: advisor-intelligence.ts (-416 lines, 29 fns + orphaned imports). T1b: 0 files.

## Blockers

None. DC-round-2 closed; T1b closed (portal); tool fix routed to graph lane.

## Current State

- portal DEV HEAD 0ac642ad = origin/DEV. advisor-intelligence.ts down to live exports only.
- T1b: InflecClientDetailRaw verified correct vs live S3; no change. comp-adapter-audit prefix bug +
  stale getPlatinumClientDetailStatic.yaml flagged to COO for graph-owner routing.
- Whole D5 PORTALSWEEP + follow-ups done: ORPHAN-PM(19)+DC-01..07(7)+ROUTE-01+ORPHAN-AI/MISC(27)+
  DC-round-2(29 fns) = 82 dead files/fns purged + ROUTE-01 fix; T1b = verified-no-issue.

## Next Steps

- [graph/NFRA_GRAPHS owner via COO] fix adapter_audit_cli.py hardcoded advisors/ prefix (derive from
  fn body path); regen/remove the false client adapter-audit YAMLs; sweep other non-advisor adapters.
- [0.4.0_DE_ClientPlatform] standing by. v2.1.122 promote (DT) + v2.1.123 follow-up carry this work.
