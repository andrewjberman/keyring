# Four invokes of irpt-status ran once; the control's envelope has no ok:true, so the verdict is ANOMALY and the check fails -- 0.7.0_AE_CloudOps~ANL

**Date:** 2026-10-12
**Task Order:** IRPT_ANLREQ.TO-READS-Y8.f2-original-route-owner-check-laptop
**Status:** BLOCKED

---

## Objective

Four read-only direct invokes of the deployed `irpt-status` against one retained request, to show whether the original-file route refuses a different advisor of the record's own firm while serving the control (CTO msgs 6378, 6387, 6541).

## What was done

- Acked crossbox XB-20261012T205806Z-552a. Step 0: id file at HEAD; `lambda:InvokeFunction` allowed on my own identity (policy simulation); deploy ledger 2 worktrees read, 36 open entries, 0 naming `irpt-status`.
- Step 1: CodeSha256 JmOhV/ep4m... (last modified 2026-10-12 14:12:21Z) is the package of the ADVI_FIRMBKTS act-4 build; the five route-rule files are byte-identical between that era and d90edb3367 (positive control: the whole-package diff names 1 other file).
- Step 3: one run, order control, b, a, b_absent_id. Control: link present, expiry, sha256 and byte_length present, `ok` absent or null; log check CLEAN. b NOT_AUTHORIZED, a FIRM_BINDING, b_absent_id NOT_AUTHORIZED.
- Verdict by the order's rule: ANOMALY (control `ok` is not true). `reads8_check.py` prints READS8-FAIL: it expects UNEXERCISED_LIVE for a control whose `ok` is not true, which would say the record was unreachable, and the control was served. I did not change the verdict to pass the check.
- No second run: bounds require the issuer's word.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| reads8_check | python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r16/reads8_check.py | FAIL | READS8-FAIL, verdict rule vs the control envelope |
| comp-iam | none | SKIPPED | read-only order; policy simulation on own identity |

**What worked:** the log check, the ledger sweep, the same-record control.
**What failed:** the verdict rule assumes a success envelope carries `ok: true`; the control's did not (absent or null, not separated by my read).
**Gap found:** the order's verdict rule and its check disagree with the control's real envelope; the issuer owns the rule.
