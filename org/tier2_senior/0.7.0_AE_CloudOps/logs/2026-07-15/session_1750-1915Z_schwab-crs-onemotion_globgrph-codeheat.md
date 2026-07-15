# 0.7.0_AE_CloudOps -- schwab CRS one-motion (v0.17.0) + GLOBGRPH codeheat (LD-0299 leg 1)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE
**serial:** 0.7.0_AE_CloudOps | **date:** 2026-07-15 | **window:** ~17:50Z (continues session_1650-1750Z @ f31ac7c64) -> ~19:15Z

## Summary

1. **SCHWAB CRS ONE-MOTION DEPLOYED (opal-assets-v0.17.0) -- delta-6 CRS swap + 10240->3008 in ONE apply.**
   CTO GO 183008Z (AC-2 discharged: both masters at parity, schwab fires tomorrow so no coupling to
   tonight's ETF window -> two-variable motion authorized). Source aa083a4c7: artifact sha yMma9jOm
   (streaming crs_reader + fan-out ChunkedParquetWriter, delta-6 6bfea3fdf; 11/11 vendor parity incl
   stream_parquet.py) + silver.tf schwab memory 10240->3008. **TARGETED apply** module.silver_converter
   ["schwab"] = 0/1/0 -- I -targeted because the UNtargeted plan also swept in the STAGED cell-3 bd49f
   swap (sha tj4T5e1B, HELD for tonight); targeting kept bd49f untouched. safe-apply -> live sha==yMma9jOm
   + Mem==3008 -> targeted 0-diff -> tag v0.17.0 pushed. record-terraform-deploy SKIPPED deliberately (its
   reconcile would revert the staged cell-3 source-map). CTO ACCEPTED (both judgment calls ruled right).
2. **AC-1 (conversion-peak, canonical-stamp leg ii) RULED option (a): tomorrow's natural fire.** Invoked
   the deployed converter on the heaviest rlu (schwab/08335338/bronze/rlu/20260109, 29.2MB, 296,669x82
   OOM-basis) -> SKIPPED (converted=0; all 12 rlu dates + both masters already at parity, lambda_entry
   force=False). REPORT: delta-6 code LOADS at 3008 using **946 MB** (import/skip, no cold-start OOM ->
   DEPLOYED-confirmed partial). Real conversion-peak unmeasurable tonight (no unconvertible unit exists
   BECAUSE parity is complete; no force path via S3 event). Refused to delete a served partition or fake
   it -> surfaced 3 options to CTO; he ruled (a) -- tomorrow AM fresh production data, risk accepted at
   3008 overnight (~1,036 expected = dev 786 + ~250 delta; fails-loud+idempotent+resize-recovers if OOM).
   Canonical stamp completes on tomorrow's number.
3. **GLOBGRPH_CODEHEAT_ENABLED=1 APPLIED (NFRA_GRAPHFEED LD-0299 leg 1, Andrew-direct via MSTR).** CTO
   authored the item2a.tf env-var flip (owned-paths lane-routed to me); I reviewed (one env var appended
   to derive_runner task-def, full provenance, no grant scope), unstaged 4 TAXSMA + etf concurrent-agent
   strays from the shared index, committed item2a.tf ONLY under my line (e11da0646). **TARGETED apply**
   (aws_ecs_task_definition.derive_runner + aws_cloudwatch_event_target.derive_runner_nightly) = 1/1/1 --
   the UNtargeted plan carried 3 unrelated pending changes (IAM policy, freeze_monitor Lambda, SNS sub)
   which I excluded + flagged. Live-verified: derive_runner Revision **5**, GLOBGRPH_CODEHEAT_ENABLED="1",
   nightly target retargeted to :5, targeted 0-diff. Evidence to CTO + MSTR. Tomorrow's derive = exercise.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| vendor-manifest.sh --check | schwab 11 modules | PASS 11/11 | delta-6 already vendored @ 6bfea3fdf |
| build-and-upload.sh | schwab single-fn | PASS (write-VERIFIED) | sha yMma9jOm, size 60129 |
| terraform plan (targeted) | schwab; globgrph | 0/1/0; 1/1/1 | -target both -- excluded held cell-3 (schwab) + 3 unrelated (globgrph) |
| safe-apply | schwab; globgrph | PASS both | schwab clean; globgrph blocked-then-fixed (see below) |
| aws lambda get-function-config | schwab post-apply | PASS | Mem 3008 + sha yMma9jOm live-tie |
| aws lambda invoke (REPORT) | schwab rlu AC-1 | SKIP, 946MB load | parity => no conversion; DEPLOYED-confirmed partial |
| aws ecs describe-task-definition | globgrph post-apply | PASS | rev 5, CODEHEAT=1, target->:5 |

**What worked:** the plan-read catching BOTH cross-motion contaminations (held cell-3 in the schwab plan;
3 unrelated globgrph changes) -> -targeting scoped each motion to exactly its own resources.
**What failed / GAP found:** safe-apply's comp-tagauthz pre-apply gate FAILED CLOSED with a mangled path
`C:\c\Users\...\comp-tagauthz.py` because I ran it under `MSYS_NO_PATHCONV=1` (leaked into the gate's
internal python call). Dropping MSYS_NO_PATHCONV=1 fixed it. LESSON (banked to CTO): NEVER
MSYS_NO_PATHCONV=1 with safe-apply -- already a known class per CLAUDE.md Git section; hit it live.

## MCP traffic
~7 in / ~5 out. Significant: CTO GO schwab one-motion + AC-1-ruling/motion-ACCEPT + second-motion-queued
(globgrph) + one-motion-accepted; DS ETF rules 6-8 FILLED + rule 9 STRUCK (ETF authoring unblocked);
0.8.0~Z derive-image rebuild heads-up (future, CTO-gated). Out: schwab RAVC + AC-1 options + 2 ACKs;
globgrph evidence to CTO + MSTR CC.

## Blockers
None stranded. GATED (hard external): tonight 22:00Z (cell-3 swap [+ FOLD the skipped record-deploy
reconcile per CTO], orion resize 10240->3008, batched ETF notification-rules apply); tomorrow AM (box
apply + schwab AC-1 conversion number). ETF -target rule authoring unblocked (DS filled 6-8) but APPLY
cutover-gated behind ETF parity 3/3.

## Current State (handoff)
- **schwab silver: delta-6 CRS LIVE at 3008MB** (opal-assets-silver-schwab sha yMma9jOm, v0.17.0). AC-1
  conversion number pending tomorrow's natural fire (canonical n=2 stamp). 946MB import-baseline banked.
- **globgrph derive_runner: task-def rev 5, CODEHEAT=1 LIVE**, nightly target->:5. Tomorrow's derive emits
  code_heat (clears the 153.3h comp-learns lag + the <30h freshness registry entry).
- **record-terraform-deploy for opal-assets = DEFERRED** (skipped to protect staged cell-3 source-map);
  MUST run after cell-3's bd49f swap lands tonight so schwab v0.17.0 + cell-3 both record + ledger converges.
- **3 unrelated globgrph module changes UNTOUCHED** (IAM policy, freeze_monitor, SNS sub) -- route/apply
  deliberately, likely other NFRA_GRAPHFEED legs (0.8.0~Z derive-image rebuild incoming).
- Cell-3 bd49f still STAGED/HELD (sha tj4T5e1B, live Ir0PmpFI). EC2 box AUTHORED @ 5fc641654, apply tomorrow.

## Next Steps
- [tonight 22:00Z] cell-3 swap (+ folded opal-assets record-deploy reconcile) + orion resize + batched ETF rules, on tonight-clean CTO word.
- [tomorrow AM, 1.0.0_SA_CTO] schwab AC-1 conversion number from the natural fire -> canonical stamp; EC2 box apply GO.
- [0.8.0_AE_CloudComp~Z] derive-image rebuild payload on CTO GO -- I am the standing rebuild owner.
