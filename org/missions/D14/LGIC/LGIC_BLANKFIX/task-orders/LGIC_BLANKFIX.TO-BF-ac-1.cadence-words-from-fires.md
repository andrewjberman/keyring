# TO LGIC_BLANKFIX.TO-BF-ac-1 -- round 14 BF-ac-1: FWD-4 R1: a schedule's word is read from its own expression ({N}h for evenly spaced fires, else the partial form with its reason); never a carried-over word

<to_id>LGIC_BLANKFIX.TO-BF-ac-1</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `BF-ac-1` (`decompositions/LGIC_BLANKFIX_DECOMP.round14.md`) | **outcome_ref:** FWD-4 |
**depends_on:** none (slot ~1)

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --all-roots` (the same as `python lib/opal_naming_rootcheck.py all
--map infra/logic/registry/root_map.json`) runs every Terraform root the root map covers and prints the denominator of roots
first; `infra/logic/README.md` "Run the naming check" explains its lines and fields. At this cut, on the base your worktree is
made from, it reads: `ALL-ROOTS ok=True roots_total=86 mapped=86 unmapped=0 completed=86 stopped=0 items=2601 right=672 fix=1636 not_asked=268 pattern=25 carded=0 refused=0 hole=0 carded_class_holes=0 source_bucket_holes=0 event_rule_holes=0 unknown_word_holes=0 other_holes=0 stale_hints=0 uncounted=1 counted_at_caller=17`. The round-13 close is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~B1/ALL_ROOTS_round13.txt`. The CTO's reading of round 13 is `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round13.md` -- read it first:
FWD-8 is REALIZED; FWD-4 is not yet, and this round's three cells are its rulings R1, R2, R4/R5. The PRD is
`org/missions/D14/LGIC/LGIC_BLANKFIX/prd/LGIC_BLANKFIX_PRD.md` (FWD-4 and FWD-8 DONE WHEN and ACCEPT, lines 51-90; C-CADENCE line 118). The round-13 drain end is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~B1/ROUND13_DRAIN_END.md`.
Modules, under `lib/`: `opal_naming.py` (`grade`, `census_repo`, the `census` command), `opal_naming_scope.py` (the roots, their
names, `root_items`, the UNCOUNTED reader and `UNCOUNTED_REASONS`), `opal_naming_rootmap.py`, `opal_naming_cadence.py`,
`opal_naming_keyfill.py`, `opal_naming_policyrole.py`, `opal_naming_rootcheck.py` (`decide`, `place`, `check_root`, `_ruling_of`,
`all_roots`, `HOLE_OWED`, the `lines`, `keys` and `all` commands). The gates: `.tools/naming-gate.py` (commit time),
`.tools/naming-apply-gate.py` (plan time), called by `.tools/safe-commit.sh` and `.tools/safe-apply.sh`. The registry is
`infra/logic/registry/`; only `4.0.0_SA_CRO` writes it. Read the modules your cell touches or calls before you build. Import with
`sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only in code and output; no new dependency; no AWS call and no network
call. The bar: `python -m pytest lib/tests -q -p no:cacheprovider` passes whole at the base (193 passed, 1 skipped), and every
`lib/tests/test_opal_naming_*.py` script prints `ok=True` at the base. None may newly fail after your build. A test you write
asserts relations and the rows it needs by name, never a typed total of repository names, roots or registry rows: those move
every day, and the registry's lane may add rows during this round. **The switch file `org/mcp/naming-place.enforce` is PRESENT since
@4d2bfc6dfd:** the placement refusal is live on every commit and apply. No cell deletes, moves or edits it; exercise the gates
only in a temporary copy, and never write a real override audit row.

### THE CELL

