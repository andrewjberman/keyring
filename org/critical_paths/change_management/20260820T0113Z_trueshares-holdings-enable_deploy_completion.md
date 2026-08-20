# Deploy Completion Record
**Date opened:** 2026-08-20T01:13:06.866238+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260820T012037Z
**Deploy:** TrueShares standing-egress ENABLE (Andrew-direct 0057Z): deploy the flag-reading code THEN set TS_HOLDINGS_ENABLED=1 -- the flag alone is a no-op on the deployed bytes
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | etfs-netassets-daily artifact rebuilt from current source (carries TS_HOLDINGS_ENABLED read + the TrueShares fetch path) | built package marker counts | Rebuilt from current source (pipeline name is derived from tf_file -- 'etfs-netassets', not 'etfs-pipeline'; first attempt refused loudly on that). BUILT artifact: 2 members (lambda_function.py, landing_guard.py), 55,993 B of .py, TS_HOLDINGS_ENABLED x2, trueshares x16, TrueShares x9. Flag read PRESENT in the built artifact -- the precondition for the env var meaning anything. | CLOSED 20260820T012036Z |
| L2 | verify | TF adds TS_HOLDINGS_ENABLED=1; plan enumerated from plan JSON | plan shows code hash + the env var, nothing else | Plan enumerated from plan JSON (denominator 3 resource_changes, 2 no-op): module.etfs_netassets_daily.aws_lambda_function.this UPDATE with exactly -- environment gains TS_HOLDINGS_ENABLED="1" (BRONZE_BUCKET/BRONZE_GRAMMAR/ETFS_BUCKET/SILVER_ROOT all UNCHANGED), source_code_hash 4/6gMExwwY1w3No9D4AeTARMXZaVjDHf1cBYq7yL5gw= -> tHeVS53pKxV4hX9UXciJsigvO8t5v10T3CmN2VwQURI=, s3_object_version bumped. No IAM, no sizing, no schedule. BOTH HALVES OF THE ENABLE IN ONE ACT. | CLOSED 20260820T012036Z |
| L3 | verify | safe-apply matches the staged plan exactly | apply counts == plan counts | safe-apply (HALTGT passed): 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed' == the staged plan exactly. | CLOSED 20260820T012036Z |
| L4 | verify | 0-diff on-target re-plan | No changes | 0-diff on-target re-plan: 'No changes. Your infrastructure matches the configuration.' | CLOSED 20260820T012036Z |
| L5 | verify | DEPLOYED BYTES read the flag AND the applied env carries it -- both planes | deployed package TS_HOLDINGS_ENABLED > 0 AND get-function-configuration env shows =1 | BOTH PLANES, which is the whole point of this ledger. PLANE 1 applied config: State=Active, CodeSha256=tHeVS53pKxV4hX9UXciJsigvO8t5v10T3CmN2VwQURI=, LastModified=2026-08-20T01:18:32Z, Environment.TS_HOLDINGS_ENABLED = 1. PLANE 2 DEPLOYED BYTES (package downloaded post-apply): 55,993 B of .py (was 49,871), TS_HOLDINGS_ENABLED x2 (WAS ZERO), trueshares x16, TrueShares x9. So the running code READS the flag and the applied env SETS it. Pre-apply the flag was 0-in-deployed / 2-in-repo, i.e. setting the env var alone would have applied clean, shown green, and fetched NOTHING on a forward-only source. | CLOSED 20260820T012036Z |

## Log

- 20260820T011306Z OPENED by 0.7.0_AE_CloudOps with 5 leg(s)
- 20260820T012036Z LEG L1 closed: Rebuilt from current source (pipeline name is derived from tf_file -- 'etfs-netassets', not 'etfs-pipeline'; first attem
- 20260820T012036Z LEG L2 closed: Plan enumerated from plan JSON (denominator 3 resource_changes, 2 no-op): module.etfs_netassets_daily.aws_lambda_functio
- 20260820T012036Z LEG L3 closed: safe-apply (HALTGT passed): 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed' == the staged plan exactly.
- 20260820T012036Z LEG L4 closed: 0-diff on-target re-plan: 'No changes. Your infrastructure matches the configuration.'
- 20260820T012036Z LEG L5 closed: BOTH PLANES, which is the whole point of this ledger. PLANE 1 applied config: State=Active, CodeSha256=tHeVS53pKxV4hX9UX
- 20260820T012037Z CLOSED -- all 5 legs proven
