# bdapimig_bronze_sentinel_iam_cure.md

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE
**window:** 2026-07-06 ~13:07Z (COO DRIVE GO) -> ~14:53Z (leg closed) -- base 0.7.0, Monday post-holiday restart

## Summary
Drove the P0 ADVI_BDAPIMIG durable-REST leg to a PROVEN cure. Grounded the mechanism instead of the
framing: FALSIFIED the COO/0.6.2 "proxy-gap" hypothesis (box self-mints nightly, no proxy secret
exists) and pinned the 07-03 BD silver freeze to a clean IAM gap -- `bd-49f-runner-role` lacked
`s3:PutObject` on `opal-data-bd/bronze/*`, so the runner's `_BRONZE_COMPLETE.json` sentinel emit was
AccessDenied -> `bd-silver-merge` starved -> silver frozen while auth+bronze were healthy. Fixed via
`bd-v2.47.0` (1-statement additive grant), full deploy discipline, and EXERCISE-PROVEN end-to-end (the
exact put_object that was AccessDenied now succeeds -> all-4-silver PASS @07-02 + A_00 PASS). Caught
TWO false-greens before they shipped (force=true token-expiry re-fail x3; force=false stub-emit) and
filed the WS-5 durable-hardening findings that became the CTO-pre-approved Path-A design ref.

## Work done
1. **Startup** -- /watcher (registered LIVE, persistent Monitor `b4qa0wdw6`), /cloud-ops, org/XXX.md.
   Superseded the stale 07-02/03 NFRA_PPL49F pre-read directive with COO's fresh 07-06 13:07Z DRIVE GO.
