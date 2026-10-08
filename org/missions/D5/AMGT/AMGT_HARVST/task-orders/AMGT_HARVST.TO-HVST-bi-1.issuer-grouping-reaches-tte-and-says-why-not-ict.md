# AMGT_HARVST task order -- `HVST-bi-1` -- ROUND 64 (`1.0.0_SA_CTO~Z` msg 31575, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` ADDENDUM 2 @e93cccc7be): THE ISSUER GROUPING REACHES THE TWO TotalEnergies LISTINGS, AND SAYS IN ITS OUTPUT WHY THE TWO `ICT` LISTINGS STAY APART

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bi-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~114</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and plants, plus a READ-ONLY census (S3 GET of the pool universe and the silver article parts through the served iterator). NO put, NO delete, NO gold or silver build, NO vendor or publisher host, NO collector or backfill_driver. `.runtime` is not read. Two collection legs are LIVE on the shared tree: touch nothing outside your worktree.
comp-adversary: RUN at L5 -- the adversary is a changed output for a security the rule does not name, a test with no negative control, a rule loosened to meet the census, a second list where the cell says one, or a gold build.
</preflight>

## 0. THE CELL

`lib/research/harvest/universe_securities.py` `issuer_groups(companies_by_key, leis_by_key)` (cell `HVST-bh-7`, merged) groups
two listings as ONE ISSUER by limb 1 (the same non-empty registry `lei`) or limb 2 (a shared ticker root AND, casefolded, one
company name equal to the other's company name or one of its `suffix_forms`). The build summary carries `issuer_groups` and
`listings_sharing_a_root_not_grouped`. Its census (`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/bh7_census.out`,
script beside it) read 7 ticker roots with two listings: 5 grouped (ASML, AZN, GSK, OMAB, RIO) and 2 not:
- TTE: `TTE_FP_Equity` 'Total Energies' against `TTE_US_Equity` 'TotalEnergies SE'. One company; the names differ by a space.
- ICT: `ICT_PM_Equity` 'International Container Terminals' against `ICT_US_Equity` 'International Container Termin' (a name
  cut at 30 characters). Already ruled: whether those two keys are one issuer is NOT shown by any field and is NOT inferred.

The ruling for this cell: the grouping reaches TTE; for ICT it says why not, in its output, and groups nothing.

## 1. THE BUILD (LOCAL, small)

1. **Limb 2, one widening** (`issuer_groups`): the comparison of company names and suffix forms ignores WHITESPACE as well as
   case ("Total Energies" equals "TotalEnergies"). Nothing else changes: a shared root is still required, a prefix is still
   not a match, and no other character is ignored. Say so in the docstring.
2. **The reason for a root left apart.** Each entry of `listings_sharing_a_root_not_grouped` gains a `reason` string. For a
   pair whose shorter company name is a strict prefix of the other's it reads
   `one name is a prefix of the other; a cut name is not evidence of one issuer`; otherwise `names differ`.
3. A security in no group, and every security's built dict, is byte-equal to today's UNLESS a brand refusal changes for it;
   print which do (the census below). Change nothing in `publication_gold.py` or `whole_brand_aliases.json`.
4. **Plants** `lib/research/harvest/tests/test_bi1_grouping_whitespace.py` (no network): (i) 'Total Energies' and
   'TotalEnergies SE' with root TTE are grouped; (ii) THE NEGATIVE CONTROL: 'International Container Terminals' and
   'International Container Termin' with root ICT are NOT grouped and the reason is the prefix sentence; (iii) two different
   companies with a shared root and names that differ by more than whitespace are not grouped; (iv) names equal after
   removing whitespace but with DIFFERENT roots are not grouped by limb 2; (v) the mutant: with the whitespace step off,
   (i) is not grouped.
5. **The census** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~114/bi1_census.py` (no silver read is needed unless a built dict changes):
   BEFORE = `build()` at your base; AFTER = as you leave it. Print:
   - `DENOMINATOR: securities <S>, ticker roots with two or more listings <r>`;
   - per such root: `GROUPED by limb <n>` or `NOT GROUPED: <reason>`;
   - `GROUPS: before <g0> after <g1>`; `BRAND REFUSALS: before <b0> after <b1>`;
   - `SECURITIES WHOSE BUILT DICT CHANGED: <c> of <S>` and each key;
   - last line `CENSUS OK` only if TTE reads GROUPED, ICT reads NOT GROUPED with the prefix sentence, the five roots grouped
     before are still grouped, and SECURITIES WHOSE BUILT DICT CHANGED is 0; otherwise `CENSUS FAIL` and the failing line (a
     changed dict is a finding: print its before and after alias sets and stop there). Write `bi1_census.out`.
6. `build()` reads the pool by S3 GET; no put. Build no gold.

Change an existing test assertion only where this cell's rule is the reason, and list each in your report.

## AMENDMENT 1 (issuer, 2026-10-08 ~05:0xZ, on row AMGT_HARVST-Z-W114-S1; no gate limb graded it)

Your first pass (commit b8f52c248a on this branch) is right as far as the face went, and the face was short: "TotalEnergies SE"
has no suffix form, because `SE` is not in `CORPORATE_SUFFIXES`, so ignoring whitespace alone cannot group TTE. You were right
not to add a suffix. The ruling:

1. **Limb 2, one more step, in the COMPARISON only.** After the whitespace-and-case squash, two names also match when one
   squashed name equals the other squashed name with ONE trailing corporate-form word removed, where the form words are the
   module's own `_FORM_WORDS` (squashed and casefolded the same way). "Total Energies" -> `totalenergies`;
   "TotalEnergies SE" -> `totalenergiesse` -> minus the form word `se` -> `totalenergies`: a match. The removed tail must be
   a WHOLE form word and what remains must be non-empty and equal to the other name exactly.
2. `CORPORATE_SUFFIXES`, `suffix_forms`, `_FORM_WORDS` and every alias path are NOT changed: no security's aliases move.
3. ICT must still stay apart: `internationalcontainerterminals` minus `internationalcontainertermin` leaves `als`, which is
   not a form word.
4. The `reason` for a root left apart is computed on the names as written (strict prefix of the unsquashed, casefolded
   strings), as you have it.
5. Plants: (i) now passes by this step; add (vi) a name that equals the other only after removing a tail that is NOT a form
   word is not grouped (use the ICT pair's shape with different words); (vii) the mutant: with this step off, (i) fails to
   group again.
6. Re-run `bi1_census.py` and overwrite `bi1_census.out`; write the proof instance. Your next row id is
   `AMGT_HARVST-Z-W114-S2`.

The three criteria are unchanged.

<paths>
lib/research/harvest/universe_securities.py
lib/research/harvest/tests/
lib/research/identity/registrations.json
lib/opal_data_harvest/test_az1_alias_set.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~110/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~114/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bi-1"><invocation>python -m pytest lib/research/harvest/tests/test_bi1_grouping_whitespace.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bi-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~114/bi1_census.out</invocation><expect>CENSUS OK</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bi-1"><invocation>python -m pytest lib/research/harvest lib/opal_data_harvest/test_az1_alias_set.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W114-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~114/AMGT_HARVST.TO-HVST-bi-1.issuer-grouping-reaches-tte-and-says-why-not-ict.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bi-1.issuer-grouping-reaches-tte-and-says-why-not-ict`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31575, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` ADDENDUM 2 @e93cccc7be. Decomposition section 78.
- ADDENDUM 2, enrichment list: "Z-W110-S5 (ICT and TTE listings are not grouped as one issuer: the issuer grouping of R8
  reaches them or says why not)". R13: ICT's two keys are not inferred to be one issuer.
- **Issuer rulings inside the decomposition** (no gate limb graded them): TTE is reached by ignoring whitespace in limb 2's
  name comparison and nothing more; ICT stays apart and the output says a cut name is not evidence.
- **The merge waits for rebuild #9's act.** The act's gate checks the list file `round64/securities.universe.r64.json` against
  `build()` at HEAD; this cell is cut to leave every built dict unchanged, and it is merged after the act so that check is
  not put in question mid-pair.
- **Round 64 holds this one order.** The analysis's two other items are not orders of this issuance: rebuild #9 is the
  issuer's act under its never-widen pair (as rebuild #8 was), and the first walk of the Security Analysis feed needs the
  rebuilt gold and its stamp, so it is cut as the next round the tick the act ends.
- Slot ~114. **Checks dry-run at the base:** AC1 base FAIL as expected (the test is absent); AC2 base FAIL as expected (no such
  file); AC3 base PASS as expected (491 passed).

**COMPLETE 2026-10-08 ~06:4xZ (issuer):**
- **Built:** worker-light ~114 in two passes: @b8f52c248a (whitespace squash, the reason field; TTE not grouped, row Z-W114-S1)
  and, under AMENDMENT 1, @9beb2b23ce (one trailing form word dropped in the comparison). Merged @0090d94c29 AFTER rebuild
  #9's act ended (record @60818dd705), 7 paths, index check 0 of 7 differ.
- **AC1 PASS:** 7 of 7. **AC2 PASS:** CENSUS OK: 7 two-listing roots; TTE GROUPED by limb 2; ICT NOT GROUPED ("one name is a
  prefix of the other; a cut name is not evidence of one issuer"); groups 5 to 6; brand refusals 0 to 0; built dicts changed 0
  of 242. **AC3 PASS:** 498 on the branch; the issuer's drain check and the list check are in this close's commit message.
- **Existing assertion changed (1):** `test_bh7_brand_belongs_to_the_issuer.py` test iii expects the `reason` field.
- **Rows:** Z-W114-S1 (answered by AMENDMENT 1); Z-W110-S5 is answered by this cell.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>issued</status>
<status>complete</status>
<round>64</round>
<slot>~114</slot>
<fabric>site-z</fabric>
