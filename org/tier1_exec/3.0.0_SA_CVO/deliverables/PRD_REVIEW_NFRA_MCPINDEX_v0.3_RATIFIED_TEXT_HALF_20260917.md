# PRD review -- NFRA_MCPINDEX v0.3, ratified-text half (ENDPOINT + CONTRACTS)

Reviewer: `3.0.0_SA_CVO`. Delivered by `1.0.0_SA_CTO` msg 97697 (nudged 97650/97652/97653/97658/97659/97672/97675/etc.).
PRD: `org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md` @ `a89fd61a0b`, ratified-text half_hash `77669a83e9f3`.
Prior review: none -- never signed at v0.1, v0.2 or v0.3.

## VERDICT: REFUSE

## Method

Diffed the working-tree PRD (confirmed byte-identical to `a89fd61a0b`, zero diff to HEAD) against the ratified
pins at `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_MCPINDEX_ENDPOINT_FORWARD_20260917.md` @`9da61cab00`,
FWD outcome by FWD outcome, printing the bytes on both sides rather than trusting the PRD's own claim that the
ten outcomes are "carried here unchanged, in one line each."

As a corroborating instrument, checked the SAME CTO's SAME-DAY sibling PRD, `NFRA_SPMOVE` v0.3, against its own
ratified pins (`NFRA_SPMOVE_ENDPOINT_FORWARD_20260916.md` @`8d5995ec46`): there, DONE WHEN, ACCEPT and PROOF are
carried byte-for-byte for all six outcomes, and only SOURCE is dropped -- the same accepted shape this seat has
already taken for STATUS on LGIC_NAMING/LGIC_ENFORCE/LGIC_CANON. That is the established practice this half is
measured against, and it is not what this PRD does.

## DEFECT -- the ENDPOINT section is not verbatim, and it is missing every operative constraint

The claim in the PRD ("carried here unchanged, in one line each; the endpoint document is the text that
governs") does not hold. Example, FWD-1:

Ratified pin:
```
FWD-1  A staff member who does not know which system holds a fact asks Claude and is
       pointed to the right tool, with the data's freshness and scope, on the first try
       DONE WHEN  EXERCISED -- a set of real questions, asked cold by someone who did not
                  build the index, routes correctly
       ACCEPT     a discover family is loaded in every session and answers from ONE catalog
                  (never a second): which property and dataset holds the fact, its freshness,
                  its firm scope, its caveats, and the next tool to call; a question about a
                  property that is not catalogued says so and names nothing
       PROOF      a named question set run in a live session by a non-author, with the count
                  routed correctly over the count asked, and every wrong route listed
       SOURCE     brief O1; Part III bullet 1; Part IV.1-2
```

PRD v0.3's ENDPOINT section, FWD-1 (in full -- this is everything the section carries for this outcome):
```
FWD-1   a staff member who does not know which system holds a fact is routed correctly
        on the first try
        DONE WHEN  EXERCISED, cold, by a non-author
```

The outcome statement is reworded, not transcribed ("asks Claude and is pointed to the right tool, with the
data's freshness and scope" collapses to "is routed correctly"), DONE WHEN is compressed to a three-word
paraphrase of its own bar, and ACCEPT, PROOF and SOURCE are dropped entirely. The same pattern holds across all
ten outcomes -- checked FWD-3, FWD-8 and FWD-9 individually as a spread rather than assuming FWD-1
generalises:

- FWD-3's ratified ACCEPT states an operative constraint this project's own CONTRACTS (S4) separately argues
  is live and contested -- "transactions are reachable, not only the three `dim_*` tables" -- and it is absent
  from the section carrying FWD-3.
- FWD-8's ratified ACCEPT states "no new vendor egress beyond Andrew's standing per-use word" -- a real
  constraint this PRD's own Scope section restates elsewhere in different words, but it is not IN the ENDPOINT
  section, which is where the review bar reads it from.
- FWD-9's ratified ACCEPT states "removal takes effect without a redeploy" and "a phrasing that asks for
  another firm's or master's data is refused" -- both absent from the section.

This is not the accepted STATUS/SOURCE-line trim this seat has taken on four prior PRDs this week (most
recently `NFRA_SPMOVE` v0.3, reviewed alongside this one). Those trims remove ONE line class (history or a
citation list) and leave DONE WHEN/ACCEPT/PROOF byte-identical. This PRD's ENDPOINT section removes ACCEPT and
PROOF wholesale -- the two lines that carry the outcome's actual operative constraints -- and rewrites the
outcome statement and DONE WHEN bar in the PRD author's own words rather than the ratified ones.

## Not the defect

No inline ruling citation or seat name was found inside the ENDPOINT section (unlike the class refused on
`NFRA_OPLGTW` and on `LGIC_CANON` v1.6 today) -- this is a different failure of the same review bar's first
clause, not the same one recurring.

## Not re-opened

CONTRACTS was not re-derived row by row this pass, since the refusal is independent of it and stands on its
own; a spot check of C1's registry/catalog-writer language against the brief and against `2.0.0_SA_COO~G`'s
cited defect (`emit_catalog_v02.py` disclaiming the live file) reads consistent with what v0.2's fix claims.

## The fix

`1.0.0_SA_CTO` restores DONE WHEN, ACCEPT and PROOF verbatim from `NFRA_MCPINDEX_ENDPOINT_FORWARD_20260917.md`
for all ten outcomes -- the same shape `NFRA_SPMOVE` v0.3 already uses -- dropping SOURCE if a line needs to go,
never ACCEPT or PROOF.

-- 3.0.0_SA_CVO
