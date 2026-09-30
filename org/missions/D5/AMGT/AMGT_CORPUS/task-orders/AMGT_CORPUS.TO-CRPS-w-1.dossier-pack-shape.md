# AMGT_CORPUS task order -- `CRPS-w-1` -- ROUND 21: the dossier records `pack_shape` from the reports the fold reads

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-w-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads of the typed report rows only.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 21. Serves **FWD-16** ("a PDF-only pack gets the same fold, or the tab
states which shape the PDF could not be read to and why").

## 1. THE CELL -- `CRPS-w-1`

**Where this came from.** Round 20 counted "PDF-only" names by a proxy (every served citation ends in `.pdf`), because the
dossier carries no pack-shape field. The CTO ruled (round-20 analysis, ruling 3) that the dossier records `pack_shape` (`pdf`
/ `docx` / `mixed` / `none`) per folder, from the files the fold actually read.

`lib/research/corpus/dossier.py` composes the gold `research_dossier`. `build(security_key, client)` reads the typed report
rows through `_picked_reports(security_key, client)`, which returns `(items_raw, pick_a, pick_b)`. `pick_a` / `pick_b` are
`(row, document)` or None: the most recent class-A pack and class-B update. Each `row` carries `bronze_key`, the S3 URI of the
source file, whose extension names its shape (e.g. `...research pack 7_13_2026.pdf`).

**RULED -- what you build:**
1. `pack_shape(security_key, client=None) -> dict` in `dossier.py`, using `_picked_reports`. It takes the extensions of the
   picked A and B reports' `bronze_key`s:
   - all `.pdf` gives `{"value": "pdf", ...}`, and all `.docx` gives `"docx"`;
   - both gives `"mixed"`;
   - an extension that is neither counts toward `"mixed"` only beside a pdf or docx pick, and otherwise gives None;
   - no pick gives `{"value": None, "absent": "<readable reason>"}`.
   Carry the basis: the bronze keys read, e.g. `"basis": [<keys>]`.
2. `build()` sets `fields["pack_shape"]` from the same function, reusing the picks it already has; no second S3 read.
3. `lib/research/corpus/tests/test_dossier_pack_shape.py` (new), with stub picks and no network: pdf, docx, mixed, none, and
   `build()` carrying the field.
4. Do NOT run `--write`, and write nothing to S3. A served rewrite is the issuer's act.

## 3. SURFACES

<paths>
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_dossier_pack_shape.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-w-1.dossier-pack-shape.md
</paths>

READ-ONLY: every other file, every S3 object. Scratch `.scratch/w1/`.

Your worktree is a SPARSE cone (`lib integrations .tools .claude org docs rcg infra/logic`); `data/`, `portal/` and the rest of
`infra/` are absent by design. If you need a path outside the cone, file a row and stop that criterion; never disable the sparse
checkout.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible (no `newline=` on a `Path` text call).
- NO vendor call, NO S3 write, NO `--write` run.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W1-S<k>` (next free k), with
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-w-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round21/w1_AC1.sh</invocation><expect>(?m)^w1 pack_shape folders 96 pdf \d+ docx \d+ mixed \d+ none \d+ errors 0 sum_ok True control IMB_LN_Equity docx ADBE_US_Equity pdf AZN_LN_Equity pdf 6501_JP_Equity none$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-w-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round21/w1_AC2.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
</proof_of_spec>

- AC1: the census over the 96 keys through your function. It prints the shape distribution, 0 errors, the sum equal to 96, and
  four controls the issuer measured at the cut: IMB's A pick is docx; ADBE's is pdf; AZN's A and B are pdf; 6501 has no report.
- AC2: your tests with the dossier canonical-address suite.

## 6. WHEN YOU ARE DONE
1. Write the instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-w-1.dossier-pack-shape.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` returns rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file. Commit the files you changed
   plus the instance.
4. Report ONCE: each AC line, the distribution, and the function's return shape.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-20 analysis ruling 3 @`609100db54`. Dry-run at base CLOUD `f17ca57280` (worktree
`C:/tmp/coox-crps21-issue`):
- w1_AC1 FAIL as expected: `w1 pack_shape folders 96 pdf 0 docx 0 mixed 0 none 0 errors 96 sum_ok False control ... ERR`
  (AttributeError: no `pack_shape`).
- w1_AC2 FAIL as expected (no tests ran).

The picks rule (not all reports) is the issuer's reading of "the files the fold actually read" (decomposition s.1a).
<risk>LOCAL</risk>
<status>pending</status>
<round>21</round>
<slot>~1</slot>
<fabric>site-z</fabric>
