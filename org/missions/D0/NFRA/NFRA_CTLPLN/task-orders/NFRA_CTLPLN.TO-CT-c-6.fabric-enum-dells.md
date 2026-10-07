# TO NFRA_CTLPLN.TO-CT-c-6 -- round 3 CT-c-6: the fabric enum -- dell1 and dell2 join it, with the record and every reader repaired

<to_id>NFRA_CTLPLN.TO-CT-c-6</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~5</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~C</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-c-6` (`decompositions/NFRA_CTLPLN_DECOMP.round3.md`) | **outcome_ref:** FWD-7 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CT-c-6`, FWD-7 / C-PLACEMENT, the CTO's round-3 item (msg 105973): "`.tools/to-pipeline-gate.py` FABRIC_ENUM is ('laptop','site-z'):
missions-tree-index refused fabric='dell1' on four rows tonight, so ... those project.json rows keep fabric laptop with the box in
placement. The cell adds dell1 and dell2 to the enum with its rule-24 record (four postulates, token census)". You add the two values,
write the record, and repair every reader that would mishandle them. You do NOT flip any `project.json` row: the rows are the CTO's.

**What exists:** `.tools/to-pipeline-gate.py:93` `FABRIC_ENUM = ("laptop", "site-z")`, read at `:2316-2319` (the gate's refusal) and
`:3102` (the sweep's flag); `.tools/missions-tree-index.py:720-721` (a self-test arm comparing its `fabric` enum, read from the gate's
source, to the gate's; its fixtures at `:613`, `:620`); the device register `org/devices/DEVICES.json`, whose box names are `laptop`,
`sitez` (aliases `site-z`, `Z`), `dell1`, `dell2`. Both tools have `--self-test`.

**Build:**

1. **The token census, first** -- `.tools/tests/fabric_value_census.py`: over tracked files under `.tools/`, `lib/`, `org/devices/`,
   `org/modules/`, `.claude/skills/` and `org/standards/` (skip binaries and files over 1 MB), find every line where `site-z` or
   `sitez` appears on a word boundary within the same line as, or within three lines of, the word `fabric` (case-insensitive). For
   each hit print `path:line` and classify it by a table inside the script, keyed by path, into: `ENUM-SOURCE` (defines the allowed
   set), `COMPARES` (code that branches on a fabric value or tests membership), `DISPLAY` (prints or documents), `FIXTURE` (test
   data). A hit whose path is not in the table is `UNCLASSIFIED`. LAST line
   `FABRIC-CENSUS files_scanned=<f> hits=<h> enum_source=<e> compares=<c> display=<d> fixture=<x> unclassified=<u> ok=<True|False>`
   with `ok=True` only when `u == 0`. The denominator (`files_scanned`) is printed; classify every hit by reading it.
2. **The enum.** `FABRIC_ENUM = ("laptop", "site-z", "dell1", "dell2")` in `.tools/to-pipeline-gate.py`, with a comment naming this
   order, PRD C-PLACEMENT and the record's path. Where `.tools/missions-tree-index.py` holds or derives its own copy, it must agree by
   construction (it reads the gate's source today; keep that, do not add a second literal).
3. **Every `COMPARES` hit:** read it. Code that treats "not laptop" as site Z, or that has a two-way branch on the pair, is repaired
   so that `dell1` and `dell2` are handled as their own boxes -- but ONLY in the two files your grant names. A `COMPARES` hit in any
   other file is NOT edited: list it in the record and file ONE surprise row carrying the full list (the issuer amends the grant).
4. **The record** -- `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~5/FABRIC_ENUM_RULE24_RECORD.md`: the four
   postulates for the enum `{laptop, site-z, dell1, dell2}` -- (i) MECE over the declared domain "a box in `org/devices/DEVICES.json`":
   print the register's box names beside the enum and name any member one holds and the other does not (the register key is `sitez`
   and the enum value is `site-z`: state that mismatch plainly; it is not yours to resolve); (ii) same grain (each value one box);
   (iii) intent coherence (the axis is "which box executes this project", one intent); (iv) state coherence (name what a change of
   this value does NOT move: `placement`, the lane, the inbound queue). Then the census table from step 1.
5. `.tools/tests/test_fabric_enum_dell.py` -- runs the gate's fabric check on four temporary project rows (`fabric` = `dell1`, `dell2`,
   `laptop`, `site-z`) and expects no refusal, and on two (`fabric` = `dell3`, `DELL1 ` with a trailing space and capitals -- the
   check lower-cases and strips, so that one is admitted; say so) with `dell3` refused; then runs
   `python .tools/missions-tree-index.py --self-test` and `python .tools/to-pipeline-gate.py --self-test` and reads their result
   lines. If either self-test exceeds 100 s, run it once for the record outside the test and have the test read only the gate's and the
   index's fabric arms; say which you did. LAST line
   `FABRIC-ENUM admitted=<a>/5 refused=<r>/1 tree_selftest=<ok|fail|skipped> gate_selftest=<ok|fail|skipped> ok=<True|False>`.

### ACCEPTANCE

<criterion id="CT3c6-AC1" cell_refs="CT-c-6"><invocation>python .tools/tests/test_fabric_enum_dell.py</invocation><expect>FABRIC-ENUM admitted=5/5 refused=1/1</expect></criterion>
`CT3c6-AC1` -- the gate admits the two Dell values and still refuses a value outside the enum (the control arm).

<criterion id="CT3c6-AC2" cell_refs="CT-c-6"><invocation>python .tools/tests/fabric_value_census.py</invocation><expect>unclassified=0 ok=True</expect></criterion>
`CT3c6-AC2` -- every reader of a fabric value in the scanned tree is found and classified, with the denominator printed.

<expected_criteria>CT3c6-AC1,CT3c6-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **No `project.json`, no `SEQUENCE.yaml`, no `DIRECTIVES.yaml`, no `DEVICES.json` edit.** No change to any other gate limb.
- Both tools are commit gates for the whole fabric: after your edit run `python -m py_compile` on each and both `--self-test`s, and
  put their result lines in your report.
- No non-ASCII added to either tool.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_CTLPLN-W5-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or the
  expected value.

<paths>
.tools/to-pipeline-gate.py
.tools/missions-tree-index.py
.tools/tests/test_fabric_enum_dell.py
.tools/tests/fabric_value_census.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit: `org/devices/DEVICES.json`, every file the census scans.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round3.md</decomp_doc> (round 3), cell `CT-c-6`.
<owned_cells>CT-c-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CT3c6-AC1, CT3c6-AC2. Instance at `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~5/NFRA_CTLPLN.TO-CT-c-6.fabric-enum-dells.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CT3c6-AC1,CT3c6-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines; the census counts per class; every `COMPARES` hit outside your grant; both self-test result lines; the
register-versus-enum mismatch as you measured it; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a widened enum admitting a typo (the refused arm of AC1); a reader that assumes two values and silently treats a Dell as site Z (the census, every COMPARES hit read; hits outside the grant rowed, not edited); a gate edit breaking every commit on the fabric (both self-tests and py_compile on the face; the issuer re-runs both at the drain); BLIND: readers outside the scanned directories (the denominator is printed so the bound is visible).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: CTO msg 105973; PRD v0.8 C-PLACEMENT, FWD-7; CLAUDE.md rule 24 (a value-enum change arrives with its four-postulate record and
token census); decomposition round 3. Base dry-run at the cut: CT3c6-AC1 and CT3c6-AC2 base FAIL as expected (neither file exists).
