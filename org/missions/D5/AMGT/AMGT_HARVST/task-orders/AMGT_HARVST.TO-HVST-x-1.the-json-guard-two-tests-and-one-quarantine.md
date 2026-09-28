# AMGT_HARVST task order -- `HVST-x-1` -- ROUND 9 cell 1 of 2: the `publishers.py:672` `.json()` GUARD (a product change), the ONE completable test, and ONE quarantine

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-x-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~26</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on lib/opal_data_harvest; this cell arms nothing and deploys nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no vendor call. Every criterion runs in-process.
comp-adversary: RUN at L5 -- the adversary is a GREEN SUITE that implies a guard which does not exist. AC1 is written as that adversary's test and is why this cell is shaped as it is.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO VENDOR CALL. NO NETWORK. NO S3 READ, WRITE OR DELETE.** Every criterion runs in-process. If you find
   yourself needing the network, STOP and file a BLOCKING row.
2. **Scripts go in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~26/scripts/` --
   **never `.scratch/`**, which does not survive the drain.
3. ⛔ **YOUR proof-of-spec INSTANCE MUST BE NAMED EXACTLY:**
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~26/AMGT_HARVST.TO-HVST-x-1.the-json-guard-two-tests-and-one-quarantine.proof_of_spec.json`
   **and its `to_id` MUST be** `AMGT_HARVST.TO-HVST-x-1.the-json-guard-two-tests-and-one-quarantine`.
   A gate globs for that exact stem and refuses anything else BEFORE any limb runs. (Round 8 lost three
   attempts to this; see decomp `s.14x`.)
4. **Your write surface is exactly the `<paths>` below.**

<paths>
lib/opal_data_harvest/publishers.py
lib/opal_data_harvest/test_worker.py
lib/opal_data_harvest/test_verification.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~26/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE CELL, AND THE COUNT IS ALREADY CORRECTED FOR YOU

