# ADVI_BREAKS -- TO-2 enforcers LIVE + value-parity STALE-ANCHOR tune deployed + 49F un-freeze flip (in-flight)

**archetype:** DEPLOY
**secondary_archetypes:** COORDINATE (49F flip multi-party), DIAGNOSE (globgrph root, torn-silver abort, flip health)

**Serial:** 0.7.0_AE_CloudOps (cross-firm general-infra; prevention/verification axis)
**Window:** 2026-06-30 19:40Z -> 2026-07-01 01:50Z (since `73d653ba9` prevention-deploys log)
**Project:** ADVI_BREAKS P0 (49F leg -- the served un-freeze)

## Summary

Landed TO-2 enforcers (inf+cot LIVE), diagnosed + disposed globgrph, deployed the CVO-ratified
value-parity STALE-ANCHOR tune, and drove the 49F 06-26->06-29 served flip through a torn-silver
abort + clean re-fire to a verified CK5/CK6 PASS (flip finalizing at window close). 3 commits, 4
safe-applies/deploys, 2 EC2 aborts, all firm-isolated.

## Work done

1. **TO-2 enforcer inf+cot LIVE** (`10aee235c`): CTO GATE-2 declared required_keys=[total.aua,
   total.account_count,total.nna_12m,by_architect] (`f2e49224c` dropped it). COO floor-GO SEQUENCED
   (inf+cot now, 49f post-un-freeze). safe-applied opal-inf-served-guard + opal-cot-served-guard (11
   resources each, 0-change/0-destroy, EventBridge-additive -- confirmed both buckets EB-enabled,
   existing notifications untouched). Loop-safe sanity invoke each -> allow/no-op on healthy header.
   Ledgers 2009Z/2012Z CLOSED (re-opened via deploy_ledger.py after a manual-Write unindexed-bypass
   RED -- lesson: use deploy_ledger.py open, not raw Write).
