# ADVI_COTBKF decomposition -- ROUND 27 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~03:1xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s analysis ADDENDUM 2 (msgs 2213, 2257): close round 26 (CB-z-2 withdrawn, AC2 NOT MET; MAY-CLOSE
@2f8c0737bf); round 27 = E1 trace the 512 untraced DIFF months; E2 the price input for UNPRICED (74,846 months, 94.2% of non-MATCH)
filed with dell1's MDPF_DEMQUE queue -- "the lever", owner `~C2`, a parked hop never a wait; E3 a cell SERVING FWD-3, which no cell serves
today (endpoint read: FWD-3 NOT, "no daily-returns table served").

**Rule 24.** Domain: E1, E2, E3. Four cells, three chains. E1 reads the chain and writes one tracing script. E2 reads the census and
writes the ranked need file. E3 is build -> apply: a builder of the served tables, then the SERVED write by the box applier under a
never-widen pair. The write surfaces are disjoint.

## Measured constraints

1. Round 26's real run on the trunk (@718291c2c7): the default `method_r26`, 82,593 graded months: MATCH 3,098; DIFF 886 (512 untraced:
   478 where no posting category's exposure reaches the difference, 34 with no driver row); UNGRADABLE 78,609 (UNPRICED 74,846).
2. The served addresses come from the builder, measured now (`lib/opal_naming.address`, scope from the registry):
   `s3://opal-data-assets/commonwealth/cottonwood/silver/daily_returns/date=2026-06-23`, `.../month_grades/date=2026-06-23`,
   `.../account_day_value/date=2026-06-23`. Nothing exists at those keys today (endpoint read, row W49-S1).
3. dell1 MDPF_DEMQUE's price store contract @8abd95ad3b keys on Commonwealth's 9-character CUSIP. The CRO's ranking (@e112184d3b
   section 6): P1 a living client holds it; P2 match open; P3 gone; within a tier, held days x accounts weighted by the largest purchase.
4. Applies on dell2 go to `0.7.0_AE_CloudOps~DELL2` (Andrew ~22:0xZ, MSTR msg 1751). Egress is open except Bloomberg (law edit
   4d77a9c3ea).

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-aa-1` | E1: trace each of the 512 to a named valuation-side cause (price, holdings, carried level, ...) or `untraced:<what was checked>` | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~50` |
| `CB-aa-2` | E2: the ranked price-need file for every UNPRICED security-span, key CUSIP, tiered P1/P2/P3 and scored | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~51` |
| `CB-aa-3` | E3a: the FWD-3 serve builder -- daily returns, account-day values and month grades (with Commonwealth's reported figures beside them) as silver tables at the builder's addresses; dry-run and verify modes | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~52` |
| `CB-aa-4` | E3b: the SERVED write of those tables, under a never-widen pair and a ledger, read back | FWD-3 | SERVED | `CB-aa-3` | `0.7.0_AE_CloudOps~CB2` (MSTR msg 2264) |

**Fan-out:** `3 of 3 chains, cap 8`. After CB-aa-2 lands, the issuer files the need file with dell1's queue (the issuer's record, not an
order -- round 25's precedent).
