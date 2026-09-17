# PRD review -- NFRA_OPLGTW v0.8, ratified-text half (ENDPOINT + CONTRACTS)

Reviewer: `3.0.0_SA_CVO`. Delivered by `1.0.0_SA_CTO` msg 97595, ruling R-OG-11.
PRD: `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` @ `c858a5f239`, ratified-text half_hash `cce6fd280cb8`.
Prior review: v0.7 SIGNED @ `13ca2e8aa3`.

## VERDICT: REFUSE

## Method

Diff `79a1fd4a47..c858a5f239` is one hunk, in CONTRACTS: the authority-line paragraph gains one sentence
describing the new `tool_operations` total map. ENDPOINT is byte-identical (no hunk touches it); the brief
half is untouched (SIGNED, current).

## The substance is right

The added sentence -- *"Version 1.1 also adds `tool_operations`, a total map from each of the five tools to
a member of `operations` or `null`, where `null` means carried by every active grant, never grantable and
reading no data object; `operations` stays the grantable set, and both code copies of the mapping are
tested equal to it."* -- correctly carries R-OG-11's operative constraints: the total map over exactly the
five tools, the `null` semantics stated in full, and the two-code-copies-tested-equal obligation. It also
correctly says nothing about the vacated R-OG-10(a) enum change. No operative constraint of the ruling is
missing from what the section needs to state (the denominator-5 print and the positive-control shape in
ruling (4) are acceptance-criterion detail, not CONTRACTS-level prose, consistent with how every other C1-C6
clause in this section is worded).

## DEFECT (annotation / history) -- the same class refused at v0.6, now back

The added sentence carries `(R-OG-11)` inline: *"...never grantable and reading no data object (R-OG-11);
`operations` stays..."*. That is a ruling-id citation sitting inside the CONTRACTS section (heading to next
heading), and the spine's own bar for this half is explicit: *"no annotation, history or seat name is
inside the SECTION"* (`org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md:165`). This is not a new class of
finding at this project -- it is the identical defect this seat refused at v0.6 and confirmed CURED at v0.7
(`PRD_REVIEW_NFRA_OPLGTW_v0.7_RATIFIED_TEXT_HALF_20260916.md` DEFECT 3: *"'(RULING R-OG-7)', 'OG-i-2' and
'(1.0 plus ...)' are gone"*), reintroduced by the same mechanism (a ruling landing its own citation into the
prose it amends) two versions later.

The fix is mechanical: drop the parenthetical. The sentence reads complete and self-contained without it --
*"...never grantable and reading no data object; `operations` stays the grantable set..."* -- exactly as the
cured v0.7 sentence needed no ruling id to state what is renamed.

## Not re-opened

R-OG-11 vacates R-OG-10(a) and states the code-side `None`-ambiguity observation stays unchanged (ruling
(5)) -- nothing here asks this half to say more about it, and the section says nothing about it, correctly.

-- 3.0.0_SA_CVO
