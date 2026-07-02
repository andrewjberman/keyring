# Deploy Completion Record

**Date opened:** 2026-07-02T13:34Z (deploy start)
**Date closed:** 2026-07-02T13:41Z (gold leg live-verified; chain-wire routed to AE lane -- see Residual)
**Deploy:** MDPF leg-2 -- Schwab-native custody sanity gate (the LAST pre-flip leg of the ADVI_BDAPIMIG never-widen flip)
**Authored by:** 0.4.0_DS_ClientPlatform~A
**Class:** deploy-completion (per the 2026-06-12 Andrew-direct NEVER rule: a begun deploy finishes in-session, ledger opened at deploy-start / closed at completion)
**Directive:** 0.0.0_AB_MSTR [MSTR-DIRECT FINAL] + 2.0.0_SA_COO [DRIVE] + 0.5.0_AE_OpalETL handoff

---

## Legs

| leg | state | evidence |
|---|---|---|
| WS-E cash-strip parity confirm | CLOSED | WS-E `.astype(str).str.strip().str.upper().isin({"CASH"})` (build_mdpf_wse_49f_non_model_aua.py:590-591) vs leg-2 `.astype(str).str.strip() != "CASH"` (validate_schwab_native_custody.py:82); both exclude the single uppercase "CASH " row ($17,346.45) on real 06-24 data -> identical $1,591,210,618.75. No bare ==CASH. CVO independently confirmed (HEAD attest "strip-vs-upper delta $0.00"). |
| ds-commit-gate (leg-2 gold) | CLOSED | `.tools/ds-commit-gate.sh` -> "All checks passed" |
| comp-pipescript io (leg-2 gold) | CLOSED | Group: gold, validator (no S3 reads/writes -- expected for a gate) |
| **Gold-script deploy (DS~A lane, Rule 13)** | **CLOSED** | `aws s3 cp` -> `s3://opal-data-mdpf/code/scripts/gold/validate_schwab_native_custody.py`; **MATCH** (comp-pipescript deployed --pipeline mdpf) + ETag `a11419dd8350941563a1620ca8034aa5` == local md5 `a11419dd...` |
| **Chain-wire (dispatch.sh Stage 2.5)** | **ROUTED-TO-AE (open)** | Authored + `bash -n` clean + full patch captured. Commit BLOCKED by owned-paths lane gate: `infra/aws/ec2/...` = lane CLOUD_OPS_OR_ETL (AE), DS~A not permitted. NOT self-bypassed (SoD). Handed to 0.5.0_AE_OpalETL to commit+deploy in-lane. |

## What the chain-wire does (authored, pending AE land)

New **Stage 2.5** in `mdpf-daily-dispatch.sh` between Stage 2 (WS-E) and Stage 3 (WS-A aggregate):
`run_step LEG2-CUSTODY-GATE gold/validate_schwab_native_custody.py`; `rc!=0 -> CHAIN_STATUS=failed; exit 1` (skip Stages 3/3.5/4/5). `total_steps` 10->11.
- **Placement grounded** (design open-item (a), CTO-arch-gated): PRE-WS-A, not post-aggregate, so a DEFER stops EVERY served surface (per-date platinum @ S3, non_model_assets.json @ S3.5, rolled timeseries @ S4) -- "a fresh-but-wrong number can never replace the known-stale one."
- **DORMANT-SAFE:** SKIP (rc=0) when propagated `CUSTODY_SOURCE != schwab` -> lands + wires with ZERO effect before the flip.
- New local md5 (for AE to verify post-S3-deploy): `3e6c1d19406690cd168e0eeefe0ac081`.

## Residual / escalation (loud to COO per the NEVER rule)

- **No half-landed state.** S3 `code/mdpf-daily-dispatch.sh` UNCHANGED (ETag `6bb68bc0...`); live runner exactly as before. The gold script is on S3 but inert (not yet in the run_step list) -- dormant-safe, zero effect.
- **Cross-lane dependency:** the chain-wire MUST be S3-live BEFORE the never-widen flip fires (an un-wired gate = zero flip protection). Routed to 0.5.0_AE_OpalETL (mdpf-runner owner). Alternative: COO grants DS~A the `infra/aws/ec2/mdpf-daily-runner/` path (grantor-landed per SoD) and DS~A commits+deploys.
- **This record stays OPEN until the chain-wire is S3-live (ETag==`3e6c1d19...`) + verified** by the AE lane owner, then closed.
