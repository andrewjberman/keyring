# 0.5.0_AE_OpalETL -- MDPF custody flip FIRED (bd->schwab) + leg-2 chain-wire landed + NFRA_INTEGRATIONS P3 fold

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, DIAGNOSE, IMPLEMENT, COORDINATE

**Window:** 2026-07-02 ~1318Z -> 1617Z (first log of the day; session continues -- flip ledger OPEN). 7 commits + 1 live SSM flip + 1 cross-lane handoff.

## Summary
Drove the MDPF 49F Schwab-native un-freeze from "teed to one flip" to **FLIP FIRED**, plus closed my NFRA_INTEGRATIONS P3 pillar to CTO-approve-pending. Three arcs:
1. **MDPF custody flip** -- verified flip-readiness (caught + dismissed a phantom SSM drift), landed the leg-2 chain-wire (OPTION A), then **FIRED the flip** (`/mdpf/custody_source` bd->schwab v2) on the 3-way never-widen co-sign. Ledger OPEN, rollback armed; un-freeze now gated on inf(b) alone (I grounded the decoupling).
2. **NFRA_INTEGRATIONS-003 P3** -- finalized + grounded the storage schema, folded it into STANDARD.md as new sec 9 (audited ANY_CTO override). Complete-pending-CTO-approve.
3. **Two corrections** -- the mdpf trigger is event-driven (not a cron); EC2_MANIFEST cron field was stale (handed the fix to lane-owner 0.7.0).

## Work done

### MDPF custody flip (the headline)
- **Flip-readiness verified against LIVE AWS.** A Git-Bash `aws ssm get-parameter --name /mdpf/custody_source` returned a spurious `ParameterNotFound` that looked like real drift (param in TF state, missing in AWS). Grounded it via `terraform state show` + `plan -refresh-only` + a PowerShell query -> the param EXISTS (=bd v1); the "drift" was the **MSYS leading-slash arg mangle** (banked to memory `gotcha-aws-ssm-leading-slash-msys-mangle`). Did NOT apply anything to fix a non-problem.
- **Leg-2 chain-wire landed (OPTION A).** DS~A gold-deployed the leg-2 gate script (I independently confirmed `comp-pipescript deployed` = MATCH) but was owned-paths-blocked on the `infra/aws/ec2/` chain-wire (AE lane). DS~A handed me the authored patch (uncommitted in the working tree, md5 3e6c1d19... == authored, `bash -n` clean). I committed it (`208826724`, owned-paths PASS for AE) + `aws s3 cp` -> `s3://opal-data-mdpf/code/mdpf-daily-dispatch.sh` (Rule 12; no wrapper -- runner pulls at fire-time). S3 ETag flipped `6bb68bc0` -> `3e6c1d19406690cd168e0eeefe0ac081` (head-object verified). All 5 CVO verify-bar criteria met. Closed the wire-leg of DS~A's ledger (`dff351d9f`).
- **THE FLIP FIRED** (`12dd979c7` ledger). On the 3-way co-sign (CVO 135732Z + COO + CTO 140325Z; COO FIRE GO 140517Z): PowerShell `put-parameter /mdpf/custody_source bd(v1)->schwab(v2)`, verified live get-parameter=schwab v2 @14:06:52Z. PS-only (the MSYS gotcha would flip the WRONG param). Deploy-completion ledger `20260702T1405Z` OPEN; rollback ARMED (value=bd). Runbook `c4ff4c63e` pre-banked.
- **Trigger mechanism grounded + DECOUPLING found.** CVO flagged that mdpf-daily-trigger is event-driven, not a 15:00 cron. Ground-truthed live: EventBridge `mdpf-daily-refresh-trigger` ScheduleExpression=null, EventPattern=S3 ObjectCreated `opal-data-inf/gold/meta/pipeline-complete.json` (INF sentinel). Handler `:295`: under CUSTODY_SOURCE=schwab the convergence gate checks `_check_schwab_rps` NOT `_check_bd_silver` -> **the flip DECOUPLED bd(a); MDPF un-freeze is gated on inf(b) ALONE** (+ RPS fresh through 06-30). Relayed to COO + CVO (CVO independently cross-confirmed). Shortened COO's P0 critical path from bd+inf to inf-only.

