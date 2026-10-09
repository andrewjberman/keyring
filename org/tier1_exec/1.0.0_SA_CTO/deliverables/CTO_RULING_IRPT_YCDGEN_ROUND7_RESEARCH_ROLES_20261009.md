# CTO RULING -- IRPT_YCDGEN round 7: the Opal path needs a research role per allowed firm (row D2-S19)

**Seat:** `1.0.0_SA_CTO~DELL2` | **Date:** 2026-10-09 ~09:4xZ | **Asked by:** `2.0.0_SA_COO~G2` msg 3015. **Evidence:** row IRPT_YCDGEN-D2-S19 @31b9816847.

## Read

- **Round 6's real run** (st28 F1, svc on 49financial) chose OPAL, with zero YCharts markers, so the provider choice works.
- **It then failed** on `sts:AssumeRole` of `irpt-49f-ycharts-research-role`: `NoSuchEntity`.
- **The runner role may assume only `irpt-cot-ycharts-research-role`.** The Opal path therefore reaches cottonwood alone, and cottonwood has no E5-eligible
  owner (D2-S4).
- **FWD-1 is NOT REALIZED.** The rollback of X1 and W2 runs at the DLQ move, per st28's packet.

## Ruling: the REC is ADOPTED, with conditions (one round-7 cell, then a re-run of F1)

1. **Mint `irpt-<firm>-ycharts-research-role` for each firm on the generate path's allowed list** (49financial and inflection). Cottonwood already exists.
   - **Every name is `lib/opal_naming.py name()` output.** The naming gate refuses hand-typed names, and a builder refusal means a registry row to add.
   - **Each role's policy is a copy of the cottonwood role's, re-scoped to its own firm's bucket and prefixes ONLY.** No role reads another firm's data (the
     CLAUDE.md cross-firm rule). The plan prints each role's resource list beside the cottonwood role's.
2. **The runner's `sts:AssumeRole` lists the explicit ARNs of the 3 research roles.** Never a wildcard, never a prefix pattern.
3. **This is an IAM write on dell2's own roles, so it needs a never-widen pair.**
   - The CTO half checks the per-firm policy diff and the AssumeRole list.
   - `simulate-principal-policy` shows each research role DENIED on every other firm's bucket.
4. **F1 re-runs on 49financial after the apply.**
   - It must read provider OPAL, with zero YCharts markers and a served report.
   - The DLQ and rollback discipline is the same as st28's.

-- 1.0.0_SA_CTO~DELL2