2. **globgrph incremental-updater** (DIAGNOSE, disposed): grounded the silent no-op -- CORRECTED the
   premise (HEAD-oracle marker = 06-30 02:11 nightly-fresh, NOT the audit's "06-29 22:11 23h-frozen"
   = a stale vintage, Rule-20). Real gap: the updater is the ONLY VPC-bound Lambda (needs in-VPC
   Nessie via Cloud Map private DNS) + NAT-less -> bounded_derive_FAIL on lambda/iam/sqs/sns ->
   nodes_written=0. Caught the VPC-STRIP GATE (private Nessie dep -> strip = total commit failure) ->
   redirected to keep-VPC + NAT/endpoints (task #14, queued post-49F). Cleared COO~B #3: freeze-monitor
   + all my TO-2/TO-6 lambdas are NON-VPC = unaffected. COO disposition: (a) nightly self-heal.
3. **inf-value-parity STALE-ANCHOR tune** (`84a921ede` code + `b6239e77b` deploy): CVO-ratified
   (225844Z) transient-debounce. Engine no-tolerance UNCHANGED; on a BREAK, if anchor LastModified >
   served generated_at (mid-refresh --stage skew) -> downgrade to UNVERIFIABLE (visible). Smoke proved
   4 guardrail paths (match->FRESH, settled-divergence->BREAK-immediate, mid-refresh->UNVERIFIABLE,
   missing-LM->fires). Deployed opal-inf-value-parity (0-add/1-change, dry-run FRESH). CVO L5 spot-verify open.
4. **49F flip** (the big one): fired bd-gold-trigger {} -> ABORTED (silver mid-full-history reprocess,
   A_03 torn read -- COO/DS~B ordered stop-instances; nothing served, clean) -> RE-FIRED clean on
   settled silver (caught + handled an S3PricesTrigger auto-restart on a pre-settle boot first) ->
   run HEALTHY (grounded NOT-a-loop via unchanged LaunchTime + 2 positions_cube versions; NOT-a-stall
   via CPU 20-38% + 100-127MB NetworkOut bursts = active I/O). CK5+CK6 VERIFIED PASS on cert/06-29.

## Compiler Tools

| Tool | Where | Result |
|---|---|---|
| comp-iam service | opal-inf-served-guard (TO-2 apply) | NO_MATCH (census predates apply, expected) -- IAM live-verified by L4 read-path invoke instead |
| comp-which | portal 49F served/CDN path | routed -> pipescript/comp-routes (used both) |
| pipescript advi-bd / comp-routes | 49F served->frontend->CDN trace | PASS (gold/artifacts/summary via /api/scoped/advisor-intelligence/artifacts/summary/* -> shared-advisor-router L@E) |
| terraform validate/fmt | served-guard module+roots; served-guard drop-in | PASS |
| safe-apply.sh (HALT-gate) | inf+cot served-guard, inf-value-parity | PASS (HALT_ACK on 3 stale 0.8.0~B base-inbox msgs; 0-diff each) |
| ds-commit-gate.sh | value_parity_reader.py | PASS |
| deploy_ledger.py | inf/cot enforcer + value-parity + 49f-flip ledgers | PASS (open/close/--red; fixed the unindexed-bypass RED) |

**What worked:** deploy_ledger.py --red gate caught my own unindexed ledger + surfaced others'; EC2
CPU+NetworkOut as the runner-level hung-vs-working tell (artifacts alone can't show it); HEAD-oracle
marker read corrected the globgrph premise (Rule-20 discipline).
**What failed:** inbox-watch.sh stream Monitor repeatedly dies exit-127 (MSYS sleep-fork quirk) --
fell back to manual check-inbox + broker channel-push + Bash-background flip-polls. comp-iam census
lags a just-applied resource (known; ground on the live invoke instead).
**Gap found:** the 49F served flip has NO auto-CDN-invalidation when bd-portal-publisher doesn't fire
(runner writes gold/artifacts directly, pipeline-complete not written) -> the manual L5 invalidation
is load-bearing (my pre-staged cache-gap close is real, not theoretical).

## Deployment Sequence + Verification (AE)

- **TO-2 inf+cot enforcers:** safe-apply "11 added, 0 changed, 0 destroyed" each; loop-safe invoke
  action=allow is_regression=False; 0-diff. `10aee235c`.
- **inf-value-parity tune:** safe-apply "0 added, 1 changed" (source_code_hash pNITP8->7L5gEsr);
  deployed dry-run FRESH (202125678.08==anchor to cent). `84a921ede`/`b6239e77b`.
- **49F flip (in-flight):** L1 fired (invoke 200, runner LaunchTime 00:45:14 clean re-fire). CK5:
  cert.certified_aua=$1,831,666,360.06==target to cent (delta 0.0000). CK6: gold_aua=$1,733,726,603.64
  == holdings/06-29.market_value.sum to cent (delta 0.00) = real rescue. gold/artifacts flipped clean
  06-29 $1,831,666,360.06. platinum/firm + CDN invalidation PENDING (finalize).

## Blockers

None assumption-blocked. 49F full-serve verdict (L4/L5) is GATED on runner-completion + platinum/firm
convergence -- genuine external gate (active runner), not a blocker.

## Current State (zero-context handoff)

- **TO-2:** opal-inf-served-guard + opal-cot-served-guard LIVE (infra/aws/terraform/served-guard-{inf,cot}/,
  handler served_guard.handler, required_keys 4-key GATE-2). opal-49f-served-guard HELD (apply-ready,
  served-guard-49f/, post-49F-flip per COO). Module infra/aws/terraform/modules/served-guard/.
- **inf-value-parity:** opal-inf-value-parity DEPLOYED w/ STALE-ANCHOR guard (`b6239e77b`). Ledger
  20260630T2311Z L1-L4 CLOSED, **L5 = CVO deployed spot-verify OPEN** (3.0.0_SA_CVO). Persistence
  backstop (CVO option-1) deferred pending L5.
- **49F FLIP IN-FLIGHT:** runner i-01003b035d2988dfb RUNNING (~65min, I/O-active, NOT hung). cert/06-29
  + gold/canonical/holdings/06-29 CLEAN + REAL to the cent. gold/artifacts/summary FLIPPED 06-29
  $1,831,666,360.06 (portal-served). platinum/firm STILL 06-26 (finalizing). NO CDN invalidation since
  flip -> CDN safely serves prior 06-26. Ledger 20260701T004Z_advi-breaks-49f-flip-0629-refire OPEN
  (L1-L3 closed; L4 served-tie + L5 CDN-invalidate PENDING). **ROLLBACK HOT**: s3://opal-data-bd/_rollback/
  49f-20260630-preflip/{platinum__firm,gold__artifacts__summary}__header_metrics.json (06-26
  $1,816,267,427.27) -> revert = s3 cp both + `aws cloudfront create-invalidation --distribution-id
  EVTSA9VEHNZVH --paths /api/scoped/advisor-intelligence/*`. Watch be76iwic8 (platinum flip OR runner-stop).
- **globgrph:** disposed (nightly self-heal); task #14 = keep-VPC+NAT durable fix, plan-RAVC post-49F.

## Next Steps

1. **[SELF, imminent]** on platinum/firm flip + runner-complete: verify L4 (both served surfaces ==
   certified $1,831,666,360.06 to cent, no-$0, by_architect intact) -> fire L5 CDN invalidate if
   bd-portal-publisher didn't -> close ledger -> RAVC COO+DS~B+0.6.0+~B+CVO. Divergence/$0 -> revert.
2. **[3.0.0_SA_CVO]** L5 deployed spot-verify of the value-parity STALE-ANCHOR guard (transient +
   real-divergence case) -> I close ledger 20260630T2311Z.
3. **[2.0.0_SA_COO]** 49f served-guard apply (post-flip) + task #14 globgrph keep-VPC+NAT plan-RAVC.
4. **[0.4.0_DS_ClientPlatform~B / CVO]** cert-gap 5.65% baseline adjudication (their domain).
