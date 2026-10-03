# DSGN_REBRND -- status (FAST: /closer-drive under the lease)

Seat `2.0.0_SA_COO~D` (CLAUDE). Contract: PRD `org/missions/D13/DSGN/DSGN_REBRND/prd/DSGN_REBRND_PRD.md`. Reviewer
`3.0.0_SA_CVO` (grades each landed pin after the fact; round-2 grade
`org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND2_GRADE_20261001.md` @599d33a722). Authority: 1.0.0_SA_CTO RULINGS
batch 80 items 8-12 (the round-2 analysis; round 3 owed, this seat's, FAST, after the Investor Reporting work) and batch 165
@10d2b1c445 (msg 104234: round 3 un-parks now, every IR line being blocked outside this seat; its own `/positioning` lease;
IR keeps priority -- return to DSGN_IRPTV1 the tick any of its Next lines unblocks). **As of 2026-10-03T01:4xZ** (E4 done: DEV fe461611/44d6a215/b23917f7, rows S6-S8; E2: clause c9d303db and /positioning's page end 8526dacb on DEV).

## Pins

| What | Value |
|---|---|
| Lease | FAST `DSGN_REBRND` until 2026-10-02T14:10:34Z, armed 12:5xZ by this seat (`--by` batch 165): `portal/src/pages/Positioning/{Positioning.tsx, README.md, constants, index.ts, panels, shared, types.ts}`. NOT `Positioning/tabs/HoldingsTab.tsx` (the DSGN_IRPTV1 lease holds it; the arm's overlap refusal is the check) |
| Round | 3 (round 2 graded by the CVO 10-01: 4 of 10 outcomes REALIZED -- FWD-2, FWD-5, FWD-7, FWD-8; FWD-3, FWD-10, FWD-11, FWD-12 NOT REALIZED; FWD-4 partly evaluated; FWD-13 not evaluated; 5 remediation rows closed, 32 open) |
| Open task orders | 0 of 15 at the FULL -> FAST boundary (nothing to finish or supersede) |
| Working tree | the main portal checkout, branch DEV (shared with the DSGN_IRPTV1 lease, disjoint surfaces) |

## Write claims

- `2.0.0_SA_COO~D`: the `/positioning` page surface above. No claim open at 22:1xZ.

## Next (round 3's enrichment list, batch 80 item 9, in the ruled order; E4 started first by batch 165)

1. **E4 -- the page pass for FWD-12 and FWD-13 on `/positioning`** (first by batch 165). SURFACE HALF (FWD-12) LANDED:
   - portal fb5d6116: the Positioning Summary's six translucent fills on opaque rungs (bar tracks, placeholder and
     inputs: tile; the blend strip: body; the Collapse button: tile, hover rung on hover);
   - portal fe461611: the Holdings Breakdown's subtotal rows on the tile rung and grand-total rows on the selected rung,
     in the shared table and HoldingsTab's extra cells.
   Origin DEV fe461611, ls-remote 22:1xZ. After-walks: `tmp/ui-walk/20261002T214636Z` and `20261002T220333Z` against
   baseline `20261002T130259Z` (local). Hairlines are enumerated in fb5d6116's message and left as the band's light rule
   idiom.
   FWD-13 HALF LANDED for /positioning (portal DEV 44d6a215, ls-remote 00:0xZ):
   - The instrument is the walker's `--contrast-table`. Walk 20261003T000242Z graded 316 interactive text pairs (Models
     Portfolio and Custom, ETFs, Satellites), 0 under their bar.
   - Fixes (portal 661e49b3 + 44d6a215):
     - the AGG chip takes indigo400;
     - a highlighted book name keeps its colour and takes the band as its own ground;
     - the satellite ramp blends in OKLab (same stops and order; Models and ETFs unchanged).
   - RULING on row W2-S8 (this seat, CORRECTED in 44d6a215 after 661e49b3 removed the hover colour against Andrew's
     2026-09-15 word): the locked canon hex stays the hover ink, and the hover state supplies a ground (the band)
     on which every canon hex clears 4.5:1.
   - OWED: row W1-S11 (in the selected DARK mode no accent clears both white-on-accent and accent-on-band). It is
     this seat's to rule with a dark-mode table in hand; dark mode is not measured yet.
   The original text follows: every surface on the page resolves to a
   role of the one named-layer table (page, section strip, panel body, tile, inset, hover, selected, tooltip) with an opaque
   rung in both worlds; every interactive role's (ground, ink) state pairs clear the contrast bar in the state it is actually
   in. Measure first (the page rendered on 5174 and read), then fix in the surface. The two contrast rulings that bound
   FWD-13 (rows W2-S8, W1-S11) are this seat's, made with the contrast table in hand (batch 80 item 10).
2. E1 -- the Global RSI bands onto one hue (row S3; FWD-3). HELD AT ANDREW (card to 0.0.0_AB_MSTR 2026-10-03T06:18Z): Andrew-direct 2026-09-14 ~19:0xZ kept /market's original sentiment gradient ("it was changed to a Blue Gradient, that is not necessary"; portal 45aaf58a; the row predates it), and E1 would put /market's RSI bars on that same blue ramp. BUILT, not landed: the patch `deliverables/2.0.0_SA_COO~D/e1/e1-rsi-ramp.diff` (RSIBars gradients and RSIModal bands, zones and guide lines on `--ramp-1..5`; the modal declares `dark-band`) and its pin `e1/rsi-ramp.test.ts.txt`. Yes -> apply and land; no -> E1 closes. Looked at on 5174 before the hold: the bars read the ramp on the band. Found while looking: the 70D/90D marker labels overlap the bars, a layout item outside E1.
3. ~~E2 -- the page-terminator clause in `portal/DESIGN.md` (row W1-S29; FWD-10)~~ WRITTEN: DESIGN.md C10 gains the PAGE END
   (portal c9d303db on DEV after PROMOTED 104493; lease re-armed with portal/DESIGN.md). /positioning ADOPTED it (portal 8526dacb,
   origin DEV): shared/PageEnd.tsx after the Holdings section. Signed-in walk 20261003T013711Z reads "End of Positioning. Data as
   of October 1st, 2026, 5:00p ET.", the footers' own format, with no format:dates finding. The clause names `typography.footnote`.
   Other routes adopt it in their own cells.
4. E3 -- the state census to zero, the no-permission and error states wired (rows W3-S5, W3-S1, W3-S4; FWD-11).
5. E5 -- the two project checkers that read red on the accepted tree (the grade's Q2).
6. E6 -- the old law still standing in the `/frontend-dev` skill and the "silver" mentions (Q4, rows W2-S15, W1-S24).

Each of E1-E3, E5 and E6 needs its own surface in the lease (a re-arm), outside today's `/positioning` arm.

## Open at Andrew

- FWD-9 (Andrew's own side-by-side) and FWD-1 (a walk by a person new to the portal) are person acts, unchanged.
- PRD v0.11 (batch 80 item 11: FWD-3's PROOF sentence against Andrew's 09-11 word that the ladder's five hues are canon) is an
  ENDPOINT change, both halves re-signed; it rides the round's FULL cut, not this FAST lease.

## Limits

- FAST never lowers a `<risk>` class; this lease touches the portal bundle only (DEV; PROD is Andrew's promote).
- Investor Reporting keeps priority (batch 165): a DSGN_IRPTV1 Next line that unblocks pre-empts this round.