### NFRA_INTEGRATIONS-003 (P3 storage pillar)
- Finalized + **re-grounded** the firm-separation invariant (was asserted): commit-gate PIPELINE_MAP (`.tools/safe_deploy_core.py:22-25/85/94`) + runtime IAM cross-firm Deny (`cot-pipeline/iam.tf:192-210` Sid DenyCrossFirmBuckets, Deny-overrides-Allow). Commit `6f742253c`.
- **Folded into `docs/architecture/NFRA_INTEGRATIONS_STANDARD.md` sec 9** (`bbd766bc2`) on COO GO (approve-not-author for CTO), via the audited `GIT_COMMIT_AUTHOR_OVERRIDE=ANY_CTO` (logged to git-author-override-audit.log). Surgical: net-new only (two dependency models + grounded firm-sep + egress-governance); code-location/tool_prefix/one-SM-secret already canonical in sec 2/4/5/8. Fidelity sec 9->10; Status v1.2->v1.3. Seed brief retired->pointer. RAVC'd COO + CTO to approve.

### Corrections
- EC2_MANIFEST.json `cron_schedule` for mdpf-daily-runner was STALE (said cron; live is event-driven). It's SHARED_CLOUD_OPS (0.7.0's lane -- owned-paths correctly blocked my commit) -> handed 0.7.0 the exact fix, SoD-clean.

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| `comp-pipescript deployed validate_schwab_native_custody.py` | leg-2 gold deploy verify (x2) | MISSING_ON_S3 (pre-DS~A) -> MATCH (post) -- verify-served, not self-report |
| `terraform state show / plan -refresh-only` | phantom-drift grounding | PASS -- confirmed the SSM param exists (=bd); the ParameterNotFound was MSYS mangle, not drift |
| `comp-which "firm-sep IAM-enforced"` | route the firm-separation grounding | PARTIAL -- near-tie (comp-dups/comp-kuzu); TO named comp-iam/PIPELINE_MAP, used those |
| `comp-iam` (gaps) + `comp-glob` | IAM gaps view + locate safe_deploy_core.py | PASS -- grounded PIPELINE_MAP + the cross-firm Deny |
| `.tools/safe-commit.sh` (x7) + ds-commit-gate | every commit (py_compile/ruff ride the wrapper) | PASS; the ANY_CTO override on bbd766bc2 audited cleanly |

**What worked:** the banked MSYS-slash memory made me instantly recognize the second spurious ParameterNotFound (Bash) as a tooling artifact, not re-chase it. comp-pipescript deployed gave the MATCH ground-truth for the leg-2 S3 deploy.
**What failed:** comp-which near-tied on the firm-sep grounding question (routed to comp-dups/comp-kuzu, neither the IAM-enforcement view); the TO's explicit comp-iam/PIPELINE_MAP directive was the right call.
**Gap found:** none new; the MSYS-slash SSM trap is now memory-banked for the fabric.

## Deployment Sequence + Verification (AE)
1. **Leg-2 wire (EC2 S3-artifact, Rule 12):** commit `208826724` -> `aws s3 cp` local -> `s3://opal-data-mdpf/code/mdpf-daily-dispatch.sh`.
   ```
   S3 ETag: "6bb68bc0..." -> "3e6c1d19406690cd168e0eeefe0ac081"  (== DS~A authored md5; head-object 13:52:12Z; size 17849->19576)
   bash -n: CLEAN
   ```
2. **The flip (SSM param, PowerShell):**
   ```
   BEFORE: {"Value":"bd","Version":1}
   put:    {"Version":2}
   AFTER:  {"Value":"schwab","Version":2,"LastModified":1783001212.313}  (14:06:52Z)
   ```

