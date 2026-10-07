# TO LGIC_BLANKFIX.TO-BF-e-6 -- round 2 BF-e-6: service words leading a name -- measured, and the registry move proposed

<to_id>LGIC_BLANKFIX.TO-BF-e-6</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~6</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-e-6` (`decompositions/LGIC_BLANKFIX_DECOMP.round2.md`) | **outcome_ref:** FWD-3 |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

**Where the project stands.** Round 1 built one command: `python lib/opal_naming.py census --root infra/aws/terraform/bd-pipeline`
prints one line per name of that root, each of kind `RIGHT`, `FIX`, `NOT-ASKED`, `PATTERN`, `CARDED` or `HOLE`, and exits 1 while any
line is a `HOLE`. Its last run is saved at `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round1_bd-pipeline.txt`: 140 names, 10 right, 101 fix,
6 not asked, 1 pattern, 6 carded, 16 holes. The modules, all under `lib/`: `opal_naming.py` (`grade(name, type) -> (verdict,
canonical)`, `census_repo()`, `census_tf_names()`), `opal_naming_scope.py` (`root_items(root)`), `opal_naming_rootmap.py`
(`load_map`, `resolve`; the landed map is `infra/logic/registry/root_map.json`), `opal_naming_cadence.py` (`word_for`, `cadences`),
`opal_naming_keyfill.py` (`fill_keys`), `opal_naming_rootcheck.py` (`decide`, `check_root`). Read the ones your cell touches or
calls before you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only in code and output; no new
dependency. The bar for the library's own suite: `python -m pytest lib/tests/test_opal_naming.py -q -p no:cacheprovider` fails six
named tests at the base (see `lib/tests/test_opal_naming_fourth_verdict.py` for the list); no test that passes at the base may fail.

### THE CELL

`BF-e-6`. Andrew ruled that an AWS service name is never a system. The grader gives a name the verdict `NO-SYSTEM-ASKED` when its
first token is in `infra/logic/registry/systems.json` `refused_keys.purpose_word` (`cross`, `s3`, `cloudwatch`, `invoke`,
`secretsmanager`, `lambda`, `kms`, `secrets`). But other AWS service words sit in `refused_keys.generic_noun` (for example
`events`, `cloudfront`, `ec2`, `ecs`, `ecr`, `dynamo`, `codebuild`, `fargate`), so `events-emit` and `cloudfront-invalidate` still
print as broken names that need a system. Moving a word between those lists is the registry lane's edit (`4.0.0_SA_CRO`). You
measure and propose; you edit no registry file.

**Build**, all in your deliverables folder `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~6/`:
1. `service_words.py`: reads `generic_noun`; classes each word `AWS-SERVICE` or `OTHER`, an `AWS-SERVICE` word being one that is
   the name of an AWS service or its API prefix AND appears as the service prefix of at least one IAM action (`"<word>:`) in the
   repository's `.tf` or policy JSON files (print the first such file and line as evidence; a word with no such occurrence is
   `OTHER`). Then, on a temporary COPY of the registry folder with the `AWS-SERVICE` words moved to `purpose_word`, loads the
   grader against the copy (`opal_naming.load_registry` takes a folder; read how the vocabulary cache is keyed and build a fresh
   vocabulary, never mutate the real registry) and re-grades `census_repo()`'s items: counts the names whose verdict changes, by
   old and new verdict. Runs `opal_naming.validate()` on the copy. Last line
   `SERVICE-WORDS ok=True generic_noun=N aws_service=N moved_names=N to_no_system_asked=N other_changes=N validate_refusals=0`;
   `ok=True` when every changed name moved from `OUT-OF-PATTERN` to `NO-SYSTEM-ASKED` (`other_changes=0`), the copy validates,
   and the real registry files are byte-identical before and after the run (hash them).
2. `PROPOSAL_SERVICE_WORDS.md`: one page for the owning lane: the words with their evidence, the names that move, the names
   that do NOT move though they lead with one of the words (and why), and the last line.

### ACCEPTANCE

<criterion id="BE6-AC1" cell_refs="BF-e-6"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~6/service_words.py</invocation><expect>SERVICE-WORDS ok=True</expect></criterion>
`BE6-AC1` -- the move changes only names from broken to not-asked, on a copy, with the real registry untouched.

<expected_criteria>BE6-AC1</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- Your whole build lives in your deliverables folder, which the tree convention grants; the block below names only the investigation file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W6-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>

org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round1_bd-pipeline.txt`, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round1.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round2.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round2.md</decomp_doc> (round 2), cell `BF-e-6`.
<owned_cells>BF-e-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BE6-AC1. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~6/LGIC_BLANKFIX.TO-BF-e-6.service-words-proposal.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BE6-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last line whole; the `AWS-SERVICE` words with evidence; the count of names that move, with five examples; the proposal's path; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed; the cell reads schedule text.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a word classed a service by the worker's memory alone (the IAM-action occurrence in the repository is required as evidence); a move that changes a name's system instead of its verdict (other_changes=0 is in ok); the real registry mutated by the measurement (hashed before and after); BLIND: service words that lead only live names -- the measurement is the repository plane.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round1.md @e40eddd4e8 (the CTO's enrichment list); decomposition round 2. Base dry-run at the cut: BE6-AC1 base FAIL as expected (file absent).
