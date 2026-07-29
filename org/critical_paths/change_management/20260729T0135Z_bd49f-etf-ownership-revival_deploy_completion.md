# DEPLOY LEDGER: bd-49f-etf-ownership-daily REVIVAL (monolith re-source + scheduled floor)

**Owner:** `0.7.0_AE_CloudOps~A` · opened 2026-07-29T0135Z · **STATUS: CLOSED 2026-07-29T0155Z -- ALL LEGS COMPLETE, NOTHING STRANDED**
**Authority chain:** Andrew-direct ~0106Z/~0113Z (writer order, COO-recorded verbatim 011436Z) ->
CTO ratification 013015Z (recommended monolith design; freeze exception granted, standard battery)
-> CTO addendum 013139Z (NEVER#2 explicitly cleared for the monolith read, STOP-not-override if the
commit gate denies; window choice mine per COO 011043Z item 4).
**Window choice: TONIGHT, stated per the addendum.** Why: the writer proves at tomorrow's 10:45Z
fire, fully clear of the D2 evidence paths (15:00Z chain / 16:15Z publisher / 17:15Z emitter -- CTO
scope-checked no contention 013015Z); tonight buys the 07-28 slice at the first natural fire instead
of adding two more backfill days; and it keeps this deploy out of a post-freeze window already
carrying Design A + the 4c set.

## Legs (all-or-rollback, NEVER#6)

| # | Leg | Status |
|---|---|---|
| 1 | Code: vendored DS compute module (verbatim @1667aa073d, sha256 bc975c512d10... match) + thin shell | **DONE @08d0a9bff6** (commit-gate 2/2 clean) |
| 2 | Local QA: 07-27 dry-run vs DS~A's landed slice | **DONE -- 4/4 cent-exact, byte-shape IDENTICAL** (denominator 93,298 rows / 6,012 accounts) |
| 3 | TF: env trim + MonolithFactRpsRead/List + floor rule/target/permission | **DONE @08d0a9bff6** |
| 4 | source-map `files` refresh | **DONE @08d0a9bff6** (surgical 2-line diff; two earlier whole-file reformat attempts REVERTED before commit) |
| 5 | safe-commit / NEVER#2 gate | **DONE -- gate PASSED the monolith ref; CTO's STOP branch not triggered** |
| 6 | artifact build+upload (house build-and-upload.sh, sha256 metadata) | **DONE @b0608006f8** |
| 7 | targeted plan (3 add/2 change/0 destroy) -> pre-apply battery report to CTO 014450Z -> safe-apply (HALTGT passed silently; per Rule 18 a pass is not proof of not-halted -- noted) -> **0-diff re-plan: "No changes"** | **DONE 0146Z** |
| 8 | tag | **DONE: bd-v2.53.0** (pipeline convention is bd-vX.Y.Z, not bd-pipeline-v*; local -- push is COO's, rides --follow-tags) |
| 9 | Post-apply battery | **DONE 9/9**: applied-truth Sids present (get-role-policy); floor rule ENABLED cron(45 10 * * ? *); fn resource policy Sid SchedFloorBd49fEtfOwnership; TARGET fact_rps read allowed + POS-CTRL allowed + 7 negatives ALL implicitDeny (blackdiamond, eclipse, serve-json, serve-platinum, cot, cross-prefix write, monolith WRITE) -- every call single-arn, isolated |
| 9b | **Deployed-runtime exercise (behavior grade, Rule 22a + "deployed = downloaded AND imported")**: QA invoke `{"date":"2026-07-27"}` -> 200, no FunctionError, re-landed the slice at 01:51:44Z with values cent-identical (total 533,236,148.20). Import path + layer + in-situ IAM all exercised. QA instrument, not production evidence -- production evidence is tomorrow's 10:45Z floor fire. | **DONE** |
| 10 | Ledger close + RAVC2 | **DONE (this commit)** |

**Deploy-record substitution disclosed:** `record-terraform-deploy.sh` skipped (known tooling failure
noted in /cloud-ops: CHANGELOG writer + owned-paths hook on Andrew identity); its two map fields
(`last_deployed_commit`/`last_deployed_at`) updated by hand in this closing commit instead.

**ACCEPTANCE STILL OUTSTANDING (owner: this lane / successor): tomorrow's UNATTENDED 10:45Z floor
fire is the schedule's own evidence -- read the fire's OWN log (EVENT-IDENTITY line should show
source=aws.events), confirm daily/49financial/2026-07-28.json (or newest) landed with matching
vintage, and THEN retire the bd-tree Sids (ReadOwnFirmRpsSilver + ListOwnFirmRpsSilver) with their
own ledger line per CTO 013015Z. Do NOT manufacture the fire (NEVER#4).**

## Deferred (NOT tonight, recorded so they are not lost)
- bd-tree read path (Sids ReadOwnFirmRpsSilver + ListOwnFirmRpsSilver) retires on FIRST CLEAN
  SCHEDULED EMIT (tomorrow ~10:45Z), with its own ledger line -- not before, not silently (CTO
  013015Z condition). `-canonical` repo dir + `_stage_49f_canonical/` prefix stay parked exactly
  as-is (the ~4% basis decision is DS/DE/COO's, not touched).
- Design A (inf floor) apply: ratified, NOT freeze-excepted -- post-freeze window.
- Design B (MDPF read grant): HELD by COO pending the consumer trace.

## Rollback plan
Any leg fails -> `terraform apply` the prior artifact version (yang-lambda pins s3_object_version;
previous zip version retained by bucket versioning) + revert commit; floor rule resources are pure
adds, destroyable by targeted revert-apply. Escalate loud to COO+CTO per NEVER#6.

## Retirement line CLOSED -- 2026-07-29T10:52Z (0.7.0_AE_CloudOps~A)
First clean UNATTENDED emit CONFIRMED at 10:45:12Z (scheduled-floor rule fired, EVENT-IDENTITY
source=aws.events, RequestId a03a73d9; DENOMINATOR source_rows=93051 accounts=6016 universe
DIVZ,IDVZ,PFDE,PFOE day=2026-07-28; artifact daily/49financial/2026-07-28.json listing-verified
1305B ETag 2fb701cf @10:45:12Z; total_ownership=537,668,272.77 source_as_of=2026-07-28 = T-1
correct). bd-tree Sids (ReadOwnFirmRpsSilver + ListOwnFirmRpsSilver) RETIRED @ad91743c55, targeted
plan 0/1/0, safe-apply, 0-diff, live get-role-policy shows 5 monolith/etfs-scoped Sids only. Code
carries zero opal-data-bd references (checked at retirement). Tag bd-v2.53.1.
