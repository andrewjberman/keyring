# AMGT_RESAPP task order -- `AMGT-ab-4` -- THE ADAPTER'S COMMENTS STATE ITS REAL `lib.opal_naming` IMPORT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ab-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~188</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- comments only; no AWS call.
comp-adversary: RUN by the issuer at the cut -- AC1 reads the text AND a dynamic import probe; base FAIL (two stale claims, none naming the dossier path).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AMGT-ab-4` (round 52, decomposition s.60)

`lib/research/api/scoped_amgt.py:120` says `lib.opal_naming` is "never a runtime ... import here (it sits outside the adapter's vendored
closure ...)" and `:193` says it "sits OUTSIDE the adapter's vendored closure". Both are false: the build packages `lib/opal_naming.py`,
and the /thesis path imports it at REQUEST time -- `:3218`'s lazy `from lib.research.corpus import dossier` imports
`lib.research.harvest.store`, which imports `lib.opal_naming` at module scope. (The adapter's own import does not load it.)
**Correct the comments, text only:** remove both false claims and state, in a comment that names `opal_naming` and the `dossier` path
on one line, that it is packaged and imported at request time through corpus.dossier -> harvest.store. No code line changes.

## 2. BOUNDS

1. Comment lines of `scoped_amgt.py`, AND (AMENDMENT 1) the wording of the one docstring near `:2175` that still says `lib.opal_naming` is
   "outside this adapter's vendored closure" (a claim wrapped across two lines) -- the same correction, text only; no code line, no
   other docstring. Standing: no install, no push, no promote, no deploy.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~188/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ab-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round52/checks/ab_4_comment.py; echo "exit=$?"</invocation><expect>(a) stale claims: 0; (b) a comment line naming opal_naming and the dossier path; (c) True; THE ADAPTER'S COMMENTS STATE ITS REAL lib.opal_naming IMPORT: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~188/AMGT_RESAPP.TO-AMGT-ab-4.the-true-import-comment.proof_of_spec.json`. Report once: the lines changed, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-51 analysis item 4 / ruling 6. Base: AC1 FAIL ((a) 2 stale claims at :120 and :193; (b) none; (c) True). Queued on
~188 after ab-2 (same file).

<status>pending</status>
**AMENDMENT 1 (`2.0.0_SA_COO~Z`, 2026-09-30 ~08:2xZ):** the worker's report named a third false claim, in the docstring near `:2175`, wrapped across two lines so the check's per-line regex missed it (the issuer's check gap); the bounds now admit that docstring's wording and `ab_4_comment.py` also reads the whitespace-normalised text (base on the worker's branch: FAIL, 1 wrapped claim). The order re-opens.
<status>complete</status>
<round>52</round>
<slot>~188</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
