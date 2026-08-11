# CPR queue landed end-to-end: CPR-1 deployed x3, CPR-4 serve-released (4-step choreography), CPR-2+C-3 committed, CPR-5 second-target declared, X-iii DS half minted, both RECON-4 residuals closed

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DEPLOY, VALIDATE, COORDINATE

**Window:** 2026-08-11 0507Z (post-/clear reinstantiation) -> 0641Z. Event-driven seat; COO's
CANONICAL_PATTERN register (@014e7af672 -> @9029676799) drove the queue.

## What happened, in landing order

1. **Startup:** context-clear discriminators measured (broker PID 16056 = my session's MCP child of
   claude.exe 24072; TaskOutput(bcnfwc95f) -> running) -- watcher NOT killed, NOT re-armed (the MSTR
   false-positive class avoided). LD-0290 stamp written for session 610af0c3.

2. **CPR-1 (INF Sunday full-pull union-preserve, hard date 08-16):** two-commit protocol.
   Baseline @9b29609e42 (deployed bytes byte-exact into data/inf/scripts/gold/; drift vs deployed
   MEASURED ZERO -- md5=ETag 78f60cc7; register corrected MISSING_IN_REPO -> MISHOMED, manual_api
   twin byte-identical). Fix @9196959b53 (CRO~A draft + 2 review upgrades: FutureWarning mirror,
   preserve-set-keyed-on-PULLED-DATA semantics named). Twin sync @76386cd21c.
   **Deploy: ALL THREE S3 homes** (code/gold/ + code/manual_api/ + code/bronze/, each ETag=local
   md5 c78348204de8607a689abbcb29a3fbe1) -- caught that orion-gold-dispatch.sh sync_scripts()
   FAILS LOUD on differing-content basename collisions, so the gold-only deploy the dispatch
   implied would have refused the next INF chain sync. Acceptance 13/13 (T1 positive / T2 negative
   control / T3 mutant vs baseline) + live leg: carry set 26,371 rows / 16 accounts EXACT vs
   CRO~A's independent oracle. CLOSED by CRO~A RAVC + COO ("exemplary"). Carried: Sunday 08-16
   chain log must show the UNION-PRESERVE line (absence = fail).

3. **CPR-4 (non-fee-AUA residual retired from serving; scope upgraded by Andrew's @d272021791
   ratification mid-act):** fix @7341b27d50 -- served non_fee_earning_aua now FROM the billing
   is_fee_earning classified sum; subtraction survives ONLY as unreconciled_aua (signed,
   UNCLAMPED); acceptance 12/12 incl. negative-gap and mutant-vs-HEAD. Found the LIVE
   DEPLOY-SERVE-HELD sentinel the register's "no precondition" missed; did NOT s3-cp around it;
   NEVER#2 halves given (COO 055036Z conditional-4 + CTO SERVE-RELEASE-ACK 055259Z).
   **Executed the 08-05 choreography:** ledger OPENED BEFORE LIFT @d6ae6cbd73 -> lift @96334728b4
   (SERVE-RELEASE-ACK in-message) -> deploy ETag 4192c665 verified -> re-hold @c33d2e5260
   (sentinel verbatim :39, 79s open window; CVO-certified "textbook"). Shipped-delta control:
   deployed+sentinel == pre-CPR4 repo BYTE-EXACT, so the serve shipped the CPR-4 delta only
   (AoR-absence verified at bytes, not asserted). Step-4 republish: my 0558Z direct-SSM gold-d
   COLLIDED with CRO~A's in-flight chain (no trigger env exports -> fold-OFF stamp; C_01 refused
   clean; republish never executed). RULED (CTO+COO adopting CVO's split verdict): step 4 =
   PENDING-ON-SCHEDULED-13:47Z-CYCLE, QA flips are not evidence, steps 1-3 SATISFY the deploy
   obligation (state consistent+safe). Ledger amendments @a3440996f2 + @3a1769c018. CVO P1
   (stale step table + unowned step 4) discharged same turn. Exception-set retirement stays open
   for the CVO cert chain (13:47Z -> delta-cert -> exception-set exit -> spec sec3 amend).
   Standing lesson adopted: ad-hoc INF dispatches via inf-gold-trigger, NEVER direct SSM.

4. **CPR-2 + C-3 folded (cot retry-net double-lag + probe-universe anchor)** @ea2400401a:
   _window_for_asof ends the window exactly on the probed day (the sweep's re-pull of day d no
   longer lands d-1bd); AE's anchor diff verbatim (universe anchors at the primary's landing day;
   lag=0 degenerates); marker schema 1.1 adds universe_anchor (frame travels with the number;
   measured zero production readers of the old frame). ssm.tf order untouched (load-bearing).
   Acceptance: REAL window builders, mutant contrast on EACH half; 85 tests, 81 pass, 4 failures
   proven PRE-EXISTING on a pristine HEAD extraction. DEPLOY HELD to post-bar (timer 15:06Z,
   before the 22:30Z cot run) per COO.

