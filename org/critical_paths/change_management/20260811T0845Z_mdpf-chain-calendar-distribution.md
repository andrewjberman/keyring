# Deploy-completion ledger: MDPF chain calendar distribution (WS-A recovery)

**Opened:** 2026-08-11T08:36Z (deploy-start) | **Closed:** 2026-08-11T08:50Z (same session)
**Operator:** 0.7.0_AE_CloudOps | **Trigger:** CRO~A 082623Z surface of an Andrew-direct MDPF
assessment (~0820Z): first post-INF-resumption chain run mdpf_daily_20260811_073903 died 07:40:59Z
in WS-A at 45.5%, NO partition written, bandaid floor stays.

## Mechanism (source-verified, not relayed)

`/opt/mdpf/scripts/gold/mdpf_calendar_binding.py:37` flat-sibling `import trading_calendar` ->
ModuleNotFoundError; `:44` repo-layout fallback -> ImportError; `:46` raises the ruled fail-closed
`CANONICAL CALENDAR ABSENT` (traceback read verbatim from
s3://opal-data-mdpf/telemetry/mdpf-daily-runner/logs/mdpf_daily_20260811_073903.log:236-263).

SCOPE CORRECTION vs the surfacing message: P1-2 (ruled scope = the mdpf-gold-lambda PACKAGE, COO
wave plan MDPF_CANRTE_WAVE_PLAN_20260806.md:55) LANDED (@a4d71e954, v2.2.0) -- the deployed lambda
zip carries trading_calendar.py + mdpf_calendar_binding.py at root (verified on the scratchpad copy
of the deployed zip). The defect is a MISSING SECOND-TARGET DISTRIBUTION LEG: the EC2 chain's code
store (s3://opal-data-mdpf/code/scripts/gold/) needs the same flat-sibling calendar and no deploy
mechanism carries lib/trading_calendar.py there (lib/ is outside safe_deploy_core's repo homes; the
P1-1 gold scripts THEMSELVES synced fine via the DS flow -- atomic-commit-not-atomic-deploy, same
class as CPR-5).

## Legs

1. **Land:** `aws s3 cp lib/trading_calendar.py s3://opal-data-mdpf/code/scripts/gold/trading_calendar.py`
   with metadata content-sha256=41b1c0c12651c62e59d27537a5bafb5bc34a3bb6562d94d57029a2f77ccac4c6,
   authority=lib/trading_calendar.py@0cbb0ad174d4786879466662b1f9a7c5f3d75b14. VersionId
   Oyi6Tkzg8Q1S6XqOA5fURyFVzMumf09X (08:36:56Z).
2. **Verify:** download-back sha256 == claimed sha VERIFIED; authority == deployed-lambda zip-root
   copy VERIFIED byte-identical (one calendar, two targets, zero divergence).
3. **Coverage check:** one copy suffices -- dim_* run with sys.path[0]=gold/; the cottonwood slice
   runs under COT_PYPATH whose FIRST entry is ${SCRIPTS_DIR}/gold (dispatch :546); the only
   assert_pmc_backend caller (mdpf_gold_consolidator.py:722) is NOT a chain stage, so pmc-absence
   on the runner cannot convert this fix into a Stage-6 refusal; the calendar fallback backend is
   holiday-correct through 2026 (binding docstring).
4. **Manifest:** EC2_MANIFEST.json mdpf-daily-runner gains `calendar_distribution` (this commit).

## INCIDENT NOTE -- concurrent duplicate land, and my own gate failure

My pre-land `head-object` was CHAINED in the same command as the `cp`, so when it returned 200
(key EXISTED, 08:33:17Z, ~3.5min earlier, EMPTY metadata, uploader unidentified from S3) the cp
fired anyway and overwrote. **The gate did not gate -- a precondition check whose result cannot
stop the action is not a control** (the exact class of
memory/feedback_verify_live_state_before_treating_mutation_as_noop.md, restated here because I
re-committed it while citing it). Blast: ZERO -- bucket versioning Enabled, both versions ETag
3de6a337e268614698943b038248113b (byte-identical; the prior actor uploaded the same authority
file), prior version ETxtlBXRIg.LgCxD5GXf2BOfU5Z2MqSV preserved. Surfaced same-turn to COO with a
who-uploaded question. Residual defect at MY seat, self-assigned rule: a state-gated mutation runs
as TWO tool calls -- read, STOP, then act on the read.

## Behavioral proof (outstanding, event-shaped)

The chain fires ONLY on INF's completion sentinel (no mdpf cron -- manifest cron_schedule field).
Next natural fire = INF's next completion (~13:01Z historically, IF the normal INF cycle completes
again today post its 07:38Z recovery completion; else tomorrow). The fixed store syncs at chain
start (dispatch sync --delete). No ad-hoc re-dispatch fired by me: bar proximity (13:30Z) makes an
induced pre-bar chain run a terrain change COO must own; my default = natural fire, COO can order
a QA re-dispatch post-window. Bar Amendment 3 content (conditional branch iii) sent to COO -- the
atomic-window file is COO-owned, amendments fold via them.

## Rollback

Single additive key: `aws s3api delete-object` (or restore prior version) reverts the store to the
pre-fix state. No repo code changed; no IAM changed; no schedule changed.
