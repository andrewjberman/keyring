# TO LGIC_BLANKFIX.TO-BF-r-1 -- round 3 BF-r-1: the 18 lines a reader could not act on -- each says why, and what to do

<to_id>LGIC_BLANKFIX.TO-BF-r-1</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-r-1` (`decompositions/LGIC_BLANKFIX_DECOMP.round3.md`) | **outcome_ref:** FWD-1, FWD-3 |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --root infra/aws/terraform/bd-pipeline` prints one line per name of
that root: `KIND type current -> detail  [where]`, kinds `RIGHT`, `FIX`, `NOT-ASKED`, `PATTERN`, `CARDED`, `REFUSED`, `HOLE`; it
exits 1 while any line is a `HOLE`. Round 2's run is saved at `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round2_bd-pipeline.txt`: 140 names,
9 right, 113 fix, 9 not asked, 1 pattern, 6 carded, 2 refused, 0 holes. A seat that built none of it read that run and could act on
122 of the 140 lines from the line alone; its grade, with the 18 lines it could not act on, is
`org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND2_L9_GRADE_BE8_AC3_20261007.md` -- read it first. The modules are under `lib/`:
`opal_naming.py` (`grade`), `opal_naming_scope.py` (`root_items`, `root_table`, `contested`), `opal_naming_rootmap.py` (`load_map`,
`resolve`; the landed map is `infra/logic/registry/root_map.json`), `opal_naming_cadence.py`, `opal_naming_keyfill.py` (`fill_keys`,
`bucket_of`), `opal_naming_policyrole.py` (`policy_roles`, `system_for`), `opal_naming_rootcheck.py` (`decide`, `check_root`). Read
the ones your cell touches or calls before you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only
in code and output; no new dependency. The bar for the library: `python -m pytest lib/tests -q -p no:cacheprovider` passes whole at
the base (194 passed); no test may fail after your build.

### THE CELL

`BF-r-1`. The grade file lists four groups of lines a reader who did not build the check could not act on. You change what
`lib/opal_naming_rootcheck.py` PRINTS for each. You decide no name and edit no registry file.

1. **NOT-ASKED (8 lines).** Today: "this kind of name is not asked to carry a system; s3-access-policy" -- it says the name is not
   wrong and then prints a different name, with no reason. Each `NOT-ASKED` line must say WHY in plain words, by the kind of
   name: its first word is an AWS service or action word (name the word); or it is an inline policy name written as one
   capitalised word; or it is a library layer. And it must say whether a rename is owed: when the graded form equals the current
   name, "no rename is owed"; when it differs, "a rename is owed for the form only, not for a system: " and the whole form. Take
   the kind from the same tests the grader uses (`refused_keys.purpose_word`, the PascalCase policy test, `LAMBDA_LAYER`); do not
   re-derive them by hand.
2. **CARDED (6 lines).** The CTO's corrected ruling: a carded line prints its whole correct name, or says in plain words that none
   is owed and why; a card that can say neither is a defect of the card. No card in
   `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/NOT_JUDGED_R13.json` names a correct name. So:
   (a) test `PATTERN` BEFORE `CARDED`: a carded name with a variable segment (`%s`, a brace, `*`) is a `PATTERN` line, which is
   already a complete line; (b) a carded name whose card has a field naming a correct name (`canonical`) or a field saying none is
   owed (`no_name_owed`, a plain sentence) prints `CARDED` with that; (c) any other carded name prints `HOLE`, with the detail in
   plain words -- what kind of thing the name is (for a storage key: "a stored-file path the check cannot read"), that it was
   skipped by a card, and "the card gives no correct name and does not say none is owed" -- and NO rule code (`K1`, `V7`) and no
   word "re-measurement". Neither field exists in any card today; you do not edit the card file.
3. **REFUSED (2 lines).** Today: "this key belongs to another firm's store", though the same line shows the key's bucket is this
   firm's. A `REFUSED` line must say what was MEASURED and what the reader does: when the refusal comes from a path word (the key's
   bucket belongs to the root's firm): "a file named for THE-OTHER-FIRM (THE-PATH-WORD) is kept in this firm's bucket
   THE-BUCKET; no rename is given: ask the owner of the code at the place shown whether it should run another firm's file". When
   the key's BUCKET belongs to another firm, say that instead, naming the bucket and the firm. Read which case it is from the
   `fill_keys` row (`bucket`, `basis`); if the row does not let you tell the two cases apart, report it and print the path-word
   sentence only when the bucket's firm equals the root entry's scope.
