# AMGT_RESAPP task order -- `AMGT-ee-3` -- PyMuPDF IS IMPORTED ONLY WHERE A PDF IS READ, SO THE FILING MODULES IMPORT ON A BOX WITHOUT IT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ee-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~320</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one import moved.
comp-iam: DECLARED-NOT-APPLICABLE -- no read or write path changes.
comp-adversary: RUN at the cut -- on dell1 `import lib.research.filings.fetch` and `...analyze` fail: document.py:56 imports fitz (PyMuPDF) at module top; PyMuPDF is installed but needs the VC++ runtime, an admin install (MSTR~DELL1 msg 1693). The SEC .htm path never calls fitz. AC1 FAILs at the base, AC2 PASSes (217 passed, fitz stubbed).
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-320`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ee-3` (round 81, decomposition s.89)

`lib/research/filings/document.py` imports `fitz` (PyMuPDF) at the top of the module (`:56`). Only the PDF functions use it
(`pdf_to_text` and its helpers, about `:153-275`). On this box fitz cannot load, so every module that imports `document` --
`fetch`, `analyze`, `batch`, `battery`, `drafting_build` -- fails to import, even for an SEC .htm filing that never reads a PDF.

1. Remove the module-level `import fitz`. Import it inside each function that uses it, at the top of that function's body.
2. Nothing else in `document.py` changes: no logic, no pattern, no cap. A PDF read on a box with PyMuPDF behaves exactly as
   today; on a box without it, the PDF function raises the ImportError when it is called, not when the module is imported.
3. Add one test in `lib/research/filings/tests/test_document.py`: with fitz blocked (a `sys.meta_path` finder raising ImportError
   for `fitz`), importing `document` succeeds and `cut()` cuts a 10-K plant.

Run the filings test folder with a stub `fitz.py` on PYTHONPATH and report its last line.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W320-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. You edit `document.py`'s imports and the one test file only.

## 3. SURFACES

<paths>
lib/research/filings/document.py
lib/research/filings/tests/test_document.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~320/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ee-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round81/checks/r81_ee3.py" --crit AC1; echo "exit=$?"</invocation><expect>document, fetch and analyze import with fitz unimportable and cut() still cuts; no module-level fitz import remains; F1-F2 PASS; R81 EE3 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ee-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round81/checks/r81_ee3.py" --crit AC2; echo "exit=$?"</invocation><expect>the filings test folder passes with a stub fitz, 0 failed; B1 PASS; R81 EE3 AC2 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~320 <0.9.0_WK_AMGT_RESAPP~320@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~320/AMGT_RESAPP.TO-AMGT-ee-3.pymupdf-imported-only-where-a-pdf-is-read.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the filings folder's last line;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-80 analysis R1 fallback, made the round's opening cell by ADDENDUM 1 @62c6adbde9 (msg 1697). document.py is a site-Z producer path (msgs 1267/1394): its MERGE is a site-Z deploy and waits for 1.0.0_SA_CTO~Z's half. Checks dry-run at the base: AC1 base: FAIL as expected (F1, F2 FAIL); AC2 base: PASS as expected (217 passed).

<status>pending</status>
<round>81</round>
<slot>0.9.0_WK_AMGT_RESAPP~320</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
