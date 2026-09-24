# AMGT_CORPUS task order -- `CRPS-e-5` -- ROUND 3: the coverage census gains a FOURTH disposition, `served-as-empty-shell`, so a workbook-only or empty folder whose dossier object carries every field absent is never counted as served

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-e-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates (C1=23 C2=5 C3=12 C4=21 C5=334), 0 on these surfaces; no deploy.
comp-iam: RUN at L5 (round-1 read, not re-run); this cell's one S3 write is a new research-backlog scan vintage through gold_put, as d-4's was.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, continued from `CRPS-e-4`. Serves **FWD-19 and FWD-14** (the census's partition is honest:
CTO R-75 / round-2 analysis s.2, row `AMGT_CORPUS-Z-W1-S4`).

## 1. THE CELL -- `CRPS-e-5`

**Where this came from.** `backlog --coverage` (round 2, d-4) reads `dossier-served` whenever `dossier.read_dossier(key)` returns an
object. Nine workbook-only folders carry a stored all-fields-absent shell (the dossier builder has no report-count floor), so they
read served while giving a reader neither layers nor a reason. The CTO ruled the content axis: 44 substantive / 9 empty-shell /
40 unresolved over 93.

**RULED -- what you build (`backlog.py`, its tests):**
- A fourth disposition `served-as-empty-shell`: the folder resolves, a dossier object exists, AND the folder's own files carry no
  prose document (every file `.xlsx`/`.png`/`.html`, or zero files) -- measured from the folder's files as `never_prose` already
  is, never from the dossier's field census. `dossier-served` then requires at least one prose file. The totals line becomes
  `folders_read F dossier_served S served_as_empty_shell M resolved_no_prose P unresolved_with_reason U sum F` (asserted in code),
  `never_prose_named K` and its list unchanged. `--folder`/`--folder-by-index` print the new value with `dossier_uri` +
  `content_sha256` (the shell object exists) and `reason <workbook-only|empty>`.
- The scan vintage's `records[].disposition` carries the fourth value; `state` and `security_key` stay exactly as today (the
  continuation and dossier readers of `read_latest()` depend on them).
- Tests: the fixture library gains a workbook-only resolved folder with a dossier stub, asserting `served-as-empty-shell` and the
  four-way sum; the word `served-as-empty-shell` occurs nowhere else in `lib/research/corpus/` (a token census in the test).

## 3. SURFACES

<paths>
lib/research/corpus/backlog.py
lib/research/corpus/tests/test_backlog.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-e-5.coverage-empty-shell-disposition.md
</paths>

READ-ONLY: every other `lib/research/corpus/` module, `lib/research/identity/crosswalk.py`. Scratch `.scratch/e5/`.

## 4. BOUNDS
- Pure ASCII source, LF, Python 3.9-compatible. NO S3 DELETE. The one S3 write is the new scan vintage (`gold_put`, never
  overwriting). The library is listed only.
- REFUSE a criterion you cannot satisfy as written, with your measurement -- a sum that does not close is a finding, printed,
  never forced; rows `AMGT_CORPUS-Z-W1-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-e-5"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round3/e5_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ deselected)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-e-5"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round3/e5_AC2.sh</invocation><expect>(?s)folders_read (\d+) dossier_served \d+ served_as_empty_shell [1-9]\d* resolved_no_prose \d+ unresolved_with_reason \d+ sum \1\b.*never_prose_named [1-9]\d*</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-e-5"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round3/e5_AC3.sh</invocation><expect>(?s)folder Costco COST.*disposition served-as-empty-shell.*(dossier_uri s3://opal-data-harvest/amgt/harvest/gold/research-dossier/|reason \S)</expect></criterion>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe against the real library and store, four-way sum asserted; AC3 FWD-14's by-name
  answer on a folder known workbook-only (Costco COST), never a silence.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-e-5.coverage-empty-shell-disposition.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: the AC2 totals line, the shell list, the scan vintage's S3 URI, and AC3's lines.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER AMENDMENT 1 (2026-09-24 ~19:4xZ):** AC1's expect admits pytest's `-k`-filtered summary (`N passed, M deselected in`), which the as-cut pattern could never match (row AMGT_CORPUS-Z-W3-S4, found by `0.9.0_WK_AMGT_CORPUS~3`); at the base the check still FAILS (0 passed). Graded by: GATE (viii) (the order declares `<placeholders>`); no other limb grades a modification.

**ISSUER NOTES:** the enum row (Rule 24 record in decomposition v3.0 s.2). Checks dry-run at the base: AC1 FAIL (no such tests),
AC2 FAIL (no fourth token), AC3 FAIL (Costco reads dossier-served today) -- recorded in the issuance commit.

<risk>LOCAL</risk>
<status>pending</status>
<round>3</round>
<slot>~1</slot>
<fabric>site-z</fabric>
