# 0.5.0_AE_OpalETL — Session Close (SCTY guard live + MDPF Schwab-native un-freeze built end-to-end + NFRA_INTEGRATIONS)

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, IMPLEMENT, DIAGNOSE, COORDINATE

**Window:** 2026-07-01 (whole session; first log of the day) → 2215Z. 18 commits, ~1 tag, ~60 MCP dispatches.

## Summary
Three Andrew-direct threads driven to completion/gate:
1. **SCTY_MCPGUARD** — user-type action-guardrail wired into the live m365 MCP gateway. **CERTIFIED LIVE 4/4, ledger-closed.** Roster: andrew@=MASTER_ADMIN, alyssa@=STANDARD_EMPLOYEE (write, via .env), else READ_ONLY.
2. **MDPF 49F custody Schwab-native basis switch** (P1 served-AUA un-freeze) — designed, all 3 my legs deployed/handed, delta-3 resolved via a Rule-22 self-retraction, RPS source gap backfilled. Down to one governed flip.
3. **NFRA_INTEGRATIONS** — canonical MCP-integrations project created (CTO), Pillar-3 storage schema drafted.

## Work done

### SCTY (author lane; 0.7.0~A deployed)
- Built + integrated the guard into `infra/aws/ec2/m365-mcp-gateway/app/`: `tier.py`/`destructive_ops.py`/`guard.py` (new) + `config.py` (+3 tier vars) + `audit.py` (tier param + G6 teams_poll) + `tools.py` `_run` guard chokepoint + `server.py` (audit import + /teams/poll fold). Commit **2763b3035** (earlier build commits ae651397e→8de441c6b). 47/47 module tests + 9/9 applied-tree smoke.
- Handed to **0.7.0_AE_CloudOps~A** (deployer-of-record); author-co-witnessed the live cert. The two DENY cases are transport-unreachable BY DESIGN (identity_required = defense-in-depth belt behind the 401; read_only_denied needs an unforgeable verified non-roster id) → certified via on-box exercise of the DEPLOYED bytes (Rule-12 harness, CommandId 8710fb1f). Result: **4/4 LIVE**.

