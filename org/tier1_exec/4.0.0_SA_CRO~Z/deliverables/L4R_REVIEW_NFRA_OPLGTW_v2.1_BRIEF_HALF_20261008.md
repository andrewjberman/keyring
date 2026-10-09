# L4-R review: NFRA_OPLGTW PRD v2.1, brief half -- SIGNED

**Reviewer:** 4.0.0_SA_CRO~Z. **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` @8dccd20fa2, half `brief`,
half_hash 0ba5e33a96c7. **Delivered:** 1.0.0_SA_CTO~O msgs 32124 and 32126. **Read:** the pinned bytes, in full for
FWD-14 to FWD-19 (lines 175-233), BRIEF COVERAGE (411-430) and the v2.1 addendum (775-837).

**The brief for v2.1** is `docs/briefs/oplgtw-tax-workflow-midstream-brief-20261008.md` @dae0456eb4 (this seat, midstream).

## Outcomes, one by one

| Brief outcome | PRD | Content carried | Verdict |
|---|---|---|---|
| O1 thread, one 08335338 account's quarter | FWD-14 (:175-183), A26 | the six reconciliation inputs; each value names its source field; a figure that does not tie to the statement says why | carried. The "says why" clause also covers my Part VI.5, where the quarter-start value ties on no date |
| O2 the key | FWD-15 (:185-193), item 4 (:802-804), A27 | last four plus name, or full number; ambiguity returns candidates; last four alone refused; MDPF_TAXSMA's identity rule reused | carried |
| O3 since inception | FWD-16 (:195-203), item 5 (:805-808), A28 | roster inception never account-open; flows include `security_transfer_in`/`_out` at market value and `advisory_fee` as required members; inputs only, no return | carried |
| O4 realized, four buckets | FWD-17 (:205-213), item 7 (:813-817), A29 | short/long x gain/loss, quarter and since inception, lot grain, tie to Schwab's totals line | carried |
| O5 lots as of quarter end | FWD-17, item 7 | lots held ON the date, never today's repriced; shorts included; missing basis is `null` with `basis_status: missing` | carried, sharper than the brief (it names the null shape) |
| O6 Black Diamond | FWD-18 (:215-223), item 3 (:796-801), A30 | the four Cottonwood tables, roster accounts only, read only, same shape, source named, non-roster account refused | carried. Note 1 |
| O7 08403355 to inception | FWD-19 (:225-233), item 8 (:818-821), A31 | backfill from the earliest roster inception on that master; the "no files before a date" stop | carried; it answers my Part VII unknown with a stop rule |
| O8 Alyssa's access | item 1 (:788-793) | identity, three sources, window to each roster inception; hidden classes stay hidden; no download operation, on his ~19:2xZ word | carried |
| O9 top-10 and sector | FWD-17 (top-10); item 7 (:817) | top-10 served; sector NOT served, reason stated | dispositioned in writing. Andrew said "may potentially", so a named cut is enough |
| Part II, returns not computed | :785-786, FWD-16 | stated as his scope bound | carried |
| G-6 value field | item 6 (:809-812) | `eqty_incl_option` served, named, never substituted; the MDPF_TAXSMA difference surfaced to its owner | carried |
| G-4 completion floor | item 5 | backfill reaches the earliest roster inception; 13 months stays the cap | carried |

## The heading denominator

The BRIEF COVERAGE table (:411-430) still enumerates the September commission's ten headings and not this brief's parts.
The addendum invokes rule 27's proportionate sign-off. I map the denominator here instead. The brief has Parts 0 and I to
VII plus refs. Part I (O1 to O9) is in the table above. Parts II, III and V are carried as item 1's scope bound, FWD-14's
"names its source field" and item 3's grant. Part IV.B's gaps G-1 to G-10 and G-12 are carried. Part VI is
not outcome-bearing by its own label. Part VII's unknowns are carried as stop rules or surfaced to owners. The
remainder is in the notes.

## Notes returned by pinned line (none blocks)

1. **:796-801, Black Diamond.** My brief's Part V asked for Andrew's word before serving Cottonwood's data across the
   firm boundary. The addendum reads his ~22:0xZ words as covering the roster's Black Diamond accounts and nothing wider.
   That reading is narrow, matches his words and is stated as a reading, so I do not refuse on it. Andrew can still widen
   or narrow it.
2. **Not carried and not named as cut: G-11 corporate actions and G-13 statement PDFs** (brief IV.B; Alyssa's P1 items 8
   and 9). Neither appears in Andrew's ~22:0xZ words, so dropping them is in his scope bound. But item 7's last line names
   sector as not served, and these two are not named. One added line after :817 ("corporate actions and statement PDFs
   are not served in v2.1") would make the cut visible. Under rule 27 this is a wording change.
3. **Double presence.** The two Cottonwood accounts are Schwab-custodied (brief VII). If the 08403355 run shows them on
   that master too, one account would answer from two sources. :823 forbids summing across sources. Which source answers
   by default is not stated. That is for round 33's cells, once the run settles it, not for this half.

## Verdict

**SIGN.** All nine outcomes are carried, or their cut is stated in writing, at the width of Andrew's ~22:0xZ words.
