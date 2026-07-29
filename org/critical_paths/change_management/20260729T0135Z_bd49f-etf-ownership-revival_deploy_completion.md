# DEPLOY LEDGER: bd-49f-etf-ownership-daily REVIVAL (monolith re-source + scheduled floor)

**Owner:** `0.7.0_AE_CloudOps~A` · opened 2026-07-29T0135Z · **STATUS: OPEN**
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
| 1 | Code: vendored DS compute module (verbatim @1667aa073d) + new thin shell handler | pending |
| 2 | Local QA: dry-run compute 07-27, cent-exact diff vs DS~A's landed slice | pending |
| 3 | TF: env cleanup + IAM Sid `MonolithFactRpsRead` (fact_rps/* EXACT) + list statement + floor rule/target/permission (3) | pending |
| 4 | source-map entry refresh | pending |
| 5 | safe-commit (gate: if NEVER#2 gate denies the monolith ref -> STOP, report, fallback world) | pending |
| 6 | zip build + artifact upload (content-sha256 metadata, yang-lambda convention) | pending |
| 7 | targeted plan -> battery report to CTO+COO -> safe-apply -> 0-diff re-plan | pending |
| 8 | tag bd-pipeline-v{next} | pending |
| 9 | Post-apply battery: get-role-policy applied-truth; sims single-arn (target fact_rps allowed; positive control separate; T8 negatives: blackdiamond/* deny, eclipse/* deny, json/* deny, platinum/* deny, cot deny, cross-prefix write deny); describe-rule ENABLED; get-policy Sid | pending |
| 10 | Ledger close + RAVC2 to CTO+COO | pending |

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
