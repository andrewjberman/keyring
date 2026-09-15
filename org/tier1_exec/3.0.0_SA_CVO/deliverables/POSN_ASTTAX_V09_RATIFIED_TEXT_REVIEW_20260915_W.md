# POSN_ASTTAX v0.9 ratified-text review - REFUSE

**archetype:** VALIDATE

Reviewer: `3.0.0_SA_CVO~W`. Delivery: Msg-ID 22965 from `1.0.0_SA_CTO~Z`.
PRD: `org/missions/D4/POSN/POSN_ASTTAX/prd/POSN_ASTTAX_PRD.md@8eabf98d81cd3b713b792916bc785792f1b7f99e`.
Reviewed half hash: `c81dd95ccaafa29dad8e2c414056ae51bac9b516aa4218da81d8593a574b9028`.

## Verdict

REFUSED. Three corrections are required in the ratified-text review. This is a text review, not an implementation grade or a deployment decision. All PRD line references below are at the exact pin above.

## For CTO: corrections by pinned line

1. **Remove the history annotation from the ENDPOINT section (line 300).** The parenthetical beginning `(appended v0.9 at L10 ...` is inside ENDPOINT, including its code fence. The spine's L4-R rule (`org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md`, lines 164-167 as read) explicitly excludes annotations and history from the entire section. Preserve provenance outside the section; the v0.9 addendum already carries the records. This repeats the section-boundary defect removed in the accepted v0.7 correction, review `POSN_ASTTAX_V07_CORRECTED_RATIFIED_TEXT_REVIEW_20260914_Z.md@49c48aa2fe`.

2. **Reconcile FWD-6's literal bar with the newly operative presence rule (lines 283-285 versus 59-65).** The endpoint still says all modes show the same five classes. C-PRESENT-CLASSES instead requires each view to omit classes absent from its displayed books and explicitly supplies a different grading rule without changing the endpoint. The new ruling is supported by the read source at `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_021xZ_ZERO_CLASS_ROWS_HIDDEN_AND_SATELLITES_HOLDINGS_BREAKDOWN_EMPTY.md@65410eedaf`: Andrew's Models example excludes Commodities and Alternatives. Put the operative acceptance condition into the bound endpoint through the endpoint amendment process; retain the common five-class taxonomy and stable order/colour for classes actually shown. A brief-half interpretation must not silently substitute a different DONE WHEN for the signed bytes.

3. **Reconcile FWD-7's blank-cell acceptance with its disclosed source gaps (lines 294-299 versus 53-58 and 79-81).** FWD-7 permits blanks only where nothing prices the holding. The addendum says GLD is priced by Bloomberg, while its returns are absent and must remain NULL; `active` and `credit` also have no Bloomberg columns. F4 explicitly accepts GLD's blank returns. A priced ticker with no return field is a concrete case that passes the proposed cell bar and fails the literal endpoint. State the field-level availability condition and the disclosed limitations consistently in the endpoint, subject to the ratification required for that change. Do not use this finding as authorization for a vendor pull or as permission to invent values. The record `ANDREW_DIRECT_20260915_023xZ_ADHOC_FIX_SATELLITES_TONIGHT_NO_WAITING.md@0553548fe2` explicitly preserves the vendor-pull boundary in its recorded reading.

These findings are source-confirmed comparisons of the committed text and the cited ruling records. The PRD's live-data assertions were not independently re-measured during this L4-R review.

## Coverage and controls

- Scope follows the spine's delta-review rule. Read the complete current ENDPOINT, the complete v0.9 addendum and its whole-file diff, the previous accepted review and stamp, the pinned brief, and all three newly cited ruling records at `85621749e2`, `65410eedaf`, and `0553548fe2`.
- Compared FWD-1 through FWD-6 against the signed v0.7 PRD at `99cc4310757f2e4441008d2341c414fad1b6dee1`: 6/6 outcome blocks match after stripping surrounding block whitespace. FWD-7 is the sole new outcome, appended without renumbering; the header lists all seven in order. FWD-6's old text is unchanged, but the new presence rule changes its meaning if applied as instructed.
- Canonical `prd_signoff_lib.top_sections` identifies exactly one ratified section: ENDPOINT. No CONTRACTS section is present or introduced by this delta; the accepted prior review records no counterpart obligation. No cross-PRD contract equality is claimed for an absent section.
- `prd_signoff_lib.half_hashes` independently reproduces the delivery hash. HEAD had the same half hash at review measurement. The stamp must use `--expect-half-hash` with the full hash above, so a concurrent unreviewed change is refused.
- The previous CVO~Z stamp is STALE for the new half; it was read and not modified. This seat is permitted to render the delivered L4-R ratified-text act under its exact identity; this does not transfer POSN's L8/L9 ownership or begin AMGT round-10 L8.

## Compiler Tools

| Tool | Result and limit |
|---|---|
| comp-which | Ran before inspection; startup/document questions had weak or unrelated routes. |
| comp-read | Indexed the PRD and spine. Full section and pin reads supplied the text beyond its excerpts. |
| prd-signoff.py status | v0.9 WITHHELD; ratified-text STALE and owed by CVO~W; brief STALE and routed to CRO~W at first measurement. |
| prd_signoff_lib | Reproduced current/pinned hash, section membership, and the seven-outcome census; direct comparison matched 6/6 prior blocks. |

## What you should have asked but did not

An unchanged endpoint can become inconsistent when an addendum replaces its grading rule. Hash stability proves unchanged bytes; it does not prove that the surrounding PRD still gives those bytes the same operative meaning. FWD-6 is that case in this delta.

## Push state

LOCAL. No push. Measured origin/SITEZ: `6f09a06dc919bf21ef96b52aff5cd7e9608ccf85`.

-- 3.0.0_SA_CVO~W
