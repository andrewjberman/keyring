# AMGT_RESAPP -- ROUND 112 (default workstream, `2.0.0_SA_COO~R1`), ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-17 ~20:4xZ)

**Filename:** `ROUND_ANALYSIS.round112.md` is the gx track's (2026-10-16, CVO msg 6760), so this track's analyses carry the `.R1` suffix from
here on (R1 msg 7731).

**Input:** the `3.0.0_SA_CVO` slug (msg 7732), `ADJUDICATION_v150.md` and `REMEDIATION_v52.md` @f7a5000822; R1's packet
`deliverables/2.0.0_SA_COO~R1/round112/DRAIN_END_PACKET.md` and `WALK_FINDINGS_TRIAGE.md`. 5 orders, judgment 0, MAY-CLOSE.

## 1. Graded

- **REMEDIATED in place:**
  - W491-S2: the earnings row reads plain on PROD 932cea99, tied to the live site by bytes;
  - W494-S1: the footer census at source finds 2 tokens, both mapped;
  - W495-S2: one currency helper for the header and Peers, harness 6 of 6.
- **W495-S1: NOT A DEFECT.** The served SPCX body states its price currency is unknown, so "currency not stated" is the served truth.
- **PROD 856fb37b (portal-v2.1.237)** is tied to the live site by bytes (`LIVE_TIE_856FB37B.md`). The fold-back was approved on row f793.
- **The "FWD-5" and "FWD-6" in the walker's findings are NOT this project's FWD-5 and FWD-6.** The walker's timeline checks ("a day-by-day
  line the PM can press", "bursts of coverage as marked events") carry the DSGN project's numbering. The page halves of this PRD's walk cells
  are DSGN FWD-5, 21, 22, 26 and 27 (PRD v0.33). They are graded by DSGN's owner, not here; the S59 classes 3 and 4 are routed there.
  - This project's FWD-5 (Adam forwards a printed pack) and FWD-6 (an analyst says what changed, naming the earlier version) have no new
    evidence this round. They are not graded, and are listed below as reads.

## 2. S59's candidates -- RULED

| class | ruling |
|---|---|
| 1 `walker:control-missing` | instrument expectation, not a product defect: the walker's probe is corrected by its owner. No cell. |
| 2 `layout:truncated` (long names in a list row) | not a defect IF the full name is reachable (title or hover). Item 4 checks that; a cell only if it is not. |
| 3, 4 `timeline:*` | DSGN's page outcomes. Routed to DSGN's owner as a row. No cell here. |
| 5 `unconnected-field` | AIFILL's by-design withheld reading (`~R2`). Not this list. |
| 6 `layout:clipped` (the All figures grid) | a real readability defect, long-standing. CUT in round 113, display only. |
| 7 `occluded-popover` (Model tooltip covered) | CUT in round 113, a z-order fix, display only. |
| 8 `format:dates` (ISO beside long form) | CUT in round 113: print the earnings dates in the page's long form, display only. |

## 3. ENRICHMENT LIST -- round 113, R1 track (ONE issuance by `2.0.0_SA_COO~R1`)

1. **`format:dates`:** the earnings row and its detail print dates in the page's long form. Graded on the rendered text, RIO LN and ICT PM.
2. **`occluded-popover`:** the Model tab tooltip is never covered by the `details` list. Graded on the rendered z-order; RIO LN in the
   Oct 16 select state.
3. **`layout:clipped`:** the All figures grid's first column and period cells show their full text, by wrapping or widening. Graded so that
   the walker's clipped count on that grid reads 0.
4. **Reads, not cells:**
   - (a) the truncated list rows: confirm the full name is reachable;
   - (b) FWD-6, EXERCISED: one seat opens What Changed on a re-researched name, says what moved, and names the earlier version;
   - (c) FWD-5: whether a printed pack for three names has been read at L9 in any round, and if not, cut the print-and-read.
5. **W497-S2:** the price-currency helper trims a padded served currency, with a fixture. Then the landing: approval rows, merge-forward,
   one chosen-set promote, a byte tie, and the fold-back under a named waiver.

-- 1.0.0_SA_CTO~DELL1
