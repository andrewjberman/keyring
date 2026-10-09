# MDPF_DEMQUE PRD v0.3 -- ratified-text half review (L4-R re-sign)

**Reviewer:** `3.0.0_SA_CVO` (dell1). **Object:** `org/missions/D8/MDPF/MDPF_DEMQUE/prd/MDPF_DEMQUE_PRD.md` @e90c4d4756, half_hash
`7102348e62da` (msg 1336). **Prior signature:** v0.1 @ac05f0256e (current through v0.2 by ENDPOINT hash). **Diff read:** the fenced
FWD block, v0.2 @94d21953b7 against v0.3: 62 -> 66 lines, 8 changed, all inside FWD-1 (ACCEPT reworded, AMENDED line added).
**Verdict: SIGN.** One wording finding.

## Checks

| Check | Result | Evidence |
|---|---|---|
| Authority for an ENDPOINT change after L2 | PASS | Andrew-direct 2026-09-03 ~05:2xZ, message 5 (record `ANDREW_DIRECT_20260903_052xZ_WHO_DECIDES_DONE_...md`): "if upon receipt it is in question, or if there is a scope change, the CTO can run /open-calls on the subject and then CTO adjudicates on the recs and it picks up from there via a new (or adjusted) PRD". Andrew confirms the DONE WHEN lines; FWD-1's DONE WHEN is unchanged. The CTO record states the card went to Andrew ~00:0xZ, no answer in ~1 h, and that he may override. |
| Only FWD-1 moved | PASS | The 8 changed lines are FWD-1's ACCEPT and the new AMENDED line; FWD-2..9 are byte-identical. |
| Grounded premise | PASS | Row `MDPF_DEMQUE-D1-W4-S2` (REMEDIATION_v1 @94d0ca79a6), verified on this seat's own reads: no Cottonwood page reads `canonical_prices.parquet`; `comp-find canonical_prices portal/src` 0 of 1,368 files. |
| Narrowed, not retired | PASS | Id kept; the trade-price agreement and "no person ran a pull by hand" survive verbatim; the consumer becomes the client's holding values for the backfilled dates. |
| Gradable | PASS | "has its daily prices value that client's holdings on the client's pages for the dates the backfill fills" is readable on the served client artifacts for a named security and date range. The consumer (ADVI_COTBKF, dell2) is a cross-box seam the round-2 issuance carries as a file contract. |

## Finding (wording; for `1.0.0_SA_CTO~DELL1`)

- **F1.** The AMENDED line sits inside the fenced ENDPOINT block and names a record, a version and a box. That is history inside the
  outcome text, which the L4-R standard keeps out of the section. It also changes the half hash on every future history edit. Move it to
  an ADDENDUM v0.3 below the block; the ACCEPT line alone carries the outcome.

-- 3.0.0_SA_CVO
