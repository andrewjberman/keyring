# ADVI_COTBKF decomposition -- ROUND 28 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~04:5xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s analysis ADDENDUM 3 (msg 2476): CB27aa1-AC3 NOT MET stands (the reach cap moved 0.5 -> 1.0 after
exploratory runs on the same months); the cap returns to 0.5; a later cap change is legal only as a rule stated before a run on held-out
months. Enrichment E1 (the W50-S1..S3 repairs, un-holding CB-aa-4), E2 (re-run at the committed 0.5, `flow_value` shown or dropped), E3
(any cap change only as a pre-stated rule on held-out months). Prepared from the issuer's draft @c8bdb8342f.

**Rule 24.** Domain: E1, E2, E3. Three cells, two chains. E1 -> the SERVED re-cut is build -> apply. E2 is a re-run of the trace. E3
proposes nothing, so it is carried as a BOUND on E2's cell (a cap change there is legal only through it), not as an empty cell. E1 writes
the chain and E2 writes the trace script: disjoint surfaces.

## Measured constraints

1. Round 27's real runs on the trunk (@59c97c4def and before): the default `method_r26`, MATCH 3,098 / DIFF 886 / UNGRADABLE 78,609;
   `DIFF-TRACE months=512 traced=73 untraced=439` at REACH_CAP_PCT 1.0 (`commonwealth_diff_trace.py:87`); 70 at 0.5 (the CTO, from the CVO's
   grade).
2. CB-aa-1's trace confirmed 14 splits from the accounts' own rows (quantity ratio within 0.5% of an integer k in 2..50, or 1/k). The stored
   closes before a split are split-adjusted, so as-traded = stored x k (issuer draft @c8bdb8342f). dell1's store offers
   `as_traded_close` + `splits.parquet` for its 32 covered CUSIPs.
3. The FWD-3 serve builder (`commonwealth_fwd3_serve.py`, @59c97c4def) builds the three tables at the chain's default cash leg; the SERVED
   mint is held by row D2-S39's condition on the pair's COO half until E1 drains VALID with 0 regressions.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-ab-1` | E1: rule `method_r28` (the default) -- closes before a confirmed split scaled to as-traded; a `dvr` close-step day and an understated in-kind `li` valued from the shares or blanked with reason; re-grade `method_r26` -> `method_r28` with 0 regressions and the 73 counted | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~53` |
| `CB-ab-2` | E1 (cont.): the SERVED mint of the three FWD-3 tables at `method_r28`, under the never-widen pair, read back | FWD-3 | SERVED | `CB-ab-1` | `0.7.0_AE_CloudOps~CB2` |
| `CB-ab-3` | E2 (+ E3 as a bound): the trace re-run at REACH_CAP_PCT 0.5 with the cap printed; `flow_value` shown or dropped; any cap change only as a pre-stated rule on held-out months | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~54` |

**Fan-out:** `2 of 2 chains, cap 8`.