5. **CPR-5 (second deploy target, CTO-ruled same-day)** @4100c90f47: cot tree second_targets
   declares opal-data-bd/code/bronze/cot_bronze_ingest.py (Model-B shared engine; bd role Denies
   opal-data-cot); deploy-flow leg with target-grain membership-guard semantics (exists=update
   ENFORCED, 404=LOUD skip, fail-closed probe). COO's aimed 3-target firm-agnostic predicate
   answered per-path with file:line: (#3) the bd runner NEVER sweeps (lambda_function.py:105-174)
   so C-3 is inert bd-side and the double-lag path never executed there -- the urgency premise
   held at the BYTES level, not the executed path; (#2) lag=1 both paths by design (bd explicit
   bd-49f-interim.tf:318, cot designed default @bf4c0aabbe); (#1) COT_MARKET_HOLIDAYS absent
   bd-side (real PRE-EXISTING divergence, not widened, bounded by the 0-row REJECT limb;
   routed as census fact). First carry rides the 15:06Z deploy.

6. **X-iii DS half (accrual bundle)** @7ce609e560: bundles.accrual_bridge in safe_deploy_core --
   deterministic hash-stamped tar.gz (script + roster materialized from the ONE committed
   authority), packaging INSIDE the deploy flow (push-gate routing + --mint-bundle), roster-only
   commits re-mint (config-leg class closed), SERVE-HELD respected, loose objects frozen as AE's
   rollback target. FIRST MINT landed + independently verified (download/extract/byte-compare +
   metadata echo; md5 2cec1a0c, script-sha 648cf3f5..., roster-sha e86e4631...). Delivered to AE
   2.5h ahead of estimate; AE applies post-bar, scheduled 14:10Z leg is the closer.

7. **RECON-4 residuals BOTH MEASURED + CLOSED** (COO queue): inflection 11/561 = the feeder's
   DESIGNED portfolio_{pid} fallback stubs (build_mdpf_wsc_inflection_feeder.py), all $0.00,
   custodian/household NULL -- real-account join 100.0%, zero AUA unjoined; RECON-4's "numeric
   long tail" corrected (0/11 all-digit, they are slugs -- name-vs-content specimen 4). 49F
   14/5,715 re-grained (11 nine-digit + 3 eight-digit over 14 DISTINCT; 12+2 was row-grain):
   nine-digit fully concentrated in ONE model (Opal Conservative Growth), no Schwab transform
   matches, custodian not nameable at rest; eight-digit = 2 closed Schwab accounts (departed
   2025-01..2025-07 window, 525 partitions) + 1 never-in-book. CRO folded all three @8f14253ae9.

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| comp-find | pull_inflection_transactions_rest (estate-wide) | PASS | surfaced the EC2 backfill dispatcher's code/bronze reference -- led to the triple-homing catch |
| comp-find | cot_bronze_ingest (infra/aws/lambda) | PASS | DEF-band showed bd-49f runners LOAD the script from opal-data-bd (the CPR-5 ground) |
| comp-find | oldest_still_incomplete\|retry_net | PASS | marker-age reader census: suite+doc only, no production consumer (C-3 check 1) |
| comp-find | COT_MARKET_HOLIDAYS\|BD_SNAPSHOT_ASOF_LAG_BDAYS (infra) | PASS | the CPR-5 predicate answers #1/#2 with file:line |
| comp-pipescript | deployed pull_inflection_transactions_rest.py --pipeline inf-gold | WARN | MATCH, but renders ONE aux:manual_api row for a TRIPLE-homed script -- instrument gap fed to CTO rows 1/2 |
| comp-pipescript | io INF_D_04 --pipeline inf-gold | PASS | write map (11 platinum keys) for the ledger's served-read target |
| comp-pulse | diff (via safe-commit gate, every commit) | PASS | fired the immune-response citation on cot_bronze_ingest -- led to reading the 06-25 bd-49f deploy record pre-commit |
| comp-find | first bd-lambda grep attempt | BLOCKED->rerouted | rail gate correctly denied a raw infra grep; comp-find answered it |

**What worked:** comp-find's DEF band separated "loads the script" from "mentions it" instantly --
the CPR-5 ground truth came from band structure, not reading. The gate-embedded comp-pulse citation
system worked as designed twice (read the cited deploy record before touching the danger node).
**Gap found:** comp-pipescript deployed models one home per script; triple-homed (CPR-1) and
second-target (CPR-5) scripts are invisible at their other homes -- both instances fed to CTO's
instrument-gap thread; second targets deliberately excluded from the per-file verify with the
mint/ETag verify named as their acceptance surface.

## Files Modified

See commit messages: @9b29609e42 @9196959b53 @76386cd21c @7341b27d50 @d6ae6cbd73 @96334728b4
@c33d2e5260 @ea2400401a @7ce609e560 @a3440996f2 @3a1769c018 @4100c90f47 (all pathspec-scoped,
own author line; commits LOCAL on CLOUD -- MSTR holds the push per LD-0367/0368).
Deploys (Rule 13, all ETag-verified): inf pull script x3 code homes; INF_D_04 code/gold (under
SERVE-RELEASE); mdpf-accrual-bridge.tar.gz first mint. Scratch harnesses (session scratchpad,
run-and-read, nothing standing): r1_acceptance_harness.py, cpr4_acceptance_harness.py,
residuals_measure/followup/final.py.

## MCP traffic

~25 handled. Significant: COO CPR dispatch + label remap + 3 acceptances + serve-release half +
step-4 ruling + CPR-5 staffing + predicate targets; CTO serve-release ACK + step-4 ruling +
cross-firm gate change + Andrew-direct free-egress record (session-scoped, does not survive
handoff); CVO P1 (discharged same turn); AE C-3 fold-in + X-iii joint plan + bd-side consumer
finding + CPR-5 targets; CRO~A CPR-1 draft/validation + collision FYI; CRO residual fold
@8f14253ae9; MSTR free-egress mirror.

## Blockers

None. (CPR-4 step 4 and the exception-set half are NAMED WAITS with owners and triggers in the
ledger, not blockers. CPR-2/CPR-5 deploy is a timer, not a block.)

## Current State (zero-context handoff surface)

- **CPR-1 CLOSED.** Sunday 08-16 read carried: INF chain log must show UNION-PRESERVE (owner: this
  seat, in COO's register).
- **CPR-4:** code deployed under a completed lift/re-hold; sentinel BACK at INF_D_04:39; ledger
  org/critical_paths/change_management/20260811T0554Z_inf-d04-cpr4-serve-release.md steps 1-3 DONE
  (CVO-certified), step 4 PENDING-ON-SCHEDULED-13:47Z-CYCLE (tick owner: this seat, on SERVED
  payload -- platinum/firm/dashboard.json on opal-data-inf carries unreconciled_aua; monitor
  bg7p7iu65 = early signal only; first value may be legitimately NEGATIVE). Exception-set exit =
  CVO cert chain, NOT this ledger.
- **CPR-2+C-3+CPR-5:** committed (@ea2400401a + @4100c90f47), NOT yet deployed. Timer (Monitor,
  15:06Z) fires the sanctioned run: `python .tools/safe_deploy_core.py
  data/cot/scripts/bronze/cot_bronze_ingest.py --author 0.4.0_DS_ClientPlatform` -- lands cot
  primary + bd second target, both ETag-verified. Check COO bar verdict first. Live confirms:
  22:30Z cot run prints universe_anchor; 49F leg-b = runner's next fire (~00:11Z, AE verifies).
- **X-iii:** DS half DONE + minted; AE applies post-bar (13:35-14:05Z), 14:10Z scheduled leg
  closes it, AE's ledger.
- **Watchers live:** inbox Monitor bcnfwc95f; served-artifact watch bg7p7iu65; deploy timer
  bvz9hq02u (15:06Z).
- **Minor open carry:** eclipse_id=31 crosswalk review -- registry v4 lacks id 31; the 08-09/08-10
  eclipse gold partitions surveyed did not surface a model-31 row under the checked column
  heuristics; needs one targeted read of model_portfolio_summary.parquet columns when convenient.

## Next Steps

1. [this seat] 15:06Z: fire the CPR-2/C-3/CPR-5 deploy (after reading [2.0.0_SA_COO] bar verdict);
   deploy record carries the leg-a/leg-b split; bd-side ETag to [0.7.0_AE_CloudOps] for leg-b.
2. [this seat] Post-13:47Z: tick CPR-4 step 4 on the SERVED read; evidence to [2.0.0_SA_COO] +
   [1.0.0_SA_CTO]; [3.0.0_SA_CVO] delta-certs the flip.
3. [0.7.0_AE_CloudOps] X-iii apply post-bar; [this seat] on call for the 14:10Z leg outcome.
4. [this seat] Sunday 08-16: CPR-1 UNION-PRESERVE log-line read.
5. Expected on the normal cycle, not tonight: R-a host mutex + R-b fold-mode single-homing
   (collision remedies, my lane per COO); the bd-side holiday-env census line ([0.7.0_AE]/CTO).
