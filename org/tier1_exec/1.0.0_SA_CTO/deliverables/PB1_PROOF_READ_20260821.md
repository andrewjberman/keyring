# PB-1/PB-2 PROOF-READ — FRI 2026-08-21 13:30Z scheduled run: PASS
**archetype:** VALIDATE
**Author:** 1.0.0_SA_CTO · **Read window:** 2026-08-21 13:40–13:52Z · **Chain:** LD-0429 single-green
Friday (Andrew-direct "Better do do it now (a)"), staffing per LD-0438; DS~B's 12:45Z fire read =
GREEN (msg 64687, S3-verified) preceded this leg.

**Verdict: PASS — materialised-artifact reads, not the chain's own rc (per the R14 calendar's own
bar). The T-B re-point is EXERCISED END-TO-END at the executing plane on a scheduled fire.**

## PB-1 — "run succeeds reading the {D-1} gold self-carry; no json/mdpf read at executing bytes"

**Executing plane (invocation: `aws lambda get-function mdpf-gold-lambda` → package download →
member sha + byte greps):**
- Package LastModified `2026-08-19T13:48:28Z` — the T-B member-rebuild deploy (ledger
  `20260819T1349Z_mdpf-gold-lambda-tb-member-rebuild`, CLOSED).
- Member `dim_mdpf_aggregate_aua_timeseries.py`: sha256[:16] **`a7db07bb68f465d5`** — byte-equal to
  the safe-deploy-verified HEAD bytes in the T-B proof instance. Executing = repo. The 08-19
  executing-plane gap (old member `ce9c0284537e1948`) is CLOSED.
- `f"json/mdpf` read-construction: **0 of 2,948 lines**. Bare-string census: 2 hits, both one
  comment (member lines 655–656) *describing* the retirement — no read. Second member
  `mdpf_aggregate_aua.py`: 0 hits of 1,471 lines.

**Run + self-carry (invocation: s3api listing + artifact fetch, UTC):**
- `portal/gold/mdpf/49financial/aggregate-aua-timeseries/2026-08-20.json` LastModified
  **2026-08-21T13:31:07Z**, 134,295 B — in-cadence (siblings land 13:31:0xZ daily), size-consistent.
  `_provenance`: producer `mdpf-gold-lambda (mdpf_gold_consolidator)`, trigger `scheduled`,
  process_time `2026-08-21T13:30:38Z`, data_as_of `2026-08-20`.
- **Self-carry POSITIVELY discriminated:** count frontier carries `2026-08-18/-19/-20` stamps on
  the 5 core models (704 / 1606 / 3279 / 1387 / 168; the 2 SMA models honestly None — same cohort
  class as the prior measurement). Carried cells (08-18, 08-19) **equal yesterday's vintage
  `2026-08-19.json` exactly, 7/7 models** — and those dates structurally CANNOT come from the
  frozen source (frozen `json/mdpf/…` LastModified 2026-07-23, as_of_last 2026-07-22). Under the
  old path this class of cell measured None-on-every-model (T-B instance, 08-19). The loader is
  C2 fail-loud: a failed self-carry read produces no output, and the output exists.

## PB-2 — "coverage unchanged; carry ties to the cent vs frozen on common dates"

- `count_coverage_end` = **2026-07-18**, unchanged (today AND yesterday's vintage; matches the T-B
  unit exercise both-sides value).
- Value tie vs frozen on **429/429 common dates** (new 450, frozen 429): `model_aua` **427/429
  tie-to-cent**, `non_model_aua` **427/429**. The 2 non-ties are ONE CENT shifted between the two
  buckets on a single date (2025-11-03: model +0.01, non_model −0.01) with the date's **total
  conserved exactly at 1,272,693,921.46 both sides** — an allocation-rounding boundary, not data
  movement. Dispositioned as disclosed-finding, no action.

## What this discharges / unblocks

- **B1 (ADVI_49F brief) = PASS → B2 unblocks:** the held
  `json/mdpf/49financial/aggregate-aua-timeseries.json` delete (one object, both NEVER#3 halves
  signed) now has its proof citation — **this file**. The executing producer provably no longer
  reads that key (member sha + 0-of-2,948 grep at executing bytes). AE-class act; reader census
  stands per T-B (6,457-file census; the one other json/mdpf reader was `json/mdpf/global`,
  dispositioned + routed 08-19). NOT executed here — the act is AE's with COO routing.
- **T-B PB-1/PB-2 rows:** were UNCOMPUTABLE awaiting exactly this scheduled-run proof; this read
  supplies the PASS-grade evidence. Instance update is the assignee's (`0.4.0_DS_ClientPlatform`)
  on next live session; no gate manufactured on it.
- **LD-0429 chain:** DS GREEN (12:45Z fire, 64687) + CTO proof-read PASS (this file) → next leg is
  **CVO pin act + flip verification**, then flip → PROD promote SAME DAY (MSTR routes DT).

## Findings travelling with the PASS (none blocking)

1. One-cent bucket split on 2025-11-03 (above) — disclosed, total conserved.
2. DS~B's two WARNs ride the green unchanged: fact_fam declared-stale 08-10 (auto-lifts);
   BD xref AccessDenied (`bd-exporter-ec2-role` lacks `s3:ListBucket` on `opal-data-assets`) —
   IAM finding in my infra lane (`bd-pipeline/iam.tf`), owned by me, no hold on the chain.
3. `b02` materiality 1.7828% remains PENDING-RULING at Andrew+CTO — unchanged by this fire.

## Compiler tools

| tool | invocation | result |
|---|---|---|
| comp-find | `-i "PB-1" org/` (73 hits / 14,805 files) | PASS — located criterion + annex + brief |
| raw aws (rail-checked) | PB-1's own prescribed invocations: get-function, package download, s3api listing, artifact fetch | PASS — no comp-tool reads Lambda package members (the T-B executing-plane-gap class); comp-freshness answers age, not vintage-key identity |
