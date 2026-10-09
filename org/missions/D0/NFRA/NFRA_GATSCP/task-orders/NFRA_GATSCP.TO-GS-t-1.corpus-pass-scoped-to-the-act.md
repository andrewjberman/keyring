# TO NFRA_GATSCP.TO-GS-t-1 -- round 1 GS-t-1: the surprise-channel corpus pass refuses only a failure in the act's own documents

<to_id>NFRA_GATSCP.TO-GS-t-1</to_id>
<project>NFRA_GATSCP</project>
<issued_to>0.9.0_WK_NFRA_GATSCP~1</issued_to>
<issued_by>2.0.0_SA_COO~N1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~N1</workstream>

**Directive:** D0 | **Fabric:** dell1 | **Decomp cell:** `GS-t-1` (`decompositions/NFRA_GATSCP_DECOMP.md`) | **outcome_ref:** FWD-1 |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

A commit or merge that touches a surprise-channel document runs `.tools/surprise-row-gate.py`. Inside it, the "corpus pass"
`.tools/surprise-corpus-validate.py` validates EVERY channel document in the repository (331 documents, 9,940 rows at the base)
against the schemas and refuses the act if ANY document anywhere has a failure that is not in the baseline. So a seat whose
act is clean is refused for another project's fresh error. This cell makes the pass refuse only a failure in the documents the
act itself carries, and print every other failure as STANDING, naming its project. It does not change what counts as a failure.

Facts at the base (read them before you build):
- `surprise-corpus-validate.py`: `main(argv) -> int` (:338); flags `--write-baseline`, `--json`, `--index`, `--index-rows`.
  Documents are enumerated from the index (`_channel_docs`, :110; `_index_paths`, :157-175) and read from index blobs in one
  `git cat-file --batch` (`_index_blobs`, :178-203, honours `GIT_INDEX_FILE` and `GIT_DIR`; `_read_doc`, :206-227). BUT the
  schemas (`_schemas`, :61-67) and the baseline (:271-276, `org/surprise_channel/.corpus-baseline.json`) are read from the
  working tree with `open()`. A tuple is `[doc_rel, row_id, json_pointer, digest]` (`_tuple`, :230-233); `new = current -
  baseline`, `resolved = baseline - current` (:369-371). Refusal: baseline absent (:361-368), any malformed block (:389-395), any
  NEW or RESOLVED tuple (:396-399).
- `surprise-row-gate.py` :3979-3992 imports the pass with importlib and calls `_scv.main([])`. Its dispatched paths come from
  `_dispatched_from_argv_or_env(argv)` (:1884-1911: argv, else the `STAGED` env var); `main` keeps those matching `CHANNEL_RE`
  (:3961). `_folder_identity(rel)` (:69-98) returns the project of a channel path.
- Channel paths: tree `org/missions/D<n>/<MACRO>/<CODE>/surprise-channel/(investigations|adjudications|remediations)/<file>`;
  flat `org/surprise_channel/<CODE>/<file>`. The owning project is `<CODE>`.

### THE CELL

`GS-t-1`. The corpus pass takes the act's documents (`--act PATH`, repeatable); a NEW failure or malformed block outside them
prints `STANDING <CODE>` and does not refuse; inside them it refuses as today; a RESOLVED tuple always refuses; the schemas and
the baseline are read from the graded index; the row gate passes its dispatched paths.

**Build**, in `.tools/surprise-corpus-validate.py`:
1. `--act PATH`, repeatable. With at least one `--act`: a NEW tuple whose `doc_rel` is not an act path prints exactly
   `STANDING <CODE> surprise-corpus <doc_rel> <row_id> <json_pointer>` (one line, starting at column 0) and does not count
   toward the exit code; a malformed block in a non-act document prints `STANDING <CODE> surprise-corpus <doc_rel> malformed
   <detail>` likewise. A NEW tuple or malformed block in an act document refuses exactly as today. A RESOLVED tuple refuses
   whatever the act (re-baselining is a deliberate CVO act). A missing baseline refuses. Print a denominator line naming how many
   findings were in-act and how many STANDING.
