# 0.7.0_AE_CloudOps — session 1720-1955Z (MDPF P0 rows 10/13/16/18, freeze measurements, cot-rebalancer scan)

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, VALIDATE, COORDINATE

## Window
2026-07-24 ~1720Z (launch) -> ~1955Z. 6 base-serial commits, ~14 MCP messages handled
(COO GO/law-change/routing/STOP, CTO GO/conflict-resolution, ~A AC-5 interface, ~B handover,
MSTR commit-ask, Andrew-direct pause). No deploys, no applies, no pushes. Ended under
Andrew-direct fabric pause (~1943Z), then Andrew lifted the hold to me directly (~1953Z) and
approved the cot-rebalancer report commit.

## What I did

**MDPF_CHANNEL_INDEPENDENCE closure P0 — scope rows 10, 13, 16-L1, 16-L2, 18 (two files: the
trigger Lambda + the dispatch script). ONE owner, one applier (CTO-confirmed) after ~B and I
collided live in the trigger file.**

- **Row 10 (scheduled floor)** @5c3ca9e7fc. Gave MDPF its own `cron(0 20 * * ? *)` DAILY-INCL-
  WEEKENDS floor (NOT MON-FRI -- the cron deleted 06-08 was weekday-only and missed the Sat T+1
  INF reconciliation). Door-6 event retained as accelerator; plan `3 add / 1 change / 0 destroy`,
  accelerator untouched at plan level. `_record_deferral()` = retries-or-records, fail-open,
  deterministic run_id into ~A's manifest. DLQ policy widened to both rules IN PLACE (a 2nd
  aws_sqs_queue_policy would have plans-clean drifted -- self-caught). BUILT+VERIFIED, NOT APPLIED.
- **Row 18 (Stage-6 fail-closed)** @3baf75902 + @ccb5718c3. Made the REVAMP producer present-or-
  FATAL, symmetrical with the feeder guard. FIRST cut placed it at the Stage-6 block (post-serve)
  -> would have emitted ChainFailed on a run whose serve SUCCEEDED; MOVED it to the S3-sync block
  (pre-publish) @ccb5718c3. Self-caught. Exercised both directions in isolation (absent->rc=1,
  present->rc=0). REPO-TRUE / RUNTIME-UNVERIFIED.
- **Row 16-L1** BUILT then REVERTED. Exercised the spine-exemption against the REAL dict shape:
  `_check_inf_spine` returns {source,fresh,as_of,error}; `_partner_asof` reads latest_partition/
  prefixes -> returns '' -> floor still DEFERS via must-fix-C. Reverted rather than ship
  `is_floor` that reads as a fix but isn't. Sized L1 as THREE changes, not a flag flip.
- **Rows 13/16-L2** scoped, not built (paused before).

**Freeze/measurement findings (all positive-controlled):**
- **Graph/drift freeze** @52abe228c. COO's 14:22Z billing-block hypothesis FALSE (nightly graph
  landed 02:08:59Z, writes post-block). Underneath: stitch-source.zip FROZEN 17 days (missing
  PORTAL_REPO_PAT, proven on a run 10h pre-block, publish step skipped) + opal-stitch-produce
  FAILED 4/4 nights (derive_stitch.py exit 2, undiagnosed). Clearing the block fixes neither.
- **THE FINDING OF THE DAY: mdpf-daily-trigger was NOT FIRING, not firing-and-failing.** Zero
  invocations 07-19..07-23 (5 consecutive days), Errors=0 throughout. Positive-controlled against
  opal-assets-mdpf-portal-publisher (datapoints on those exact days). INF marker stopped landing
  07-18 -> Lambda never called -> every error alarm read GREEN through a 5-day client-facing
  freeze. Caught the follow-on gate candidate defect: an invocation-count floor goes green on
  today's 5 deferrals; must key on dispatched:True.
- **07-23 residual (INFERRED, marked so):** publisher has NO event-source-mappings, NO resource
  policy; invocation days == Andrew's CreateFunction/UpdateFunctionCode days exactly. Reading:
  the "working" state is a person running a Lambda by hand, not a working pipeline. LIMIT stated:
  CloudTrail lookup-events is management-only, Invoke is a data event -> not principal attribution.

**MSTR EC2 GitHub-Actions runner** @683e06ceb -- committed under my lane at MSTR's ask (owned-
paths correctly blocked them). Reviewed not rubber-stamped: found 2 declarative-drift defects
(role description + policy comment both claimed a `secret-read` grant that was deliberately
removed). Re-verified independently: validate Success, plan 6-add/0-change/0-destroy. NOT applied.

