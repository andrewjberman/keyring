# TO LGIC_BLANKFIX.TO-BF-t-2 -- round 1 BF-t-2: the fourth verdict -- a kind of name that is not asked for a system says so

<to_id>LGIC_BLANKFIX.TO-BF-t-2</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-t-2` (`decompositions/LGIC_BLANKFIX_DECOMP.md`) | **outcome_ref:** FWD-1 (hop 3), FWD-3 |
**depends_on:** none (the verdict value is ruled: CTO msg 106198, record @bab3a0e453)

---

## WORKER FACE

### CONTEXT

**What the check is.** `python lib/opal_naming.py census --repo` reads names from the repository and grades each with
`grade(name, type) -> (verdict, canonical)`. `census_repo()` (`lib/opal_naming.py`) returns `(items, stats)`; each item is a dict
`{"plane": "repo", "type": <node type>, "current": <the name>, "where": "<repo-relative file>:<line>"}`. A canonical form may carry a
blank written in braces: `{system}`, `{cadence}`, `{source}`, `{scope}`. `grade()` raises `opal_naming.RaiseDefect` for a name it
cannot place. Import the library with `sys.path.insert(0, "lib")` then `import opal_naming`. Python 3.9 syntax only; ASCII only
in code and output; no new dependency.

**The root of this round** is `infra/aws/terraform/bd-pipeline/` read together with the Lambda source folders it deploys (at the cut:
`infra/aws/lambda/bd-pipeline/`). Measured at the cut on the repository plane: the root's `.tf` files give 96 graded names, 12 with a
`{system}` blank and 9 with a `{cadence}` blank; the source folder gives 37 graded names, 16 with a `{source}/{scope}` blank, and 6
names skipped by the cards in `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/NOT_JUDGED_R13.json`.

### THE CELL

`BF-t-2`, the thread's hop 3. Andrew ruled on 2026-09-21 that an AWS service name is never a system, and that the ruling extends to
inline policy names and library layers; the check "gives these their own verdict instead of failing them against the registry".
Today `grade()` returns `OUT-OF-PATTERN` with a `{system}` blank for them. `org/standards/NAMING_SCHEMA.json` `grade.verdicts`
lists three values: `CONFORMANT`, `ALIAS`, `OUT-OF-PATTERN`.

**THE VALUE is `NO-SYSTEM-ASKED`**, ratified by `1.0.0_SA_CTO` (msg 106198); its record is
`org/missions/D14/LGIC/LGIC_BLANKFIX/prd/C_VERDICT_FOURTH_VALUE_RECORD.md` -- read it first. Use that spelling exactly. The ruling
adds: a `NO-SYSTEM-ASKED` name carries no `{system}` placeholder in its canonical form; and the membership count the issuer
measured (106 of the 141 repository-plane names that carry a `{system}` blank at the cut: 84 purpose-word, 19 PascalCase, 3
layers) was not re-run by the CTO, so you re-read it and your proof carries the number.

**The population (group A).** A name whose first token is in `infra/logic/registry/systems.json` `refused_keys.purpose_word`; a
policy name that is one PascalCase token with no hyphen; a `LAMBDA_LAYER` name -- in each case only when no later token and no
`resources.json` row resolves a system (today's `{system}` outcome in `_slots()`, rules R1.d and R1.e). A name whose first token is
in any OTHER refused list (for example `generic_noun`: `pipeline-chain`, `gold-layer-trigger`) is group B and is NOT moved: it
still returns `OUT-OF-PATTERN` with `{system}`.

**Build:**

1. `lib/opal_naming.py`: `grade(name, type)` returns the fourth value for a group-A name. Its canonical form is the form the grammar
   gives WITHOUT a system slot and with no blank in it (for `s3-access`, type `IAM_POLICY`: the tokens the rules keep, then the
   kind). The signature stays `(name, type) -> (verdict, canonical)`. The census's report table gains the fourth column.
2. `org/standards/NAMING_SCHEMA.json`: the value added to `grade.verdicts` with one sentence of meaning beside the other values,
   and the two sentences that deny a fourth (`grade.not_graded`, `grade.unplaceable`) corrected to say four. Bump `version` and add
   one `changelog` line naming this order. Nothing else in the schema moves.
3. `.tools/naming-gate.py` and `.tools/naming-apply-gate.py`: read how each handles a verdict today and make each handle the fourth
   value as a name that is NOT refused for lacking a system; each gate's own `--self-test` gains one arm for it and still passes.
4. `lib/tests/test_opal_naming_fourth_verdict.py`, runnable as a plain script with three modes:
   - no argument: four real group-A names of three kinds (`s3-access` IAM_POLICY, `cloudwatch-metrics` IAM_POLICY,
     `AdditionalPermissions` IAM_POLICY, one `LAMBDA_LAYER` name you take from `census_repo()`) each return the fourth value with a
     canonical carrying no `{`; and the DIFFERENCE CONTROL in the same run: `pipeline-chain` IAM_POLICY and `gold-layer-trigger`
     IAM_POLICY still return `OUT-OF-PATTERN` with `{system}` in the canonical; and the schema lists exactly four verdicts; and
     the membership re-read: over `census_repo()`'s items (cards in `NOT_JUDGED_R13.json` applied, raising names skipped), the count
     of names that now return `NO-SYSTEM-ASKED` and the count that still carry `{system}`.
     Last line `VERDICT4-TEST ok=True group_a=N control=N repo_no_system_asked=N repo_system_blank=N`.
   - `--suite`: runs `python -m pytest lib/tests/test_opal_naming.py -q -p no:cacheprovider --color=no`, collects the failing test
     ids, and compares them with THE SIX THAT FAIL AT THE BASE (below). Last line
     `VERDICT4-SUITE ok=True failed=N outside_base=0`, `ok=False` when any failing id is outside the six.
   - `--gates`: runs each gate's `--self-test`. Last line `VERDICT4-GATES ok=True naming_gate=PASS apply_gate=PASS`.

**The six tests that fail at the base** (measured at the cut, before any edit; they are not yours to fix and not yours to break
further): `test_grade_agrees_with_every_worked_case` for the cases `inf-silver-chain|LAMBDA`, `opal-portal-data-proxy-api|API_GW`,
`Inflection-SilverChain-DimConversionFailure|CW_ALARM`, `wsb-49f-model-aua-pull-daily|SCHEDULE`, `inf/otp-relay/token|SECRET`; and
`test_lambda_plane_consumers_is_import_aware_not_a_bare_substring`. Where a worked case in `lib/tests/test_opal_naming.py` records
`OUT-OF-PATTERN` for a group-A name, update that case to the fourth value and list each one you changed in your report.

**Other readers of a verdict, outside your grant.** `lib/opal_lgctfm.py`, `.tools/safe-apply.sh`,
`infra/logic/render_naming_section.py` and `infra/logic/registry/exemptions.json` each mention a verdict value. Read each; for any
that would mishandle the fourth value, file one row naming the file and line. Do not edit them.

### ACCEPTANCE

<criterion id="BF2-AC1" cell_refs="BF-t-2"><invocation>python lib/tests/test_opal_naming_fourth_verdict.py</invocation><expect>VERDICT4-TEST ok=True</expect></criterion>
`BF2-AC1` -- group-A names take the fourth value with no blank, and group-B names in the same run do not (the difference control).

<criterion id="BF2-AC2" cell_refs="BF-t-2"><invocation>python lib/tests/test_opal_naming_fourth_verdict.py --suite</invocation><expect>VERDICT4-SUITE ok=True</expect></criterion>
`BF2-AC2` -- the library's own suite shows no failure outside the six that fail at the base.

<criterion id="BF2-AC3" cell_refs="BF-t-2"><invocation>python lib/tests/test_opal_naming_fourth_verdict.py --gates</invocation><expect>VERDICT4-GATES ok=True</expect></criterion>
`BF2-AC3` -- both naming gates still pass their self-tests with the new arm.

<expected_criteria>BF2-AC1,BF2-AC2,BF2-AC3</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- `python lib/opal_naming.py generate` output is NOT committed by you; if your edit changes a generated file's content, say so in the report (the issuer regenerates at the merge).
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming.py
lib/tests/test_opal_naming.py
lib/tests/test_opal_naming_fourth_verdict.py
org/standards/NAMING_SCHEMA.json
.tools/naming-gate.py
.tools/naming-apply-gate.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit: every file under `infra/logic/`, `lib/opal_lgctfm.py`, `.tools/safe-apply.sh`, `org/missions/D14/LGIC/LGIC_BLANKFIX/prd/C_VERDICT_FOURTH_VALUE_RECORD.md`, `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/NOT_JUDGED_R13.json`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.md`.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.md</decomp_doc> (round 1), cell `BF-t-2`.
<owned_cells>BF-t-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF2-AC1, BF2-AC2, BF2-AC3. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/LGIC_BLANKFIX.TO-BF-t-2.fourth-verdict.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BF2-AC1,BF2-AC2,BF2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three last lines whole; the diff stat; each worked case changed; each outside reader and what it does with the fourth value; whether any generated file's content moves; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a fourth value that swallows group B and hides names that do need a system (the difference control is in AC1's own run); a gate that starts refusing or stops refusing every name (both self-tests, AC3); a schema edit wider than one row (the face bounds it; the diff stat is in the report); a worker repairing the six base failures to make the suite green (the face names them as not its own); BLIND: a reader that builds the verdict string at run time.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.2 @47ef4c98cc section 2 (THREAD); decomposition round 1 @f15f222030. Base dry-run at the cut: BF2-AC1, BF2-AC2, BF2-AC3 base FAIL as expected (file absent). Beside them, ran at the cut: `python -m pytest lib/tests/test_opal_naming.py -q` -> 6 failed, 87 passed (row LGIC_BLANKFIX-S1). The decomposition cut this cell STAGED on the CTO's record; the record landed before the issuance (msg 106198, @bab3a0e453), so the order is issued pending.
