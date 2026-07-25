# CVO~Z — SYSPARITY cycle-30: `inf-intraday-iam`

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · cron `f0291f27`

---

**Gate:** `comp-system --check` → SYSTEM CURRENT (24 regions / 6 files, 0 drifted).

## VERDICT: CLEAN — no defect found

### DESIRED plane (TF)

| | |
|---|---|
| `infra/aws/terraform/globgrph/iam.tf` exists | yes |
| `BoundedDeriveReadOnly` occurrences | 2 |
| `dynamodb:DescribeTable` occurrences | 2 |
| block-anchored pattern matches | **yes**, 738-char span |

### APPLIED plane (live IAM) — Rule 22a, a TF read cannot tell landed from planned

`aws iam get-role-policy --role-name opal-globgrph-incremental-updater --policy-name BoundedDeriveReadOnly`

`dynamodb:DescribeTable` is **present in the live policy.**

### Full set-diff, not just the sentinel

The unit's check asserts one action. I compared the whole action set both directions:

```
TF-declared actions  : 28
LIVE applied actions : 28
APPLIED but NOT in TF (console drift) : NONE
TF but NOT APPLIED   (not landed)     : NONE
```

**Exact set match. Zero drift in either direction.**

### Denominator

Role carries **5 inline policies** (`BoundedDeriveReadOnly`, `CloudWatchLogs`, `IncrementalUpdaterSNS`,
`S3WarehouseWrite`, `SQSConsume`) **+ 1 attached** (`AWSLambdaVPCAccessExecutionRole`). I diffed the one
inline policy this unit is about; the other four inline and the attached policy are **not covered by this
measurement**.

### Bound

This is a **point-in-time** applied-plane reading. It says the grant is live now; it is not a standing
guarantee, and a fresh IAM change re-grounds.

---

## Compiler Tools

| Tool | Result |
|---|---|
| `comp-system --check` | CURRENT |
| `sysparity_register.py report` | 12/22 before this cycle |
| block-anchored regex, re-run standalone | MATCH, 738 chars |
| `aws iam get-role-policy` (live) | 28 actions, `dynamodb:DescribeTable` present |
| `aws iam list-role-policies` + `list-attached-role-policies` | 5 inline + 1 attached (denominator) |

Raw `aws` IAM inspection carried `# rail-checked:` — comp-iam parses TF (DESIRED) only, and Rule 22a
requires the APPLIED plane for a landed-vs-planned claim.

**Two tool errors of mine, both mechanical, neither affecting the result:** a shell redirect to a
`ANDREW~1` scratch path silently produced no file; and native Python `subprocess` could not spawn `aws`
(WinError 2 — it is a bash shim, not a Windows exe resolvable by CreateProcess). Fixed by piping `aws`
output into Python from bash.
