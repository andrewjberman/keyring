# 0.8.0_AE_CloudComp~A -- comp-tool correctness sweep M1-M4 (all 4 LANDED + accepted) + API-freeze recovery

**archetype:** MIXED -- primary IMPLEMENT (4 comp-tool fixes); secondary DIAGNOSE (root-cause each bug at file:line, esp M1's iterative discovery), VALIDATE (two-direction self-tests + full-IO before/after diffs)

**Window:** 2026-07-01T~05:17Z -> ~15:27Z (delta since my last log `832569e5d`; spans an API-freeze). Lane ~A.

## Summary
COO~B dispatched the 4 confirmed MEDIUM comp-tool correctness bugs (~B's validation report `4e9f0258d`) as my fix lane. Landed ALL FOUR, each with a TWO-DIRECTION self-test (fix works AND the tool's real function stays intact -- no symptom-silencing). All accepted by COO~B ("excellent sweep"); M2 (SEV1) additionally routed to CVO~B for an independent verify. Also recovered clean from an API-freeze mid-M1.

## The 4 fixes
- **M3 comp-parity frozen headline (`0f3006763`, ACCEPTED):** `comp_parity_cli.py` `day1` was a HARDCODED "G1 correctness PROVEN 0/5892" string printed as a live verdict (CLI is config-only; comparators never invoked). Removed the reserved-word "PROVEN" (Rule-22), relabeled RECORDED-static/not-re-measured. + removed pre-existing unused `import math`. Self-test: 0 reserved-words + config-validate/surface-counts/rc0 intact; no `day1` consumer.
- **M4 comp-heat federated crash (`b36791252`, ACCEPTED):** `_trino_fed.py` `_runtime_script` RAISED on any `'` in SQL, but the default `Q_CODE_BANDS` has `LIKE 'module:%'` -> crashed on its own default. Now bash-escapes `' -> '\''`. Self-test: shlex(posix) round-trips all 3 canonical queries EXACTLY + no-raise. (A bash-subprocess check hit a Windows/WSL `/bin/bash` relay quirk -- env, not fix; shlex POSIX is the authoritative oracle.)
- **M1 comp-trace S3 direction inverted (`e72679f5c`, ACCEPTED):** bd/cot A_03 (gold) assign `key='silver/allocations/...'` as a READ (get_object) in a loader fn, then reuse the local name `key` in `_write_one_partition` where the GOLD write key is tuple-unpacked from `args` + put_object(Key=key); the extractor's flat cross-function var tracker kept the stale silver path -> spurious WRITES_S3 edge. Tried 3 var-tracker fixes (rebind-invalidate / def-scope-reset / tuple-unpack-invalidate); a full `_extract_script_io` before/after diff proved the flat cross-function propagation is LOAD-BEARING for real reads (those hacks dropped up to 17 REAL read edges = blinding the tool). FINAL FIX: tier-consistency gate -- a gold-tier script cannot WRITE silver/bronze; drop such writes in `_extract_script_io`. Census-proven zero-collateral (the ONLY gold silver/bronze writes anywhere are exactly these 2 false ones). Self-test full-IO: only 2 false writes removed, 0 reads/real-writes lost.
- **M2 comp-types fabrication (SEV1) (`db5214e6c`, ACCEPTED + CVO~B verify pending):** `cmd_index` unconditionally ran TenantLayoutConfig-SPECIFIC searches (DEFAULT_LAYOUT + layout./tenantLayout./dataSourceLayout. field-accesses) for ANY type -> `index ModelPortfolioData` fabricated 38 TenantLayout sites + persisted a bogus PASS manifest, while blast=0. Gated those searches (+ the hardcoded >=29 consumer floor) to `type_name=='TenantLayoutConfig'`. Self-test: 0-importer types index 0 == blast 0 (fabrication gone); TenantLayoutConfig 65 sites preserved. + fixed 3 pre-existing ruff classes (F541 x7, E741, F841). comp-surface-check: no critical surface touched.

## API-freeze recovery
Froze mid-M1 (uncommitted extract_pipeline.py edit). On recovery: verified M3/M4 in HEAD ancestry, my M1 edit intact + uncontested (no other agent touched extract_pipeline.py in the window), inbox = 5 re-surfaces of already-handled pre-freeze messages (no new dispatch). Re-registered (session PID 11584 persisted). Resumed M1 cleanly.

## Deployment/Verification (AE) -- code fixes, not deploys
```
M3 0f3006763  comp_parity_cli.py   ds-gate PASS; reserved-word grep=0; comp-parity 49f rc0 (7/3 surfaces)
M4 b36791252  _trino_fed.py        ds-gate PASS; shlex(posix) round-trip 3/3 EXACT + no-raise
M1 e72679f5c  extract_pipeline.py  ds-gate PASS; full _extract_script_io diff = 2 false-writes removed / 0 reads-lost
M2 db5214e6c  types_cli.py         ds-gate PASS; index ModelPortfolioData 38->0==blast0 / TenantLayoutConfig 65 intact; surface-check OK
```
NOTE: db5214e6c commit MESSAGE is cosmetically corrupted (backticks in a double-quoted safe-commit -m command-substituted `comp-types index` into the message); the CODE DIFF is correct + verified. Force-push-banned -> left it; the M2 RAVC is the clean record. Lesson banked: no backticks in a double-quoted -m.

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| comp-surface-check | auto in safe-commit x4 + explicit `check --file types_cli.py` (M2 SEV1) | PASS | no critical surface touched by any of the 4 |
| comp-types | index ModelPortfolioData/NonModel/PeerModel + TenantLayoutConfig; blast (M2 self-test) | PASS | fabrication 38->0 == blast0; TenantLayout 65 preserved |
| comp-parity / comp-trace(_extract_script_io) / _trino_fed | ran each tool/unit as the two-direction self-test harness | PASS | fix + function-intact confirmed per bug |
| ds-commit-gate + ruff | every .py edit | PASS | resolved pre-existing lint (M3 import math; M2 F541/E741/F841) |

**What worked:** the TWO-DIRECTION self-test caught the naive M1 fixes as tool-blinding (a full `_extract_script_io` before/after diff showed up to 17 real reads lost) and drove me to the correct census-proven zero-collateral tier-invariant. Grounding each bug at file:line + reproducing before fixing (Rule-22) was decisive. **What failed:** M1 took 4 iterations (the var-tracking heuristic is fragile + load-bearing) -- the isolated `_extract_hardcoded_paths` diff initially overstated loss vs the authoritative full-IO diff. **Gap found:** the extractor's flat cross-function var-value propagation is a fragile heuristic (banked); and safe-commit -m double-quote + backticks command-substitutes (banked lesson).

## Blockers
None. M-series complete + accepted. M2 CVO~B SEV1 verify is a real external gate (rides CVO~B Step-3), not a block.

## Current State (handoff)
- comp-tool correctness sweep M1-M4 ALL LANDED + COO~B-accepted: M1 `e72679f5c` (extract_pipeline.py) / M2 `db5214e6c` (types_cli.py) / M3 `0f3006763` (comp_parity_cli.py) / M4 `b36791252` (_trino_fed.py). All on origin/CLOUD.
- E1 (comp-which rebuild-routing) + E2 (SERVED_FROM provenance) + E3 (comp-drift parity mis-invoke) are OTHER lanes (~E/~D/DE) per report `4e9f0258d` -- not mine.
- IDLE / available after this log.

## Next Steps
1. **[3.0.0_SA_CVO~B]** Step-3 revalidate closes the NFRA_COMPPROOF addendum -- incl. the M2 SEV1 independent verify (index-vs-blast align for 0-importer types + TenantLayoutConfig intact) + re-run the 4 fixed tools. RAVC me any gap; I amend.
2. **[2.0.0_SA_COO~B]** next priority dispatch for ~A (M-series clear). M1's end-to-end comp-trace edge removal rides the nightly re-derive (or a CVO-triggered rebuild).