2. Without `--act`: behaviour, output and exit codes unchanged.
3. Read the two schema files and the baseline from the index the pass grades (the same index as the documents; `git cat-file`
   / `git show :<path>` honouring `GIT_INDEX_FILE` and `GIT_DIR`), falling back to the working tree only where the index read is
   impossible, with a `WARN:` line on stderr, as the documents already do.

In `.tools/surprise-row-gate.py`, change only the corpus-pass call (:3979-3992) so it passes `--act <p>` for every dispatched
channel path, and so the STANDING lines it prints are shown (they reach stdout already through the pass). Touch nothing else in
that file.

### ACCEPTANCE

<criterion id="GS1-AC1" cell_refs="GS-t-1"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round1_prep/checks/r1_corpus_scope.py"</invocation><expect>GS-T1-SCOPE ok=True</expect></criterion>
`GS1-AC1` -- with a planted NEW failure in `LGIC_BLANKFIX`'s channel, an act carrying another project's document passes and prints
`STANDING LGIC_BLANKFIX`; an act carrying the planted document is refused (the difference control).

<criterion id="GS1-AC2" cell_refs="GS-t-1"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round1_prep/checks/r1_rowgate_seam.py"</invocation><expect>GS-T1-ROWGATE ok=True</expect></criterion>
`GS1-AC2` -- the seam: the real row gate, with `STAGED` set, lands beside the planted failure and refuses on it.

<criterion id="GS1-AC3" cell_refs="GS-t-1"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round1_prep/checks/r1_corpus_bytes.py"</invocation><expect>GS-T1-BYTES ok=True</expect></criterion>
`GS1-AC3` -- the baseline is read from the graded index: a baseline tuple dropped in the index only makes that failure NEW.

<expected_criteria>GS1-AC1,GS1-AC2,GS1-AC3</expected_criteria>

Each check plants its defect in a private copy of the git index and restores nothing because it changes nothing else; read the
check before you build. Each prints its arms and ONE last line, which is the line the expectation is matched against. All three
FAIL at the base. You do not edit the checks.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- No edit outside the grant. No change to the schemas, the baseline, or any channel document's content. No new flag beyond
  `--act`. No override (`# surprise-row-override`, `SURPRISE_ROW_OVERRIDE`) at any commit.
- `surprise-row-gate.py --self-test` must still pass after your change (run it once; it is long).
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_GATSCP-D1-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the check or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not
  block.

<paths>
.tools/surprise-corpus-validate.py
.tools/surprise-row-gate.py
org/missions/D0/NFRA/NFRA_GATSCP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside it, in particular the check files under
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round1_prep/checks/` and `org/surprise_channel/schemas/`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_GATSCP/decompositions/NFRA_GATSCP_DECOMP.md</decomp_doc> (round 1), cell `GS-t-1`.
<owned_cells>GS-t-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: GS1-AC1, GS1-AC2, GS1-AC3. Instance at
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~1/NFRA_GATSCP.TO-GS-t-1.corpus-pass-scoped-to-the-act.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> GS1-AC1,GS1-AC2,GS1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three last lines whole; the row gate self-test's last line; the STANDING line as printed; commits.

### AMENDMENT 1 (2.0.0_SA_COO~N1, 2026-10-09) -- the row id carries the dell1 coordinate

A row filed on dell1 is `NFRA_GATSCP-D1-W1-S<k>` (the row gate refuses a dell1 row without `-D1-`; measured on the issuer's own
row `NFRA_GATSCP-D1-S1` @6911a2f5d7). The refusal clause above now reads that form. Graded by: the surprise-row gate's fabric
coordinate limb; no TO-gate limb grades this modification beyond GATE (viii).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the thread touches no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the cut's own arms: every criterion carries the difference control (the same plant in the act's own document is refused), so a pass that stops refusing passes nothing. BLIND: a defect only in a working tree (by design, C-BYTES).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.2 @7cb6183997 (FWD-1; C-SCOPE, C-BYTES, C-NO-FRICTION); decomposition round 1. Base dry-run at the cut (box/dell1
95669cba44): GS1-AC1 FAIL as expected; GS1-AC2 FAIL as expected; GS1-AC3 FAIL as expected.
