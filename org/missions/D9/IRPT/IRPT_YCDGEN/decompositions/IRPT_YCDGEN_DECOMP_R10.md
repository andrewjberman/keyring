# IRPT_YCDGEN round 10 -- decomposition: the page says a true reason, and the one account is read three ways

Issuer `2.0.0_SA_COO~G2`, 2026-10-11.

**Input:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_YCDGEN_ROUND_10_20261011.md` @ea78b95649, section 4
(six items, in order). It answers `3.0.0_SA_CVO`'s REMEDIATION_v8 @dafae769e6. The sitting is not asked: it is asked when ONE
Cottonwood account of six or more positions reads 90% covered on a regenerated report whose page sentences are true.

## Finding (round 9, by read)

The stored reason is fixed in the tree (merge @9a4242e1ce) and not deployed. The PAGE is not fixed:
`layout_overview._reason_line` prints one sentence for every `NOT_HELD:` cause and appends the stored string. Per account, 41 of
59 fully priced and symbolled Cottonwood accounts would read 90% covered after a 14-symbol list, one of them with six or more
positions; whether the store's source can describe those 14 at all is not established.

## Cells (round 10)

| cell | lane | item (analysis) | what EXISTS at the end |
|---|---|---|---|
| `YCD-a-10` | worker | 1 (row D2-S44) | The page prints one sentence per cause and no raw string: a figure with no rule, a figure with no row for the portfolio's securities, and any other not-held cause each read their own sentence, none containing `NOT_HELD` |
| `YCD-b-10` | ~G2 (direct read) | 2 | On the store's existing 172 securities, by kind: how many mutual funds, ETFs and cash symbols carry a country and a sector today. NO pull |
| `YCD-c-10` | ~G2 (direct read) | 3 | For the one account of six or more positions: its position count and its coverage by value today, after the 14, and after only those of the 14 that `YCD-b-10` says the source can describe. Counts and percentages; no account id, no figure |
| `YCD-d-10` | ~G2 (release, under its own pair) | 4 | The resident release that carries the reason fix and the page sentence, then the census re-run on a regenerated report |
| `YCD-e-10` | ~G2 (direct, after reading `integrations/bloomberg/READ_HERE.md`) | 5 | The data request WRITTEN for the describable subset of the 14, in the form the Bloomberg queue takes, and NOT sent |
| `YCD-f-10` | ~G2 (direct reads) | 6 | The two carried reads: the status re-read with the date opt-in (row D2-S38), and the generation hop from TCKT_VNEXT's run 3 trace (row S16) |

## Dependencies

- `YCD-c-10` and `YCD-e-10` follow `YCD-b-10`. `YCD-d-10` follows `YCD-a-10`.
- `YCD-f-10` waits on `2.0.0_SA_COO~Y2`'s irpt-status release (then ONE batch window, `1.0.0_SA_CTO~DELL2` msg 4392) and on
  TCKT_VNEXT's run 3 trace.
- `YCD-a-10` and `YCD-b-10` have no unmet dependency and start now.

## Not cells

- **The sitting**: Andrew's act; not asked (analysis section 2 states when).
- **Sending any Bloomberg request**: round 11, under its own pair; adding rows to the store moves served data.
- **The 70 rule-less elements**: FWD-14's scope, enrichment after the thread runs.

## Four-postulate record

(i) Domain: the analysis's six items, one cell each. (ii) One build cell, one release, four reads or writes of a document.
(iii) One intent: one real Cottonwood account reads 90% covered on a page whose sentences are true. (iv) What this round does
NOT move: the store's contents and the report contract. The resident host moves only under `YCD-d-10`'s pair.

fanout: 1 of 6 chains in this issuance as a tree order (a), cap 8; b to f are this seat's direct acts.
