# AMGT_RESAPP task order -- `AMGT-aa-4` -- A SHORT INITIALISM THE REGISTERED NAME PRINTS IN CAPITALS KEEPS ITS CAPITALS IN THE SERVED DISPLAY NAME (CSL LTD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-aa-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~391</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-aa-4.a-short-initialism-keeps-its-capitals-in-a-display-name</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a declared-word list and its test, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- r95_casing.py reads the crosswalk's registered names (a read) and nothing else.
comp-adversary: RUN at the cut -- r95_casing.py FAILs K1, K2, K3 at the base ('CSL LTD' -> 'Csl Ltd', 'JD.COM INC-ADR' -> 'Jd.Com Inc', 0 names depend on the two words) and PASSes K4, K5, and PASSes 5 of 5 against a throwaway candidate (the two words added to the declared set: exactly those two of 68 registered names change). r95_casing_deployed.py FAILs D1 at the live base ('Csl Ltd') and PASSes D2, D3.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-391` (branch `wk-AMGT_RESAPP-391`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-391`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-aa-4` (round 95, decomposition s.103)

CTO~DELL1 round-94 analysis item 4 (cosmetic; rides item 2's redeploy). `scoped_amgt._clean_display_name` serves an ALL-CAPS name in title case and keeps the words
DECLARED in `DISPLAY_NAME_ACRONYMS` upper. The crosswalk's registered name 'CSL LTD' serves 'Csl Ltd' because CSL is not declared. Measured over the 68 registered names, exactly
two initialisms are missing from the declared set: **CSL** ('CSL LTD') and **JD** ('JD.COM INC-ADR'); every other short token is a word (RIO, ELI, NIKE, VISA, UBER, COPA) or a
legal word the rule already handles. Do exactly this:

1. In `lib/research/api/scoped_amgt.py` add `"CSL"` and `"JD"` to `DISPLAY_NAME_ACRONYMS` (the issuer initialisms row), and add `CSL` and `JD` to the comment that names the
   source of the declared words (the crosswalk's own registered names 'CSL LTD' and 'JD.COM INC-ADR', read 2026-10-11, row `D1-S26` / CTO round-94 analysis item 4). Change nothing
   else in the file (this order follows `AMGT-aa-2` on the same file and must apply on its merge).
2. Add `lib/research/api/tests/test_display_name_initialisms.py` (pure): one test per arm K1-K5 of `r95_casing.py`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W391-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install`. The checks' S3 and DynamoDB reads (GET only) are permitted; nothing else is fetched.
3. Standing: no S3 delete, no push of shared branches.
4. Edit the named product files minimally: do not reformat them and touch no function the cell does not name.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/test_display_name_initialisms.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~391/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-aa-4"><invocation>cd C:/dev/wk-resapp-391 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round95_prep/checks/r95_casing.py"; echo "exit=$?"</invocation><expect>PASS K1 ('CSL LTD' is served 'CSL Ltd'), PASS K2, PASS K3 (exactly two of the registered names depend on the two declared words), PASS K4, PASS K5; arms passed 5 of 5; R95 CASING: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-aa-4"><invocation>cd C:/dev/wk-resapp-391 &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/api/tests --ignore=lib/research/api/tests/test_print_format_rich.py -q -p no:cacheprovider; echo "exit=$?"</invocation><expect>the control: the new test file and every other test of lib/research/api/tests pass (no failed, no error); and exit=0</expect></criterion>
</proof_of_spec>


<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-94 analysis item 4: "The 'Csl Ltd' casing (_clean_display_name on a short all-capitals name): a short all-capitals token that the registered name prints in capitals stays in capitals. Close: CSL AU reads 'CSL Ltd', and a control name's casing is unchanged. It is cosmetic, and it rides item 2's redeploy." READ: a rule on 'short all-capitals' cannot tell an initialism from a word (ELI, RIO, NIKE print in capitals in the registered names too), so the cell extends the estate's own DECLARED list with the two measured initialisms and the census arm K3 states that no other of the 68 names moves. JD changes nothing served today (JD_US_Equity is served from the table's mixed-case 'JD.com Inc'); it is declared for the path that serves the registered name. Queued behind aa-2 on slot ~391 (same file); handed to the same worker when aa-2 is terminal.

<status>complete -- 2026-10-11T16:47Z by the issuer (2.0.0_SA_COO~R1): wk-AMGT_RESAPP-391 @f2532b1f0e (code @1aa49782ec) merged @ecb3e3689b, proof instance VALID; issuer re-run on the merged tree: AC1 R95 CASING YES (5 of 5: 'CSL LTD' -> 'CSL Ltd', 'JD.COM INC-ADR' -> 'JD.Com Inc', exactly those two of the 68 registered names depend on the two declared words; controls ELI, RIO, NIKE unchanged), AC2 lib/research/api/tests 955 passed. scoped_amgt.py +4/-2 (the declared initialisms row and its source comment), one new test file of five. Served change: NONE until AMGT-aa-5. JD_US_Equity is served from the table's mixed-case name and does not move; the declared word guards the path that serves the registered name.</status>
<round>95</round>
<slot>0.9.0_WK_AMGT_RESAPP~391</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