**It is TWO failing tests, not three.** `python -m pytest lib/research/harvest/tests/ lib/opal_data_harvest/ -rA`
reports `3 failed, 306 passed` -- but **pytest counts SUBTEST failures separately** and
`test_single_broken_dow_jones_article_is_skipped_but_repeated_server_failure_stops` **SUBFAILS twice**. Do not
go looking for a third test. The full diagnosis is
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_Y/WHY_THE_RED_TESTS_ARE_STILL_RED_20260928.md`
(@`9a5d538d35`) -- **read it; you are not being asked to re-derive any of it.**

## 2. ITEM 1 -- THE `.json()` GUARD. A PRODUCT CHANGE, AND THE REASON THIS CELL EXISTS

```
lib/opal_data_harvest/publishers.py:672   (class DowJones.check)
value = self.session.get(self.base + "/client?legacy=false", headers={...}).json()
if value.get("isLoggedIn") is not True: raise AuthExpired(...)
```

⛔ **`.json()` IS UNGUARDED.** A real non-JSON or empty body makes `.json()` return `None`, and `.get` then
raises **`AttributeError`** -- **instead of the clean `AuthExpired` this method exists to raise**, on a LIVE
AUTH PATH. **Guard it so a body that is not usable JSON raises `AuthExpired`**, which is what every caller of
`check()` already handles.

⭐ **THIS IS SEPARATE FROM ITEM 2 AND MUST NOT BE PROVEN THROUGH THE SUITE.** Completing the test double
(item 2) turns the red test green **and leaves this brittleness standing.** So AC1 demonstrates the guard
DIRECTLY -- construct a fake session whose `.json()` returns `None`, and show `AuthExpired` is raised. **A green
suite is not evidence for this item.**

## 3. ITEM 2 -- THE TEST-DOUBLE GAP (the one genuinely completable test)

`test_single_broken_dow_jones_article...`'s fake session has **no handler for `/client?legacy=false`**, while its
siblings all provide one: `test_bronze_capture.py:285`
(`_Resp(b'{"isLoggedIn": true, "type": "subscriber"}', url=".../client?legacy=false")`), `:296` for barrons, and
`test_retrieval_provenance.py:239`. **Complete the double in the same shape those use.**
**`DowJones.check()` is correct; the DOUBLE is incomplete** -- do not change `check()`'s contract to suit it.

## 4. ITEM 3 -- QUARANTINE, NOT REPAIR

`test_verification.py::Tests::test_disabled_barrons_contract_defers_before_opening_a_browser` **alternated
between `KeyError: 'bundle'` and `FileExistsError: [WinError 183]` across two identical runs with no intervening
edit.** ⛔ **A test that fails differently on identical input is not a regression baseline -- do NOT try to fix
it here.** Mark it quarantined (a skip/xfail carrying the REASON in its marker text, naming the alternation and
that the diagnosis belongs to cell `w-4`'s scope). **Do not weaken or delete its assertions** -- a quarantine
states that the test is untrustworthy, which is different from asserting less.

## 5. BOUNDS

1. **Three mechanical criteria, no fourth.** A fourth finding is a surprise ROW; you keep working.
2. **Do not touch `lib/research/harvest/`** -- not in your grant this round.
3. **Do not alter any assertion to make a count move.** A test made green by weakening it FAILS the cell.
4. **`w-4`'s diagnosis is not yours.** Quarantine and name it; do not investigate the barrons flake.

## 6. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical criteria

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-x-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~26/scripts/ac1_json_guard.py</invocation><expect>THE GUARD IS SHOWN DIRECTLY, NEVER THROUGH THE SUITE. Print, in order: (a) a NEGATIVE CONTROL at pre-fix behaviour -- a fake session whose `.json()` returns None driven through `DowJones.check()`, raising `AttributeError`, with the exception type and message verbatim; (b) the SAME input after the guard, raising `AuthExpired` with its message; (c) a POSITIVE control that the guard did not swallow the normal path -- a well-formed logged-in body still passes `check()` without raising, and a logged-OUT body still raises `AuthExpired` (so the guard is not returning early on valid JSON). A pass requires (a) to FAIL pre-fix: a criterion that never makes the defect appear proves nothing. Print the three outcomes with the exception class named in each</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-x-1"><invocation>python -m pytest lib/research/harvest/tests/ lib/opal_data_harvest/ -rA --tb=line</invocation><expect>THE SUITE'S FAILED COUNT IS ZERO, OR EVERY REMAINING FAILURE IS QUARANTINED WITH A NAMED REASON. Print the BEFORE and AFTER lines verbatim. BEFORE, measured by the issuer at this cut: `3 failed, 306 passed` across TWO tests (one SUBFAILS twice). Expected AFTER: the dow-jones test passes once its double is completed, and the barrons test appears as QUARANTINED (skipped/xfailed) rather than failed, with its marker reason visible in the `-rA` output. State the passed count too -- a failed count that falls while the passed count also falls means tests were removed, not fixed, and that FAILS this criterion</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-x-1"><invocation>python -m pytest lib/opal_data_harvest/test_verification.py -rA --tb=line</invocation><expect>THE QUARANTINE IS VISIBLE AND CARRIES ITS REASON, on the file that holds it. BEFORE, measured by the issuer at this cut: `1 failed, 3 passed`. Expected AFTER: 0 failed, with `test_disabled_barrons_contract_defers_before_opening_a_browser` reported as skipped/xfailed and its REASON TEXT printed in the `-rA` summary, naming (i) that it alternates between `KeyError: 'bundle'` and `FileExistsError: [WinError 183]` on identical input and (ii) that its diagnosis belongs to cell `w-4`. Print the reason string verbatim -- a quarantine whose reason is not in the output is a silent skip, which is worse than the red test</expect></criterion>
</proof_of_spec>

## 7. WHAT THIS CELL DOES NOT DO

It makes no vendor or network call. It does not diagnose the barrons flake (that is `w-4`'s). It does not touch
`lib/research/harvest/`. It does not capture anything -- the capture cell `w-2` is CARDED at Andrew pending a
per-use vendor word and is not yours.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. ⛔ **s.14x's NEW CLAUSE WAS HONOURED AT THIS CUT, and it changed the criteria.** AC2 and AC3's invocations
   were **RUN BY ME before cutting** (`3 failed, 306 passed` and `1 failed, 3 passed`), so their BEFORE figures
   are measured rather than quoted from round 8. **And both are written with NO shell operators at all** -- no
   `&&`, no pipe, no `2>&1` -- which REMOVES the escaping trap rather than documenting it. Round 8's orders
   carried `&amp;&amp;`, so alignment there certified a mirror of an unrunnable string.
2. **AC1 carries a POSITIVE control as well as a negative one.** A guard is the kind of fix that passes its own
   negative test by breaking the normal path; the logged-in and logged-out arms catch that.
3. **AC2's "state the passed count too" is deliberate.** A failed count falling while passed also falls means
   tests were deleted. The count pair is the discriminator.
4. **Two tests, not three, is stated in the worker face** so the worker does not spend a cycle hunting a third.

<risk>LOCAL</risk>
<status>pending</status>
<round>9</round>
<slot>~26</slot>
<fabric>site-z</fabric>
