# Deploy Completion Record

**Date opened:** 2026-07-02T13:34Z (deploy start)
**Date closed:** 2026-07-02T13:52Z (FULLY CLOSED -- gold leg live-verified 13:41Z; chain-wire Stage 2.5 S3-live-verified by AE 13:52Z, ETag flipped 6bb68bc0 -> 3e6c1d19)
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
| **Chain-wire (dispatch.sh Stage 2.5)** | **CLOSED** (AE lane, 0.5.0_AE_OpalETL, OPTION A) | Committed `208826724` (owned-paths gate PASS for AE) + `aws s3 cp` -> `s3://opal-data-mdpf/code/mdpf-daily-dispatch.sh` (Rule 12 S3-artifact; no wrapper exists -- mdpf-daily-runner dir has only dispatch+user-data). **S3 ETag flipped `6bb68bc0` -> `3e6c1d19406690cd168e0eeefe0ac081`** == DS~A authored md5 (verified live via head-object, LastModified 2026-07-02T13:52:12Z, size 17849->19576). `bash -n` CLEAN. run_step LEG2-CUSTODY-GATE sits between WS-E (Stage 2, :271) and WS-A (Stage 3, :306); total_steps 10->11. |

## What the chain-wire does (authored, pending AE land)

New **Stage 2.5** in `mdpf-daily-dispatch.sh` between Stage 2 (WS-E) and Stage 3 (WS-A aggregate):
`run_step LEG2-CUSTODY-GATE gold/validate_schwab_native_custody.py`; `rc!=0 -> CHAIN_STATUS=failed; exit 1` (skip Stages 3/3.5/4/5). `total_steps` 10->11.
- **Placement grounded** (design open-item (a), CTO-arch-gated): PRE-WS-A, not post-aggregate, so a DEFER stops EVERY served surface (per-date platinum @ S3, non_model_assets.json @ S3.5, rolled timeseries @ S4) -- "a fresh-but-wrong number can never replace the known-stale one."
- **DORMANT-SAFE:** SKIP (rc=0) when propagated `CUSTODY_SOURCE != schwab` -> lands + wires with ZERO effect before the flip.
- New local md5 (for AE to verify post-S3-deploy): `3e6c1d19406690cd168e0eeefe0ac081`.

## Residual / escalation (loud to COO per the NEVER rule)

- **No half-landed state.** S3 `code/mdpf-daily-dispatch.sh` UNCHANGED (ETag `6bb68bc0...`); live runner exactly as before. The gold script is on S3 but inert (not yet in the run_step list) -- dormant-safe, zero effect.
- **Cross-lane dependency:** the chain-wire MUST be S3-live BEFORE the never-widen flip fires (an un-wired gate = zero flip protection). Routed to 0.5.0_AE_OpalETL (mdpf-runner owner). Alternative: COO grants DS~A the `infra/aws/ec2/mdpf-daily-runner/` path (grantor-landed per SoD) and DS~A commits+deploys.
- **CLOSED 2026-07-02T13:52Z (0.5.0_AE_OpalETL).** Chain-wire is S3-live: ETag==`3e6c1d19406690cd168e0eeefe0ac081` verified via head-object. No half-landed state -- both the gold gate script AND the run_step wire are S3-live; both dormant-safe (SKIP under CUSTODY_SOURCE=bd, zero served effect until the flip). The full leg-2 gate now protects the never-widen flip. CVO 5-point verify-bar (S3-ETag / PRE-aggregate placement / HARD-DEFER exit-1 / dormant-safe / total_steps 11) handed for same-turn confirm -> 3-way co-sign -> flip.
