# MDPF 49F Custody Basis Flip — Execution Runbook (bd -> schwab)

**Owner:** `0.5.0_AE_OpalETL` (holds + fires the single flip). **GO:** `2.0.0_SA_COO` only,
on the CTO+COO+CVO never-widen co-sign. **Do NOT fire early.**
**Created:** 2026-07-02 (banks the PowerShell-only execution catch, COO-directed).

The flip is a served-critical cutover of the MDPF 49F custody basis from `bd`
(BD-silver allocations/fees crosswalk, the frozen-06-25 break) to `schwab`
(schwab/silver/rps straight positions, CASH-excluded). ONE SSM parameter write
atomically co-activates the trigger + WS-E + leg-2 gate.

---

## Pre-flip gate chain — ALL must be GREEN before the fire

1. **Leg-1 trigger** deployed dormant; `/mdpf/custody_source = bd`; IAM (`ssm:GetParameter`
   + `schwab/silver/rps` read) live. — VERIFIED 2026-07-02 (param=bd v1, trigger LastModified 07-01T21:14Z).
2. **RPS source** continuous through the latest partition (06-26/06-29 backfilled). — VERIFIED prior session.
3. **WS-E** (`build_mdpf_wse_49f_non_model_aua.py`, DS~A `49af9819b`) dormant-deployed. — VERIFIED prior session.
4. **Leg-2 sanity gate** (`validate_schwab_native_custody.py`, `c414574ee`) gold-deployed to
   `s3://opal-data-mdpf/code/scripts/gold/` + chain-wired (post-WS-E, pre-rollup; DEFER on rc=1) by DS~A.
   -> **AE RAVC-validates to `comp-pipescript deployed <script>` = MATCH** (verify-served, never self-report).
   Currently `MISSING_ON_S3` (2026-07-02) — awaiting DS~A deploy.
5. **CVO** live gate-PASS + pre-parity GREEN (served-would-be == straight-RPS-sum, CASH-excluded, to the cent).
6. **COO** convenes CTO+COO+CVO never-widen co-sign -> GO to AE.

## THE FLIP — PowerShell ONLY (NOT Git Bash)

> CRITICAL: run from **PowerShell**. Git Bash MSYS path-conversion mangles the leading-slash
> `--name /mdpf/custody_source` into a Windows path, silently writing/flipping the WRONG param
> at the served-critical moment. (Same gotcha spoofed a ParameterNotFound on 2026-07-02.)
> See memory `gotcha-aws-ssm-leading-slash-msys-mangle`.

```powershell
aws ssm put-parameter --name "/mdpf/custody_source" --value "schwab" --overwrite --region us-east-1
```

Verify the flip took (PowerShell):
```powershell
aws ssm get-parameter --name "/mdpf/custody_source" --query "Parameter.Value" --output text --region us-east-1
# expect: schwab
```

## What the flip co-activates (atomic, one-read-propagated)

- **Trigger** re-points BD-silver-freshness -> `schwab/silver/rps` freshness; ONE fire-time read
  STAMPS `schwab` into the dispatch env (no mid-flip race). `ignore_changes=[value]` on the TF-managed
  param means a later `terraform apply` will NOT drift-revert the flip.
- **WS-E** computes non_model_aua on the schwab basis.
- **Leg-2 gate** activates (keys off the propagated `schwab` value) — SKIP under `bd`.
- Effective on the next mdpf nightly (or an on-GO run).

## Post-flip

- **CVO parity cert** on the first nightly: served == straight-RPS-sum (CASH-excluded, to the cent),
  residual non-negative. AE co-witnesses.
- **Deploy-completion ledger:** open an entry in `org/critical_paths/change_management/` at flip-start,
  close at CVO cert (NEVER leave a served-critical cutover half-landed).

## ROLLBACK — PowerShell ONLY

```powershell
aws ssm put-parameter --name "/mdpf/custody_source" --value "bd" --overwrite --region us-east-1
```

## Parity constant (identical across trigger / WS-E / leg-2 gate / CVO)

Cash rule, to the cent: `ticker.astype(str).str.strip() != 'CASH'`
(ticker is whitespace-padded -> `.str.strip()` required) -> custody **$1,591,210,618.75 @06-24**.
Leg-2 gate bands: partition+schema / positions[85k,96k] / accounts[5.6k,6.2k] /
custody[$1.4B,$1.8B] + RPS-to-RPS DoD<=1.6% (flip-day-exempt by construction).
