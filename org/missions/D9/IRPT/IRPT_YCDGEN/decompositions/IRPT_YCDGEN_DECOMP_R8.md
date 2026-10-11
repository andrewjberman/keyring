# IRPT_YCDGEN round 8 -- decomposition: the thread, re-measured before Andrew's sitting

Issuer `2.0.0_SA_COO~G2`, 2026-10-11.

**Input:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_YCDGEN_ROUND_8_20261011.md` @fe73849335, section 3
(five items), and its ADDENDUM 8.1 @02689893e2 (`1.0.0_SA_CTO~DELL2` msg 4332), which REVERSES the ruling on row D2-S38: the
producer conforms to contract v2; the reader (`ops/prospect_dates.py`) is fixed by `2.0.0_SA_COO~Y2` inside one irpt-status
release. No producer cell and no regeneration.

## Finding

FWD-1 is NOT MET and has never been run as written. The run of record (irpt-status revision 6, 2026-10-11) is a service account
reading an existing 49financial request: 6 of 6 calls HTTP 200, 6 of 257 sections carrying a value. Nobody has counted what the
251 unavailable sections say, and six generator, test and builder rows are armed against code that later cells rewrote.

## Cells (round 8)

| cell | lane | item (analysis) | what EXISTS at the end |
|---|---|---|---|
| `YCD-a-8` | ~G2 (direct read) | 1, as amended by 8.1 | One read of REQ-5e4149d2's status-job WITH the portal's date opt-in on the irpt-status release that carries the reader fix: it answers one of the two designed branches, not INVALID_INPUT. Row D2-S38 disarms on the reviewer's read of it |
| `YCD-b-8` | ~G2 (direct read) | 2 | The generation hop of TCKT_VNEXT's R2-tr-1 run, read from that run's own trace: reached or not, with what changed since 2026-10-07 stated. Row S16 closes or is re-cut on it. No second vendor-facing run |
| `YCD-c-8` | ~G2 (direct read) + applier | 3 | A census of the 257 sections of the retained report of the run of record: counts by page, status, method and the reason the page would state, taken through the served read. It goes to `1.0.0_SA_CTO~DELL2`, which rules D2-S39 (b) |
| `YCD-d-8` | worker + applier | 4 | Each of rows W6-S1, W6-S2, D2-W6-S3, D2-W7-S1, D2-W6-S1 and D2-W6-S2 is read again at the tree as it stands and carries one new row that RESOLVES it or RE-CUTS it; and one listing of the resident host's brand spec and logo exists (row D2-S3) |
| `YCD-e-8` | ~G2 (direct read) + applier | ADDENDUM 8.2 | For the run of record's own securities: how many of them the held-characteristics store carries a row for, per input (`CNTRY_OF_DOMICILE`, `GICS_SECTOR_NAME`), denominator printed; plus the code split of the 158 Opal-held elements by rule and the store's own row counts. It tells a read or join break from data that is not kept |

## Dependencies

- `YCD-a-8` waits on `2.0.0_SA_COO~Y2`'s irpt-status release (its round-3 item Y2: rows IRPT_ANLREQ-D2-S24, D2-S21 and the
  reader fix, one pair). It then needs one served-read window.
- `YCD-b-8` waits on TCKT_VNEXT's R2-tr-1 run existing.
- `YCD-c-8` and `YCD-d-8` have no unmet dependency and are cut now.

## Not a cell: the sitting (item 5)

Andrew, signed in as himself, one real Cottonwood portfolio, an Opal-branded Overview opened in the same sitting. Asked of him
only when cells a to d read clean. This seat prepares what he needs to know beforehand in three lines and no more.

## Four-postulate record

(i) Domain: the analysis's five items; item 5 is Andrew's act, which leaves four cells. (ii) Each cell is one read or one
re-measure; none builds product code. (iii) One intent: know what the thread does today before the sitting. (iv) What this round
does NOT move: the producer, the report contract, the resident host's root and any deployed byte.

fanout: 2 of 4 chains in this issuance (c, d), cap 8; a and b are direct reads cut when their dependencies clear.

## AMENDMENT 1 (issuer `2.0.0_SA_COO~G2`, 2026-10-11): cell `YCD-e-8`, before anything else in the round

`1.0.0_SA_CTO~DELL2` ADDENDUM 8.2 @d954d8deba (msg 4362) rules row D2-S39 (b): 6 of 257 is NOT an acceptable first Overview,
because all 155 Opal-held unavailable sections state `INPUT_MISSING` (census @ab43002cf5). It orders one cell first: read the
held-characteristics store directly for this request's securities. Part 1 (the code split and the store's own contents) is
`deliverables/2.0.0_SA_COO~G2/r8/HELD_STORE_READ_YCD-e-8_PART1_20261011.md`. Part 2 needs the request's tickers: one served read
of the request's original upload in window 9 (`IRPT_YCDGEN.TO-APPLY-sr4`), which writes only counts. Gate limb that graded this
amendment: `to-pipeline-gate` on the newly-added order, as printed at this commit.

fanout after the amendment: 3 of 5 chains cut (c, d, e), cap 8.
