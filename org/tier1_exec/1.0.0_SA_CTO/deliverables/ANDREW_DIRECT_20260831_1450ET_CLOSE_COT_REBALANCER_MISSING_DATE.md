# Andrew-direct record -- close Cottonwood rebalancer missing date

**Recorded by:** `1.0.0_SA_CTO`  
**Channel:** direct user message in active Codex CTO seat  
**Time received:** 2026-08-31 14:50:38 ET  
**Scope:** `MDPF_HEALGAP` / Cottonwood rebalancer missing bronze date, 2026-08-31.

## Verbatim Andrew Instruction

> Close the missing date, yes, and let's get this sorted out, COO is coming onlin enow.

## CTO Reading

This is the explicit per-use Andrew authorization for the one-shot Cottonwood
rebalancer recovery that was previously held: run `cot-rebalancer-runner` for
`date=2026-08-31` only, with no historical sweep, no Terraform, no deploy, and
no schedule/design widening. The production write and vendor egress are limited
to closing the known missing 2026-08-31 bronze date.

COO is being brought online for the D8/`MDPF_HEALGAP` decomposition path. The
longer-lived guard hardening and schedule/retry design still return through COO
atom-decomp before TOs.
