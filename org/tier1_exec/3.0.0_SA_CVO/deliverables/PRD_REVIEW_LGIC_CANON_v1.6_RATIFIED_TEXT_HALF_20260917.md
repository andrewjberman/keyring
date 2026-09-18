# PRD review -- LGIC_CANON v1.6, ratified-text half (ENDPOINT + CONTRACTS)

Reviewer: `3.0.0_SA_CVO`. Delivered by `1.0.0_SA_CTO` msg 97695 (nudged 97641/97647/97673/97674/etc.), ruling R-34.
PRD: `org/missions/D14/LGIC/LGIC_CANON/prd/LGIC_CANON_PRD.md` @ `af8d694cce`, ratified-text half_hash `d163690f05da`.
Prior review: v1.4 SIGNED at half_hash `1cd7a3546d93` -- STALE, bytes moved.

## VERDICT: REFUSE

## Method

Diffed the working-tree PRD (confirmed byte-identical to `af8d694cce` via `git diff af8d694cce HEAD -- <path>`,
zero output) against the ratified pins at `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_D14_PIPELINE_CANON_20260912.md`
(last touched `e2210bf34c`, 2026-09-13), FWD outcome by FWD outcome, printing the bytes rather than trusting the
PRD's own claim that its ENDPOINT section is the ratified block "verbatim, except ... each outcome's STATUS line."

FWD-1, FWD-2, FWD-4 and FWD-6 match the ratified pins exactly (module the STATUS-line removal, the accepted
precedent). FWD-3 matches the v2 amended text exactly. **FWD-5 does not.**

## DEFECT -- FWD-5's DONE WHEN and ACCEPT carry substance the ratified pins do not have, and an inline ruling
## citation sits inside the section

Ratified pins, FWD-5 (unchanged since v1, `STATUS unchanged from v1`):
```
DONE WHEN  EXERCISED -- a firm has actually been taken on this way and its people can see their dashboard
ACCEPT     someone follows the checklist from start to finish, the new firm's people see their dashboard
           at the end, and nowhere in it did anyone have to make a judgement call the rules should already
           have made -- where today every firm has been a one-off
```

PRD v1.6's ENDPOINT section, FWD-5:
```
DONE WHEN  EXERCISED -- the checklist has been run end to end on a LGIC_LGCTFM practice wave over an
           existing firm's subject, and that firm's people can see their dashboard at the end
ACCEPT     someone follows the checklist from start to finish on the practice wave, the firm's people see
           their dashboard at the end exactly as before, and nowhere in it did anyone have to make a
           judgement call the rules should already have made -- where today every firm has been a one-off;
           no demonstration firm is made up for it, and the first genuinely new firm re-runs it as
           confirmation only. A step that cannot complete because a live firm bucket does not exist yet is
           CARDED as a named gap with its owner and re-run when that bucket lands -- it never holds this
           outcome, and the run is graded on the steps the practice wave can reach (R-34)
```

This is not the STATUS-line removal this seat has already accepted as the section's one permitted edit. Both
clauses carry new, substantive text -- the LGIC_LGCTFM practice-wave scoping, the "exactly as before" qualifier,
the no-demo-firm / confirming-arm sentence, and the whole CARDED carve-out -- none of which exists at the
ratified pins, which still read the unamended v1/v2 FWD-5 verbatim (`STATUS unchanged from v1`, confirmed by
printing the bytes at `ENDPOINT_FWD_D14_PIPELINE_CANON_20260912.md:109-120`, last commit `e2210bf34c`, predating
both the 2026-09-16 ~18:2xZ call and R-34 itself). DEC-6 in this same PRD is the correct place for that
amendment's reasoning -- and it is done well there, with both authorities named -- but the ENDPOINT section's
job is to be the ratified pins, not a second place the amendment is argued.

Independent of that gap, the section carries its own annotation: `(R-34)` sits inline in the ACCEPT clause,
inside the fenced ENDPOINT block. That is the identical defect class this seat has refused twice this week on
a sibling project (`NFRA_OPLGTW` v0.6, and again at v0.8 for a one-word `(R-OG-11)` citation,
`PRD_REVIEW_NFRA_OPLGTW_v0.8_RATIFIED_TEXT_HALF_20260917.md`): "no annotation, history or seat name inside the
SECTION" (`org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md:165`). Here the citation is smaller than the underlying
problem -- even with `(R-34)` stripped, the surrounding sentence is still text the ratified pins do not carry --
but it is refused on its own terms too.

## The fix, named so it is not a re-derivation next round

FWD-5's ACCEPT/DONE WHEN bar has genuinely moved on two Andrew-direct authorities (2026-09-16 ~18:2xZ call 2,
and R-34 2026-09-17 ~19:0xZ) that this seat does not dispute and is not re-litigating. What is missing is the L2
step that makes that move a ratified pin rather than a PRD-local rewrite: `1.0.0_SA_CTO` re-cuts
`ENDPOINT_FWD_D14_PIPELINE_CANON_20260912.md` to a v3 (the same mechanism used for FWD-3/FWD-6's v1->v2 move,
each STATUS-tagged `AMENDED at v3` with the new text and its authority), and the PRD's ENDPOINT section then
transcribes that fresh, ratified FWD-5 verbatim, with the citation living in DEC-6 and the STATUS line (as with
every other outcome) rather than inside the section.

## Not re-opened

FWD-1, FWD-2, FWD-3, FWD-4, FWD-6 -- all four confirmed verbatim against the ratified pins (module the accepted
STATUS-line removal) and are not the subject of this refusal. CONTRACTS is unchanged in substance since v1.4 on
this read and was not re-derived line by line this pass, since the refusal is independent of it; the registry
and `NAMING_SCHEMA.json` rows were spot-checked against `LGIC_ENFORCE`'s and `LGIC_NAMING`'s own CONTRACTS
tables and agree (the registry row, direction reversed as `LGIC_ENFORCE`'s own CONTRACTS states explicitly).

-- 3.0.0_SA_CVO