**cot-rebalancer strategy-level Opal scan** @5e718bf35 (Andrew-direct, read-only, committed with
his express approval post-pause). See Current State.

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| comp-glob / comp-grep | locate rebalancer+blackdiamond code | PASS | on-rails, systems-context |
| comp-which | route roll-source lineage (row 16/17) | PARTIAL | near-tie, refused to guess (correct) |
| pipescript --resource | consumers of platinum/mdpf/aggregate_aua | WARN | 39-day-stale snapshot named MY key as its OWN staleness exhibit -> UNDETERMINED, per Rule 20 |
| comp-pipescript io | cot rebalancer gold script I/O | PASS | 5 monolith silver reads |
| comp-iam (implicit, rule) | -- | -- | flagged NECESSARY-NOT-SUFFICIENT for the row-13 new-prefix grant |

**What worked:** comp-glob/grep + comp-pipescript io grounded the cot pull chain cleanly.
**What failed:** the graph lineage instruments could not answer the row-16/17 question -- pipescript
snapshot 39d stale (self-declared), comp-kuzu unresponsive (0 output >7min earlier). Reported to COO
as row-19 substance (deployed-vs-repo / stale-instrument blind spot), 3rd-4th instance today.
**Gap found:** comp-tools-first (Andrew ~1924Z) currently unsatisfiable for mdpf lineage because the
graph producers (stitch chain) have been frozen 17 days -- the directive lands as its producers are dark.

## Blockers
None of mine. Halted (not blocked) under Andrew-direct fabric pause ~1943Z; hold since lifted to me
directly for the cot report commit. Downstream/adjacent (evidence-cited, not chasing):
- [Andrew/IT] PORTAL_REPO_PAT missing -> stitch-source frozen 17d. [undiagnosed] derive_stitch.py exit 2.
- [~B] owns s3://opal-data-mdpf/code refresh (M3); executing with CTO's 6 conditions + my rollback pin.
- [CTO] rows 13/16-L2 sequencing; the M3 code-refresh GO-vs-routing conflict (CTO resolved: ~B first).

## Current State (zero-prior-context handoff)

**Commits (all on origin/CLOUD except the last two -- push is COO/Tier-1):**
- 52abe228c graph/drift freeze measurement (deliverable)
- 5c3ca9e7fc row 10 floor: infra/aws/terraform/mdpf-pipeline/scheduled-floor.tf (new) + eventbridge.tf
  (DLQ policy) + mdpf-daily-trigger/lambda_function.py (FLOOR_SOURCE, is_floor, _record_deferral) +
  ledger 20260724T1830Z
- 683e06ceb MSTR runner: infra/aws/terraform/github-actions-runner/* + ec2/github-actions-runner/* +
  EC2_MANIFEST.json
- 3baf75902 + ccb5718c3 row 18: infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh (present-or-
  FATAL guard at the s3-sync block)
- 5e718bf35 cot-rebalancer strategy-scan report (deliverable)

**Deploy state:** NOTHING applied to live AWS this session (all AWS calls read-only). Row 10 (TF) and
row 18 (EC2 shell) are repo-true, runtime-unverified. NONE count toward closure.
**Open ledger:** org/critical_paths/change_management/20260724T1830Z_mdpf-scheduled-floor-row10_
deploy_completion.md -- OPEN BY DESIGN, ZERO legs begun, no NEVER#6 exposure.
**Working tree:** clean on my paths.

**Rollback pin (for ~B's M3 refresh, handed over):** opal-data-mdpf versioning=Enabled;
code/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py = 51,999 B, ETag 283b395f660f0de09137282be00b1afe,
VersionId nLuWoyenxWPBDaYFTPj_xt7r_oH2BCCe. CAVEAT: bucket lifecycle config NOT read -> version
survival unverified; independent byte-copy pin still required.

**cot-rebalancer scan (Andrew-direct, read-only):** deliverable COT_REBALANCER_STRATEGY_LEVEL_OPAL_
SCAN_20260724.md. Finding: composition pull is MODEL_DETAIL_SCOPE=opal_closure (name-seeded, down-only)
-> strategies holding Opal models but not NAMED Opal are invisible. Roster (60) + accounts (912,
strategyName on every row) are raw-complete; only 25/60 compositions landed. Gaps on Andrew's list:
Anna *9237/*9238, Moderate Income Portfolio (non-opal-named, never pulled); Opal Satellite 15 does
not exist. Close-out = MODEL_DETAIL_SCOPE=all run -> reverse-attribute -> join holdings for per-Strategy
AUM. NOT executed (config change + live pull; Andrew's call).

## Next Steps
- [0.7.0_AE_CloudOps] On hold-lift confirmation to the fabric: row 16-L1 as 3 changes (spine exemption
  + partner-shaped inf record + roll-source via config not literals); rows 13 (roster-derived, prefix-
  scoped IAM via simulate-principal-policy) + 16-L2 (dispatch is_stale_partner for inflection).
- [0.7.0_AE_CloudOps] cot MODEL_DETAIL_SCOPE=all scope-change writeup on Andrew's word.
- [~B] M3 code refresh -> then row 10/18 acceptance is the next scheduled run (DEPLOYED-NOT-YET-EXERCISED).
- [CTO] rows 13/16-L2 gate; invocation-floor gate candidate (dispatched:True, not invocations).
