# Session Log — SL-P1c SLEEVE_SHADOW_DISABLE Investigation
**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-05-05
**Scope:** SL-P1c AC#6 gate — unset SLEEVE_SHADOW_DISABLE on bd-gold-layer-runner per COO GO

---

## Context

COO GO received (20260505T132442Z inbox): DS~C Fix B correction (e3463bffa) shipped and MATCH on S3.
Action required: unset SLEEVE_SHADOW_DISABLE env var on bd-gold-layer-runner (i-01003b035d2988dfb).

Kill switch location in code: `data/black_diamond/scripts/gold/B_01.holdings_lots.py:2835`
```python
if os.environ.get('SLEEVE_SHADOW_DISABLE', '') != '1':
```
When var = '1', sleeve shadow output is suppressed. Unset = shadow output resumes.

---

## Investigation

Search coverage — SLEEVE_SHADOW_DISABLE NOT found in:
- Any `.sh` script in the codebase (gold_dispatch.sh, run_gold_layer.sh, ssm-run-gold.sh)
- Any `.tf` Terraform file (bd-pipeline, shared-infra)
- SSM Parameter Store (`/opal/bd/SLEEVE_SHADOW_DISABLE` → ParameterNotFound)
- Instance user-data (only PATH in /etc/environment)

Instance state at investigation start: stopped.

Started instance i-01003b035d2988dfb → running → sent SSM diagnostic.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | RAVC2 ACK to COO | Delivered 20260505T132442Z |
| 2 | Search codebase for SLEEVE_SHADOW_DISABLE | NOT found in any .sh/.tf/.json — must be on-instance |
| 3 | Check SSM Parameter Store `/opal/bd/SLEEVE_SHADOW_DISABLE` | ParameterNotFound |
| 4 | Read instance user-data (i-01003b035d2988dfb) | PATH only; no SLEEVE_SHADOW env var |
| 5 | Start instance | pending → running |
| 6 | SSM RunCommand a7e5e6b8 — check /etc/environment, printenv, profile files | NOT SET in all locations |
| 7 | Stop instance | stopping (started only for check; no gold dispatch) |
| 8 | RAVC3 to COO | Delivered 20260505T133929Z |

---

## SSM Evidence (cmd a7e5e6b8-f6a7-4494-9954-ea1caca0b6ce)

```
/etc/environment:
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin"

printenv SLEEVE_SHADOW_DISABLE:
NOT_SET_IN_ENV

Profile file search (/home/ubuntu/.bashrc, .profile, /etc/profile.d/, /etc/profile):
NOT_IN_PROFILE_FILES
```

**Verdict:** SLEEVE_SHADOW_DISABLE is NOT SET on bd-gold-layer-runner. Kill switch is already clear.

---

## Compiler Tools

| Tool | Phase | Run | Result |
|------|-------|-----|--------|
| (none applicable) | n/a | n/a | IAM-only investigation; no gold script or CF change. comp-iam not relevant to env var check. |

---

## Outcome

- No unset action needed — env var was never persistently set on the instance.
- B_01 line 2835 will evaluate sleeve shadow enabled on next gold run.
- AC#6 observation window starts with next nightly BD gold chain.
- Expected shadow output (first nightly): ~78 accounts / ~163 lots (per COO GO).

---

## Next Actions

- AC#6 requires 3 consecutive clean nightly shadow emissions. AE is passive from here — DS/COO own nightly validation.
- If shadow output does NOT appear in first nightly, escalate: possible the env var was set mid-run by the dispatch script (not persistent); or another suppression path exists. Check gold chain logs for SLEEVE_SHADOW_DISABLE references at runtime.
