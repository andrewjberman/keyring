# NFRA_TRNSPT decomposition -- ROUND 22 (2026-10-09, issuer 2.0.0_SA_COO~T2, dell2, box/dell2)

Cut on `1.0.0_SA_CTO~DELL2` msg 3796, `CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_12_20261008.md` ADDENDUM 13 @d1f23acf0c: "Round 22 enrichment list: (1)
the FWD-3 fetchable-vs-landed census; (2) each new meeting type's first landing read as it occurs; (3) FWD-9's grade on t1's landing." For (1):
"ONE LOCAL cell: list every meeting the gateway reports as fetchable on 2026-09-29, printed with that denominator, against the silver
landings, with each missing one named and its reason."

| cell | item | outcome | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|
| `TR-c-22` | (1) `teams/census.py`: given the gateway's transcript listing per allowlisted series and the silver keys, return every transcript created on or before a cutoff date (the "fetchable on" set, denominator printed), each marked `landed` or missing with a `completeness.py` cause; a `--live --cutoff 2026-09-29` CLI that reads read-only. Built on fakes | FWD-3 | dell2 worker | LOCAL | worker-light | -- |
| `TR-cr-22` | (1) the issuer's ONE live run of `census.py --live --cutoff 2026-09-29`, recorded as counts, series and causes (no content) | FWD-3 | ISSUER (read-only) | SERVED | -- | TR-c-22 |
| `TR-n-22` | (2) the issuer's read of each NEW meeting type's first scheduled landing as it occurs (ocio_ic, asset_management_ic), with `p18_readback.py` (residual re-wipe 0, planted control) | FWD-2 | ISSUER (read-only) | SERVED | -- | each series' next occurrence (event) |
| `TR-f-22` | (3) FWD-9: once t1 lands, one served commentary read through `query/securities_across.py --live` (counts only) | FWD-9 | ISSUER (read-only) | SERVED | -- | IRPT_ANLREQ TO-APPLY-t1 |

**Chains.** A = TR-c-22 -> TR-cr-22 (worker slot, then the issuer). TR-n-22 and TR-f-22 are event-gated issuer reads. Fan-out 1 of 1 worker chain, cap 8.

**Issuer rulings.**
(1) "Fetchable on 2026-09-29" = a transcript the gateway lists today, under an allowlisted series, whose created time falls on or before
2026-09-29 23:59:59Z. The research meeting is in the denominator and carries cause `refused` while the gateway answers 502 for it.
(2) Counts, series, dates and causes only; never transcript text.

## Rule 24 record

Domain: ADDENDUM 13's three items.
- (1) = TR-c-22 + TR-cr-22.
- (2) = TR-n-22.
- (3) = TR-f-22.

Remainder: none. Carried and not cut: FWD-6 (parked on site Z OG-ab-2), FWD-8 admitted read (site Z), Andrew's acts (the Monday read, the
research grant, the named past meeting).

## Battery

`org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R22_CHECKS/r22_checks.py c22` at base: FAIL (absent).
