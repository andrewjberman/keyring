# Andrew-direct 2026-10-14 ~20:1xZ (dell1, `1.0.0_SA_CTO~DELL1` terminal) -- /portfolios smoke (CN-i-2): Trend needs full history; Cottonwood Trend to be specced

## VERBATIM

> "I'm going through the model portfolios edits and have the following comments. First on the Global View: All global edits are fine on the
> various popup modals except for the trend view here [Image #1]. If we're going to do it like this, breaking all this stuff out, then we have
> to figure out how to render it historically. That should be fairly easy to do considering how the mass majority of client supervised is just
> what we used to call "other aua" from 49 Financial. Need CRO to spec out how this would be done to get us full history. If it cannot be done,
> then we need to stay with the old layout, however I believe it can be done as we have all that data. Furthermore if we are missing totals on
> any given day, just roll forward last known values, something that may be helpful for the Custom Models and etc. Second for the 49 Financial
> View: No comments, everything is good to go here. Third for the Inflection view: No need to touch these. Fourth for the Cottonwood view: This
> one could benefit from some surgery look how uneven this is [Image #2]. CRO needs to spec this out afterward, how to upgrade this, potentially
> employing the same tricks it comes up with on the aggregate view regarding how to find/fill/roll-forward the asset taxonomy grops as needed."

Image #1: Global view, AUA Trend Analysis (quarterly bars and daily area). Before 2026-05-15 only an Other-AUA grey total is drawn; the
per-model break-out starts at the Jun 30, 26 bar. Image #2: Cottonwood view, AUM Trend (monthly). There are empty months, an "Interpolated
model mix (estimate)" region from 2026-05-28 to about 2026-07-18, a shaded Jan 30, 26 column and no Aug 31, 26 bar.

## What it decides (verbatim scope; nothing wider)

1. **Global view, every popup-modal edit EXCEPT the Trend: approved.** That includes the Total Assets Client Unsupervised lime repaint.
2. **Global view, the Trend as built on `cand/dell1/mdpf-canon-aua-trend-groups-repair` @`fd5433a3` (break-out from 2026-05-15, earlier dates
   in the Total only): NOT approved.** Approval row `dell1-20261014T193937Z-19ae` closes DECLINED `--by andrew` on this record.
3. **The Trend break-out must render the FULL history.** The CRO specs how. Andrew's lead: most of Client Supervised is what was called "Other
   AUA" from 49 Financial. If the full history cannot be built, the Trend stays on the OLD layout (PROD's).
4. **A day missing a total rolls forward the last known value** (Andrew names Custom Models as a likely user). This supersedes, for this page, the
   MDPF_CANON PRD v2.18 FWD-9 clause (2) exception (ii) ("per-model detail begins <date>; ... not broken out ... the gap is printed"). The PRD
   addendum follows the CRO's spec.
5. **49 Financial view: approved as is. Inflection view: not touched.**
6. **Cottonwood view, Trend: the CRO specs an upgrade AFTER the Global spec**, reusing its find/fill/roll-forward methods for the asset-taxonomy
   groups.

## Open, on the reply that carries this record

Whether the approved edits (1 and 5) ship now with the Trend held at PROD's layout, or the page waits for the full-history Trend. This seat's
recommendation: ship now. That is asked, not assumed.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (~20:18Z) -- reconciled with Andrew's laptop word on 19ae

The laptop CTO's record `ANDREW_DIRECT_20261014_200xZ_TWO_APPROVALS_90A9_19AE.md` @`0234fae9af` (CLOUD `69c37f5376`) quotes Andrew: "CALL 2 I
ACTUALLY LIKE ALL THESE CHANGES SO THOSE ARE FINE WITH ME. FURTHERMORE, I PROVIDED MORE FEEDBACK ON THE MATTER TO THE CTO ON THE DELL1 BOX".
The feedback it names is the VERBATIM above. Read together:

- **19ae's four changes are approved as changes**: the lime repaint, no zero tooltip row, the boundary note, and the type field. They carry
  into the full-history Trend.
- **The branch does not go to PROD as built.** His feedback sets the Trend's end state: the break-out over the full history, or else the old
  layout. A PROD Trend that breaks out only from 2026-05-15 is neither. The row was closed `declined` at ~20:12Z, before the relay arrived.
  It stays closed: the tool has no reopen. Its `declined` means the branch-to-PROD act, not the four changes.
- **Unchanged:** the open question (ship the approved edits now with PROD's Trend, or wait), and the CRO spec ask.