`BF-ac-1` (ruling R1 in `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round13.md`; row D1-W1-S8). Round 13's checker `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/check_fwd4_cadence.py` read 180 schedules:
144 agree, 36 undecided, 0 mismatch -- but ten undecided rows keep the word the CURRENT name carries: seven fire twice a day under
`daily`, and `finbert-scoring-post-ingestion-45min` fires three times a day. R1 under the ratified rules `org/missions/D14/LGIC/LGIC_BLANKFIX/prd/E1_CADENCE_RULES_RATIFIED.md` (P1, P2):
evenly spaced fires take `{N}h` (twice a day, 12 h apart, is `-12h`; three times, 8 h apart, is `-8h`); uneven fires have no word and
the row prints its partial form with the reason. The list never carries over the old word.

**Build** in `lib/opal_naming_cadence.py` (and its test) only:
1. The cadence word for an expression with several fires a day: evenly spaced fires read `{N}h`; uneven fires read no word and give
   the reason. A word already in the current name is never used when the expression decides otherwise or decides nothing.
2. Cases in `lib/tests/test_opal_naming_cadence.py`: twice-a-day 12 h apart -> `12h`; three-a-day 8 h apart -> `8h`; uneven -> no word
   with its reason; the DIFFERENCE CONTROL, a once-a-day expression still reads `daily`.
3. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/check_fwd4_cadence_r14.py`: over every mapped root, every schedule line's word is read against its expression's fire
   count; a word that disagrees with its expression is a MISMATCH and FAILS the run (the NEGATIVE ARM, inside: a planted line whose word
   disagrees is counted and would fail). Last line: `FWD4-CADENCE-R14 ok=True schedules=N agree=N partial=N mismatch=0 carried_over=0`.
4. `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/exercise_fwd4_rename_12h.py`: one twice-a-day schedule renamed from its list line alone (now `-12h`) in a temporary copy of its
   `.tf`, graded by the real `.tools/naming-gate.py --diff`: CONFORMANT, no placement refusal. Last line:
   `FWD4-RENAME-12H ok=True name=<new> grade=CONFORMANT`. No apply, no AWS.

### ACCEPTANCE

<criterion id="BAC1-AC1" cell_refs="BF-ac-1"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/check_fwd4_cadence_r14.py</invocation><expect>FWD4-CADENCE-R14 ok=True</expect></criterion>
`BAC1-AC1` -- every schedule's word agrees with its expression's fires, or the row prints its partial form; a disagreeing word fails.

<criterion id="BAC1-AC2" cell_refs="BF-ac-1"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/exercise_fwd4_rename_12h.py</invocation><expect>FWD4-RENAME-12H ok=True</expect></criterion>
`BAC1-AC2` -- one twice-a-day schedule renamed -12h from its list line alone passes the real gate.

<expected_criteria>BAC1-AC1,BAC1-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource;
  `org/mcp/naming-place.enforce` is never deleted or edited.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-D1-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; a row filed on dell1 carries the `-D1-` coordinate
  or the row gate refuses it) in the investigation file, and do not weaken the test or the expected value. A fact in this order that
  the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_cadence.py
lib/tests/test_opal_naming_cadence.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under
`infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round13.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round14.md`, and the `lib/` modules and `.tools/` scripts your block does
not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round14.md</decomp_doc> (round 14), cell `BF-ac-1`.
<owned_cells>BF-ac-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BAC1-AC1, BAC1-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-ac-1.cadence-words-from-fires.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BAC1-AC1,BAC1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last lines whole; the ten S8 rows before and after; schedules, agree, partial, mismatch; the renamed schedule; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a word carried over from the current name (counted as carried_over, must be 0); an uneven schedule given a word (partial form with its reason instead); the once-a-day control drifting; BLIND: expressions set at run time.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round13.md @9abfddbcff (`1.0.0_SA_CTO~DELL1`, msg 2402), item item 1 (R1, row D1-W1-S8); decomposition round 14. Base dry-run at the cut, by the
issuer at base 263271c6db: BAC1-AC1 base: FAIL as expected (file absent; 10 S8 rows carry over a contradicted word); BAC1-AC2 base: FAIL as expected (file absent).
