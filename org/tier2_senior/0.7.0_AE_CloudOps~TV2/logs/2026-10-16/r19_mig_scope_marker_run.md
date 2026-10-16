# TCKT_VNEXT R19-MIG: scope_all_firms written on 19 of 19 staff PROFILE rows, MIG-OK -- 0.7.0_AE_CloudOps~TV2

**archetype:** DEPLOY
**Date:** 2026-10-16
**Task Order:** TCKT_VNEXT.TO-R19-MIG.staff-profile-rows-carry-the-explicit-global-scope-marker
**Status:** COMPLETE

---

## Objective

Write the attribute `scope_all_firms` = BOOL true to exactly the active internal PROFILE rows of `opal-users-v2` that carry no `allowedFirmIds`, so the fail-closed firm scope of the ticket service (S134 item 3) does not lock them out when `TO-R19-REL` ships. Procedure and bounds: the never-widen pair `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R19_MIG/R19_MIG_PAIR.md`.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open / close-leg M1-M4 / close | PASS | entry opened at STEP 0, closed 4 of 4 after MIG-OK |
| r19_mig_apply.py (this seat's applier) | select, apply | PASS | counts 19/3/1 of 23; written 19, failed 0, readback_bad 0 |
| r19_mig_check.py (issuer) | AC1 invocation | PASS after correction | first run MIG-BAD (issuer defect, blob 24286f537272); corrected blob af529513ba89 printed MIG-OK |
| commit-gate.sh | on the applier | PASS | py_compile, ds-precommit, ruff clean |
| proof-of-spec-check.py | with --governing-order | PASS | VALID rc=0, 0 violations |
| comp-* graph tools | not run | SKIPPED | one DynamoDB attribute write on a table named by the pair; no Lambda, IAM or infra change, so no graph dependency to check |

**What worked:** the ledger tool and the proof checker named their own refusals (the instance must sit flat under deliverables/ for a flat-layout order). **What failed:** the rail denied one call that used `find`; the first sweep of 70 worktrees (one git call per entry per tree) ran 30+ minutes, and one `git grep` per tree did it in seconds. **Gap found:** none in the tools; the issuer's check mis-classified a non-list `allowedFirmIds`.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Conditions: CTO half SIGNED; pair blob at HEAD `ee84f96d70` = the half's RE-SIGN section (the half's header still names revision 1 `a4dd43f239f2`; read the RE-SIGN section per issuer msg 9007); order blob `558473dce2f9` = pair row | both reads printed in R19_MIG_RESULT.json |
| 1 | NEVER-2 denominator: 70 worktrees, 70 read OK, 0 read failures; `git grep opal-users` over `.open_deploys/` at HEAD | 3 trees hit, all stale snapshots of `irpt-fwd1-run-20261015` / `-run2-` (both CLOSED on trunk, close commits `e25b646f7e`, `faf23f293f` ancestors of HEAD); shared tree incl. dotfiles: no hit; positive control found a known entry in 7 trees |
| 2 | Ledger opened | `tckt-vnext-r19-mig-scope-marker-20261016`, 4 legs |
| 3 | Selection read (ConsistentRead scan, SK=PROFILE, firmId=opal-capital) | 23 internal; 19 selected; 3 with allowedFirmIds; 1 not active; ScannedCount 86; all equal the pair |
| 4 | 19 conditional update-items (`attribute_not_exists(allowedFirmIds) AND attribute_not_exists(scope_all_firms)`) | written=19 failed=0 |
| 5 | ConsistentRead read-back of 19 | marker BOOL true, sha256 of every other attribute equal to before: readback_bad=0 |
| 6 | Check, first run (signed blob 24286f537272) | `MIG-BAD 1 active internal row(s) have neither a non-empty list nor the marker` |
| 7 | Cause measured read-only (types only) | the one string-valued `allowedFirmIds` service row, key c56e4e2e507b; pair leaves it unchanged; surprise row `TCKT_VNEXT-D2-S55` filed |
| 8 | Issuer corrected the check (msg 9027, commit `357bbd02af`); I verified blob `af529513ba89` equal at HEAD and in the tree, read the diff (one classification line) | MIG-OK |
| 9 | Proof-of-spec instance, order flipped to complete, commits | `699ba8dd77` (run), `b8cc41d8f7` (close); both LOCAL on box/dell2 (only the integrator pushes the shared branch, hook LD-0367; `ls-remote` tip `6c8e76f0e0` carried neither) |

## Verification

```
python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R19_CHECKS/r19_mig_check.py
MIG-OK rows_written=19 markers_live=19 internal_rows_scanned=23
```
Proof-of-spec: `VALID (rc=0)`, instance `org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/TCKT_VNEXT.TO-R19-MIG.staff-profile-rows-carry-the-explicit-global-scope-marker.proof_of_spec.json`.

---

## Decisions Made

- Row keys in every output and file are the first 12 hex of sha256(PK): 7 of the 23 internal PKs embed an email address, so the CTO condition (opaque keys only, no address) could not be met with raw keys. The real keys lived only in the applier's memory.
- Condition (b) read from the CTO half's RE-SIGN section, on the issuer's stated reading (msg 9007). Declared in the instance.
- Nothing rolled back after MIG-BAD: the 19 writes matched the pair and the offending row was never touched.

## Blockers

None for this order.

## Current State

`opal-users-v2`: 19 active internal PROFILE rows carry `scope_all_firms` = BOOL true; the 2 list rows, the disabled row and the string-valued service row (c56e4e2e507b) are unchanged. The release (`TO-R19-REL`, `TO-R18-REL`, `TO-R18-RUN`) was not started. Rollback if ever needed: release first, then `REMOVE scope_all_firms` per row (match by sha256-12 of PK). Files: `org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r19_mig/` (applier, before-hashes, result) and the closed ledger `org/critical_paths/change_management/20261016T0407Z_tckt-vnext-r19-mig-scope-marker-20261016_deploy_completion.md`. Order status: complete.

## Next Steps

1. `[2.0.0_SA_COO~V2]` Disposition surprise row `TCKT_VNEXT-D2-S55`; decide whether the CTO half (which binds check blob 24286f537272) needs a re-read now that the check is af529513ba89.
2. `[2.0.0_SA_COO~V2]` The string-valued service row is refused 403 "malformed" by the released code (`lambda_function.py:426-429`); rule whether that service identity calls the ticket service.
3. `[0.0.0_AB_MSTR]` Carry commits `699ba8dd77` and `b8cc41d8f7` from box/dell2 in the integration window.
