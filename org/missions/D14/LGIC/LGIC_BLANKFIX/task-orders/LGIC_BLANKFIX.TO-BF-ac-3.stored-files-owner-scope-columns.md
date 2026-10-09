# TO LGIC_BLANKFIX.TO-BF-ac-3 -- round 14 BF-ac-3: FWD-4 R4/R5: stored-file lines print owner and scope as two columns; the 14 per-firm rows show as patterns

<to_id>LGIC_BLANKFIX.TO-BF-ac-3</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~2</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `BF-ac-3` (`decompositions/LGIC_BLANKFIX_DECOMP.round14.md`) | **outcome_ref:** FWD-4, FWD-8 |
**depends_on:** BF-ac-2 (same slot, same file)

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

`BF-ac-3` (rulings R4 and R5 in `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round13.md`). Round 13's stored-file lines end `source=<x> owner=<y>`, where `owner=` printed the
address's scope (`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_fwd4_stored_files.py`: 254 files, 230 with both, 24 UNDECIDED). R4: two labelled columns,
`owner` (from the ruling row: who moves the store) and `scope` (from the address: whose file it is), never one in place of the other.
R5: the 14 per-firm rulings (owner filled per firm at run time) are PATTERNS under FWD-8, each shown with its per-firm fill named; the 10
with an open `{source}`/`{scope}` place stay UNDECIDED with their reason printed.

**Build** in `lib/opal_naming_rootcheck.py` (stored-file lines) and its test:
1. Stored-file FIX and RIGHT lines print `source=<x> owner=<y> scope=<z>`; `owner` from the ruling row, `scope` from the address; a field
   no row decides prints `UNDECIDED` with its reason.
2. The 14 per-firm rows print as `PATTERN` with the per-firm fill named; the census `pattern=` count rises by 14 and nothing else moves.
3. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_fwd4_stored_r14.py`: last line `FWD4-STORED-R14 ok=True files=N owner_and_scope=N per_firm_patterns=14 undecided=10`,
   with `ok=True` when every stored-file line carries the three fields or is one of the named patterns or UNDECIDED-with-reason rows.
   Keep `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_fwd8_patterns.py` passing (patterns shown as patterns, none as names).

**AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-09 ~12:5xZ; row LGIC_BLANKFIX-D1-W1-S9, handed from BF-ac-1):** add build item 4 in `lib/opal_naming_rootcheck.py` `decide()`, the same file this cell owns: when the cadence reader gives NO word for a schedule whose expression is stated (BF-ac-1 @7a82774af7 now returns None with a reason for uneven or non-interval fires), and the current name carries a cadence word (not an `on-` form), rebuild the listed name on `{cadence}` so the existing H14 hole prints the partial form with the reader's reason, never the carried-over word. Case in the root-check test: an uneven twice-a-day schedule prints its partial form with the reason; the DIFFERENCE CONTROL, an evenly spaced one prints `-12h`. Six rows are expected to move (fear-greed-daily-update, trending-topics-portal-publisher-daily, keyword-drilldown-generator-daily, finbert-scoring-post-ingestion-45min, teams-global-transcripts-pull-hourly, fred-ingestion-monthly-early); report the census `hole` before and after. Criteria text unchanged; BAC3-AC2 (ROOTCHECK-TEST) covers the new case.

### ACCEPTANCE

<criterion id="BAC3-AC1" cell_refs="BF-ac-3"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_fwd4_stored_r14.py</invocation><expect>FWD4-STORED-R14 ok=True</expect></criterion>
`BAC3-AC1` -- stored-file lines print owner and scope separately; the per-firm rows are patterns; the rest UNDECIDED with a reason.

<criterion id="BAC3-AC2" cell_refs="BF-ac-3"><invocation>python lib/tests/test_opal_naming_rootcheck.py</invocation><expect>ROOTCHECK-TEST ok=True</expect></criterion>
`BAC3-AC2` -- the root check's test holds.

<expected_criteria>BAC3-AC1,BAC3-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource;
  `org/mcp/naming-place.enforce` is never deleted or edited.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-D1-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; a row filed on dell1 carries the `-D1-` coordinate
  or the row gate refuses it) in the investigation file, and do not weaken the test or the expected value. A fact in this order that
  the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_rootcheck.py
lib/tests/test_opal_naming_rootcheck.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under
`infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round13.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round14.md`, and the `lib/` modules and `.tools/` scripts your block does
not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round14.md</decomp_doc> (round 14), cell `BF-ac-3`.
<owned_cells>BF-ac-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BAC3-AC1, BAC3-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/LGIC_BLANKFIX.TO-BF-ac-3.stored-files-owner-scope-columns.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BAC3-AC1,BAC3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last lines whole; files, owner-and-scope, per-firm patterns, undecided with reasons; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- owner and scope merged again (two labelled columns, the checker asserts both); a per-firm row counted as a name (shown as a pattern; FWD-8's checker kept passing); BLIND: owners named only outside the registry.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round13.md @9abfddbcff (`1.0.0_SA_CTO~DELL1`, msg 2402), item item 3 (R4, R5); decomposition round 14. Base dry-run at the cut, by the
issuer at base 263271c6db: BAC3-AC1 base: FAIL as expected (file absent; owner= prints the scope); BAC3-AC2 base: PASS as expected (ROOTCHECK-TEST ok=True cases=334).
