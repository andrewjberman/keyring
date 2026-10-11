# ADVI_COTBKF decomposition -- ROUND 65 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-11T10:25Z)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` ROUND-65 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_65_20261011.md` @1e9128413f (msg 4715), answering `3.0.0_SA_CVO` REMEDIATION_v37 @054e94e8fc.
Section 4 is this round's rectangle: three items cut, one carried.

**Where the project stands (the analysis, sections 1 and 2).** `account_return_daily` is a ONE-TIME backfill ending 2026-06-22
(C-ONE-TIME), read by no product (C-SCOPE-OUT). It is served, truthful and about 94% blank; no data already held prices the unpriced
securities; FWD-3 is not met in substance until the ruled price sources are drawn on.

**Rule 24.** Domain: the four items of section 4. Items 1 to 3 -> one cell each, none depending on another. Item 4 (the read-back of
the method row) is CARRIED, not a cell: it waits on IRPT_DASHBD's cell (row D2-S108), owner `2.0.0_SA_COO~C2`.

## Measured constraints (issuer)

1. **Nothing is sent or pulled this round.** The two price requests are documents. Bloomberg pulls go only through their queue
   (CLAUDE.md); `0.0.0_AB_MSTR~DELL2` carries each request to MDPF_SECHIST's owner in round 66, on the CTO's read of them.
2. **The legs.** Andrew's word (PRD lines 217 to 219) splits by KIND: Yahoo Finance for equity, ETF and fund securities; Bloomberg at
   site Z for fixed income and other. The analysis sizes the legs by SYMBOL (206 with, 253 without, on one date). The cell uses the
   build's own kind grouping and reports the symbol-less securities of the Yahoo kinds separately, so both readings are on the table.
3. **The Class D fix is not pinned to two days.** The cell measures the rule's reach first. The CTO's ruling re-mints "only those
   days"; if the reach is wider, that count goes back to the CTO before any re-mint order is cut.
4. **No served write, no re-mint, no deploy in this round.**

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-bm-1` | class the 207 measured days with an absolute return above 100%, by mechanism and kind, with the threshold table over all 107,311 measured rows | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~94` |
| `CB-bm-2` | the two price requests (Yahoo Finance; Bloomberg at site Z), each with its securities, date span, security-days and the account-days it would unblank; written, not sent | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~95` |
| `CB-bm-3` | a tax withholding is an external outflow with or without a same-day withdrawal row; reach measured first; tests | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~96` |

**Fan-out:** `3 of 3 chains, cap 8`. `CB-bm-3` is a DIRECT-ACT cell (LOCAL, mechanical only); `CB-bm-1` and `CB-bm-2` carry a judgment
criterion and take L8 to L10.
