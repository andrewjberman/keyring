# AMGT_RESAPP task order -- `AMGT-ao-1` -- FWD-38 (b): EVERY SERVED DISPLAY NAME IN TITLE CASE, AT THE PRODUCER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ao-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~216</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- no new read or write; the re-case is a pure function over a name the function already serves.
comp-adversary: RUN by the issuer at the cut -- r65_served c17 FAILS at the base, local and deployed: 60 of 94 price names and 61 of 95 chatter names all-caps; both serve 'MITSUBISHI UFJ FINANCIAL GRO'.
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r65-216` (branch `wk-AMGT_RESAPP-216`, cut from the issuance commit with `--portal-ref a730d8ce`, so the
portal fixture the api tests read is present). Work and commit only there. Start every shell call with `cd /c/tmp/r65-216`: a call that
starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ao-1` (round 65, decomposition s.73; PRD FWD-38 (b))

FWD-38 (b): every route serves ONE display name per security, in title case, with no share-class code. Today 60 of 94 price-ranking
names and 61 of 95 collected/chatter names are served all-caps.

1. **The seam is `scoped_amgt._clean_display_name`** (`lib/research/api/scoped_amgt.py` about :773). Every display-name chain ends
   there: `monthly_chatter._display_names` (classification, then crosswalk, then model block), `_overlay_name` and
   `_with_display_name`. Re-case there, so every route gets it at once.
   - Only an ALL-CAPS name is re-cased. A name that already carries a lower-case letter is served exactly as it is today.
   - Legal-form suffixes take their conventional case (for example INC, CORP, CO, LTD, PLC, NV, AG, SA, SE, HOLDINGS). Declare the
     suffix table in the module.
2. **Declare the acronym list** as the module constant `DISPLAY_NAME_ACRONYMS` (a set of upper-case words kept upper, such as BP,
   ASML, AIA, UFJ), with `DISPLAY_NAME_ACRONYMS_SOURCE`, a one-line string naming where the list comes from. The check reads both
   names exactly.
3. **The share-class remnant:** 'SHOPIFY INC - CLASS' is served today, because the an-3 rule (`_SHARE_CLASS_TAIL` about :770) matches
   "Class" case-sensitively, so an all-caps 'CLASS A' loses only the 'A'. No share-class word survives in a served name.
4. **The cut names.** Crosswalk names are cut at a fixed width ('MITSUBISHI UFJ FINANCIAL GRO').
   - Measure the width and count the served names at it.
   - Each cut name takes a full name the estate ALREADY holds, with its source cited (a path, table or object and key). Prefer a
     source the function already reads. Otherwise use a declared map in the module, each entry with its source in a comment.
   - Never guess and never call a vendor. A cut name with no estate source stays as it is and is listed as residue.
   - Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~216/CUT_NAMES.md`: the width, the count with its
     denominator, each name with its full name and source, and the residue.
5. **The plant test** `lib/research/api/tests/test_display_name_case.py`. It holds at least 8 cases through the seam the routes use.
   Each case declares the exact served string. The cases must include the six below; the given start is required, and the rest is
   your declared suffix case.
   - SYNOPSYS INC -> starts 'Synopsys'
   - CADENCE DESIGN SYS INC -> starts 'Cadence Design'
   - BP PLC -> starts 'BP '
   - ASML HOLDING NV -> starts 'ASML Holding'
   - AIA GROUP LTD -> starts 'AIA Group'
   - MITSUBISHI UFJ FINANCIAL GRO -> starts 'Mitsubishi UFJ Financial Group'

   The other cases must include 'SHOPIFY INC - CLASS A' (no Class word served) and one already mixed-case name, which must come back
   unchanged.

Run `lib/research/api/tests/` before your commit and report its last line. **Stamp any surprise row's `surfaced_at` with `date -u
+%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W216-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no vendor or model call, no portal write.
2. `name`, `name_source` and `display_name_source` keep their values. Only `display_name` changes.
3. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~216/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ao-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/api/tests/test_display_name_case.py; echo "exit=$?"</invocation><expect>at least 8 cases pass, among them the six named names, each reading its declared served string; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ao-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round65/checks/r65_served.py --cell c17 --where local; echo "exit=$?"</invocation><expect>declared acronyms over 0 with a source; C1 PASS on both routes (0 all-caps names, acronym-only excepted); C2 PASS on both routes; R65 C17 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ao-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round64/checks/r64_served.py --cell c12 --where local; echo "exit=$?"</invocation><expect>R64 C12 SERVED: YES (one display name per security, unchanged); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~216 <0.9.0_WK_AMGT_RESAPP~216@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~216/AMGT_RESAPP.TO-AMGT-ao-1.display-name-title-case.proof_of_spec.json`.
Report once:
- the commit hash
- every criterion's output lines
- the api suite's last line
- the functions you changed
- the cut-name count and residue
- any row

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-64 analysis @504827836c ruling 1; rows Z-S340, Z-W212-S1. JUDGMENT at L9: 3.0.0_SA_CVO~Z reads the served
list as a reader would (never self-graded). Served by ao-2.

<status>pending</status>
<round>65</round>
<slot>0.9.0_WK_AMGT_RESAPP~216</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-03 ~18:1xZ):** ACCEPTED. Worker ~216 `d72eed67f7` + `90b269d95b`, drained `9f8f4ee4b6` (one append-only channel conflict, resolved). Re-graded in a clean worktree at the merge commit:
- union (peers + management + api + harvest + coverage): 1030 passed, exit=0;
- c17 local YES (0 of 94, 0 of 95 all-caps; MUFG whole on both routes);
- c12 YES;
- at build commit `9a8cbd2c97`: c9-c14 YES.

Cut names: width 28, 7 of 67 crosswalk names at it. 5 take an estate full name with its source; 3 are residue (Singapore Telecommunications, Roche Holding AG-Genussschein, Hon Hai Precision Industry) and ride Andrew's Bloomberg card (call 3).

Row Z-W216-S1 (OBSERVATION, INERT): the worker edited two test pins of the all-caps name, and added a caps-only Bloomberg share-type tail rule. Both are inside the cell and ruled acceptable by the issuer.

JUDGMENT at L9 is CVO~Z's. Served by ao-2.

<status>complete</status>