2. **Root-cause (DIAGNOSE, source+live+log grounded).** comp-freshness bd: silver txn/realized/unrealized
   FAIL @07-03, allocations PASS (own trigger). Ground: box `i-0fa1846f` self-minted the cookie 07-06
   00:02:36Z (2min after its scheduled 00:00Z launch, datacenter subnet, device-trust set) -> proxy-gap
   FALSIFIED. Runner log run-2: landed ALL 4, failed=[], then `AccessDenied s3:PutObject on
   bronze/2026-07-06/_BRONZE_COMPLETE.json` -> sentinel starved -> silver frozen. Confirmed the sentinel
   IS the silver trigger (bd-49f-rest-runner-cutover-plan + s3-notifications.tf, ~A grounded) and the TF
   gap (bd-49f-interim.tf:441 = PutObject only on forwardfill_v2/*).
3. **FIX + deploy (DEPLOY): bd-v2.47.0.** Added Sid=EmitBdBronzeSentinel Allow s3:PutObject on
   opal-data-bd/bronze/* to bd-49f-runner-policy; DenyCotPlane firm-sep belt unchanged. safe-apply 0/1/0,
   0-diff, live get-role-policy verified. RAVC1/RAVC2 to COO+CTO, COO APPROVED, ledger 3/3 CLOSED.
4. **Exercise-proof verify (VALIDATE).** Grounded the durable blocker on the failed 07-02 invokes
   (3x identical): bearer-TOKEN expiry mid-txn-sweep (mint-once L124; 85MB newest chunk outlives the
   token) mis-classified as cookie-death (L147 short-circuits before the existing L158 re-mint). Caught
   the 2 false-greens (force=true re-fails; force=false emits on 4KB stubs via existence-only
   _already_landed). After 0.6.0's Path-B recovery (sequential real-pull -> no-force skip-all invoke),
   VERIFIED my grant PROVEN: runner log `OK: bronze sentinel emitted (tables=4)` 14:31:47Z, all-4 bronze
   REAL (stub-guard held), bd-silver-merge +0 err -> all-4 silver PASS @07-02. RAVC3 my-half COO-ACCEPTED.
5. **WS-5 durable-hardening findings filed** (docs/briefs/bd-49f-runner-durable-hardening-findings-
   20260706.md): (F1) _already_landed existence-only stub-skip; (F2) bearer-token-expiry -> Path-A
   401-handler token-remint design (CTO pre-approved, 4 conditions) + Path-A2 EC2/SSM compute-tier.
6. **Ledger** -- closed my leg on 0.6.0's bd-0702 un-freeze ledger (IAM exercise-proof gate PROVEN).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| comp-freshness bd | silver/gold freeze scope | PASS (txn/realized/unrealized FAIL@07-03; alloc PASS -- the light/heavy split) |
| comp-iam service bd-49f-runner | DESIRED role view | PARTIAL (can't see the put_object -- it lives in the runtime-pulled cot_bronze_ingest.py, not the lambda source; grounded on live get-role-policy instead) |
| comp-which | route box-launch-trigger + sentinel questions | PARTIAL (near-tie -> fell back to EventBridge inspection w/ rail-checked marker) |
| comp-grep | _BRONZE_COMPLETE emitter/consumer, policy TF, _already_landed | PASS (pinned the sentinel=silver-trigger + the L87/L132/L147 code) |
| safe-apply / terraform | bd-v2.47.0 apply | PASS (0/1/0, 0-diff, live get-role-policy verified) |
| deploy_ledger.py | 2 ledgers (deploy + bd-0702 leg) | PASS (deploy 3/3 CLOSED; bd-0702 my leg appended+closed) |
| safe-commit | 5 commits | PASS (pathspec-scoped, all pushed) |

What worked: grounding the MECHANISM (runner log + get-role-policy + emit source) falsified the proxy-gap
framing and pinned the exact IAM gap; the runner log's run-2 all-success-but-AccessDenied refuted ~A's
txn-gate hypothesis cleanly. What failed: comp-freshness/comp-iam alone couldn't ground a fresh-IAM
APPLIED claim or the runtime-pulled put_object -- needed live get-role-policy (rail-checked exception)
+ the CloudWatch runner log (PowerShell, MSYS leading-slash gotcha on the log-group name). Gap: none new;
banked the WS-5 findings for the durable tail.

## Deployment Sequence + Verification (AE)
**bd-v2.47.0 (bd-49f-runner-role +PutObject bronze/*):** edit bd-49f-interim.tf -> ledger OPEN ->
comp-iam gaps + `terraform plan -target` (Plan: 0 add/1 change/0 destroy, only EmitBdBronzeSentinel) ->
safe-commit c331393be -> push -> `safe-apply -chdir=... apply -target=... -auto-approve` (Apply complete!
0 added, 1 changed, 0 destroyed) -> 0-diff re-plan ("No changes. Your infrastructure matches the
configuration.") -> live get-role-policy (EmitBdBronzeSentinel=Allow s3:PutObject bronze/* PRESENT,
DenyCotPlane intact) [rail-checked: Rule-22a fresh-IAM APPLIED] -> tag bd-v2.47.0 + push --follow-tags
-> ledger ce4e191e4 CLOSED 3/3. **EXERCISE-PROVEN:** runner 14:31:46Z no-force invoke -> `OK: bronze
sentinel emitted for 2026-07-02 (tables=4) failed=[]` -> sentinel LM 22:21:24Z->14:31:47Z ->
bd-silver-merge invoked 14:31:50Z +0 err -> silver txn/realized/unrealized/alloc all PASS @07-02
(COO independently confirmed 14:43-45Z).

## MCP traffic
~30 messages handled. Significant: COO DRIVE GO (P0 BDAPIMIG lead) + RAVC1-approve (apply bd-v2.47.0) +
RAVC2-ACCEPT (discipline complete) + RAVC3-ACCEPT (IAM leg PROVEN, independent flip confirm) + Path-B-
tonight / Path-A-durable split. CTO arch pre-read (Path-A 401-handler APPROVED-in-principle, 4
conditions, bring-the-diff). 0.6.0: bridge-reads-only + box-minted-cookie confirm; force-invoke coord;
run_date 07-02 frontier correction; sentinel-FIRED + Path-A option-(i) authoring. ~A: lane-split accept
+ box-rollout-DONE correction + independent comp-iam corroboration (AGREES) + stub-guarded parity split.
RAVC opened+closed: bd-v2.47.0 (COO RAVC1->RAVC2->RAVC3, all accepted).

## Blockers
None. My IAM leg is COMPLETE + PROVEN. Remaining un-freeze legs (gold tail / served-content@07-02) are
0.6.0/~A's parity lane, in-flight (not my block). Path-A durable diff is gated on 0.6.0 authoring
(post-served-confirm) -- a real sequencing gate 0.6.0 chose, not a block.

## Current State (handoff)
- **bd-v2.47.0 LIVE + EXERCISE-PROVEN.** bd-49f-runner-policy now grants EmitBdBronzeSentinel (Allow
  s3:PutObject arn:aws:s3:::opal-data-bd/bronze/*); DenyCotPlane firm-sep belt intact. commit c331393be,
  tag bd-v2.47.0, both ledgers CLOSED (deploy 20260706T1338Z ce4e191e4 + bd-0702 leg 956713e91).
- **Un-freeze chain rolled healthy:** sentinel bronze/2026-07-02/_BRONZE_COMPLETE.json @14:31:47Z ->
  all 4 silver PASS @07-02 -> A_00 accounts_dimension PASS 14:46:44 -> gold in-flight -> served pending
  (0.6.0/~A close Legs C/D).
- **Durable blocker documented:** bd-49f-runner mint-once bearer token (lambda_function.py:124) +
  L147 401->auth_dead short-circuit (existing L158 re-mint unreachable for 401s) = token-expiry-mid-
  sweep mis-classified as cookie-death. Design ref: docs/briefs/bd-49f-runner-durable-hardening-
  findings-20260706.md.
- **Box-retire: CLOSED** (per CTO guardrail-a) until parity + N-nightly.

## Next Steps
- **[0.6.0_AE_PartnerETL]** author the ~12-line Path-A 401-handler diff (re-mint-once-on-401->retry;
  re-mint-fails->cookie-death; MAX_RETRIES=3 bound; idempotent per-tile resume) post-served-confirm.
- **[0.7.0_AE_CloudOps base]** DEPLOY the Path-A diff via TF + on-box verify when 0.6.0 pings it;
  own the A2 compute-tier leg (heavy/backfill pull -> EC2/SSM) when Andrew/CTO sequence it.
- **[1.0.0_SA_CTO]** formal-gate the Path-A diff (auth-chain; align w/ A-prime schwab OAuth §2.3).
- **[0.7.0_AE_CloudOps~A]** RAVC the box-retire parity precondition when served-content@07-02 clears;
  fold the runner-run/sentinel-emit-failure alarm (the high-value item from the F5/F6 reframe).
- **[2.0.0_SA_COO]** independent served-flip confirm when ~A RAVCs Legs C/D; DATA_PLATFORM DC1/DC2
  remain sequenced behind the durable leg (~A secondary).
