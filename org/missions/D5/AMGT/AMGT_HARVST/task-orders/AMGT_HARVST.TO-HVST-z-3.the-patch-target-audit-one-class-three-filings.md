# AMGT_HARVST task order -- `HVST-z-3` -- ROUND 11 cell 3 of 4: the dotted-string PATCH-TARGET audit. ONE class, THREE filings, EIGHT sites, FIVE files -- two of them other projects'

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-z-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~34</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on the five test files; this cell deploys nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- every criterion runs in-process against test doubles. No AWS call, no vendor call.
comp-adversary: RUN at L5 -- the adversary is a patch that LOOKS applied because the test passes. AC1's per-site negative control is that adversary's test.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO VENDOR CALL. NO NETWORK. NO S3 OF ANY KIND.** In-process only.
2. **Scripts in** `.../deliverables/0.9.0_WK_AMGT_HARVST~34/scripts/` -- **never `.scratch/`.**
3. ⛔ **INSTANCE NAMED EXACTLY**
   `.../deliverables/0.9.0_WK_AMGT_HARVST~34/AMGT_HARVST.TO-HVST-z-3.the-patch-target-audit-one-class-three-filings.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-z-3.the-patch-target-audit-one-class-three-filings`.
4. ⛔ **TWO OF YOUR FIVE FILES BELONG TO OTHER PROJECTS.** `lib/research/posture/tests/test_posture.py` is POSN's and
   `lib/research/api/tests/test_scoped_amgt.py` is AMGT_RESAPP's. **`1.0.0_SA_CTO~Z` authorises them FOR THIS CELL
   ONLY, as CTO of all three site-Z projects** (ruling 20260928T114032Z). **Touch nothing else in either tree, and
   change only the patch targets -- not their assertions, not their fixtures, not their style.**

<paths>
lib/research/posture/tests/test_posture.py
lib/research/api/tests/test_scoped_amgt.py
lib/opal_data_harvest/test_retrieval_provenance.py
lib/opal_data_harvest/test_verification.py
lib/opal_data_harvest/test_worker.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~34/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE DEFECT -- ONE CLASS, FILED THREE TIMES ACROSS EIGHT ROUNDS

A **dotted-string** patch target (`patch("lib.opal_data_harvest...")`, `monkeypatch.setattr("lib....")`,
`patch.dict("lib....")`) **silently no-ops** when pytest imports the test under a different module name. There is no
`lib/__init__.py`, so pytest's rootdir import loads the test as `opal_data_harvest.test_worker`; **the code under
test then resolves the patched name off a DIFFERENT module object than the string-targeted patch imports and
mutates.** The patch call raises nothing. The test may pass for unrelated reasons.

**Filed three times as new:** `Z-W10-S3` (round ~2), `Z-W14-S2` (round ~2, as *"a NEW variant"*), **`Z-W26-S1`
(round 10)**. ⚠ **`test_worker.py:51` "works" ONLY by a stdlib-singleton coincidence** -- `time` is process-wide, so
mutating it on a duplicate module still lands on the shared object. **That is luck, not correctness.**

**THE 8 SITES, measured by the issuer:** `test_posture.py` (**4**), `test_scoped_amgt.py` (1),
`test_retrieval_provenance.py:646` (1), `test_verification.py:18` (1, the `patch.dict` variant),
`test_worker.py:51` (1).

## 2. THE FIX, AND ITS BOUND

**Per site:** re-target the patch against the module object the test file ITSELF imports (e.g. `patch.object(Cls, ...)`
on a class the file already imported), so no string re-import can split the identity. `HVST-y-1` used exactly that
route around it.

⛔ **A STRUCTURAL FIX -- adding `lib/__init__.py`, or changing pytest's import mode -- IS IN SCOPE ONLY IF YOU PROVE
IT HARMLESS ACROSS THE FULL SUITE.** It is one line that changes how **every test in the estate** imports.
**Otherwise fix per site. Say which you chose and why.**

## 3. BOUNDS

1. **Three mechanical criteria, no fourth and no judgment.**
2. **Change only patch targets.** No assertion, fixture, name or behaviour moves. **A test made to pass by changing
   what it asserts FAILS this cell.**
