# L4-R review -- DSGN_IRPTV1 PRD v0.7, ratified-text half (`3.0.0_SA_CVO`)

**PRD:** `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` @`8942931687` (v0.7). **Half:** ratified-text,
`half_hash` `eda43d9a7a6b`, ENDPOINT hash `5c40ea8d882f`, both re-measured at HEAD with `prd_signoff_lib`.
**Deliveries:** `1.0.0_SA_CTO` 100902 (v0.6), 100920 (v0.7), 100921 (v0.6 re-offer). **Prior stamp:** SIGNED at v0.4
@`2c60ba747f` (ENDPOINT hash `119a6d6086e1`). **Delta read:** v0.4 -> v0.7 ENDPOINT section, 131 diff lines; v0.6 and
v0.7 ENDPOINT sections are byte-equal.

**Verdict: REFUSE.** Two pairs of ACCEPT lines in the ENDPOINT contradict each other, so no build can pass both
lines in either pair at L9. The fix is three clauses. The rest of the half is clean and is listed below so the
re-sign is scoped to those clauses.

## R1 -- the footer: FWD-5 and FWD-6 contradict FWD-18 (BLOCKING)

- FWD-18 ACCEPT, PRD :197-198: "the bottom bars carry only the source and the time". Source: Andrew verbatim,
  `org/tier1_exec/2.0.0_SA_COO~D/deliverables/ANDREW_DIRECT_20260924_194xZ_IRPT_DESIGN_NOTES/performance_and_general_ui.verbatim.txt`
  :26-28, "We only ever put source and timestamp in the footer bars. That is consistent across the entire portal that
  has to be maintained."
- FWD-5 ACCEPT, PRD :88-89: "method and lineage sit in a footer line with a popover".
- FWD-6 ACCEPT, PRD :97-98: "basis, denominator and provenance move to the footer".

FWD-5 and FWD-6 are unchanged since v0.4 and are verbatim from the endpoint record @`5daacc16db`. The v0.6 brief
makes both lines wrong in part, but v0.6 amended FWD-2, 3, 7 and 8 and did not amend these two. By
`2.0.0_SA_COO~D`'s handoff messages (claims, not yet graded), the landed FAST pins follow FWD-18: portal DEV `c75a0fc9` (Holdings footers are timestamp and source only; the basis and denominator sit
behind the header help icon) and `af66ed43` (the Performance footer is the same). Graded as written, FWD-5 and FWD-6
fail on the work Andrew asked for.

**Fix** (amend in place, ids unchanged, per `/endpoint` step F0.2):
- FWD-5: "method and lineage sit in a footer line with a popover" -> "method and lineage are one click away behind
  the panel's help tip".
- FWD-6: "basis, denominator and provenance move to the footer" -> "basis, denominator and provenance sit one click
  away behind the panel's help tip".
- For consistency, CONTRACTS :243 "the disclosure surfaces (footer line, popover, Details)" -> "(help tip, popover,
  Details)". This is not in the ENDPOINT hash; it is named here so the bump makes the change in the same commit.

## R2 -- the first Analysis step: FWD-7 contradicts FWD-8 (BLOCKING)

- FWD-7 ACCEPT, PRD :105: "the first step is three cards in the Philosophy page's card style".
- FWD-8 ACCEPT, PRD :120 (unchanged since v0.4): "the first step leads with the upload" (with no client selected).

For a prospect, step 1 cannot both be the three cards and lead with the upload. The word "first" in FWD-7 has no
ratified source. Andrew, `analysis_ui.verbatim.txt` :57-64, places the cards "somewhere on here to give some visual
pop". The brief @`20f90739bd` Part VI S3 calls the cards "its variant step". FWD-7's own SOURCE line calls them "the
variant step".

**Fix:** FWD-7 "the first step is three cards" -> "the variant step is three cards". FWD-8 then fixes the order for
the prospect, and the COO sets it for a client at L5.

## Checked and clean at this pin (not re-opened by the bump)

- **FWD-2, FWD-3 amended; FWD-12 to FWD-17 added:** each ACCEPT carries its brief O-line (O2, O1, O3-O7, O10) and
  Andrew's cited lines. FWD-13's five colours match H:69-73 as the brief quotes it. C1 is answered green, and the answer is
  recorded (`ANDREW_DIRECT_20260924_214xZ_IRPT_UI_CALLS_C1_C3_ANSWERED.md`).
- **The retirements** (FWD-7 rail, FWD-8 history): each states in one line what the project no longer promises, as
  `/endpoint` F0 requires. "AMENDED v0.6 (the outcome was wrong in part)" is the skill's required statement of which
  case applied. I do not grade it as the annotation the spine bars.
- **Ids:** FWD-1 to FWD-18, no gap and no reuse. The header `endpoint_outcomes` matches the defined set.
- **No seat serial** in the ENDPOINT section.
- **CONTRACTS:** the v0.6 members (`asset_class`, the unclassified value, the model code) are real members.
  `asset_class` is in `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` and in the portal
  `contracts/adapt.ts` (comp-find, 70 hits across 2,611 files, DEF=3). The counterpart IRPT_BCKEND PRD v0.17 names
  none of the additive members, `display` included. This is the same shape I signed at v0.4, so it is not a finding.
- **FWD-16 against FWD-5 and FWD-6:** "at rest ... headline and one main picture" reads consistently with FWD-5 and
  FWD-6 once those lines describe what is reachable rather than what is at rest. No change asked.

## Instruments

| question | instrument | result |
|---|---|---|
| half and ENDPOINT hash at HEAD | `prd_signoff_lib.half_hashes()`, `endpoint_hash()` | `eda43d9a7a6b`, `5c40ea8d882f`; match the delivery |
| ENDPOINT moved v0.6 -> v0.7? | section-slice equality at `4746617b10` and `8942931687` | equal |
| FWD-5 and FWD-6 moved since v0.4? | block equality at `c4b9056831` and `8942931687`; substring read of the record @`5daacc16db` | unchanged; both clauses verbatim in the record |
| cited clauses | `git show 8942931687:<prd>` printed at :88-89, :97-98, :105, :120, :197-198, :243 | quoted above as printed |
| Andrew's footer and card words | the verbatim transcripts, printed at P:26-28 and A:57-64 | quoted above |

-- `3.0.0_SA_CVO`, 2026-09-24 ~22:5xZ
