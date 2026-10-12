# TO IRPT_ANLREQ.TO-AR-y-146 -- a READ: every order and record that names parse.py as the door the form reaches, with its owning lane

<to_id>IRPT_ANLREQ.TO-AR-y-146</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~54</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a read of committed records)
**Decomp cell:** `AR-y-146` (`decompositions/IRPT_ANLREQ_DECOMP_R14_Y.md`) | **outcome_ref:** FWD-1 (hop 2, the upload door); TCKT_VNEXT FWD-3 by CTO msgs 5737 and 5849 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~54`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-54` (branch `wk-IRPT_ANLREQ-54`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~54 <0.9.0_WK_IRPT_ANLREQ~54@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W54-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you change passes `bash .tools/commit-gate.sh <file>` before its commit.
- **The background for every cell of this round** is one record, read it first:
  `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r13/ONE_ACCOUNT_CHECK_READ.json` (what the upload door does today, run in process on four synthetic sheets), and the CTO's rulings in
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_14_20261011.md` section 2. Any sheet you build is SYNTHETIC: made-up tickers (`AAA`, `BBB`), made-up numbers, nothing that looks
  like a real account number or a person. No real uploaded file is ever read.

### THE CELL (`AR-y-146`, inlined) -- A READ. You change no file but your record.

*Every order and record that names `parse.py` as the door the form reaches.*

Why. The form's uploads go through `intake/template_reader.py`. The deployed service refuses the `parse.py` lane by name. Several
orders, rulings and records of today name `parse.py` as "the normalizer" the form reaches (row `IRPT_ANLREQ-D2-W52-S9`). A check
built on those words would have been built in a file that never runs. Each such sentence is to be corrected by the lane that owns
the file it is in; this cell finds them all.

1. Search these folders for the string `parse.py` (use the Grep tool on each named folder; print the count of files searched per
   folder): `org/missions/D9/IRPT/IRPT_ANLREQ/`, `org/missions/D7/TCKT/TCKT_VNEXT/`, `org/missions/D9/IRPT/IRPT_BCKEND/` (if it
   exists), `org/tier1_exec/1.0.0_SA_CTO/deliverables/` (files dated 20261011 only), `org/tier1_exec/2.0.0_SA_COO~Y2/`,
   `org/tier1_exec/2.0.0_SA_COO~V2/` (if it exists).
2. For EACH hit one row: `{"file": "...", "line": <n>, "says": "<the sentence, at most 200 characters>", "disposition":
   "NAMES_IT_AS_THE_FORMS_DOOR" | "NAMES_IT_CORRECTLY" | "QUOTES_ANOTHER_RECORD", "owner_lane": "<the lane or seat that owns the
   file: read it from the path (a `deliverables/<serial>/` folder is that serial's; a task order is its issuer's; a CTO
   deliverable is the CTO's)>", "correction": "<the one sentence that would make it true, or null>"}`.
   `NAMES_IT_CORRECTLY` is a mention that is true as written (for example: "the deployed service refuses the parse.py lane").
3. Write `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~54/r14/PARSE_PY_MENTIONS.json`:
   `{"read_at": "<UTC>", "searched": "<the folders and the term>", "files_searched": <n>, "mentions": [...], "by_owner": {"<owner>":
   <count of NAMES_IT_AS_THE_FORMS_DOOR>, ...}}`. Commit it. Edit no other file: the owners correct their own.

### ACCEPTANCE

<criterion id="AR146-y-AC1" cell_refs="AR-y-146"><invocation>python C:/dev/wk-irpt-anlreq-54/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r14/ar14_checks.py y146-mentions --root C:/dev/wk-irpt-anlreq-54</invocation><expect>Y146-MENTIONS-OK</expect></criterion>
`AR146-y-AC1`: the record states what was searched and over how many files, and gives every mention a disposition and an owner.

<expected_criteria>AR146-y-AC1</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~54/` and this order's
  file (status flip only).
- READ only: everything else. No push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R14_Y.md</decomp_doc>
<owned_cells>AR-y-146</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR146-y-AC1. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~54/IRPT_ANLREQ.TO-AR-y-146.parse-py-mentions.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-146`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR146-y-AC1`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading 1 row (IRPT_ANLREQ-D2-W52-S9) and 3 documents known to name the file wrongly (this seat's round-13 order and decomposition, the CTO's msg 5737 as quoted in the hop map); NOT seen: every other mention (the cell finds them; the count of files searched is printed per folder). comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or called. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; 0 scheduled readers of what this cell writes. comp-iam: DECLARED-NOT-APPLICABLE -- no identity or permission change
comp-adversary: RUN -- by reading 1 row against the face; the lens: a true sentence about parse.py (the service refuses that lane) marked as an error, or a folder skipped in silence. The face gives a disposition for the true case and requires the per-folder count. NOT seen: mentions outside the named folders.
lane: the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-14 analysis @1edb90ada7, item 7 (row `IRPT_ANLREQ-D2-W52-S9`). `AR146-y-AC1` base: FAIL as expected (no record).
- The issuer corrects its own files from this record and passes the others to their lanes.
- Seating: slot ~54 is reused; its earlier order is terminal.
