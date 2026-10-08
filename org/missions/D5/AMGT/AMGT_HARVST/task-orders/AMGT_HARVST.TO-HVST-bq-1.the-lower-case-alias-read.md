# AMGT_HARVST task order -- `HVST-bq-1` -- ROUND 73 (`1.0.0_SA_CTO~Z` msg 31486, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` @3b19f962e0): DOES GOLD PAIR A LOWER-CASE COMMON WORD WITH A SECURITY WHOSE ALIAS IS THAT WORD? SHOWN BY A PLANTED TEST, NOTHING REPAIRED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bq-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~124</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL test and one note only. NO S3 call, NO build, NO collector or vendor call. `lib/research/harvest/publication_gold.py` is READ and NOT changed.
comp-adversary: RUN at L5 -- the adversary is a test written to pass whatever the code does without saying what it does, a fixture that plants the capitalised form somewhere and so never tests lower case, or a quiet repair of the matcher.
</preflight>

## 0. THE CELL

`lib/research/harvest/publication_gold.py` decides which (article, security) pairs the served gold holds. A code read says:
a security that carries an `aliases` list is matched on each alias CASE-INSENSITIVELY (`_alias_pattern`, `_span_pattern`
with `re.I` or a scoped `(?i:)`), while its ticker forms (`ticker_aliases`) match in their stored case only; and the
stored-case rule of `_security_mentions` (the `if not security.get("aliases")` branch) applies only to a security with NO
alias list. If that read is right, an article that uses the common word "target" in lower case pairs with a security
whose alias is "Target". Nobody has shown it. This cell shows it, by a planted test, and repairs NOTHING.

## 1. THE BUILD (LOCAL)

1. One test file, `lib/research/harvest/tests/test_bq1_alias_case_read.py`, no network, calling `_security_mentions`
   (and `_iter`-free: build the article row dict by hand as the package's existing tests do). Three arms:
   - **(i) the planted case.** A security `{"security_key": "TGT_US_Equity", "company": "Target Corp", "aliases":
     ["Target"], "ticker_aliases": ["TGT"]}` and an article whose title and every block use only lower-case "target"
     as a common word ("the central bank kept its inflation target", three or more blocks, no "Target", no "TGT").
     Record what `_security_mentions` returns: whether a pair is made, its `mention_count`, its `match_forms`.
   - **(ii) the control that the instrument can see case at all.** The same security and an article whose only form is
     lower-case "tgt": record whether the ticker form pairs.
   - **(iii) the control that the fixture is live.** The same security and an article that says "Target" capitalised:
     it must pair.
   The test ASSERTS what you found in (i) and (ii), each with a one-line comment "today's behaviour as found on
   <date>", and asserts (iii) pairs. Do not write the test to pass either way: assert the one outcome you observe.
2. One note, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~124/BQ1_ALIAS_CASE_READ.md`, at most 20 lines: a first line that begins `TODAY:` and says in plain words
   whether a lower-case common word pairs with a security carrying that word as an alias; then the three arms' returned
   values; then the function names and line numbers that decide it.
3. Change nothing in `publication_gold.py`, `universe_securities.py` or any list file. No repair, even if (i) pairs.

<paths>
lib/research/harvest/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~124/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bq-1"><invocation>python -m pytest lib/research/harvest/tests/test_bq1_alias_case_read.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bq-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~124/BQ1_ALIAS_CASE_READ.md</invocation><expect>TODAY:</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W124-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~124/AMGT_HARVST.TO-HVST-bq-1.the-lower-case-alias-read.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bq-1.the-lower-case-alias-read`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31486, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` @3b19f962e0. Decomposition section 86.
- `1.0.0_SA_CTO~Z` R26 (msg 31845) part (a): "confirm that read by a test, a planted lower-case 'target' body on a security
  that carries aliases". R27 (msg 31867): R26(b), the repair, is NOT cut; it waits on the issuer's census over built gold.
- <risk> LOCAL. Chain of one, slot ~124, worker-light (a test and a note). **Checks dry-run at the base:** AC1 base FAIL as
  expected (the test is absent); AC2 base FAIL as expected (no such file).

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>issued</status>

COMPLETE 2026-10-08 ~19:0xZ (issuer 2.0.0_SA_COO~H): worker ~124 @359ee158d8 and @3c288e4fcc, drained @afd20e8eac. AC1 3 passed (re-run by the issuer from the worktree: 3 passed); AC2 note line 1 'TODAY: YES -- a lower-case common word ("target") pairs with a security (TGT_US_Equity) whose alias list holds "Target"; nothing was repaired.' Controls: lower-case 'tgt' does not pair (ticker forms keep their case); capitalised 'Target' pairs. Proof instance VALID.
<status>complete</status>
<round>73</round>
<slot>~124</slot>
<fabric>site-z</fabric>