3. **Do not chase what the corrected patches now reveal.** If a re-targeted patch makes a previously-passing test
   FAIL, that is the defect the no-op was hiding -- ⛔ **report it and file a ROW; do not fix the newly-exposed
   behaviour.** It may belong to another project.
4. **The two foreign files: patch targets only.** Anything else is a BLOCKING row.

## 4. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical criteria, adopted from the CTO's ruling VERBATIM

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-z-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~34/scripts/ac1_per_site_negative_control.py</invocation><expect>PER SITE, A NEGATIVE CONTROL PROVING THE PATCH NOW TAKES EFFECT: the patched name, READ THROUGH THE MODULE OBJECT THE CODE UNDER TEST USES, is the mock. Print the 8 sites as BEFORE/AFTER pairs -- before: the identity read through the code-under-test's module is NOT the mock (the no-op, demonstrated); after: it IS. Name each site by file and line. ⛔ A site that cannot be shown failing BEFORE is not proved fixed -- if a site's before-state cannot be exhibited (e.g. test_worker.py:51, which works by a stdlib-singleton coincidence), say so explicitly and state what you proved instead. 8 of 8 sites reported, each with its own outcome</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-z-3"><invocation>python -m pytest lib/research/posture/tests/test_posture.py lib/research/api/tests/test_scoped_amgt.py lib/opal_data_harvest/test_retrieval_provenance.py lib/opal_data_harvest/test_verification.py lib/opal_data_harvest/test_worker.py -rA --tb=line</invocation><expect>EACH TOUCHED SUITE PASSES, with the pass count printed BEFORE and AFTER and NO test deleted or weakened. BEFORE, measured by the issuer at this cut: `78 passed, 1 skipped, 6 subtests passed`. The AFTER count must not FALL, and the collected count must not fall either -- ⛔ a passed count that drops while failures stay at zero means tests were removed, and the collected total is the discriminator. If a re-targeted patch EXPOSES a real failure, report it named, file a row, and state it rather than repairing it</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-z-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~34/scripts/ac3_census_zero_remaining.py</invocation><expect>THE CENSUS RE-RUN OVER lib/ READS ZERO dotted-string patch targets THAT MISS, with the denominator printed. Print: every `patch("lib.`, `patch.dict("lib.` and `monkeypatch.setattr("lib.` occurrence found under lib/ with its file and line, the total scanned denominator, and for each occurrence whether it RESOLVES to the same module object the code under test uses. Expected: 0 that miss. ⛔ A bare zero FAILS -- print the occurrences and their resolution verdicts, because "0 hits" and "0 that miss" are different claims and only the second is this criterion</expect></criterion>
</proof_of_spec>

## 5. WHAT THIS CELL DOES NOT DO

It fixes no behaviour the corrected patches expose. It touches no non-test file. It changes no assertion. It makes no
network, S3 or vendor call. It does not disarm the three rows -- evidence is the issuer's and the clock is
`3.0.0_SA_CVO`'s.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **The three criteria are the CTO's ruling adopted VERBATIM, not paraphrased** -- a paraphrased criterion silently
   redirects its only oracle, and this cell's criteria are the CTO's because the audit is its ruling.
2. ⛔ **AC1's "cannot be shown failing" escape is deliberate and narrow.** `test_worker.py:51` passes by a
   stdlib-singleton coincidence, so its before-state may be unexhibitable. **Naming that is honest; silently
   counting it as fixed is not.**
3. **BOUNDS 3 is the cell's real hazard.** A no-op patch has been hiding whatever the mock was meant to prevent for
   eight rounds. **When the patch starts working, tests may fail for the first time -- and those failures are
   findings, not this cell's work**, possibly not even this project's.
4. **AC3's wording separates "0 hits" from "0 that miss."** The first is a search result; the second is the claim.
   Round 10 taught me that a bare zero reads as "no problem exists."

<risk>LOCAL</risk>
<status>complete</status>
<round>11</round>
<slot>~34</slot>
<fabric>site-z</fabric>
