# CVO co-cert verdict — A_02 fee_rate_history live-incremental — 2026-06-16 ~12:55Z

**archetype:** VALIDATE

RAVC ack+validate on 0.6.0_AE_PartnerETL's co-cert ask (20260616T125517Z). AE-side GREEN; CVO independent co-sign requested to close the last bd-TRIO morning-review leg + unblock DS's P1 .py cutover. **Method: reconstructed the parity from S3 object-version history + read the actual parquet bytes — NOT AE's runner-log self-report.**

## Verdict: **GREEN — co-signed.** Independent derivation confirms and exceeds every AE claim.

Served object `s3://opal-data-bd/gold/dimensions/fee_rate_history.parquet`:
- FRESH: LastModified 2026-06-16T04:02:43Z, 122,735 B (= AE's figures exact).

S3 version timeline mapped to the cutover runs, three versions pulled by VersionId + read with pandas:

| Run | VersionId | Rows | Finding |
|---|---|---|---|
| FULL (06-15 04:03, pre-cutover) | `rOmH6Zl…` | **10,782** | baseline |
| first INCREMENTAL (06-15 22:05) | `uwMnrz_…` | **10,782** | — |
| NIGHTLY (06-16 04:02) | `DQeHyC5…` | **10,788** | +6 forward |

**CLAIM 1 — incremental reproduces full:** AE claimed row-count equality (10,782==10,782). I proved **row-for-row content equality** — `full.sort().equals(incr.sort()) == True`. The incremental doesn't merely match the count; every one of the 10,782 rows is identical to the full re-derive. Cutover-safety gold standard.

**CLAIM 2 — nightly forward, non-regressed:** outer-merge nightly vs full → rows in BOTH = **10,782** (entire full set preserved), ONLY-in-nightly = **6** (the forward delta), ONLY-in-full = **0** (the critical invariant: nothing dropped or mutated). The +6 are purely additive.

**CLAIM 3 — watermark = BD vintage:** `effective_date` max advanced 06-11 (full) → **06-12** (nightly) = the firm-wide BD settled vintage I independently confirmed on the D1 leg (06-12 = Friday, last complete business day). A_02's source ceiling is CORRECT, not a lag. AE's cross-link holds.

**Structural (not claimed by AE, checked anyway):** 0 duplicate rows in all three versions (no incremental-merge dup blow-up — a classic incremental failure mode, absent); stable 11-column schema across all versions (no column widen — never-widen holds at the schema layer).

## Disposition
- bd-TRIO morning-review legs: D_00f daily-watch CLOSED (12:54Z) + **A_02 co-cert CLOSED (this verdict)**. Both bd-TRIO morning legs done.
- CVO gate on DS's P1 fee_rate_history .py cutover is **CLEAR** from the data-integrity side (incremental == full exactly + non-regressed + watermark-correct). DS owns the .py cutover sequence through the safe-deploy chain; CVO has no blocking finding.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| aws-cli (s3api head-object / list-object-versions / get-object --version-id) + pandas/pyarrow | independent parity reconstruction from S3 version history (F5: verify-against-served, derive don't-trust-the-log) | PASS — content-equality proven, 0 regression, watermark-correct |

— 3.0.0_SA_CVO
