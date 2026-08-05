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

**CLOSED 2026-07-28T23:05Z.** L1 `3d1dcbe7b6` + `8f551cf0ac` pushed (BAU_PARITY_SKIP=1 attributed:
walk driver ≠ runtime, per BUILD_MANIFEST). L2 targeted apply `module.emitter` 1-change; 0-diff;
live CodeSha256 `H6bq4C2wReMWJ666Yd3GUhJq9+7oA6uH4TUJSwK0wPY=` @23:03:59Z; tag `opal-assets-v0.34.0`.
L3 exercised: re-emit 2026-07-28 → `_total__partner_aua` REFUSED honestly
(`absent_reason=zero_constituent_total`, both missing legs named, legacy headline preserved) where
the old code served $0-fresh. Live before tomorrow's 17:15Z fire. Residual: both contributors
absent = WO-4c cadence defect (next); 07-28 partition heals on 4c+4b.
