# AMGT_RESAPP.TO-AMGT-rb-12 -- THE IDENTITY DECISION-NOTE CORRECTION: 34 MEASURED + up to 15 INFERRED candidates, observed ambiguity separated from hypothetical renaming, the fallback kept unimplemented pending Andrew

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rb-12</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~4</issued_to>

## THE CELL, INLINED IN FULL (round 2b, FWD-8/FWD-13; fixes AMGT-r-12 / finding C-S13 FAIL)

```
AMGT-rb-12. THE IDENTITY DECISION-NOTE CORRECTION (doc). AMGT-r-12's measured-source limb PASSED (34
distinct MEASURED bloomberg_ticker values, up from 32 -- IMB LN / IMPERIAL BRANDS and SAP GY / SAP SE read
from the original workbooks). The CVO graded the DECISION NOTE FAIL (C-S13): DESIGN_QUESTION_identity_
fallback.md twice promises "MEASURED-or-better coverage 34 -> as high as 49" while explicitly limiting ALL
fallback values to INFERRED, never MEASURED -- two categories that CANNOT share one denominator, so the
advertised benefit is incoherent. It also treats a hypothetical renaming (a re-org that renames a
directory) as though it were a measured failure mode. Andrew cannot rule on a benefit claim that mixes
the categories.

WHAT TO PRODUCE, under lib/research/identity/ and .../deliverables/0.9.0_WK_AMGT_RESAPP~4/ (this is a DOC
correction -- edit DESIGN_QUESTION_identity_fallback.md in your own deliverable folder; NO code, NO data
change):

  (a) THE BENEFIT, RE-STATED IN ONE DENOMINATOR'S CATEGORIES  replace every "MEASURED-or-better 34 -> 49"
      claim with the honest split: 34 MEASURED (this pass's measured workbook reads) PLUS up to 15
      additional INFERRED candidates the directory-name fallback WOULD produce -- never "49
      MEASURED-or-better". MEASURED and INFERRED are different provenance classes and are counted
      separately (A VALUE MUST CARRY ITS CLAIM).

  (b) OBSERVED AMBIGUITY vs HYPOTHETICAL RENAMING, SEPARATED  keep the OBSERVED failure mode (an ambiguous
      trailing token that is real in THIS corpus -- e.g. Nokia FH, whose bare `FH` is not a securely
      parseable ticker without the company name) distinct from the HYPOTHETICAL one (a re-org that renames
      a directory to drop or change its ticker -- not observed in the corpus, a design risk not a measured
      failure). The doc must not present the hypothetical as a measured result.

  (c) WHICH GATES STILL REFUSE INFERRED  name the downstream admissibility gate(s) that would still refuse
      an INFERRED bloomberg_ticker (so a reader knows an INFERRED candidate is NOT automatically served),
      and state that the fallback stays UNIMPLEMENTED pending Andrew's decision (unchanged from AMGT-r-12).
```

## DEPENDENCIES