### MDPF Schwab-native basis switch (my legs: trigger + sanity gate + RPS backfill)
- **Design** (01773f289) + **provenance**: no 06-24 logic change; $1.65B = v0.9 baseline; the frozen input is the `bd/silver/fees` custodian crosswalk. Andrew ruled straight-RPS (assets-only, cash dropped), re-baseline.
- **Leg-1 trigger re-point** — `mdpf-daily-trigger` re-pointed BD-silver-freshness → `schwab/silver/rps` freshness behind a `CUSTODY_SOURCE` flag (SSM `/mdpf/custody_source`, ONE fire-time read STAMPED into the dispatch env = one-read-propagated, no mid-flip race). Layout-variant reader (`date=YYYYMMDD/` dirs, 2 hardening asserts). Code **8d7b5622c** (8/8 test), **deployed DORMANT** via Terraform (**eed9f00f4** + tag **mdpf-pipeline-v1.3.0**): IAM +schwab/silver/rps +ssm:GetParameter, new SSM param `=bd` with `ignore_changes=[value]` (so a later apply can't revert the flip). Live flag verified `bd` (zero behavior change).
- **Leg-2 Schwab-native sanity gate** — replaces the dropped BD net. Chain-step HARD-DEFER validator (post-WS-E/pre-rollup), dormant-safe, 4 checks (partition+schema / positions[85k,96k] / accounts[5.6k,6.2k] / custody[$1.4B,$1.8B]+**RPS-to-RPS** DoD≤1.6% so the flip-day basis step doesn't self-trip). Spec 053ba76bd (CTO PASS), code **c414574ee** (tested: dormant SKIP + active PASS on live rps + cent-match to WS-E). Handed to 0.4.0~A for gold-deploy + chain-wire.
- **delta-3 RETRACTED (Rule 22)** — my "model/sma custodian==Schwab coherence fix" rested on a custodian column that is 100% `None` + an unsourceable "~$156M held-away" premise. DS~A's magnitude test (+$180-203M, positive/stable) + structural clincher (v0.9 already coheres model(all) vs Schwab-restricted custody) → **Path A, drop it (no-op)**. Retracted my own premise; CTO-confirmed. Docs updated (**d278a8a08**).
- **RPS backfill** — grounded (partition paginator) that `schwab/silver/rps` was missing 06-26/06-29 (same 2 dates as the freeze). Promoted 27 quartz-validation raw files (SSE AES256) → converted all 6 silver tables → S3-verified. RPS 91,190/91,201 positions. **Roll-forward ledger 20260701T1800Z CLOSED** (d278a8a08), no half-state. (Mechanism note: the TRN converter reads LOCAL OneDrive not S3 → staged the promoted raw locally to convert.)

### NFRA_INTEGRATIONS
- Proposal (9d8451df0) → CTO created the project + PRD (d98cd2353). Drafted Pillar-3 storage schema (13fe36aa3): R4.2 two-dependency-models + don't-cross, R4.4 firm-separation on persisted integration data, R4.5 hosts=SSRF-egress → CTO §4 fold.

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| `comp-iam service mdpf-daily-trigger` | pre-deploy IAM gap check | **PASS** — caught `ssm:GetParameter [MISSING]` (the one gap for the flag read); all else granted. Rail paid off (avoided a runtime AccessDenied). |
| `comp-which` (x3) | route trigger-location / integration-framework / trigger-gate | **PARTIAL** — near-ties (comp-aws/comp-iam/pipescript); resolved via Glob/Read for the specific file. |
| `.tools/ds-commit-gate.sh` (many) | py_compile+ruff on every .py | **PASS** — caught 5 (test) + 6 (validator E402 ordering) ruff issues; fixed. |
| `.tools/safe-apply.sh` (HALTGT) | trigger dormant TF apply | **PASS** — 1 add / 2 change / 0 destroy; 0-diff clean. |

**What worked:** comp-iam caught the exact IAM gap pre-deploy. ds-commit-gate caught the docstring/from-future ordering (docstring-first is the accepted gold pattern) + unused-import.
**What failed:** comp-which near-tied on file-location questions (not a dead-end, but needed Glob/Read for the exact file).
**Gap found:** the rail HARD-GATED a `aws s3 ls schwab/silver/rps/` (freshness class → comp-freshness) — correct gate; I already had the answer from my own partition paginator, so no loss, but comp-freshness doesn't enumerate a full date-list (the "is date X present" backfill question). Prior filed gap still open: comp-pipescript io/comp-blast return empty on MDPF (dynamic-S3-key coverage, 06-26).

## Deployment Sequence + Verification (AE — trigger dormant deploy)
code 8d7b5622c → `build-and-upload.sh mdpf-pipeline mdpf-daily-trigger` (artifact→S3) → commit TF+source-map eed9f00f4 → `safe-apply ... apply` → 0-diff → `record-terraform-deploy ... mdpf-pipeline-v1.3.0` → tag+push.
```
Apply complete! Resources: 1 added, 2 changed, 0 destroyed.
terraform plan -> No changes. Your infrastructure matches the configuration.
aws ssm get-parameter /mdpf/custody_source -> bd   (DORMANT verified)
```

## MCP traffic (~60 dispatches; significant only)
- **Received:** Andrew GOs (SCTY approve, integrations project); CTO arch-gates (trigger PASS, leg-2 PASS, flag-mechanism, delta-3 Path-A CONFIRMED); COO un-holds + never-widen governance + P3 GO + backfill auth; DS~A WS-E deltas-grounding (delta-3 blocker → magnitude test) + WS-E dormant-deployed; 0.7.0~A cert co-witness requests.
- **Issued:** SCTY source-handed (2763b3035) + author co-witness (cert 4/4); trigger/leg-2 arch-gate reqs; **delta-3 Rule-22 retraction → Path A ruling** (CTO/DS~A/COO); WS-E swap handoff; leg-2 handoff (deploy+wire); cash-rule lock ($1,591,210,618.75); NFRA_INTEGRATIONS issue + P3 draft.

## Blockers
None BLOCKED. The MDPF flip is at a HARD EXTERNAL GATE (the never-widen sign-off: CTO+COO+CVO), which is process-correct, not a blocker. All my legs are complete/handed.

## Current State (handoff surface)
- **SCTY:** LIVE + certified on `m365-mcp-gateway` (i-07dccb1615503ac99), build 8b24cd2bb. Ledger `org/critical_paths/change_management/20260701T1941Z_scty-mcpguard-live-gateway` (closed). Roster live: andrew@=master, alyssa@=write (deploy .env WRITE_CAPABLE_EMAILS), else read-only.
- **MDPF un-freeze — teed to ONE flip:**
  - Trigger: `infra/aws/lambda/mdpf-pipeline/mdpf-daily-trigger/lambda_function.py` — deployed dormant (`mdpf-pipeline-v1.3.0`). SSM `/mdpf/custody_source=bd`.
  - Sanity gate: `data/mdpf/scripts/gold/validate_schwab_native_custody.py` (c414574ee) — committed; **awaits 0.4.0~A gold-deploy (→ s3://opal-data-mdpf/code/scripts/gold/) + chain-wire (post-WS-E/pre-rollup, DEFER on rc=1)**.
  - WS-E: `build_mdpf_wse_49f_non_model_aua.py` (DS~A 49af9819b) — dormant-deployed; schwab dry-run custody $1,591,210,618.75 / non_model $180.5M.
  - RPS source continuous through 06-30 (06-26/06-29 backfilled, all 6 silver tables).
  - **Cash rule (one-rule-three-call-sites, to the cent):** `ticker.astype(str).str.strip() != 'CASH'` → $1,591,210,618.75 @06-24. WS-E + leg-2 gate matched; CVO to use same.
  - **THE FLIP** (held by me, not fired): `aws ssm put-parameter --name /mdpf/custody_source --value schwab --overwrite` — ONLY on the COO-convened never-widen sign-off. Rollback = same, value `bd`.
- **NFRA_INTEGRATIONS:** PRD d98cd2353; my Pillar-3 draft `docs/briefs/nfra-integrations-pillar3-storage-draft-20260701.md` → CTO §4 fold pending.

## Next Steps
- [0.4.0_DS_ClientPlatform~A] deploy + chain-wire leg-2 sanity gate; confirm the identical `.str.strip()` cash exclusion in WS-E → RAVC me + COO at leg-2-deployed+wired = all pre-flip legs complete.
- [3.0.0_SA_CVO] pre-parity on the complete RPS series (served-would-be == RPS-sum to the cent) → then post-flip nightly parity + residual-non-negative.
- [2.0.0_SA_COO] convene the never-widen sign-off (CTO+COO+CVO) once all pre-flip legs + CVO pre-parity land → I execute the single flip → CVO cert → MDPF un-freezes.
- [1.0.0_SA_CTO] fold Pillar-3 into NFRA_INTEGRATIONS_PRD §4.
- [0.5.0_AE_OpalETL / me] execute the flip on the sign-off; co-witness the CVO post-flip cert.
