# Deploy: emitter-wo4a-totals-refusal

**Opened:** 2026-07-28T22:58Z by 0.7.0_AE_CloudOps · **Authority:** MDPF_RESET Amendment 1 WO-4a
as revised by CTO 223619Z (COO 32-cohort trace); Andrew-direct order is the authorization to
touch this component (R1 hands-off yields for the emitter only).

**The defect (measured by COO):** `apply_channel_resource`'s total-row re-derivation summed
`(value or 0)` over blanked contributors → minted $0, overwrote the genuine $1.78bn carried
headline, kept the carried row's fresh `as_of` (no re-stamp), and its tautological
`reconciled` self-comparison (0==0) destroyed the genuine verdict so `assert_ac7` could not
fire. Served: $137.17mm→$0 "TOTAL — partner AUA", fresh, 07-18.

**The fix:** refusal path mirroring `_total__etf_fund`'s partial-sum refusal — zero/partial
constituents ⇒ `value=None` + `absent_reason` (`zero_constituent_total` /
`partial_constituent_total`) + named missing legs; `_stamp_state` re-called on BOTH paths
(total's vintage = min/worst contributor `as_of`, never the artifact's); the self-comparison
deleted. Plus the PIN-4 trigger-identity event log. Package tests 59/59.

## Completion

(open)