## MCP traffic (~30 dispatches this window; significant only)
- **Received:** COO (OPTION-A leg-2 route, FIRE GO, lever-1/2 decision + inf-BROKEN update, P3-fold GO, readiness-confirm); CVO (5-point verify-bar, event-driven flag, decoupling ACK, INF-fire ping-agreement); DS~A (leg-2 gold DEPLOYED=MATCH + chain-wire handoff).
- **Issued:** flip-readiness RAVC (COO), leg-2 wire RAVC (DS~A/COO/CVO), FLIP-FIRED RAVC (COO/CVO), decoupling finding (COO/CVO), P3-fold RAVC (COO CC CTO), manifest handoff (0.7.0 CC COO), on-call-ready ack + status.

## Blockers
None BLOCKED. The MDPF un-freeze is at a genuine EXTERNAL gate -- inf(b) BROKEN (Orion txn pull exit=1; 0.6.1 actively fixing, proc 17328). Not my lane; COO driving. My flip + all legs are fired/landed. Not a blocker (process-correct wait).

## Current State (handoff surface)
- **MDPF flip: FIRED.** `/mdpf/custody_source = schwab` (v2, PS-verified). Deploy-completion ledger `org/critical_paths/change_management/20260702T1405Z_mdpf_custody_flip_bd_to_schwab.md` OPEN with a pre-staged WS-3 close-checklist (`10bde8636`). **ROLLBACK ARMED:** `aws ssm put-parameter --name "/mdpf/custody_source" --value "bd" --overwrite --region us-east-1` (PowerShell).
- **Un-freeze mechanism (grounded):** mdpf-daily-trigger is EVENT-DRIVEN on the INF sentinel (`opal-data-inf/gold/meta/pipeline-complete.json`, currently @2026-06-30T17:18:02Z, NOT yet advanced). Under schwab basis the gate checks schwab/silver/rps (fresh through 06-30), NOT bd -> un-freeze gated on **inf(b) alone**. When inf emits a new sentinel -> mdpf auto-fires schwab basis -> leg-2 Stage 2.5 gate guards it -> serves.
- **Leg-2 gate:** gold script `data/mdpf/scripts/gold/validate_schwab_native_custody.py` (MATCH) + Stage 2.5 wire in `mdpf-daily-dispatch.sh` (S3 ETag 3e6c1d19...) -- both live, dormant-safe, HARD-DEFER.
- **LEVER-2 (held):** manual SSM dispatch `mdpf-daily-dispatch.sh --date <=06-30 CUSTODY_SOURCE=schwab` on runner i-02448edb624a7a7cf -- armed FALLBACK, fire ONLY on COO GO (trigger = inf can't land by mid-afternoon).
- **P3 fold:** STANDARD.md sec 9 (`bbd766bc2`), CTO-approve-pending. Seed brief `docs/briefs/nfra-integrations-pillar3-storage-draft-20260701.md` retired.
- **Watch:** Monitor `bziksr0t0` (INF sentinel + runner state) armed; CVO pings on sentinel-fire.

## Next Steps
- [0.5.0_AE_OpalETL / me] On INF-sentinel-fire (or COO lever-2 GO): watch the mdpf run telemetry (leg-2 gate PASS vs DEFER); on CVO per-field parity PASS + 06-25 freeze-clear -> fill + CLOSE the flip ledger; on any unexpected per-field widen -> fire rollback (SSM=bd) immediately + ping COO.
- [3.0.0_SA_CVO] per-field post-flip parity on the first schwab-native run (custody/model_aua/non_model_aua vs frozen bd; served == schwab/silver/rps/<date> sum to the cent; freeze clears).
- [1.0.0_SA_CTO] approve (or rework/renumber) the P3 sec-9 fold in STANDARD.md -> closes NFRA_INTEGRATIONS-003.
- [0.7.0_AE_CloudOps] land the EC2_MANIFEST mdpf cron_schedule fix (their lane; exact text handed).
- [2.0.0_SA_COO] relay the INF-sentinel-fire or the lever-2 GO if inf slips past mid-afternoon.
