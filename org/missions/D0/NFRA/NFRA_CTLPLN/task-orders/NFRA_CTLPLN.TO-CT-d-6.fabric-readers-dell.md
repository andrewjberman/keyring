# TO NFRA_CTLPLN.TO-CT-d-6 -- round 4 CT-d-6: the two fabric readers -- the surprise-row gate and the PRD header schema handle a Dell

<to_id>NFRA_CTLPLN.TO-CT-d-6</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~9</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~C</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-d-6` (`decompositions/NFRA_CTLPLN_DECOMP.round4.md`) | **outcome_ref:** FWD-7 |
**depends_on:** none

**STAGED ON A RULING.** A Dell's row-id coordinate is not ruled (the decomposition's "Open at the CTO" item 1). The face below states the
cell with the coordinate as the one unknown; the issuer amends it with the ruled form before it is handed. A worker never starts it
while `<status>` reads `staged`.

---

## WORKER FACE

### THE CELL

`CT-d-6`, FWD-7 / C-PLACEMENT, row NFRA_CTLPLN-S5: the gate's `FABRIC_ENUM` now holds `laptop`, `site-z`, `dell1`, `dell2`, and two
readers still know two fabrics. You repair both and prove it. You flip no project row.

**What exists:** `.tools/surprise-row-gate.py` -- around lines 2042-2051 it derives a new row's fabric from its id
(`site-z` when the id carries a `Z-` infix, `laptop` otherwise) and refuses a row whose `fabric` field differs; it has a `--self-test`.
`org/standards/PRD_HEADER.schema.json` -- line 20 lists `["laptop", "site-z"]`. `.tools/to-pipeline-gate.py` `FABRIC_ENUM` is the one
source of the allowed set. The rule-24 record of the enum change:
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~5/FABRIC_ENUM_RULE24_RECORD.md`.

**THE RULED COORDINATE** is in this order's AMENDMENT 1 at the end of the file: how a row id filed on dell1 or dell2 is written, and
what the gate does with a bare id filed from a Dell-fabric project. Build exactly that.

**Build:**

1. `.tools/surprise-row-gate.py`: the id-to-fabric derivation handles the ruled Dell coordinate for both Dells, keeps `Z-` -> `site-z`
   and bare -> `laptop` exactly as today, and its refusal text names all four fabrics. The smallest edit; no other limb changes; no
   non-ASCII added.
2. `org/standards/PRD_HEADER.schema.json`: the fabric enum lists the four values, in the gate's order.
3. `.tools/tests/test_fabric_readers_dell.py`: runs the gate's derivation on six ids (a bare id, a `Z-` id, a dell1 id, a dell2 id,
   an id with an unknown coordinate, a dell1 id whose row says `fabric: dell2`) and expects: laptop, site-z, dell1, dell2, the ruled
   behaviour for an unknown coordinate, and a refusal for the mismatch; validates one PRD header instance per fabric against the
   schema (4 admitted) and one with `dell3` (refused); asserts the schema's enum equals `FABRIC_ENUM` read from the gate's source; runs
   `python .tools/surprise-row-gate.py --self-test` and reads its result line. LAST line
   `FABRIC-READERS ids_ok=<a>/6 schema_ok=<b>/5 enum_equal=<True|False> gate_selftest=<ok|fail> ok=<True|False>`.

### ACCEPTANCE

<criterion id="CT4d6-AC1" cell_refs="CT-d-6"><invocation>python .tools/tests/test_fabric_readers_dell.py</invocation><expect>FABRIC-READERS ids_ok=6/6 schema_ok=5/5 enum_equal=True gate_selftest=ok ok=True</expect></criterion>
`CT4d6-AC1` -- both readers handle the four fabrics, refuse a fifth, and agree with the gate's enum; the mismatch and `dell3` arms are
the controls.

<criterion id="CT4d6-AC2" cell_refs="CT-d-6"><invocation>python .tools/tests/fabric_value_census.py</invocation><expect>unclassified=0 ok=True</expect></criterion>
`CT4d6-AC2` -- CT-c-6's census of fabric readers classifies every hit. AT THE BASE IT DOES NOT: it prints `unclassified=5 ok=False`,
because the census passed while its own two files were untracked and it scans tracked files only; once committed, three lines of
`.tools/tests/fabric_value_census.py` and two of `.tools/tests/test_fabric_enum_dell.py` are hits its path table does not hold. Repair
the table so the census classifies its own files and your new test file (`FIXTURE` or `DISPLAY` as each line is), and so that a hit in
a NEW file under `.tools/tests/` is not silently passed: it stays `UNCLASSIFIED` until the table names it. Then both readers you
touched must still be classified.

<expected_criteria>CT4d6-AC1,CT4d6-AC2</expected_criteria>

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- The surprise-row gate is a commit gate for every seat on four boxes: run `python -m py_compile` and its `--self-test` after your edit
  and put both results in your report. No `project.json`, `SEQUENCE.yaml`, `DIRECTIVES.yaml` or `DEVICES.json` edit.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_CTLPLN-W9-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or the
  expected value.

<paths>
.tools/surprise-row-gate.py
org/standards/PRD_HEADER.schema.json
.tools/tests/test_fabric_readers_dell.py
.tools/tests/fabric_value_census.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit: `.tools/to-pipeline-gate.py`, `org/devices/DEVICES.json`,
`org/ref/SURPRISE_CHANNEL_PROTOCOL.md`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round4.md</decomp_doc> (round 4), cell `CT-d-6`.
<owned_cells>CT-d-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CT4d6-AC1, CT4d6-AC2. Instance at `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~9/NFRA_CTLPLN.TO-CT-d-6.fabric-readers-dell.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CT4d6-AC1,CT4d6-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines; the diff of the gate (lines changed); the gate's `--self-test` result line; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- two boxes minting one row id in one project (the coordinate, once ruled, makes a Dell's ids distinct; the mismatch arm refuses a row filed under the wrong fabric); a gate edit breaking every commit on the fabric (py_compile and --self-test on the face; the issuer re-runs both at the drain); a third copy of the enum drifting (enum_equal reads the gate's source); BLIND: rows a Dell already filed with bare ids before this lands -- the decomposition names the first one; their re-keying is not this cell.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: row NFRA_CTLPLN-S5 (the issuer's disarm of W5-S1); CTO msgs 105973, 106017; decomposition round 4 "Open at the CTO" item 1.
Base dry-run at the cut: CT4d6-AC1 base FAIL as expected (no file); CT4d6-AC2 base FAIL as expected (ran at the cut:
`FABRIC-CENSUS files_scanned=1700 hits=58 ... unclassified=5 ok=False`; the five are the census's own two committed files).
