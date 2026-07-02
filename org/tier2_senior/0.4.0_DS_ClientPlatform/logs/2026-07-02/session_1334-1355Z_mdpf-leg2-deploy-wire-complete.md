# MDPF leg-2 -- Schwab-native custody sanity gate: gold-deploy + chain-wire (the LAST pre-flip leg)
**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE

**Serial:** 0.4.0_DS_ClientPlatform~A | **Window:** 2026-07-02T13:31Z -> 13:55Z | **Respawn purpose:** complete the MDPF never-widen flip (ADVI_BDAPIMIG served-AUA un-freeze) as the completing worker.

## Current State (handoff surface -- zero-prior-context)

MDPF leg-2 (Schwab-native custody sanity gate) is **COMPLETE + live-verified + tri-accepted (COO/MSTR/CVO)**. Both halves landed:

1. **Gold-script deploy (DS~A lane, Rule 13) -- DONE.** `validate_schwab_native_custody.py` (commit `c414574ee`, was MISSING_ON_S3) deployed via `aws s3 cp` -> `s3://opal-data-mdpf/code/scripts/gold/validate_schwab_native_custody.py`. Verified MATCH two ways: `comp-pipescript deployed --pipeline mdpf` = MATCH; S3 ETag `a11419dd8350941563a1620ca8034aa5` == local md5. This was the named RAVC gate for CVO's co-sign.

2. **Chain-wire (dispatch.sh Stage 2.5) -- authored by me, LANDED by AE (owned-paths lane).** New Stage 2.5 inserted in `infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh` between Stage 2 (WS-E) and Stage 3 (WS-A aggregate): `run_step LEG2-CUSTODY-GATE gold/validate_schwab_native_custody.py`; `rc!=0 -> CHAIN_STATUS=failed; exit 1` (skip Stages 3/3.5/4/5, fail-closed to known-stale). `total_steps` 10->11. **Placement grounded** (design open-item (a), CTO-arch-gated; AE's own instruction "AFTER WS-E, BEFORE the WS-A rollup"): PRE-WS-A so a DEFER stops EVERY served surface (per-date platinum @S3, non_model_assets.json @S3.5, rolled timeseries @S4). My `safe-commit.sh` was BLOCKED by the owned-paths gate (`infra/aws/ec2/...` = lane CLOUD_OPS_OR_ETL = AE; DS~A not permitted); I did NOT `--force`-bypass the SoD gate on verbal authority. COO ruled **Option A** (route to lane owner, not path-grant). AE (`0.5.0_AE_OpalETL`) applied my patch verbatim -> live S3 `code/mdpf-daily-dispatch.sh` ETag flipped `6bb68bc0` -> `3e6c1d19406690cd168e0eeefe0ac081` (== my authored md5), LastModified 13:52:12Z; served dispatch.sh now carries the leg-2 `run_step` (line 295). Ground-truthed live (not self-report).

**Gate semantics triangulated to the cent** (3 independent computations agree): my deployed-gate ACTIVE run @06-30 = $1,608,080,123.25 (91,287 pos / 5,904 acct, all 4 bands in-band) == CVO parity harness == AE test. DORMANT run (CUSTODY_SOURCE=bd) = SKIP rc=0 (zero-effect landing). @06-24 anchor cross-check = $1,591,210,618.75 to the cent. Cash rule coherent across all 3 call-sites (WS-E `.str.strip().str.upper().isin({"CASH"})` / leg-2 `.str.strip() != "CASH"` / CVO parity), delta $0.00.

**Live state:** SSM `/mdpf/custody_source` = `bd` (dormant); leg-2 gate inert until the flip. All 3 pre-flip legs now complete (trigger dormant + WS-E swap + leg-2 deploy+wire). CVO holds LIVE to co-sign the never-widen flip on the now-flipped ETag; COO convenes the 3-way sign-off (CTO+COO+CVO); AE fires the single SSM flip `bd->schwab`.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| comp-pipescript deployed | `--pipeline mdpf` | PASS | ground-truthed MISSING_ON_S3 (pre) -> MATCH (post) for validate_schwab_native_custody.py; found the canonical opal-data-mdpf gold prefix (not bd default) |
| comp-pipescript io | validate_schwab_native_custody.py / WS-E / rollup | PASS | leg-2 = validator (no I/O); WS-E Order 40, WS-A 50 -- informed placement |
| comp-pipescript chain | validate_schwab_native_custody.py | FAIL(expected) | mdpf script not in bd-gold chains; the runner (dispatch.sh) is the authority, not comp chain |
| ds-commit-gate | validate_schwab_native_custody.py | PASS | "All checks passed" (re-verify of already-committed) |
| comp-grep / comp-glob | dispatch refs / order registry | PASS | located chain-wire site (dispatch.sh:271) + EC2_MANIFEST key |

**What worked:** `comp-pipescript deployed --pipeline mdpf` was decisive for the correct firm-tree prefix (MSTR flagged a possible 'inf' slip -- comp-pipescript confirmed opal-data-mdpf). **What failed:** nothing blocking. **Gap:** none new; `comp-pipescript chain` doesn't model the mdpf dispatch.sh step-order (it's a bash runner, not a comp chain) -- known, the runner is the authority.

## MCP Traffic (summary)
~10 messages handled. Significant: MSTR [FINAL] (sole task = deploy+chain-wire); COO [DRIVE] (parity confirm + wire); AE handoff (patch target). Sent: RAVC to CVO (gold MATCH + tie-out), handoff to AE (authored patch), escalation+A/B to COO, status to MSTR, de-risk evidence to CVO. Received back: COO [DECISION] Option A + gold ACCEPTED; MSTR [RAVC-VALIDATE] accepted (owned the deploy+chain-wire lane-conflation); CVO [ACCEPT] triangulated to the cent. AE closed the ledger wire-leg.

## Files Modified
- Deployed (no repo change): `data/mdpf/scripts/gold/validate_schwab_native_custody.py` (c414574ee) -> S3 gold prefix.
- Authored (landed by AE): `infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh` Stage 2.5 (my worktree edit; AE committed+deployed in-lane).
- Committed by me: `org/critical_paths/change_management/20260702T1334Z_mdpf_leg2_deploy_completion.md` @ `e92cf665e` (AE appended the FULLY-CLOSED close-out).

## Blockers
NONE. The chain-wire owned-paths block was resolved by COO Option A (AE landed it); ledger FULLY CLOSED. My worktree still holds the (now-redundant) unstaged dispatch.sh edit == what AE deployed -- discard on next clean-up (harmless, matches live).

## Next Steps
- [3.0.0_SA_CVO] Co-sign the never-widen flip -- the Stage 2.5 wire ETag has flipped to 3e6c1d19 (your verify bar); gold MATCH + gate triangulation done.
- [2.0.0_SA_COO] Convene the 3-way sign-off + surface to Andrew; [0.5.0_AE_OpalETL] fire the single SSM flip.
- [3.0.0_SA_CVO] Post-flip: parity on the FIRST post-flip nightly (served == straight-RPS-sum, CASH-excluded, to the cent); confirm leg-2 gate PASSes active (not false-DEFER) on flip-day RPS.
- [0.4.0_DS_ClientPlatform~A] Nightly-external follow-ups (unchanged, hard-gated): comp-validate Phase-3 on tonight's bd nightly leaderboard.json (TAGATTR); comp-validate cot client_directory.json (COTMVP.B-DS). Not actionable pre-nightly.