4. **Two names, one target (2 lines).** EC2 instances `bd-fees` (`ec2.tf:86`) and `bd-49f-fees-runner`
   (`bd-49f-session-trigger/lambda_function.py:52`) both print `FIX ... -> blackdiamond-49f-fees-runner`. After every line is
   decided, find every group of two or more DIFFERENT current names of the same type whose `FIX` target is the same string; each
   line of such a group becomes `HOLE`: "this target is also given to THE-OTHER-NAME at ITS-PLACE; two resources
   cannot take one name, and nothing here says which keeps it". The same current name appearing twice (one resource named in two
   files) is NOT a collision.

Last line unchanged in shape; the seven counts still sum to `items`. After this build the real root is EXPECTED to print holes
again (the cards with no name, the collision): do not suppress them.

**Extend** `lib/tests/test_opal_naming_rootcheck.py`: one case per behaviour above, including: a `NOT-ASKED` line whose form
equals the name says no rename is owed and one whose form differs says a rename is owed for the form; no `CARDED` or `HOLE` line
made from a card contains `K1`, `K3`, `K4a`, `V7` or `re-measurement`; the DIFFERENCE CONTROL: two different names with one
target are both `HOLE`, and the same two names with different targets are both `FIX`. Last line `ROOTCHECK-TEST ok=True cases=N`.

**Add** a command `python lib/opal_naming_rootcheck.py lines ROOT --map PATH`: runs the root and checks its own output: every
`NOT-ASKED` line contains "rename"; no line contains a rule code from the list above; no two different current names of one type
share a `FIX` target; no `REFUSED` line contains "belongs to another firm's store" unless its bucket's firm differs from the
root's. Last line `ROOTCHECK-LINES ok=True root=... not_asked=N carded=N refused=N hole=N collisions=0`.

### ACCEPTANCE

<criterion id="BR1-AC1" cell_refs="BF-r-1"><invocation>python lib/tests/test_opal_naming_rootcheck.py</invocation><expect>ROOTCHECK-TEST ok=True</expect></criterion>
`BR1-AC1` -- each of the four behaviours is reachable, and a shared target is what turns two fixes into holes.

<criterion id="BR1-AC2" cell_refs="BF-r-1"><invocation>python lib/opal_naming_rootcheck.py lines infra/aws/terraform/bd-pipeline --map infra/logic/registry/root_map.json</invocation><expect>ROOTCHECK-LINES ok=True</expect></criterion>
`BR1-AC2` -- the real root's own lines pass the four reader checks.

<expected_criteria>BR1-AC1,BR1-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_rootcheck.py
lib/tests/test_opal_naming_rootcheck.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round2_bd-pipeline.txt`, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round2.md`, `org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND2_L9_GRADE_BE8_AC3_20261007.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round3.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round3.md</decomp_doc> (round 3), cell `BF-r-1`.
<owned_cells>BF-r-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BR1-AC1, BR1-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-r-1.eighteen-lines.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BR1-AC1,BR1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole and the root run's last line; every `NOT-ASKED`, `CARDED`, `REFUSED` and `HOLE` line whole; for each `HOLE`, what would close it and whose it is; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- holes hidden to keep the count at zero (the face says holes are expected and forbids suppressing them; AC2 counts them); a correct name invented for a carded key (the face forbids it: the card or its owner gives it); a collision missed because the two names sit in different files (the group is by type and target, across the whole root; the difference control); a not-asked reason typed per name instead of read from the grader's own tests; BLIND: whether the two EC2 names are one machine -- the check reads names, not instances.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round2.md @ef7133ec9a (the CTO's enrichment list); decomposition round 3. Base dry-run at the cut: BR1-AC1 base PASS as expected (ran: ROOTCHECK-TEST ok=True cases=48; the round-2 test, extended by the cell); BR1-AC2 base FAIL as expected (ran: no such command).