**NONE.** Independent of the other round-2b cells. Corrects AMGT-r-12's own landed
DESIGN_QUESTION_identity_fallback.md (your slot's deliverable folder); reads AMGT-s-12/AMGT-r-12's landed
universe.json (READ, not changed).

## BOUNDS

```
BLOCK NO FALLBACK CODED: this is a DOC correction; AC3 still refuses any directory-name fallback appearing
  in lib/research/identity/*.py (unchanged from AMGT-r-12's AC3). Do not implement it.
BLOCK NO DATA RE-LITIGATION: the 34 MEASURED stand; do not re-measure, add or remove a MEASURED value.
  The doc names 34 MEASURED as the measured count, not a range mixed with INFERRED.
BLOCK NO NEW VENDOR CALL; C-NO-CONTACT holds.
BLOCK MEASURED and INFERRED are SEPARATE categories with separate counts -- never one "34 -> 49" number.
WARN Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
CVO evidence @b3acbcf3dd (C-S13, BLOCKING): "DESIGN_QUESTION_identity_fallback.md twice promises
    MEASURED-or-better coverage 34 to 49 while explicitly limiting all fallback values to INFERRED, never
    MEASURED. Those categories cannot share the claimed denominator. It also treats hypothetical renaming
    as a measured failure. Correct them to 34 measured plus up to 15 inferred candidates, with downstream
    admissibility unresolved."
L10 round-2 analysis @c48576bf85 s.2: "correct to 34 MEASURED + up to 15 INFERRED candidates, separate
    observed ambiguity from hypothetical renaming, name which downstream gates still refuse INFERRED. Keep
    the fallback UNIMPLEMENTED pending Andrew's decision."
AMGT-r-12 (landed): universe.json 34 MEASURED / 34 distinct / 55 UNRESOLVED of 89; the doc's mechanism
    (read the trailing Bloomberg-shaped token off the directory's own name) is stated, never coded (AC3).
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
lib/research/identity/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rb-12.identity-decision-note-correction.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~4/` (where AMGT-r-12's DESIGN_QUESTION_identity_
fallback.md and universe.json already live). A path missing from that block is a path you are REFUSED on.
Refuse a criterion you cannot satisfy as written and report it; file a surprise ROW (`AMGT_RESAPP-Z-W4-S<k>`
continuing your prior sequence -- your next is `AMGT_RESAPP-Z-W4-S2`, project AMGT_RESAPP, fabric site-z)
and STOP on that criterion if you need a surface not listed.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rb-12"><invocation>python -c "t=open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~4/DESIGN_QUESTION_identity_fallback.md', encoding='utf-8').read().lower(); print('measured-or-better', t.count('measured-or-better'), '| as high as 49', t.count('as high as 49'), '| to 49', t.count('to 49'), '| 49 of 89', t.count('49 of 89'))"</invocation><expect>every count "0" -- NEGATIVE: the incoherent "MEASURED-or-better 34 -> 49" claim is GONE from the doc in all its forms. Any non-zero count is the mixed-category claim still present and is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rb-12"><invocation>python -c "t=open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~4/DESIGN_QUESTION_identity_fallback.md', encoding='utf-8').read(); low=t.lower(); print('states 34 MEASURED', ('34 measured' in low), '| up to 15 INFERRED', ('15' in low and 'inferred candidate' in low), '| names an INFERRED-refusing gate', ('inferred' in low and ('refuse' in low or 'refuses' in low or 'reject' in low)), '| separates observed-vs-hypothetical', ('observed' in low and ('hypothetical' in low or 'renaming' in low)))"</invocation><expect>all four True -- the doc states 34 MEASURED, up to 15 INFERRED candidates, names at least one downstream gate that refuses INFERRED, and separates observed ambiguity from hypothetical renaming. A missing term is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rb-12"><invocation>python -c "import pathlib,re; fs=list(pathlib.Path('lib/research/identity').rglob('*.py')); pat=re.compile(r'(?is)(\.name\b|basename|folder_name|dir_name).{0,60}(bloomberg_ticker|security_key)|(bloomberg_ticker|security_key)\s*=\s*[^\n]{0,50}(\.name\b|basename|rsplit)'); hits=[str(f) for f in fs if pat.search(f.read_text(encoding='utf-8'))]; print('py files', len(fs), '| fallback-coded files', len(hits), hits)"</invocation><expect>"fallback-coded files 0" with a non-zero "py files" denominator -- NEGATIVE: no directory-name-to-ticker fallback is implemented in lib/research/identity/*.py; the mechanism stays a DOCUMENTED design question only</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rb-12" judgment="true"/>
</proof_of_spec>

### What each criterion means
- **AC1** (mechanical, NEGATIVE): the incoherent mixed-category benefit claim is gone from the doc.
- **AC2** (mechanical): the corrected benefit is stated in separate categories (34 MEASURED + up-to-15 INFERRED), names an INFERRED-refusing gate, and separates observed from hypothetical.
- **AC3** (mechanical, NEGATIVE): the fallback is still not coded -- a doc-only correction.
- **AC4** (JUDGMENT -- never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason names 3.0.0_SA_CVO~Z): read the corrected note -- does it present a benefit Andrew can rule on (34 MEASURED + up-to-15 INFERRED candidates, not 49 measured-or-better), cleanly separate observed ambiguity from hypothetical renaming, and name where INFERRED is still refused downstream? This is the C-S13 regrade.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>3</round>
<slot>~4</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5 v0.4 + L6 round 2b) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @a81bd256c9 (GRANDFATHERED for L4-R)
**Authority chain:** L10 round-2 analysis @c48576bf85 (answering CVO slug REMEDIATION_v2 @b3acbcf3dd) -> L5 recut decomposition v0.4 @192c198231 (section 11, AMGT-rb-12) -> this round-2b issuance.
**Chain:** round 2b, an independent chain of one.
**Provenance:** decomposition v0.4 section 11a's AMGT-rb-12 row; the defect is C-S13 (r-12 decision-note FAIL) per the CVO evidence @b3acbcf3dd and analysis s.2.
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- v0.2's run stands; G-14 binds AC4 (judgment never self-graded).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- the L10 round-2 analysis @c48576bf85 is the authority; round-1's 10/10 stands.
comp-blast: DECLARED-NOT-APPLICABLE -- no infra act, no served-output move (a doc correction).
</preflight>
**Preflight disposition:** a doc correction to a landed deliverable; no code, no data, no new gate/IAM/adversary/vendor plane; the authority is the L10 round-2 analysis.
