# ADVI_COTBKF decomposition -- ROUND 25 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~00:2xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s round-24 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_24_20261009.md` @cdf5f13f3f (msg 1957):
`method` is the default; AC4's dividend clause stays NOT MET and routes to dell1's data queue (not amended); E1 unlisted types,
`ftax` first (35); E2 carried levels (39); E3 the ex-date filing.

**Rule 24.** Domain: E1, E2, E3. Three cells, two chains: E1 and E2 both write the cash-leg and flow treatment and are graded against
the same 3,059-match baseline, so they run as one chain on one worker; E3 is a filing, not code, and is the issuer's DIRECT ACT.

## Measured constraints

1. Round 24's real run on the trunk (@d9484f20fa): `months_after=3059/925/78609 year_chain_same=True r22_named=25/25 regressions=98`;
   the 98 by cause: unlisted types 35 (`ftax` 29, `ftax+stax` 1, `cbf` 3, `fco` 1, `stp` 1); pay-dated dividends 22; carried levels 39
   (`pre_first_valued_day` 16, `ManAltF` 14, trade cash 3, `csltfee` 2, other 4); `man` 2.
2. Unlisted types kept internal by default (row W46-S3): ASF, bcf, cbf, fco, stp, term, ftax, stax, frntax.
3. No ex-date in any store the chain reads (row W46-S2).

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-y-1` | E1: a treatment for each unlisted type, `ftax` first, each with its stated source; each of the 35 MATCH or traced; 0 new regressions against 3,059 | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~47` |
| `CB-y-2` | E2: each of the 39 carried levels traced to its first wrong month; any fix leaves the matches unchanged | FWD-3 | LOCAL | `CB-y-1` | `0.9.0_WK_ADVI_COTBKF~47` (continued) |
| `CB-y-3` | E3: the ex-date request filed with dell1's data queue, owner and the 22 months named | FWD-3 | LOCAL | none | issuer DIRECT ACT (`2.0.0_SA_COO~C2`) |

**Fan-out:** `2 of 2 chains, cap 8` (one worker chain of two cells; one direct act).
